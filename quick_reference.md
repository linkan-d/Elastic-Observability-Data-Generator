# ⚡ Quick Reference Card

## 🚀 Installation (5 minutes)

```bash
# 1. Create project
mkdir elastic-demo-advanced && cd elastic-demo-advanced
mkdir templates

# 2. Copy all 7 files from artifacts above into this directory

# 3. Install dependencies
pip install -r requirements_advanced.txt

# 4. Run
python app_advanced.py

# 5. Open browser
# http://localhost:5000
```

## 📂 Required Files

```
elastic-demo-advanced/
├── requirements_advanced.txt
├── app_advanced.py
├── generator_advanced.py
├── demo_scenarios.py
├── llm_generator.py
└── templates/
    └── index_advanced.html
```

## 🔑 Get Elastic Credentials

### Cloud ID
1. Go to cloud.elastic.co
2. Click your deployment
3. Copy Cloud ID

### API Key
1. In Kibana: Menu → Stack Management → API Keys
2. Create API key with **Superuser** role
3. Copy the key (one-time display!)

## 🎮 Usage Flow

```
1. Connect to Elasticsearch
   └─ Enter Cloud ID + API Key

2. (Optional) Enable LLM
   └─ Toggle on + enter OpenAI/Claude key

3. Select Industry
   └─ E-Commerce, Banking, Insurance, Gaming, Healthcare, or Logistics

4. Select Scenario
   └─ Choose from 4-6 scenarios per industry
   └─ Or "Normal Operations"

5. Configure
   └─ Duration: 5-60 minutes
   └─ Rate: Low/Medium/High

6. Start Generating!
   └─ Watch real-time stats
   └─ View in Kibana after 1-2 minutes
```

## 🏭 Industries & Services

| Industry | Icon | Services |
|----------|------|----------|
| E-Commerce | 🛒 | 13 services |
| Banking | 🏦 | 17 services |
| Insurance | 🛡️ | 16 services |
| Gaming | 🎮 | 18 services |
| Healthcare | 🏥 | 17 services |
| Logistics | 📦 | 18 services |

## 🎬 Scenario Examples

### E-Commerce
- Black Friday Traffic Spike
- Payment Gateway Failures
- Search Performance Degradation
- Cart Abandonment Pattern
- Inventory Sync Issues
- Recommendation Engine Slowdown

### Banking
- ATM Network Issues
- Fraud Detection Alert Storm
- Database Connection Pool Exhaustion
- Mobile App Login Failures
- Payment Processing Delays
- Regulatory Report Generation

### Gaming
- Server Matchmaking Delays
- DDoS Attack Pattern
- Season Launch Traffic
- In-game Store Issues
- Player Ban Wave Processing

### Healthcare
- EHR System Slowdown
- Appointment Scheduling Surge
- Lab Results Processing Delay
- Emergency Alert System Test

### Logistics
- Holiday Shipping Rush
- Weather-Related Delays
- Warehouse Automation Issues
- Route Optimization Failures
- Last-Mile Delivery Surge

### Insurance
- Claims Processing Backlog
- Policy Renewal Rush
- Underwriting System Overload
- Natural Disaster Claims Surge

## 📊 Data Rates

| Rate | Events/sec | Per Hour | Size/hour | Use Case |
|------|-----------|----------|-----------|----------|
| Low | 5 | 18,000 | ~50 MB | Light demos |
| Medium | 17 | 61,200 | ~170 MB | Standard demos |
| High | 50 | 180,000 | ~500 MB | Load testing |

## 🔍 View in Kibana

```
1. APM → Service Map
   └─ See connected microservices

2. APM → Services
   └─ View performance metrics per service

3. APM → Traces
   └─ Drill into individual requests

4. Observability → Logs → Stream
   └─ Search application logs

5. Observability → Uptime
   └─ Monitor synthetic checks
```

## 🐛 Troubleshooting

### No industries showing?
```bash
# Test API endpoint
curl http://localhost:5000/api/industries

# Should return JSON with 6 industries
```

### Connection failed?
- Verify Cloud ID (no spaces)
- Check API Key hasn't expired
- Ensure Superuser or write permissions

### No data in Kibana?
- Wait 1-2 minutes for indexing
- Refresh the page
- Check time range: "Last 15 minutes"
- Verify in Discover: index pattern `apm-*`

