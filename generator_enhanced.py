#!/usr/bin/env python3
"""
Enhanced Observability Data Generator with High-Quality Service Maps
Generates proper distributed traces with accurate parent-child relationships
"""

import random
import time
from datetime import datetime, timedelta
from faker import Faker
import uuid

fake = Faker()

class IndustryConfig:
    """Industry-specific service configurations with realistic dependencies"""
    
    INDUSTRIES = {
        'ecommerce': {
            'name': 'E-Commerce Platform',
            'icon': '🛒',
            'services': [
                'web-frontend', 'mobile-app', 'product-catalog', 'search-service',
                'shopping-cart', 'checkout-service', 'payment-gateway',
                'order-processing', 'inventory-service', 'shipping-service',
                'recommendation-engine', 'user-service', 'review-service',
                'notification-service', 'analytics-service', 'image-service',
                'redis-cache', 'postgres-db', 'mongodb-catalog'
            ],
            'dependencies': {
                'web-frontend': ['product-catalog', 'search-service', 'shopping-cart', 'user-service', 'redis-cache'],
                'mobile-app': ['product-catalog', 'shopping-cart', 'user-service', 'redis-cache'],
                'product-catalog': ['inventory-service', 'image-service', 'postgres-db', 'redis-cache'],
                'search-service': ['product-catalog', 'recommendation-engine', 'mongodb-catalog'],
                'shopping-cart': ['product-catalog', 'user-service', 'redis-cache'],
                'checkout-service': ['shopping-cart', 'payment-gateway', 'inventory-service', 'user-service'],
                'payment-gateway': ['order-processing', 'notification-service'],
                'order-processing': ['inventory-service', 'shipping-service', 'notification-service', 'postgres-db'],
                'recommendation-engine': ['product-catalog', 'user-service', 'analytics-service'],
                'shipping-service': ['notification-service', 'postgres-db'],
                'review-service': ['user-service', 'product-catalog', 'mongodb-catalog'],
                'inventory-service': ['postgres-db', 'notification-service']
            }
        },
        'banking': {
            'name': 'Digital Banking',
            'icon': '🏦',
            'services': [
                'mobile-banking', 'web-banking', 'api-gateway',
                'auth-service', 'account-service', 'transaction-service',
                'payment-service', 'card-service', 'loan-service',
                'fraud-detection', 'kyc-service', 'notification-service',
                'reporting-service', 'audit-service', 'currency-service',
                'redis-cache', 'postgres-db', 'kafka-broker'
            ],
            'dependencies': {
                'mobile-banking': ['api-gateway', 'auth-service', 'redis-cache'],
                'web-banking': ['api-gateway', 'auth-service', 'redis-cache'],
                'api-gateway': ['auth-service', 'account-service', 'transaction-service'],
                'auth-service': ['kyc-service', 'redis-cache', 'postgres-db'],
                'account-service': ['transaction-service', 'fraud-detection', 'postgres-db'],
                'transaction-service': ['payment-service', 'fraud-detection', 'audit-service', 'kafka-broker'],
                'payment-service': ['card-service', 'notification-service', 'postgres-db'],
                'fraud-detection': ['audit-service', 'notification-service', 'kafka-broker'],
                'loan-service': ['account-service', 'credit-check', 'notification-service'],
                'reporting-service': ['account-service', 'transaction-service', 'postgres-db']
            }
        },
        'gaming': {
            'name': 'Online Gaming',
            'icon': '🎮',
            'services': [
                'game-client', 'game-server', 'matchmaking-service',
                'player-service', 'session-service', 'chat-service',
                'leaderboard-service', 'achievement-service', 'inventory-service',
                'store-service', 'payment-service', 'anti-cheat',
                'voice-service', 'analytics-service', 'cdn-service',
                'redis-cache', 'mongodb-player', 'postgres-db'
            ],
            'dependencies': {
                'game-client': ['game-server', 'cdn-service'],
                'game-server': ['matchmaking-service', 'player-service', 'session-service', 'anti-cheat'],
                'matchmaking-service': ['player-service', 'leaderboard-service', 'redis-cache'],
                'player-service': ['inventory-service', 'achievement-service', 'mongodb-player'],
                'session-service': ['redis-cache', 'analytics-service'],
                'chat-service': ['player-service', 'anti-cheat', 'redis-cache'],
                'store-service': ['inventory-service', 'payment-service', 'player-service'],
                'leaderboard-service': ['player-service', 'redis-cache', 'analytics-service'],
                'inventory-service': ['player-service', 'mongodb-player'],
                'achievement-service': ['player-service', 'analytics-service', 'mongodb-player']
            }
        },
        'healthcare': {
            'name': 'Healthcare System',
            'icon': '🏥',
            'services': [
                'patient-portal', 'provider-portal', 'appointment-service',
                'ehr-service', 'billing-service', 'insurance-service',
                'prescription-service', 'lab-service', 'imaging-service',
                'telemedicine-service', 'notification-service', 'compliance-service',
                'integration-hub', 'analytics-service', 'patient-monitoring',
                'redis-cache', 'postgres-db', 'mongodb-ehr'
            ],
            'dependencies': {
                'patient-portal': ['appointment-service', 'ehr-service', 'prescription-service', 'redis-cache'],
                'provider-portal': ['ehr-service', 'appointment-service', 'lab-service', 'redis-cache'],
                'appointment-service': ['notification-service', 'patient-monitoring', 'postgres-db'],
                'ehr-service': ['prescription-service', 'lab-service', 'imaging-service', 'mongodb-ehr'],
                'billing-service': ['insurance-service', 'compliance-service', 'postgres-db'],
                'prescription-service': ['ehr-service', 'notification-service', 'postgres-db'],
                'lab-service': ['ehr-service', 'integration-hub', 'postgres-db'],
                'telemedicine-service': ['ehr-service', 'appointment-service', 'notification-service'],
                'insurance-service': ['integration-hub', 'compliance-service', 'postgres-db']
            }
        },
        'logistics': {
            'name': 'Logistics Platform',
            'icon': '📦',
            'services': [
                'customer-portal', 'driver-app', 'order-service',
                'warehouse-service', 'inventory-service', 'shipping-service',
                'tracking-service', 'route-optimization', 'fleet-management',
                'billing-service', 'analytics-service', 'notification-service',
                'integration-hub', 'customs-service', 'delivery-service',
                'redis-cache', 'postgres-db', 'mongodb-tracking'
            ],
            'dependencies': {
                'customer-portal': ['order-service', 'tracking-service', 'redis-cache'],
                'driver-app': ['delivery-service', 'route-optimization', 'tracking-service'],
                'order-service': ['warehouse-service', 'shipping-service', 'inventory-service', 'postgres-db'],
                'warehouse-service': ['inventory-service', 'route-optimization', 'postgres-db'],
                'shipping-service': ['tracking-service', 'notification-service', 'integration-hub'],
                'tracking-service': ['mongodb-tracking', 'notification-service', 'analytics-service'],
                'route-optimization': ['fleet-management', 'delivery-service', 'redis-cache'],
                'fleet-management': ['driver-app', 'analytics-service', 'postgres-db'],
                'delivery-service': ['tracking-service', 'notification-service', 'mongodb-tracking']
            }
        },
        'insurance': {
            'name': 'Insurance Platform',
            'icon': '🛡️',
            'services': [
                'customer-portal', 'agent-portal', 'policy-service',
                'claims-service', 'underwriting-service', 'risk-assessment',
                'premium-calculation', 'payment-service', 'document-service',
                'fraud-detection', 'notification-service', 'reporting-service',
                'renewal-service', 'quote-engine', 'integration-hub',
                'redis-cache', 'postgres-db', 'mongodb-documents'
            ],
            'dependencies': {
                'customer-portal': ['policy-service', 'claims-service', 'payment-service', 'redis-cache'],
                'agent-portal': ['quote-engine', 'underwriting-service', 'customer-service', 'redis-cache'],
                'policy-service': ['premium-calculation', 'renewal-service', 'postgres-db'],
                'claims-service': ['fraud-detection', 'document-service', 'payment-service', 'postgres-db'],
                'underwriting-service': ['risk-assessment', 'quote-engine', 'integration-hub'],
                'risk-assessment': ['integration-hub', 'analytics-service', 'postgres-db'],
                'quote-engine': ['premium-calculation', 'policy-service', 'redis-cache'],
                'fraud-detection': ['claims-service', 'notification-service', 'analytics-service'],
                'document-service': ['mongodb-documents', 'notification-service']
            }
        }
    }

