import os
import json
import re

def parse_chat(chat_text):
    pattern = r"\[(.*?)\]\s*(.*?):\s*(.*)"
    messages = []

    for line in chat_text.split("\n"):
        match = re.match(pattern, line)
        if match:
            timestamp, speaker, text = match.groups()

            role = "agent" if "agent" in speaker.lower() else "customer"

            messages.append({
                "timestamp": timestamp,
                "speaker": role,
                "text": text.strip()
            })

    return messages

def save_chat(conversation_id, messages):
    output_path = f"outputs/structured_chats/{conversation_id}.json"

    structured_output = {
        "conversation_id": conversation_id,
        "messages": messages
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(structured_output, f, indent=4)

    print(f"Saved: {output_path}")

if __name__ == "__main__":
    chat_folder = "sample_data/chats"

    for filename in os.listdir(chat_folder):
        if filename.endswith(".txt"):
            file_path = os.path.join(chat_folder, filename)
            conversation_id = filename.split(".")[0]

            with open(file_path, "r", encoding="utf-8") as f:
                chat_text = f.read()

            messages = parse_chat(chat_text)
            save_chat(conversation_id, messages)

    print("All chat files processed.")
