# GenAI-Powered Customer Support Quality Auditor

## Milestone 1: Data Ingestion & Transcription Layer

### Objective
Process customer support chats and convert audio calls to text using Whisper STT.
Normalize all transcripts into structured JSON format.

---

## Features Implemented

- Audio call transcription using OpenAI Whisper (local, free version)
- Chat log parsing and normalization
- Structured JSON output generation
- Defined transcript schema
- Organized project structure

---

## Project Structure

customer-support-qa/
│
├── data_ingestion/
│   ├── audio_transcriber.py
│   ├── chat_processor.py
│
├── sample_data/
│   ├── audio/
│   ├── chats/
│
├── outputs/
│   ├── transcripts/
│   ├── structured_chats/
│
├── config/
│   ├── transcript_schema.yaml
│
├── requirements.txt
└── README.md

---

## How to Run

1. Install dependencies:

    pip install -r requirements.txt

2. Place audio files inside:
   
    sample_data/audio/

3. Run audio transcription:

    python data_ingestion/audio_transcriber.py

4. Place chat files inside:

    sample_data/chats/

5. Run chat processor:

    python data_ingestion/chat_processor.py

---

## Output

Audio transcripts are saved in:

    outputs/transcripts/

Chat transcripts are saved in:

    outputs/structured_chats/

---

## Milestone 1 Status

Completed:
- Chats ingested
- Audio transcription working
- Structured normalization implemented
- Schema defined
