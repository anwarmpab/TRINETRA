# TRINETRA
# 🔱 TRINETRA: Vision-Aware Gesture Intelligence System

**TRINETRA** (त्रिनेत्र) is a real-time computer vision + AI-powered system inspired by the mythological "third eye" — designed to sense, interpret, and react to human hand gestures with intelligence and context-awareness.

> 🔬 "When vision meets consciousness, technology becomes instinct."

## 🚀 Key Features
- 🎯 **Gesture Recognition** via custom-trained MediaPipe + CNN classifiers
- 🧠 **EEG Brain-State Fusion** (Optional) for enhanced intent prediction
- ⚡ **Real-time Reactions**: Launch apps, control hardware, respond with speech
- 🧰 Modular **JARVIS-like engine** — includes speech, GUI, and hardware control
- 📊 **Live Dashboard** with logging, gesture analytics, and filters (React + FastAPI)
- 🧠 Future Scope: Multimodal emotion detection, holographic UI, and drone integration

## 🧩 System Architecture

User Gesture
-
[Gesture Detector]-[Gesture Classifier]-[Fusion Model (Gesture + EEG)]-[Trigger Action]


[Speech] -  [GUI]   -  [Hardware]  -  [Logger + API]

## 🛠️ Tech Stack

- **Frontend**: React.js (Dashboard, Filters, Charts)
- **Backend**: FastAPI + SQLite (Logs API)
- **AI/ML**: scikit-learn, TensorFlow Lite, MediaPipe
- **Hardware**: OpenCV, pyttsx3, system-level I/O (Windows)
- **Tools**: Git, Pydantic, SQLAlchemy, Axios
- 
## 🧠 How It Works
1. Hand is detected from live webcam feed.
2. Gesture is classified from landmark data.
3. (Optional) EEG brain state is captured (Active / Neutral / Drowsy).
4. A fusion model decides whether the system should react.
5. If valid, an action is triggered (speak, open app, control LED, log).
6. Data is logged and visualized in the React dashboard.

## 📸 Screenshots
| Gesture Recognition | Live Dashboard |
|---------------------|----------------|
| ![Gesture](docs/sample_gesture.png) | ![Dashboard](docs/sample_dashboard.png) |

## 📦 Installation

```bash
# Clone repo
git clone https://github.com/anwarmpab/TRINETRA.git
cd TRINETRA

# Create virtual environment
python -m venv .venv
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start backend
uvicorn backend.main:app --reload

# (Optional) Start frontend
cd frontend
npm install
npm start

# Run main gesture detection loop
python vision_feed_test.py

## Coming soon: neuro_model_trainer.py and gesture_trainer.py

 Inspired By
Tony Stark’s JARVIS system
Lord Shiva’s “Trinetra” — symbol of inner awakening
Real-world applications in assistive tech, AI-driven interfaces

🙏 Acknowledgements
Special thanks to ChatGPT for brainstorming features, writing modular code, debugging errors, and helping design TRINETRA from scratch like a true Stark-sidekick.
Inspired by Tony Stark’s lab systems and the concept of the mythological "Trinetra".
Thanks to the open-source community — MediaPipe, FastAPI, TensorFlow, React, and GitHub contributors — for making innovation accessible.

📜 License
MIT License © 2025 M P Anwar Baba

Contributions
Pull requests welcome. For major changes, please open an issue first.



Let me know if you want to [add GIFs or video demos](f), or [include a full API reference](f) for your FastAPI backend.

