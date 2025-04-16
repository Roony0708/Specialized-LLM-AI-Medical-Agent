# 🏥 AI Doctor Assistant Project

A comprehensive AI doctor assistant system with voice interaction capabilities, built with Python.

![Project Banner](https://drive.google.com/uc?export=view&id=1W780nHt1mt8SQ-F_vDo0e52-CRlTAkrt)


## 🚀 Quick Setup Guide

### 📋 Prerequisites
- Python 3.11
- FFmpeg
- PortAudio

---

## 🔧 Installation

### 1. Install Dependencies

#### macOS
```bash
# Install Homebrew (if not installed)
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install FFmpeg and PortAudio
brew install ffmpeg portaudio
```
#### Linux (Debian/Ubuntu)
```bash
sudo apt update
sudo apt install ffmpeg portaudio19-dev
```
#### Windows
1. Download FFmpeg from official site
2. Add FFmpeg bin folder to PATH
3. Install PortAudio from official site

### 2. Set Up Python Environment
```bash
python -m venv venv
# Linux/macOS
source venv/bin/activate
# Windows
.\venv\Scripts\activate
pip install -r requirements.txt
```
## 🏗️ Project Structure
- project/
  - brain_of_the_doctor.py (Phase 1: AI Brain)
  - voice_of_the_patient.py (Phase 2: Patient Voice)
  - voice_of_the_doctor.py (Phase 3: Doctor Voice)
  - gradio_app.py (Phase 4: Web Interface)

## ▶️ Running the Application
### Run each phase separately:
```bash
# Phase 1: AI Brain
python brain_of_the_doctor.py

# Phase 2: Patient Voice
python voice_of_the_patient.py

# Phase 3: Doctor Voice
python voice_of_the_doctor.py

# Phase 4: Web Interface
python gradio_app.py
```

