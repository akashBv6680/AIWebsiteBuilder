# 🌐 AIWebsiteBuilder

> **AI-powered website builder using Streamlit and Gemini 2.5 Flash**
>
> Create beautiful, modern websites in minutes by simply describing what you want!

## ✨ Features

- 🤖 **AI-Powered Generation**: Uses Gemini 2.5 Flash model to generate complete websites
- ⚡ **Fast & Efficient**: Create websites in just a few minutes
- 📱 **Responsive Design**: All generated websites are mobile-friendly
- 💻 **Modern Stack**: HTML5, CSS3, and JavaScript with no external dependencies
- 🎨 **Beautiful UI**: Professional designs with smooth animations
- 📥 **Download Ready**: Download generated websites as HTML files
- 🚀 **Easy Deployment**: Deployable on Streamlit Cloud

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Gemini API Key (Get it from [Google AI Studio](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/akashBv6680/AIWebsiteBuilder.git
cd AIWebsiteBuilder
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure API Key**

**For Local Development:**
- Create or edit `.streamlit/secrets.toml`:
```toml
GEMINI_API_KEY = "your_gemini_api_key_here"
```

**For Streamlit Cloud:**
- Go to your app settings in Streamlit Cloud
- Navigate to "Secrets" section
- Add the key:
```
GEMINI_API_KEY = "your_gemini_api_key_here"
```

4. **Run the application**
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

## 📖 Usage

1. **Enter your prompt**: Describe the website you want to create
   - Example: "Create a modern portfolio website for a software engineer with dark theme, project showcase, and contact form"

2. **Click Generate**: The AI agent will create your website
   - Processing typically takes 30 seconds to 2 minutes

3. **Preview**: See your website in real-time

4. **Download**: Download the HTML file and use it immediately

## 📁 Project Structure

```
AIWebsiteBuilder/
├── app.py                 # Main Streamlit application
├── website_agent.py       # AI agent for website generation
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── secrets.toml       # API configuration (local only)
└── README.md              # This file
```

## 🔧 How It Works

### 1. **WebsiteAgent Class** (`website_agent.py`)
- Initializes Gemini 2.5 Flash model
- Reads API key from Streamlit secrets
- Generates optimized prompts for better results
- Returns clean HTML/CSS code

### 2. **Streamlit App** (`app.py`)
- Provides user-friendly interface
- Handles website generation requests
- Displays generated websites in real-time
- Allows HTML download
- Manages session state

### 3. **Gemini 2.5 Flash Model**
- Fast and efficient LLM
- Generates valid HTML5/CSS3 code
- Optimized for website generation tasks

## 🎯 Model Configuration

- **Model**: `gemini-2.5-flash`
- **Temperature**: 0.7 (Balanced creativity and accuracy)
- **Max Tokens**: 8000 (Sufficient for complete websites)
- **Top-P**: 0.95
- **Top-K**: 40

## 📋 Requirements

```
streamlit>=1.28.0
google-generativeai>=0.3.0
python-dotenv>=1.0.0
```

## 🌐 Deployment on Streamlit Cloud

### Step-by-Step Deployment:

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Connect to Streamlit Cloud**
   - Go to [Streamlit Cloud](https://share.streamlit.io/)
   - Click "New app"
   - Select your GitHub repository
   - Choose branch and file path: `app.py`

3. **Add Secrets**
   - In app settings, go to "Secrets"
   - Add your GEMINI_API_KEY
   - Save

4. **Deploy**
   - Click "Deploy"
   - Your app will be live at `https://<your-username>-aiwebsitebuilder.streamlit.app/`

## 🔐 Security Notes

⚠️ **Important**: Never commit `secrets.toml` to version control
- The file is listed in `.gitignore` (recommended)
- Always use Streamlit Cloud Secrets for production
- Rotate your API key if accidentally exposed

## 📝 Example Prompts

### Portfolio Website
```
Create a modern portfolio website for a software engineer. Include:
- Dark theme with neon accents
- Hero section with name and title
- About section
- Project showcase with 3-4 projects
- Skills section
- Contact form
- Responsive design
```

### E-commerce Landing Page
```
Build an e-commerce landing page for a tech gadget store:
- Eye-catching hero banner
- Featured products grid
- Customer testimonials
- Newsletter signup
- Payment options display
- Footer with links
- Mobile responsive
```

## 🐛 Troubleshooting

### API Key not found error
- **Local**: Check `.streamlit/secrets.toml` exists and has correct key
- **Cloud**: Verify API key in Streamlit Cloud Secrets

### Generation takes too long
- Normal: First request may take 30-60 seconds
- Check your internet connection
- Ensure API key has sufficient quota

### Generated HTML not displaying correctly
- Try a more specific prompt
- Include design details in your description
- Request simpler designs for faster generation

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Google Gemini API for powerful LLM capabilities
- Streamlit for the amazing web framework
- Community support and feedback

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing issues for solutions
- Provide detailed descriptions of problems

## 📚 Resources

- [Streamlit Documentation](https://docs.streamlit.io/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [HTML/CSS Reference](https://developer.mozilla.org/)
- [Streamlit Cloud](https://share.streamlit.io/)

---

**Built with ❤️ using Streamlit and Gemini 2.5 Flash**

**Happy Website Building! 🚀**
