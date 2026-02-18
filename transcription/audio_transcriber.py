import os
import json
import whisper

def transcribe_audio(file_path):
    print("Loading Whisper model...")
    model = whisper.load_model("base")

    print(f"Transcribing: {file_path}")
    result = model.transcribe(file_path)

    return result["text"]

def save_transcript(conversation_id, text):
    output_path = f"outputs/transcripts/{conversation_id}.json"

    structured_output = {
        "conversation_id": conversation_id,
        "full_transcript": text
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(structured_output, f, indent=4)

    print(f"Saved: {output_path}")

if __name__ == "__main__":
    audio_folder = "sample_data/audio"

    for filename in os.listdir(audio_folder):
        if filename.endswith(".mp3") or filename.endswith(".wav"):
            file_path = os.path.join(audio_folder, filename)
            conversation_id = filename.split(".")[0]

            transcript_text = transcribe_audio(file_path)
            save_transcript(conversation_id, transcript_text)

    print("All audio files processed.")