class EnhancedObservabilityGenerator:
    """Enhanced generator with high-quality distributed traces"""
    
    def __init__(self, es_client, industry='ecommerce', scenario=None, use_llm=False, llm_provider='openai', llm_api_key=''):
        self.es = es_client
        self.industry = industry
        self.config = IndustryConfig.INDUSTRIES[industry]
        self.services = self.config['services']
        self.dependencies = self.config['dependencies']
        self.scenario = scenario
        
        # Statistics
        self.stats = {
            'traces_generated': 0,
            'logs_generated': 0,
            'synthetics_generated': 0,
            'start_time': time.time()
        }
        
        # Service metadata for realistic spans
        self.service_types = {
            'cache': ['redis', 'memcached'],
            'database': ['postgres', 'mysql', 'mongodb'],
            'queue': ['kafka', 'rabbitmq', 'sqs'],
            'external': ['payment', 'shipping', 'notification', 'integration'],
            'storage': ['s3', 'gcs', 'blob']
        }
    
    def _get_service_type(self, service_name):
        """Determine service type for proper span configuration"""
        service_lower = service_name.lower()
        
        if any(x in service_lower for x in ['redis', 'cache', 'memcached']):
            return 'cache', 'redis'
        elif any(x in service_lower for x in ['postgres', 'mysql', 'db']):
            return 'db', 'postgresql'
        elif any(x in service_lower for x in ['mongo']):
            return 'db', 'mongodb'
        elif any(x in service_lower for x in ['kafka', 'queue', 'rabbitmq']):
            return 'messaging', 'kafka'
        elif any(x in service_lower for x in ['s3', 'storage', 'blob']):
            return 'storage', 's3'
        else:
            return 'external', 'http'
    
    def _get_error_rate(self):
        """Get error rate based on scenario"""
        if not self.scenario:
            return 0.02
        return self.scenario.get('error_rate', 0.02)
    
    def _get_latency_multiplier(self, service_name):
        """Get latency multiplier based on scenario"""
        if not self.scenario:
            return 1.0
        
        affected = self.scenario.get('affected_services', [])
        if affected and service_name not in affected:
            return 1.0
        
        return self.scenario.get('latency_multiplier', 1.0)
    
    def generate_distributed_trace(self):
        """Generate a complete distributed trace with proper parent-child relationships"""
        trace_id = str(uuid.uuid4())
        timestamp = datetime.utcnow()
        
        # Select entry point service (frontend/gateway)
        entry_services = [s for s in self.services if any(x in s.lower() for x in ['frontend', 'app', 'portal', 'gateway', 'client'])]
        root_service = random.choice(entry_services) if entry_services else self.services[0]
        
        # Generate transaction ID
        transaction_id = str(uuid.uuid4())
        
        # Determine transaction details
        transaction_types = {
            'web-frontend': [
                ('GET /products', 'GET', '/products'),
                ('GET /product/:id', 'GET', '/product/12345'),
                ('POST /cart/add', 'POST', '/cart/add'),
                ('GET /checkout', 'GET', '/checkout')
            ],
            'mobile-app': [
                ('POST /api/login', 'POST', '/api/login'),
                ('GET /api/products', 'GET', '/api/products'),
                ('POST /api/orders', 'POST', '/api/orders')
            ],
            'mobile-banking': [
                ('POST /api/transfer', 'POST', '/api/transfer'),
                ('GET /api/accounts', 'GET', '/api/accounts'),
                ('GET /api/transactions', 'GET', '/api/transactions')
            ],
            'game-client': [
                ('POST /match/join', 'POST', '/match/join'),
                ('GET /player/stats', 'GET', '/player/stats'),
                ('POST /game/action', 'POST', '/game/action')
            ],
            'patient-portal': [
                ('GET /appointments', 'GET', '/appointments'),
                ('POST /appointments/book', 'POST', '/appointments/book'),
                ('GET /records', 'GET', '/records')
            ]
        }
        
        # Find matching transaction type
        transaction_name = 'GET /'
        http_method = 'GET'
        http_path = '/'
        
        for key, txns in transaction_types.items():
            if key in root_service.lower():
                transaction_name, http_method, http_path = random.choice(txns)
                break
        
        # Calculate duration with scenario effects
        error_rate = self._get_error_rate()
        latency_mult = self._get_latency_multiplier(root_service)
        base_duration_ms = random.randint(100, 800)
        
        # Build complete trace with all spans
        all_spans_duration = 0
        child_spans = []
        
        if root_service in self.dependencies:
            # Generate all child spans first to calculate total duration
            for child_service in self.dependencies[root_service]:
                span_duration = self._calculate_span_duration(child_service, latency_mult)
                all_spans_duration += span_duration
                child_spans.append((child_service, span_duration))
        
        # Transaction duration should be >= sum of child spans
        transaction_duration_ms = max(base_duration_ms * latency_mult, all_spans_duration + random.randint(10, 50))
        
        is_error = random.random() < error_rate
        
        # Create root transaction document
        transaction_doc = {
            '@timestamp': timestamp.isoformat(),
            'timestamp': {'us': int(timestamp.timestamp() * 1000000)},
            'trace': {'id': trace_id},
            'transaction': {
                'id': transaction_id,
                'name': transaction_name,
                'type': 'request',
                'duration': {'us': int(transaction_duration_ms * 1000)},
                'result': 'HTTP 5xx' if is_error else 'HTTP 2xx',
                'sampled': True,
                'span_count': {
                    'started': len(child_spans)
                }
            },
            'event': {
                'outcome': 'failure' if is_error else 'success'
            },
            'processor': {
                'event': 'transaction',
                'name': 'transaction'
            },
            'http': {
                'request': {
                    'method': http_method
                },
                'response': {
                    'status_code': 500 if is_error else 200
                },
                'version': '1.1'
            },
            'url': {
                'path': http_path,
                'scheme': 'https',
                'domain': f'{root_service}.{self.industry}.example.com',
                'full': f'https://{root_service}.{self.industry}.example.com{http_path}'
            },
            'user_agent': {
                'original': random.choice([
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/91.0',
                    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X)'
                ])
            },
            'client': {
                'ip': f'{random.randint(10,200)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}'
            },
            'service': {
                'name': root_service,
                'environment': 'production',
                'node': {
                    'name': f'{root_service}-{random.randint(1,3):02d}'
                },
                'language': {
                    'name': 'python',
                    'version': '3.9.0'
                }
            },
            'agent': {
                'name': 'python',
                'version': '6.15.0',
                'ephemeral_id': str(uuid.uuid4())
            },
            'host': {
                'hostname': f'{root_service}-{random.randint(1,5):02d}',
                'name': f'{root_service}-{random.randint(1,5):02d}',
                'ip': f'10.0.{random.randint(1,255)}.{random.randint(1,255)}'
            },
            'labels': {
                'industry': self.industry,
                'environment': 'production'
            }
        }
        
        if self.scenario:
            transaction_doc['labels']['scenario'] = self.scenario.get('name', 'unknown')
        
        # Index transaction
        try:
            self.es.index(index='traces-apm-default', document=transaction_doc)
        except Exception:
            self.es.index(index='apm-8.0.0-transaction', document=transaction_doc)
        
        # Generate child spans with proper parent reference
        span_offset = 5  # Start 5ms after transaction
        for child_service, span_duration in child_spans:
            self._generate_enhanced_span(
                trace_id=trace_id,
                parent_id=transaction_id,
                service_name=child_service,
                timestamp=timestamp,
                offset_ms=span_offset,
                duration_ms=span_duration,
                is_error=is_error and random.random() < 0.3  # Propagate some errors
            )
            span_offset += span_duration + random.randint(1, 5)
        
        self.stats['traces_generated'] += 1
    
    def _calculate_span_duration(self, service_name, latency_mult):
        """Calculate realistic span duration"""
        service_type, _ = self._get_service_type(service_name)
        
        # Different services have different typical latencies
        if service_type == 'cache':
            base = random.randint(1, 10)
        elif service_type == 'db':
            base = random.randint(5, 50)
        elif service_type == 'messaging':
            base = random.randint(10, 100)
        else:
            base = random.randint(20, 200)
        
        return int(base * latency_mult)
    
    def _generate_enhanced_span(self, trace_id, parent_id, service_name, timestamp, offset_ms, duration_ms, is_error):
        """Generate enhanced span with full service map details"""
        span_id = str(uuid.uuid4())
        span_timestamp = timestamp + timedelta(milliseconds=offset_ms)
        
        service_type, subtype = self._get_service_type(service_name)
        
        # Build comprehensive span document
        span_doc = {
            '@timestamp': span_timestamp.isoformat(),
            'timestamp': {'us': int(span_timestamp.timestamp() * 1000000)},
            'trace': {'id': trace_id},
            'parent': {'id': parent_id},
            'span': {
                'id': span_id,
                'name': self._get_span_name(service_name, service_type),
                'type': service_type,
                'subtype': subtype,
                'duration': {'us': int(duration_ms * 1000)}
            },
            'event': {
                'outcome': 'failure' if is_error else 'success'
            },
            'processor': {
                'event': 'span',
                'name': 'transaction'
            },
            'observer': {
                'version': '8.0.0',
                'type': 'apm-server'
            },
            'service': {
                'name': service_name,
                'environment': 'production',
                'node': {
                    'name': f'{service_name}-{random.randint(1,3):02d}'
                },
                'target': {
                    'type': subtype,
                    'name': service_name
                }
            },
            'destination': {
                'service': {
                    'name': service_name,
                    'resource': f'{subtype}/{service_name}',
                    'type': subtype
                }
            },
            'agent': {
                'name': 'python',
                'version': '6.15.0'
            },
            'labels': {
                'industry': self.industry,
                'environment': 'production'
            }
        }
        
        # Add type-specific metadata
        if service_type == 'db':
            span_doc['db'] = {
                'instance': service_name,
                'type': subtype,
                'statement': self._get_db_statement(subtype)
            }
        elif service_type == 'cache':
            span_doc['db'] = {
                'type': 'redis',
                'statement': random.choice(['GET', 'SET', 'HGETALL', 'ZADD'])
            }
        elif service_type == 'messaging':
            span_doc['message'] = {
                'queue': {'name': f'{service_name}-queue'}
            }
        
        # Index span
        try:
            self.es.index(index='traces-apm-default', document=span_doc)
        except Exception:
            self.es.index(index='apm-8.0.0-span', document=span_doc)
    
    def _get_span_name(self, service_name, service_type):
        """Generate realistic span names"""
        if service_type == 'db':
            return f'SELECT FROM {service_name}'
        elif service_type == 'cache':
            return f'GET {service_name}'
        elif service_type == 'messaging':
            return f'SEND {service_name}'
        else:
            return f'POST {service_name}/process'
    
    def _get_db_statement(self, db_type):
        """Generate realistic database statements"""
        statements = {
            'postgresql': [
                'SELECT * FROM users WHERE id = $1',
                'UPDATE products SET stock = stock - 1 WHERE id = $1',
                'INSERT INTO orders (user_id, total) VALUES ($1, $2)',
                'SELECT * FROM accounts WHERE user_id = $1 AND active = true'
            ],
            'mongodb': [
                'db.products.find({category: "electronics"})',
                'db.users.updateOne({_id: ObjectId()}, {$set: {lastLogin: new Date()}})',
                'db.orders.aggregate([{$match: {status: "pending"}}])'
            ]
        }
        return random.choice(statements.get(db_type, statements['postgresql']))
    
    def generate_log(self):
        """Generate application log"""
        service = random.choice(self.services)
        
        if self.scenario and random.random() < self._get_error_rate() * 5:
            log_levels = ['WARN', 'ERROR']
            weights = [0.6, 0.4]
        else:
            log_levels = ['INFO', 'WARN', 'ERROR', 'DEBUG']
            weights = [0.70, 0.15, 0.05, 0.10]
        
        level = random.choices(log_levels, weights=weights)[0]
        message = self._get_log_message(level, service)
        
        log_doc = {
            '@timestamp': datetime.utcnow().isoformat(),
            'service.name': service,
            'log.level': level,
            'message': message,
            'labels': {
                'industry': self.industry,
                'environment': 'production'
            }
        }
        
        if self.scenario:
            log_doc['labels']['scenario'] = self.scenario.get('name', 'unknown')
        
        self.es.index(index=f'logs-{self.industry}', document=log_doc)
        self.stats['logs_generated'] += 1
    
    def _get_log_message(self, level, service):
        """Generate contextual log messages"""
        messages = {
            'INFO': [
                f'{service}: Request processed successfully in 45ms',
                f'{service}: Cache hit rate: 87%',
                f'{service}: Health check passed',
                f'{service}: Connected to downstream service'
            ],
            'WARN': [
                f'{service}: High latency detected: 250ms (threshold: 200ms)',
                f'{service}: Retry attempt 2/3 for downstream call',
                f'{service}: Cache miss rate elevated: 25%',
                f'{service}: Memory usage at 78% of limit'
            ],
            'ERROR': [
                f'{service}: Connection pool exhausted (max: 50)',
                f'{service}: Database query timeout after 30s',
                f'{service}: Failed to connect to downstream service after 3 retries',
                f'{service}: Uncaught exception: NullPointerException in request handler'
            ],
            'DEBUG': [
                f'{service}: Processing request ID: {uuid.uuid4()}',
                f'{service}: Executing database query',
                f'{service}: Validating request payload'
            ]
        }
        return random.choice(messages.get(level, messages['INFO']))
    
    def generate_synthetic_check(self):
        """Generate synthetic monitoring check"""
        service = random.choice(self.services)
        
        if self.scenario:
            uptime_rate = 1.0 - (self._get_error_rate() * 2)
        else:
            uptime_rate = 0.98
        
        is_up = random.random() < uptime_rate
        
        synthetic_doc = {
            '@timestamp': datetime.utcnow().isoformat(),
            'monitor.name': f'{service}-health',
            'monitor.type': 'http',
            'monitor.status': 'up' if is_up else 'down',
            'monitor.duration.us': random.randint(50000, 300000),
            'observer.geo.name': random.choice(['us-east-1', 'us-west-2', 'eu-west-1', 'ap-southeast-1']),
            'url.full': f'https://{service}.{self.industry}.example.com/health',
            'http.response.status_code': 200 if is_up else 503
        }
        
        self.es.index(index=f'synthetics-{self.industry}', document=synthetic_doc)
        self.stats['synthetics_generated'] += 1
    
    def generate_batch(self, events_per_second=17):
        """Generate batch of events"""
        traces = int(events_per_second * 0.6)
        logs = int(events_per_second * 0.3)
        synthetics = int(events_per_second * 0.1)
        
        for _ in range(traces):
            self.generate_distributed_trace()
        
        for _ in range(logs):
            self.generate_log()
        
        for _ in range(synthetics):
            self.generate_synthetic_check()
    
    def get_stats(self):
        """Get generation statistics"""
        elapsed = time.time() - self.stats['start_time']
        return {
            'traces': self.stats['traces_generated'],
            'logs': self.stats['logs_generated'],
            'synthetics': self.stats['synthetics_generated'],
            'elapsed_seconds': int(elapsed),
            'traces_per_second': round(self.stats['traces_generated'] / elapsed, 2) if elapsed > 0 else 0
        }