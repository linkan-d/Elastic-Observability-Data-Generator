# 🔧 Troubleshooting Guide

## Issue: "Select Industry" Shows No Options

### Problem
After connecting to Elasticsearch, the industry selection section appears but no industry cards are displayed.

### Root Cause
The Flask backend is missing the required API endpoints that the frontend calls to fetch industry and scenario data.

### Solution

Make sure you have **all the required files** with the correct code:

#### ✅ **File Checklist**

```
elastic-demo-advanced/
├── requirements_advanced.txt     ✅ Dependencies
├── app_advanced.py               ✅ Flask backend with ALL API endpoints
├── generator_advanced.py         ✅ Data generator with IndustryConfig
├── demo_scenarios.py             ✅ 30 scenarios
├── llm_generator.py              ✅ LLM integration (optional)
└── templates/
    └── index_advanced.html       ✅ Web UI
```

#### ✅ **Required API Endpoints in app_advanced.py**

Your `app_advanced.py` must include these endpoints:

```python
@app.route('/api/industries', methods=['GET'])
def get_industries():
    """Get available industries"""
    # Returns all 6 industries with icons and service counts

@app.route('/api/scenarios', methods=['GET'])
def get_scenarios():
    """Get scenarios for a specific industry"""
    # Returns scenarios based on industry parameter

@app.route('/api/connect', methods=['POST'])
def connect_elasticsearch():
    """Connect to Elasticsearch"""
    # Establishes connection and tests it

@app.route('/api/generate', methods=['POST'])
def start_generation():
    """Start data generation"""
    # Starts background data generation

@app.route('/api/stop', methods=['POST'])
def stop_generation_api():
    """Stop data generation"""
    # Stops the generation process

@app.route('/api/stats', methods=['GET'])
def get_stats():
    """Get generation statistics"""
    # Returns real-time stats
```

### Step-by-Step Fix

#### Step 1: Verify File Structure

```bash
# Check all files exist
ls -la elastic-demo-advanced/
ls -la elastic-demo-advanced/templates/

# Should show:
# app_advanced.py
# generator_advanced.py
# demo_scenarios.py
# llm_generator.py
# requirements_advanced.txt
# templates/index_advanced.html
```

#### Step 2: Check Flask App is Running

```bash
python app_advanced.py
```

You should see:
```
============================================================
🎯 Elastic Observability Data Generator - ADVANCED
============================================================
✅ Server starting...
🌐 Open your browser to: http://localhost:5000
⏹️  Press Ctrl+C to stop
============================================================
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
```

#### Step 3: Test API Endpoints Manually

Open a new terminal and test:

```bash
# Test if industries endpoint works
curl http://localhost:5000/api/industries

# Should return JSON like:
# {"ecommerce":{"name":"E-Commerce Platform","icon":"🛒","service_count":13},...}
```

#### Step 4: Check Browser Console

1. Open browser to http://localhost:5000
2. Press **F12** to open Developer Tools
3. Click **Console** tab
4. Look for errors like:
   - `404 Not Found` for `/api/industries`
   - `500 Internal Server Error`
   - JavaScript errors

#### Step 5: Check Python Errors

In the terminal where Flask is running, look for errors like:

```python
ImportError: cannot import name 'IndustryConfig' from 'generator_advanced'
```

This means `generator_advanced.py` is missing or incomplete.

### Common Issues & Fixes

#### Issue 1: ImportError

**Error:**
```
ImportError: cannot import name 'IndustryConfig'
```

**Fix:**
Make sure `generator_advanced.py` includes the `IndustryConfig` class at the top:

```python
class IndustryConfig:
    """Industry-specific service configurations"""
    
    INDUSTRIES = {
        'ecommerce': {...},
        'banking': {...},
        # ... etc
    }
```

#### Issue 2: 404 Not Found

**Error in browser console:**
```
GET http://localhost:5000/api/industries 404 (Not Found)
```

**Fix:**
Your `app_advanced.py` is missing the endpoint. Add:

```python
@app.route('/api/industries', methods=['GET'])
def get_industries():
    from generator_advanced import IndustryConfig
    industries = {}
    for name, config in IndustryConfig.INDUSTRIES.items():
        industries[name] = {
            'name': config['name'],
            'icon': config['icon'],
            'service_count': len(config['services'])
        }
    return jsonify(industries)
```

#### Issue 3: Empty Response

**Browser console shows:**
```
{}
```

**Fix:**
Check that `IndustryConfig.INDUSTRIES` actually has data in `generator_advanced.py`.

