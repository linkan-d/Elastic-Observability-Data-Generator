# 🚀 Elastic Observability Data Generator

A powerful web-based tool for generating realistic observability data (APM traces, logs, and synthetic monitoring) for Elastic Stack demos and testing.

![Version](https://img.shields.io/badge/version-2.0-blue)
![Python](https://img.shields.io/badge/python-3.7+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## ✨ Features

- 🎯 **6 Industry Templates** - E-commerce, Banking, Insurance, Gaming, Healthcare, Logistics
- 🎬 **Demo Scenarios** - Simulate traffic spikes, outages, performance issues
- 🤖 **LLM Integration** - Optional AI-powered realistic error messages (OpenAI, Claude, Ollama)
- 📊 **Beautiful Service Maps** - See microservices and dependencies in Kibana
- 🌐 **Easy Web UI** - No command-line expertise needed
- ⚡ **Real-time Progress** - Watch data generation live
- 🔧 **Configurable** - Adjust data rates, duration, and scenarios

## 🎯 What Data Gets Generated

- **APM Traces (60%)** - Distributed traces with realistic latencies and dependencies
- **Application Logs (30%)** - INFO, WARN, ERROR, DEBUG logs with context
- **Synthetic Monitoring (10%)** - HTTP health checks and uptime metrics

## 📋 Prerequisites

- **Python 3.7+**
- **Elastic Cloud** account (or self-hosted Elasticsearch 8.x+)
- **API Key** with write permissions to `apm-*`, `logs-*`, `synthetics-*` indices

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/elastic-observability-generator.git
cd elastic-observability-generator
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install flask elasticsearch faker requests python-dateutil
```

### 3. Start the Application

```bash
python app_advanced.py
```

You should see:
```
============================================================
🎯 Elastic Observability Data Generator
============================================================
✅ Server starting...
🌐 Open your browser to: http://localhost:5000
⏹️  Press Ctrl+C to stop
============================================================
```

### 4. Open in Browser

Navigate to: **http://localhost:5000**

### 5. Connect to Elasticsearch

1. Get your **Cloud ID** from Elastic Cloud deployment
2. Create an **API Key** with appropriate permissions
3. Enter credentials in the web UI
4. Click "Connect to Elasticsearch"

### 6. Generate Data

1. Select an industry (e.g., E-commerce)
2. Choose a scenario (or use "Normal Operations")
3. Configure duration and data rate
4. Click "Start Generating Data"
5. Open Kibana → Observability → APM → Service Map

## 📁 Project Structure

```
elastic-observability-generator/
├── app_advanced.py          # Flask web server
├── generator_enhanced.py    # Core data generation logic
├── llm_generator.py         # LLM integration (optional)
├── requirements.txt         # Python dependencies
├── templates/
│   └── index.html          # Web UI
└── README.md               # This file
```

## 🔑 Getting Elastic Credentials

### Cloud ID

1. Log into [Elastic Cloud](https://cloud.elastic.co)
2. Click on your deployment
3. Copy the **Cloud ID** from the deployment overview

### API Key

1. Open Kibana from your deployment
2. Go to **Stack Management** → **API Keys**
3. Click **Create API key**
4. Name: `observability-generator`
5. Set privileges to **"All"** or grant write access to:
   - `apm-*`
   - `logs-*`
   - `synthetics-*`
6. Copy the API key (you won't see it again!)

## 🏭 Available Industries

### 🛒 E-Commerce (13 services)
Online retail platform with search, recommendations, cart, and payment processing.

### 🏦 Banking (17 services)
Financial services with account management, transactions, fraud detection, and mobile banking.

### 🛡️ Insurance (16 services)
Insurance platform with policy management, claims processing, and underwriting.

### 🎮 Gaming (18 services)
Gaming platform with matchmaking, player profiles, leaderboards, and in-game purchases.

### 🏥 Healthcare (17 services)
Healthcare system with patient records, appointments, prescriptions, and telemedicine.

### 📦 Logistics (18 services)
Logistics platform with shipment tracking, route optimization, and warehouse management.

## 🎬 Demo Scenarios

Each industry includes realistic scenarios:

- **Traffic Spike** - Simulate sudden load increases (Black Friday, game launches)
- **Service Outage** - Partial service failures with cascading effects
- **Database Issues** - Slow queries and connection pool exhaustion
- **Performance Degradation** - Gradual slowdown across services
- **Regional Issues** - Geographic-specific problems

## 🤖 LLM Integration (Optional)

Enable AI-powered realistic error messages:

### Supported Providers:
- **OpenAI** (GPT-3.5/4)
- **Anthropic** (Claude)
- **Ollama** (Local - Free)

### Setup:
1. Toggle "Enable LLM Integration" in the UI
2. Select provider
3. Enter API key (not needed for Ollama)

**Note:** The tool works great without LLM using smart templates!

## ⚙️ Configuration

### Data Rates

- **Low** (5 events/sec) - Light demo, ~18K events/hour
- **Medium** (17 events/sec) - Recommended, ~61K events/hour
- **High** (50 events/sec) - Load testing, ~180K events/hour

### Duration

- Minimum: 5 minutes
- Maximum: 60 minutes
- Recommended: 10-15 minutes for demos

## 🔍 Viewing Data in Kibana

### APM Service Map
**Observability → APM → Service Map**
- See all microservices and their dependencies
- Click services to view traces and metrics

### Logs
**Observability → Logs → Stream**
- Search and filter application logs
- View error stack traces

### Uptime
**Observability → Uptime**
- Monitor synthetic health checks
- View service availability

## 🐛 Troubleshooting

### "Connection error: Failed to fetch"
**Cause:** Flask server not running  
**Fix:** Make sure you ran `python app_advanced.py` and it's still running

### "Template not found"
**Cause:** HTML file not in `templates/` folder  
**Fix:** Ensure `index.html` is in `templates/` directory

### "ModuleNotFoundError"
**Cause:** Missing dependencies  
**Fix:** Run `pip install -r requirements.txt`

### Port 5000 already in use (Mac)
**Cause:** AirPlay Receiver uses port 5000  
**Fix:** Disable in System Settings or edit `app_advanced.py` to use port 5001

### No data appearing in Kibana
**Wait:** Data takes 1-2 minutes to index  
**Check:** Verify API key has write permissions  
**Refresh:** Refresh the Service Map page

## 🔒 Security Notes

- **Never commit API keys** to version control
- **Use `.gitignore`** to exclude sensitive files
- **Rotate keys regularly** in production environments
- **Use least privilege** - only grant necessary permissions

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Built for demonstrating Elastic Observability capabilities
- Inspired by real-world microservices architectures
- Uses [Faker](https://faker.readthedocs.io/) for realistic data generation

## 📧 Support

- **Issues:** [GitHub Issues](https://github.com/YOUR-USERNAME/elastic-observability-generator/issues)
- **Discussions:** [GitHub Discussions](https://github.com/YOUR-USERNAME/elastic-observability-generator/discussions)

## 🗺️ Roadmap

- [ ] More industry templates
- [ ] Custom service configuration
- [ ] Metrics generation (in addition to traces/logs)
- [ ] Docker support
- [ ] Pre-built dashboard templates
- [ ] Anomaly injection

## ⭐ Star History

If you find this tool useful, please consider giving it a star! ⭐

---

**Happy Observability Demo-ing! 🚀**

Slack me for any questions: Linkan Dash