### Import errors?
```bash
# Reinstall dependencies
pip install --upgrade pip
pip install -r requirements_advanced.txt --force-reinstall
```

## 🧪 Test Installation

```bash
# Test imports
python -c "from generator_advanced import IndustryConfig; print('✅ OK')"
python -c "from demo_scenarios import DemoScenarios; print('✅ OK')"

# Test Flask
python -c "from flask import Flask; print('✅ OK')"

# Test Elasticsearch client
python -c "from elasticsearch import Elasticsearch; print('✅ OK')"
```

## 🎯 Best Practices

### For Demos
- **Duration:** 5-10 minutes
- **Rate:** Medium (17 events/sec)
- **Scenario:** Match audience industry
- **Pre-generate:** Run 10 mins before demo

### For Testing
- **Duration:** 30-60 minutes
- **Rate:** High (50 events/sec)
- **Scenario:** Chaos/failure scenarios
- **Monitor:** Watch Elasticsearch resources

### For Development
- **Duration:** 5-15 minutes
- **Rate:** Low (5 events/sec)
- **Scenario:** Normal operations
- **Focus:** One industry at a time

## 🔧 Common Commands

```bash
# Start Flask
python app_advanced.py

# Stop Flask
Ctrl+C

# Check if port 5000 is in use (Mac/Linux)
lsof -i :5000

# Check if port 5000 is in use (Windows)
netstat -ano | findstr :5000

# View Flask logs
# (They appear in terminal where you ran app_advanced.py)

# Test connection to Elastic
curl -H "Authorization: ApiKey YOUR_KEY" \
     https://YOUR_DEPLOYMENT.es.region.aws.found.io:443
```

## 📝 API Endpoints

```
GET  /                      - Main UI
POST /api/connect          - Connect to Elasticsearch
GET  /api/industries       - Get all industries
GET  /api/scenarios        - Get scenarios for industry
POST /api/generate         - Start data generation
POST /api/stop             - Stop data generation
GET  /api/stats            - Get real-time statistics
```

## 🎨 Customization

### Add Your Own Scenario

Edit `demo_scenarios.py`:

```python
'your-scenario': {
    'name': 'Your Scenario Name',
    'description': 'What happens in this scenario',
    'story': 'The narrative description',
    'duration_minutes': 20,
    'error_rate': 0.05,  # 5% errors
    'latency_multiplier': 2.0,  # 2x slower
    'affected_services': ['service-1', 'service-2']
}
```

### Add Your Own Industry

Edit `generator_advanced.py`:

```python
'yourindustry': {
    'name': 'Your Industry Name',
    'icon': '🏢',
    'services': [
        'service-1',
        'service-2',
        'service-3'
    ]
}
```

## 🔐 Security Notes

- ⚠️ **Never commit API keys** to version control
- 🔒 Store API keys securely
- 🔄 Rotate keys regularly
- 📝 Use least-privilege API keys
- 🚫 Don't point at production clusters!

## 💡 Pro Tips

1. **Run generator before demos** - Give data time to index
2. **Use scenarios matching your audience** - Banking for banks, etc.
3. **Show Service Map first** - Most visually impressive
4. **Explain the scenario** - Tell the story of what's happening
5. **Drill into traces** - Show distributed tracing in action
6. **Point out error spikes** - During chaos scenarios
7. **Compare normal vs. incident** - Run twice to show difference

## 📚 Resources

- **Elastic Docs:** https://elastic.co/guide
- **APM Guide:** https://elastic.co/guide/en/apm
- **Kibana Guide:** https://elastic.co/guide/en/kibana
- **Service Map:** Observability → APM → Service Map

## 🆘 Need Help?

1. Check `TROUBLESHOOTING.md`
2. Check browser console (F12)
3. Check Flask terminal output
4. Test API: `curl http://localhost:5000/api/industries`
5. Verify files exist: `ls -la`

---

## 🎉 Quick Start Recap

```bash
# 60 seconds to data generation!
mkdir elastic-demo-advanced && cd elastic-demo-advanced && mkdir templates
# (Copy 7 files here)
pip install -r requirements_advanced.txt
python app_advanced.py
# Open http://localhost:5000
# Enter credentials → Select industry → Start!
```

**Happy Demoing! 🚀**