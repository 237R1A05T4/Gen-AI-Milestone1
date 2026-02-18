# 🤖 GenAI-Powered Customer Support Quality Auditor

## 📌 Overview

The GenAI-Powered Customer Support Quality Auditor is a modular data ingestion and transcription system designed to process customer support interactions from both audio calls and chat logs.

This project focuses on building a scalable transcription and normalization layer that converts raw conversations into structured JSON format, enabling downstream AI-based quality evaluation.

---

# 🎯 Milestone 1: Data Ingestion & Transcription Layer

## Objective

- Convert customer support audio calls into text using Whisper STT.
- Parse and normalize chat conversations.
- Standardize all transcripts into a structured JSON schema.
- Prepare clean data for AI-powered quality analysis.

---

# 🧠 How the Product Works

The system processes two input sources:

## 1️⃣ Audio Call Processing

Flow:
Audio File → Whisper STT → Raw Transcript → Structured JSON → Saved Output

- Audio files are placed in `sample_data/audio/`
- The system uses OpenAI Whisper (local model) for speech-to-text
- Transcript is cleaned and normalized
- Output is saved as structured JSON

## 2️⃣ Chat Log Processing

Flow:
Raw Chat File → Parsing → Normalization → Structured JSON → Saved Output

- Chat files are placed in `sample_data/chats/`
- Messages are parsed and formatted
- Speaker roles are identified
- Output follows predefined transcript schema

---

# 🏗️ Project Architecture

```
customer-support-qa/
│
├── data_ingestion/
│   ├── audio_transcriber.py      # Handles audio → text conversion
│   ├── chat_processor.py         # Parses and structures chat logs
│
├── sample_data/
│   ├── audio/                    # Input audio files
│   ├── chats/                    # Input chat files
│
├── outputs/
│   ├── transcripts/              # Generated audio transcripts
│   ├── structured_chats/         # Normalized chat outputs
│
├── config/
│   ├── transcript_schema.yaml    # Transcript structure definition
│
├── requirements.txt
└── README.md
```

---

# 📄 Transcript Schema

All outputs are normalized into a structured JSON format:

Example:

```json
{
  "conversation_id": "12345",
  "source_type": "audio",
  "agent_id": "A102",
  "customer_id": "C567",
  "messages": [
    {
      "speaker": "customer",
      "timestamp": "00:01:12",
      "text": "I need help with my order."
    }
  ]
}
```

This schema ensures consistency across both audio and chat inputs.

---

# ⚙️ Technologies Used

- Python
- OpenAI Whisper (local speech-to-text model)
- YAML for schema configuration
- JSON for structured outputs

---

# 🚀 How to Run

## 1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 2️⃣ Audio Transcription

Place audio files inside:

```
sample_data/audio/
```

Run:

```bash
python data_ingestion/audio_transcriber.py
```

Output saved to:

```
outputs/transcripts/
```

---

## 3️⃣ Chat Processing

Place chat files inside:

```
sample_data/chats/
```

Run:

```bash
python data_ingestion/chat_processor.py
```

Output saved to:

```
outputs/structured_chats/
```

---

# 🔄 Development Process

This milestone was developed following structured data engineering principles:

1. Defined a unified transcript schema.
2. Built audio ingestion using Whisper STT.
3. Implemented chat log parsing and normalization.
4. Structured outputs into standardized JSON.
5. Organized the project into modular components.

Key Engineering Principles:
- Separation of concerns
- Modular design
- Scalable pipeline structure
- Config-driven schema definition
- Clean project organization

---

# 📈 Future Roadmap

Upcoming Milestones:

- AI-based conversation quality scoring
- Sentiment analysis
- Compliance detection
- Agent performance metrics
- Dashboard integration
- API-based deployment

---

# 💼 Why This Project Matters

This project demonstrates:

- Real-world GenAI application
- Speech-to-text pipeline implementation
- Structured data engineering
- Clean, scalable architecture
- Production-ready repository organization

---

# 👤 Author
CODE RESOL
