#!/usr/bin/env python3
"""
Demo Scenarios for Observability Data Generator
30 realistic scenarios across 6 industries
"""

class DemoScenarios:
    """Pre-defined demo scenarios for realistic data generation"""
    
    SCENARIOS = {
        # E-COMMERCE SCENARIOS
        'ecommerce': {
            'black-friday': {
                'name': 'Black Friday Traffic Spike',
                'description': 'Traffic increases 10x, latency degrades, some services struggle',
                'story': "It's Black Friday and your e-commerce platform is experiencing unprecedented traffic. The search and recommendation services are showing increased latency.",
                'duration_minutes': 15,
                'error_rate': 0.05,
                'latency_multiplier': 3.0,
                'affected_services': ['search-service', 'recommendation-engine', 'checkout-service']
            },
            'payment-failures': {
                'name': 'Payment Gateway Failures',
                'description': 'Payment gateway experiencing intermittent failures (15% error rate)',
                'story': "The payment gateway is having issues. Customers are reporting failed transactions, causing cart abandonment.",
                'duration_minutes': 20,
                'error_rate': 0.15,
                'latency_multiplier': 2.0,
                'affected_services': ['payment-gateway', 'checkout-service']
            },
            'search-degradation': {
                'name': 'Search Performance Degradation',
                'description': 'Search service response times increase dramatically',
                'story': "Search queries are taking too long. Users are experiencing delays when searching for products.",
                'duration_minutes': 30,
                'error_rate': 0.03,
                'latency_multiplier': 5.0,
                'affected_services': ['search-service']
            },
            'cart-abandonment': {
                'name': 'Cart Abandonment Pattern',
                'description': 'Shopping cart service errors causing abandoned carts',
                'story': "Users are adding items to cart but experiencing errors during checkout flow.",
                'duration_minutes': 25,
                'error_rate': 0.08,
                'latency_multiplier': 1.5,
                'affected_services': ['shopping-cart', 'checkout-service']
            },
            'inventory-sync': {
                'name': 'Inventory Sync Issues',
                'description': 'Inventory management system out of sync, causing overselling',
                'story': "Inventory counts are not updating correctly, leading to overselling and customer complaints.",
                'duration_minutes': 45,
                'error_rate': 0.06,
                'latency_multiplier': 2.5,
                'affected_services': ['inventory-management', 'product-catalog']
            },
            'recommendation-slow': {
                'name': 'Recommendation Engine Slowdown',
                'description': 'ML-powered recommendations taking too long to compute',
                'story': "The recommendation engine is struggling with increased load, causing slow page loads.",
                'duration_minutes': 20,
                'error_rate': 0.02,
                'latency_multiplier': 4.0,
                'affected_services': ['recommendation-engine']
            }
        },
        
        # BANKING SCENARIOS
        'banking': {
            'atm-outage': {
                'name': 'ATM Network Issues',
                'description': 'Regional ATM network experiencing connectivity problems',
                'story': "ATMs across the northeast region are unable to connect to core banking systems.",
                'duration_minutes': 30,
                'error_rate': 0.12,
                'latency_multiplier': 3.0,
                'affected_services': ['transaction-service', 'account-service']
            },
            'fraud-alerts': {
                'name': 'Fraud Detection Alert Storm',
                'description': 'Fraud detection system generating high volume of alerts',
                'story': "The fraud detection system is triggering alerts at 5x normal rate, overwhelming the review queue.",
                'duration_minutes': 40,
                'error_rate': 0.04,
                'latency_multiplier': 2.0,
                'affected_services': ['fraud-detection', 'transaction-service']
            },
            'db-pool-exhaustion': {
                'name': 'Database Connection Pool Exhaustion',
                'description': 'All database connections in use, causing timeouts',
                'story': "The database connection pool is exhausted. Transactions are timing out and failing.",
                'duration_minutes': 25,
                'error_rate': 0.20,
                'latency_multiplier': 4.0,
                'affected_services': ['account-service', 'transaction-service', 'payment-service']
            },
            'mobile-login-fail': {
                'name': 'Mobile App Login Failures',
                'description': 'Authentication service issues preventing mobile logins',
                'story': "Mobile banking users cannot log in. The authentication service is returning errors.",
                'duration_minutes': 15,
                'error_rate': 0.25,
                'latency_multiplier': 1.5,
                'affected_services': ['mobile-banking-app', 'authentication-service']
            },
            'payment-delays': {
                'name': 'Payment Processing Delays',
                'description': 'Payments taking longer than usual to process',
                'story': "Customer payments are being processed but with significant delays, causing frustration.",
                'duration_minutes': 35,
                'error_rate': 0.05,
                'latency_multiplier': 6.0,
                'affected_services': ['payment-service', 'transaction-service']
            },
            'regulatory-report': {
                'name': 'Regulatory Report Generation',
                'description': 'End-of-month regulatory reporting causing system load',
                'story': "Running regulatory compliance reports is putting heavy load on reporting systems.",
                'duration_minutes': 60,
                'error_rate': 0.03,
                'latency_multiplier': 2.5,
                'affected_services': ['reporting-service', 'audit-service']
            }
        },
        
        # INSURANCE SCENARIOS
        'insurance': {
            'claims-backlog': {
                'name': 'Claims Processing Backlog',
                'description': 'High volume of claims causing processing delays',
                'story': "A major storm has resulted in thousands of claims being filed simultaneously.",
                'duration_minutes': 45,
                'error_rate': 0.04,
                'latency_multiplier': 3.5,
                'affected_services': ['claims-processing', 'document-management']
            },
            'renewal-rush': {
                'name': 'Policy Renewal Rush',
                'description': 'End of quarter policy renewals overwhelming the system',
                'story': "It's policy renewal season and the system is processing thousands of renewals per hour.",
                'duration_minutes': 50,
                'error_rate': 0.06,
                'latency_multiplier': 2.5,
                'affected_services': ['policy-management', 'renewal-service', 'payment-service']
            },
            'underwriting-overload': {
                'name': 'Underwriting System Overload',
                'description': 'Risk assessment system struggling with complex calculations',
                'story': "Complex underwriting calculations are taking too long, delaying quote generation.",
                'duration_minutes': 30,
                'error_rate': 0.05,
                'latency_multiplier': 4.0,
                'affected_services': ['underwriting-engine', 'risk-assessment', 'quote-engine']
            },
            'disaster-claims': {
                'name': 'Natural Disaster Claims Surge',
                'description': 'Hurricane causes massive influx of property claims',
                'story': "A hurricane has hit and we're receiving claims at 20x normal volume.",
                'duration_minutes': 120,
                'error_rate': 0.08,
                'latency_multiplier': 3.0,
                'affected_services': ['claims-processing', 'fraud-detection', 'document-management', 'customer-portal']
            }
        },
        
        # GAMING SCENARIOS
        'gaming': {
            'matchmaking-delays': {
                'name': 'Server Matchmaking Delays',
                'description': 'Matchmaking service taking too long to find matches',
                'story': "Players are waiting in queue for extended periods. Matchmaking algorithms are struggling.",
                'duration_minutes': 20,
                'error_rate': 0.04,
                'latency_multiplier': 5.0,
                'affected_services': ['matchmaking-service', 'game-server']
            },
            'ddos-attack': {
                'name': 'DDoS Attack Pattern',
                'description': 'Distributed denial of service attack overwhelming servers',
                'story': "We're under DDoS attack. Game servers are receiving malicious traffic.",
                'duration_minutes': 35,
                'error_rate': 0.30,
                'latency_multiplier': 8.0,
                'affected_services': ['game-server', 'authentication-service', 'session-management']
            },
            'season-launch': {
                'name': 'Season Launch Traffic',
                'description': 'New game season causing massive player surge',
                'story': "New season just launched and we have 10x normal concurrent players trying to log in.",
                'duration_minutes': 40,
                'error_rate': 0.07,
                'latency_multiplier': 4.0,
                'affected_services': ['game-server', 'authentication-service', 'player-service', 'leaderboard-service']
            },
            'store-issues': {
                'name': 'In-game Store Issues',
                'description': 'Microtransaction system experiencing payment failures',
                'story': "Players can't complete purchases in the store. Payment processing is failing.",
                'duration_minutes': 25,
                'error_rate': 0.15,
                'latency_multiplier': 2.0,
                'affected_services': ['store-service', 'payment-service', 'inventory-service']
            },
            'ban-wave': {
                'name': 'Player Ban Wave Processing',
                'description': 'Anti-cheat system processing large ban wave',
                'story': "Anti-cheat detected widespread cheating. Processing thousands of account bans.",
                'duration_minutes': 30,
                'error_rate': 0.03,
                'latency_multiplier': 2.5,
                'affected_services': ['anti-cheat', 'player-service', 'analytics-service']
            }
        },
        
        # HEALTHCARE SCENARIOS
        'healthcare': {
            'ehr-slowdown': {
                'name': 'EHR System Slowdown',
                'description': 'Electronic health records system experiencing performance issues',
                'story': "Physicians are reporting slow access to patient records. EHR system is degraded.",
                'duration_minutes': 35,
                'error_rate': 0.06,
                'latency_multiplier': 4.5,
                'affected_services': ['ehr-service', 'patient-monitoring', 'prescription-service']
            },
            'appointment-surge': {
                'name': 'Appointment Scheduling Surge',
                'description': 'Flu season causing appointment booking spike',
                'story': "It's flu season. Appointment scheduling system overwhelmed with booking requests.",
                'duration_minutes': 45,
                'error_rate': 0.05,
                'latency_multiplier': 3.0,
                'affected_services': ['appointment-scheduling', 'patient-portal', 'notification-service']
            },
            'lab-delays': {
                'name': 'Lab Results Processing Delay',
                'description': 'Lab interface experiencing delays in result delivery',
                'story': "Lab results are delayed. Integration with external lab systems is slow.",
                'duration_minutes': 50,
                'error_rate': 0.08,
                'latency_multiplier': 5.0,
                'affected_services': ['lab-results', 'integration-hub', 'notification-service']
            },
            'emergency-alert': {
                'name': 'Emergency Alert System Test',
                'description': 'Testing emergency notification system under load',
                'story': "Running quarterly emergency notification test. System sending alerts to all providers.",
                'duration_minutes': 15,
                'error_rate': 0.02,
                'latency_multiplier': 2.0,
                'affected_services': ['emergency-service', 'notification-service', 'provider-directory']
            }
        },
        
        # LOGISTICS SCENARIOS
        'logistics': {
            'holiday-rush': {
                'name': 'Holiday Shipping Rush',
                'description': 'Peak holiday season causing system overload',
                'story': "Holiday season is here. Order volumes are 15x normal and system is struggling.",
                'duration_minutes': 60,
                'error_rate': 0.06,
                'latency_multiplier': 3.5,
                'affected_services': ['order-management', 'warehouse-management', 'shipping-service', 'tracking-service']
            },
            'weather-delays': {
                'name': 'Weather-Related Delays',
                'description': 'Severe weather affecting route optimization and tracking',
                'story': "Snowstorm in midwest disrupting deliveries. Route optimization recalculating constantly.",
                'duration_minutes': 90,
                'error_rate': 0.10,
                'latency_multiplier': 4.0,
                'affected_services': ['route-optimization', 'driver-app', 'tracking-service', 'delivery-scheduling']
            },
            'warehouse-automation': {
                'name': 'Warehouse Automation Issues',
                'description': 'Automated warehouse systems experiencing malfunctions',
                'story': "Warehouse robots are reporting errors. Inventory movements are delayed.",
                'duration_minutes': 40,
                'error_rate': 0.12,
                'latency_multiplier': 3.0,
                'affected_services': ['warehouse-management', 'inventory-service', 'order-management']
            },
            'route-failures': {
                'name': 'Route Optimization Failures',
                'description': 'Route calculation system producing suboptimal routes',
                'story': "Route optimization algorithm failing. Drivers getting inefficient routes, increasing costs.",
                'duration_minutes': 35,
                'error_rate': 0.15,
                'latency_multiplier': 6.0,
                'affected_services': ['route-optimization', 'fleet-management']
            },
            'last-mile-surge': {
                'name': 'Last-Mile Delivery Surge',
                'description': 'Same-day delivery promises causing driver app overload',
                'story': "Same-day delivery spike. Driver app struggling with real-time updates and location tracking.",
                'duration_minutes': 30,
                'error_rate': 0.08,
                'latency_multiplier': 2.5,
                'affected_services': ['driver-app', 'delivery-scheduling', 'tracking-service', 'customer-portal']
            }
        }
    }
    
    @staticmethod
    def get_scenarios_for_industry(industry):
        """Get all scenarios for a specific industry"""
        return DemoScenarios.SCENARIOS.get(industry, {})
    
    @staticmethod
    def get_all_scenarios():
        """Get all scenarios across all industries"""
        return DemoScenarios.SCENARIOS
    
    @staticmethod
    def get_scenario(industry, scenario_key):
        """Get a specific scenario"""
        industry_scenarios = DemoScenarios.SCENARIOS.get(industry, {})
        return industry_scenarios.get(scenario_key)