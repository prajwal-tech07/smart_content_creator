# 🎨 Smart Content Creator Assistant

A multi-agent AI system built with Phi Framework and Groq's LLaMA-3 model that automates social media content creation. The system uses specialized agents to research trends, generate engaging content, and optimize posts for different platforms.

---

## 🚀 Features

- 🧠 **Multi-Agent Architecture** - 3 specialized AI agents working together  
- 📱 **Platform Optimization** - Adapts content for Instagram, Twitter, LinkedIn  
- 🔥 **Real-Time Trends** - Finds trending topics and hashtags  
- 📊 **Content Variations** - Generates multiple versions for A/B testing  
- ⚡ **Fast Processing** - Powered by Groq's ultra-fast LLMs  

---

## 🏗️ Agent Architecture

- **Research Agent** → Finds trending topics and hashtags using web search  
- **Content Agent** → Creates engaging posts and captions  
- **Optimization Agent** → Adapts content for different social platforms  
- **Orchestrator** → Coordinates all agents for comprehensive output  

---

## 🛠️ Prerequisites

- Python 3.8+  
- Groq API Key → [Get it here](https://console.groq.com)  
- Phi API Key → [Get it here](https://phidata.com)  

---

## ⚡ Quick Start

```bash
# Clone repository
git clone https://github.com/yourusername/smart-content-creator.git
cd smart-content-creator

# Create virtual environment
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo "GROQ_API_KEY=your_groq_api_key_here" > .env
echo "PHI_API_KEY=your_phi_api_key_here" >> .env

# Run the system
python main.py
```

---

## 📝 Usage Examples

```python
# Generate fitness content
content_creator_system.print_response(
    "Create Instagram posts for a fitness influencer focusing on home workouts",
    stream=True
)

# Create business content
content_creator_system.print_response(
    "Generate LinkedIn content for a tech startup launching an AI product",
    stream=True
)

# Multi-platform optimization
content_creator_system.print_response(
    "Create content about productivity tips and optimize for Instagram, Twitter, and LinkedIn",
    stream=True
)
```

---

## 🌐 Web Interface

```bash
# Launch playground interface
python playground.py

# Open in browser
http://localhost:7777
```

---

## 📦 Dependencies

- phidata  
- groq  
- python-dotenv  
- duckduckgo-search  
- requests  
- beautifulsoup4  

---

## 🎯 Use Cases

- **Marketing Agencies** → Manage multiple client accounts efficiently  
- **Small Businesses** → Automate social media presence  
- **Content Creators** → Scale content production  
- **E-commerce** → Generate product-focused social content  

---

## 📊 Sample Output

- ✅ Trending topic research with sources  
- 📝 Platform-specific content variations  
- 📊 Hashtag recommendations with engagement data  
- 📋 Optimized formatting for each platform  

---

## 🔧 Customization

```python
# Change content niche by modifying the query
content_creator_system.print_response("Your custom content request here", stream=True)
```

---

## 🤝 Contributing

1. Fork the repository  
2. Create feature branch (`git checkout -b feature/amazing-feature`)  
3. Commit your changes (`git commit -m 'Add amazing feature'`)  
4. Push to the branch (`git push origin feature/amazing-feature`)  
5. Open a Pull Request  

---


## 🙏 Acknowledgments

- [Phi Framework](https://github.com/phidatahq/phidata) - Multi-agent AI framework  
- [Groq](https://groq.com) - Ultra-fast LLM inference  
- [DuckDuckGo](https://duckduckgo.com) - Privacy-focused search API  