#### Issue 4: Module Not Found

**Error:**
```
ModuleNotFoundError: No module named 'generator_advanced'
```

**Fix:**
Make sure you're running Flask from the correct directory:

```bash
cd elastic-demo-advanced
python app_advanced.py  # Run from this directory!
```

#### Issue 5: Wrong HTML Template

**Error:**
```
TemplateNotFound: index_advanced.html
```

**Fix:**
```bash
# Create templates directory
mkdir templates

# Move HTML file
mv index_advanced.html templates/
```

### Testing Checklist

Run through these steps:

- [ ] Start Flask: `python app_advanced.py`
- [ ] Open browser: http://localhost:5000
- [ ] Check page loads (no blank screen)
- [ ] Enter Cloud ID and API Key
- [ ] Click "Connect to Elasticsearch"
- [ ] See green "✅ Connected" badge
- [ ] See 6 industry cards appear
- [ ] Click an industry (e.g., E-Commerce)
- [ ] See scenarios list appear
- [ ] See configuration section appear

### Quick Validation Script

Create a file `test_imports.py`:

```python
#!/usr/bin/env python3
"""Test if all imports work"""

print("Testing imports...")

try:
    from generator_advanced import IndustryConfig
    print("✅ IndustryConfig imported")
    print(f"   Found {len(IndustryConfig.INDUSTRIES)} industries")
except Exception as e:
    print(f"❌ IndustryConfig import failed: {e}")

try:
    from demo_scenarios import DemoScenarios
    print("✅ DemoScenarios imported")
    all_scenarios = DemoScenarios.get_all_scenarios()
    total = sum(len(scenarios) for scenarios in all_scenarios.values())
    print(f"   Found {total} total scenarios")
except Exception as e:
    print(f"❌ DemoScenarios import failed: {e}")

try:
    from flask import Flask
    print("✅ Flask imported")
except Exception as e:
    print(f"❌ Flask import failed: {e}")

try:
    from elasticsearch import Elasticsearch
    print("✅ Elasticsearch imported")
except Exception as e:
    print(f"❌ Elasticsearch import failed: {e}")

print("\nAll checks passed! ✅")
```

Run it:
```bash
python test_imports.py
```

### Still Not Working?

#### Debug Mode

Edit `app_advanced.py` and change the last line to:

```python
app.run(debug=True, host='0.0.0.0', port=5000)
```

This will show detailed error messages.

#### Check Python Version

```bash
python --version
# Should be 3.7 or higher
```

#### Reinstall Dependencies

```bash
pip install --upgrade pip
pip uninstall -y flask elasticsearch faker
pip install -r requirements_advanced.txt
```

#### Start Fresh

```bash
# 1. Stop Flask (Ctrl+C)
# 2. Delete __pycache__ directories
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null

# 3. Restart Flask
python app_advanced.py
```

### Need More Help?

If industries still don't show:

1. **Share the terminal output** where Flask is running
2. **Share browser console errors** (F12 → Console)
3. **Test the API directly:** `curl http://localhost:5000/api/industries`
4. **Check file contents:** `head -20 generator_advanced.py`

The issue is almost always:
- Missing/incomplete `generator_advanced.py`
- Missing API endpoint in `app_advanced.py`  
- Running Flask from wrong directory
- Import errors due to typos

---

## Other Common Issues

### No Data Appearing in Kibana

**Problem:** Data is generated but not visible in Kibana.

**Solutions:**
1. **Wait 1-2 minutes** for indexing
2. **Refresh the page**
3. **Check time range** - Set to "Last 15 minutes"
4. **Verify indices exist:**
   ```
   GET _cat/indices/apm*
   GET _cat/indices/logs*
   ```

### Connection Failed

**Problem:** Cannot connect to Elasticsearch.

**Solutions:**
1. **Verify Cloud ID format** (should start with deployment name)
2. **Check API Key** hasn't expired
3. **Test connection:**
   ```bash
   curl -H "Authorization: ApiKey YOUR_API_KEY" \
        https://YOUR_DEPLOYMENT.es.us-east-1.aws.found.io:443
   ```

### High Memory Usage

**Problem:** Python process using too much memory.

**Solutions:**
1. **Lower generation rate** (use Low: 5 events/sec)
2. **Reduce duration** (max 15 minutes)
3. **Restart Flask between runs**

---

**Remember:** The industry cards issue is always a backend problem, not a UI issue. The artifacts I provided above have all the correct code! 🚀