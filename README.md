# 🎙️ AI Podcast Generator (CrewAI + Ollama + Gradio + Docker)

An end-to-end **AI-powered podcast generator** that:
- Scrapes blog content using **Firecrawl**
- Summarizes it using **CrewAI agents + Ollama (DeepSeek-R1)**
- Converts the summary into **natural voice using ElevenLabs**
- Provides a clean **Gradio web interface**
- Runs fully inside **Docker** with local **Ollama LLM**

---

## 🚀 Features

- ✅ Blog scraping with Firecrawl
- ✅ Multi-agent reasoning using CrewAI
- ✅ Local LLM inference using Ollama (no OpenAI/Gemini needed)
- ✅ High-quality text-to-speech using ElevenLabs
- ✅ Interactive Gradio web UI
- ✅ Fully Dockerized for easy deployment
- ✅ Secure `.env` based API key handling

---

## 🧠 Architecture Overview

User → Gradio UI → CrewAI Agents
│
├── Firecrawl (Scraping)
├── Ollama (DeepSeek-R1 LLM)
└── ElevenLabs (Text-to-Speech)


---

## 🛠️ Tech Stack

- Python 3.11
- CrewAI
- Ollama (DeepSeek-R1)
- Firecrawl API
- ElevenLabs API
- Gradio
- Docker

---

## 📁 Project Structure

.
├── app.py # Gradio UI + Audio generation
├── blog_summarizer.py # CrewAI pipeline + Ollama LLM
├── agents.py # CrewAI Agents (optional)
├── tasks.py # CrewAI Tasks (optional)
├── podcast_transitions.py # Optional podcast formatting
├── styles.css # Custom UI styling
├── requirements.txt
├── Dockerfile
├── .env # API keys (NOT pushed to GitHub)
└── README.md


---

## 🔐 Environment Variables (`.env`)

Create a `.env` file in the project root:

```env
FIRECRAWL_API_KEY=your_firecrawl_key
ELEVENLABS_API_KEY=your_elevenlabs_key

⚠️ Never commit .env to GitHub.
🐳 Running with Docker (Local)
1️⃣ Start Ollama Container

sudo docker run -d -p 11434:11434 --name ollama ollama/ollama

Pull the model:

sudo docker exec -it ollama ollama pull deepseek-r1:1.5b

2️⃣ Build Your App Image

sudo docker build -t ai-podcast .

3️⃣ Run the App

sudo docker run -it -p 7777:7777 --env-file .env ai-podcast

Open in browser:

http://localhost:7777

🌐 How It Works

    User pastes a blog URL

    CrewAI agent scrapes content

    Second agent summarizes it into podcast script

    ElevenLabs converts text to MP3 voice

    Gradio returns summary + playable audio

🧪 Sample Test Blog

You can test with:

https://martinfowler.com/articles/microservices.html

🧩 Requirements

Installed automatically via Docker:

crewai
crewai-tools
langchain-ollama
firecrawl
gradio
python-dotenv
requests
litellm
elevenlabs

⚠️ Limitations

    Requires active internet for Firecrawl + ElevenLabs

    Ollama model must be pulled before first run

    Free ElevenLabs quota is limited

📌 Future Improvements

    ✅ Multiple voice support

    ✅ Podcast background music

    ✅ Episode auto-formatting

    ✅ Cloud deployment

    ✅ YouTube auto-publishing

👤 Author

Samprit Roy
GitHub: https://github.com/Samprit74
⭐ Support

If you like this project:

    ⭐ Star the repository

    🧑‍💻 Fork it

    📢 Share it with others

Happy Building! 🚀
