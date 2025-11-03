#!/usr/bin/env python3
"""
Enhanced Flask Web Application for High-Quality Observability Data
Uses improved generator with proper service maps and dependencies
"""

from flask import Flask, render_template, request, jsonify
from elasticsearch import Elasticsearch
from generator_enhanced import EnhancedObservabilityGenerator, IndustryConfig
from demo_scenarios import DemoScenarios
import threading
import time

app = Flask(__name__)

# Global state
es_client = None
generator = None
generation_thread = None
stop_generation = False

@app.route('/')
def index():
    """Render main page"""
    return render_template('index_advanced.html')

@app.route('/api/connect', methods=['POST'])
def connect_elasticsearch():
    """Connect to Elasticsearch with enhanced validation"""
    global es_client
    
    data = request.json
    cloud_id = data.get('cloud_id')
    api_key = data.get('api_key')
    
    if not cloud_id or not api_key:
        return jsonify({'error': 'Cloud ID and API Key are required'}), 400
    
    try:
        es_client = Elasticsearch(
            cloud_id=cloud_id,
            api_key=api_key,
            request_timeout=30,
            max_retries=3,
            retry_on_timeout=True
        )
        
        # Test connection and validate permissions
        info = es_client.info()
        
        # Try to check if we can write to traces
        try:
            # Test write permission
            test_doc = {
                '@timestamp': '2024-01-01T00:00:00.000Z',
                'test': 'connection_validation'
            }
            es_client.index(index='traces-apm-test', document=test_doc)
            # Clean up test document
            es_client.delete_by_query(
                index='traces-apm-test',
                body={'query': {'match': {'test': 'connection_validation'}}}
            )
        except Exception as write_error:
            print(f"Warning: Write test failed: {write_error}")
            # Continue anyway, we'll handle errors during generation
        
        return jsonify({
            'success': True,
            'cluster_name': info['cluster_name'],
            'version': info['version']['number']
        })
    
    except Exception as e:
        es_client = None
        return jsonify({'error': f'Connection failed: {str(e)}'}), 500

@app.route('/api/industries', methods=['GET'])
def get_industries():
    """Get available industries with service counts"""
    industries = {}
    for name, config in IndustryConfig.INDUSTRIES.items():
        industries[name] = {
            'name': config['name'],
            'icon': config['icon'],
            'service_count': len(config['services']),
            'has_dependencies': len(config['dependencies']) > 0
        }
    return jsonify(industries)

@app.route('/api/scenarios', methods=['GET'])
def get_scenarios():
    """Get scenarios for a specific industry"""
    industry = request.args.get('industry')
    
    if not industry:
        return jsonify({'error': 'Industry parameter required'}), 400
    
    if industry not in IndustryConfig.INDUSTRIES:
        return jsonify({'error': 'Invalid industry'}), 400
    
    # Get scenarios for this industry
    scenarios = DemoScenarios.get_scenarios_for_industry(industry)
    
    # Format for frontend
    formatted_scenarios = {}
    for key, scenario in scenarios.items():
        formatted_scenarios[key] = {
            'name': scenario['name'],
            'description': scenario['description'],
            'story': scenario.get('story', ''),
            'error_rate': scenario.get('error_rate', 0.02),
            'latency_multiplier': scenario.get('latency_multiplier', 1.0)
        }
    
    return jsonify(formatted_scenarios)

