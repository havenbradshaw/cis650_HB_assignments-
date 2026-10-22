import json
import os
from datetime import date

TEXT_FILE = "study_log.txt"
JSON_FILE = "study_log.json"

def is_valid_text(text):
    return len(text) > 0


def is_valid_minutes(value):
    return value.isdigit() and int(value) > 0


def get_subject():
    while True:
        subject = input("Subject: ").strip()
        if is_valid_text(subject):
            return subject
        print("Subject cannot be empty.")


def get_minutes():
    while True:
        minutes = input("Minutes studied: ").strip()
        if is_valid_minutes(minutes):
            return int(minutes)
        print("Minutes must be a positive whole number.")


def get_note():
    while True:
        note = input("One-line note: ").strip()
        if is_valid_text(note):
            return note
        print("Note cannot be empty.")


def append_text_entry(entry):
    line = f"{entry['date']} | {entry['course']} | {entry['minutes']} | {entry['note']}\n"
    with open(TEXT_FILE, "a", encoding="utf-8") as f:
        f.write(line)


def load_json_entries():
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data if isinstance(data, list) else []
    except json.JSONDecodeError:
        return []


def append_json_entry(entry):
    entries = load_json_entries()
    entries.append(entry)
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2)

def print_file(path, title):
    print(f"\n{title} ({path})")
    if not os.path.exists(path):
        print("(file not found)")
        return
    with open(path, "r", encoding="utf-8") as f:
        print(f.read())


def show_history():
    print_file(TEXT_FILE, "Text log")
    print_file(JSON_FILE, "JSON log")


def main():
    entry = {
        "date": date.today().isoformat(),
        "course": get_subject(),
        "minutes": get_minutes(),
        "note": get_note(),
    }
    append_text_entry(entry)
    append_json_entry(entry)


if __name__ == "__main__":
    main()