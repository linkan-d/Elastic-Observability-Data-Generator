#!/bin/bash
# Automated Setup Script for Elastic Observability Generator

echo "============================================================"
echo "🚀 Elastic Observability Generator - Auto Setup"
echo "============================================================"
echo ""

# Check if required files exist
echo "📋 Checking files..."
echo ""

if [ ! -f "app_advanced.py" ]; then
    echo "❌ app_advanced.py not found!"
    exit 1
fi
echo "✅ app_advanced.py found"

if [ ! -f "generator_enhanced.py" ]; then
    echo "❌ generator_enhanced.py not found!"
    exit 1
fi
echo "✅ generator_enhanced.py found"

if [ ! -f "index_advanced.html" ] && [ ! -f "templates/index.html" ]; then
    echo "❌ index_advanced.html not found!"
    exit 1
fi
echo "✅ HTML file found"

echo ""
echo "🔧 Setting up folder structure..."
echo ""

# Create templates folder if it doesn't exist
if [ ! -d "templates" ]; then
    echo "📁 Creating templates/ folder..."
    mkdir templates
fi

# Move HTML file to templates if needed
if [ -f "index_advanced.html" ]; then
    echo "📄 Moving index_advanced.html to templates/index.html..."
    mv index_advanced.html templates/index.html
fi

# Check for llm_generator.py
if [ -f "llm_generator.py" ]; then
    echo "✅ llm_generator.py found (optional)"
fi

echo ""
echo "📦 Installing dependencies..."
echo ""

# Create requirements.txt if it doesn't exist
if [ ! -f "requirements.txt" ]; then
    echo "📝 Creating requirements.txt..."
    cat > requirements.txt << 'EOF'
flask==3.0.0
elasticsearch==8.11.0
faker==20.1.0
requests==2.31.0
python-dateutil==2.8.2
EOF
fi

# Install dependencies
pip install -r requirements.txt

echo ""
echo "============================================================"
echo "✅ Setup Complete!"
echo "============================================================"
echo ""
echo "📂 File structure:"
echo "   ├── app_advanced.py"
echo "   ├── generator_enhanced.py"
echo "   ├── llm_generator.py (optional)"
echo "   └── templates/"
echo "       └── index.html"
echo ""
echo "🚀 To start the application:"
echo ""
echo "   python app_advanced.py"
echo ""
echo "Then open your browser to: http://localhost:5000"
echo ""
echo "============================================================"