@app.route('/api/generate', methods=['POST'])
def start_generation():
    """Start enhanced data generation"""
    global generator, generation_thread, stop_generation, es_client
    
    if not es_client:
        return jsonify({'error': 'Not connected to Elasticsearch'}), 400
    
    data = request.json
    industry = data.get('industry')
    scenario_key = data.get('scenario')
    duration_minutes = data.get('duration', 10)
    events_per_second = data.get('rate', 17)
    use_llm = data.get('use_llm', False)
    llm_provider = data.get('llm_provider', 'openai')
    llm_api_key = data.get('llm_api_key', '')
    
    if industry not in IndustryConfig.INDUSTRIES:
        return jsonify({'error': 'Invalid industry'}), 400
    
    # Get scenario configuration
    scenario = None
    if scenario_key:
        all_scenarios = DemoScenarios.get_scenarios_for_industry(industry)
        scenario = all_scenarios.get(scenario_key)
    
    # Create enhanced generator
    try:
        generator = EnhancedObservabilityGenerator(
            es_client, 
            industry,
            scenario=scenario,
            use_llm=use_llm,
            llm_provider=llm_provider,
            llm_api_key=llm_api_key
        )
        print(f"✅ Generator created for {industry}")
        if scenario:
            print(f"📋 Scenario: {scenario.get('name')}")
            print(f"   Error rate: {scenario.get('error_rate', 0.02)*100}%")
            print(f"   Latency multiplier: {scenario.get('latency_multiplier', 1.0)}x")
    except Exception as e:
        return jsonify({'error': f'Failed to create generator: {str(e)}'}), 500
    
    stop_generation = False
    
    # Start generation in background thread
    def generate():
        global stop_generation
        start_time = time.time()
        end_time = start_time + (duration_minutes * 60)
        
        print(f"🚀 Starting data generation...")
        print(f"   Duration: {duration_minutes} minutes")
        print(f"   Rate: {events_per_second} events/second")
        
        batch_count = 0
        error_count = 0
        
        while time.time() < end_time and not stop_generation:
            try:
                generator.generate_batch(events_per_second)
                batch_count += 1
                
                # Log progress every 30 seconds
                if batch_count % 30 == 0:
                    stats = generator.get_stats()
                    print(f"📊 Progress: {stats['traces']} traces, {stats['logs']} logs, {stats['synthetics']} synthetics")
                
                time.sleep(1)
            except Exception as e:
                error_count += 1
                print(f"❌ Error generating batch {batch_count}: {e}")
                
                # Stop if too many consecutive errors
                if error_count > 10:
                    print("⚠️ Too many errors, stopping generation")
                    break
                
                time.sleep(1)
        
        print(f"✅ Generation completed! Generated {batch_count} batches")
        stats = generator.get_stats()
        print(f"📈 Final stats: {stats['traces']} traces, {stats['logs']} logs, {stats['synthetics']} synthetics")
    
    generation_thread = threading.Thread(target=generate)
    generation_thread.daemon = True
    generation_thread.start()
    
    return jsonify({'success': True, 'message': 'Generation started'})

@app.route('/api/stop', methods=['POST'])
def stop_generation_api():
    """Stop data generation"""
    global stop_generation
    stop_generation = True
    print("⏹️ Stop requested by user")
    return jsonify({'success': True})

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get generation statistics"""
    global generator
    
    if not generator:
        return jsonify({
            'traces': 0,
            'logs': 0,
            'synthetics': 0,
            'elapsed_seconds': 0,
            'traces_per_second': 0
        })
    
    stats = generator.get_stats()
    return jsonify(stats)

@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'es_connected': es_client is not None,
        'generating': generation_thread is not None and generation_thread.is_alive()
    })

if __name__ == '__main__':
    print("=" * 80)
    print("🎯 ENHANCED Elastic Observability Data Generator")
    print("=" * 80)
    print("✨ Features:")
    print("   • High-quality distributed traces with proper parent-child relationships")
    print("   • Realistic service dependencies for accurate service maps")
    print("   • Detailed span metadata for APM correlation")
    print("   • Industry-specific scenarios with realistic failure patterns")
    print("=" * 80)
    print("✅ Server starting...")
    print("🌐 Open your browser to: http://localhost:8080")
    print("⏹️  Press Ctrl+C to stop")
    print("=" * 80)
    
    app.run(debug=False, host='0.0.0.0', port=8080)