from datetime import date  # 1b

TEXT_FILE = "study_log.txt"  # 1b

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


def append_text_entry(entry):  # 1b
    line = f"{entry['date']} | {entry['course']} | {entry['minutes']} | {entry['note']}\n"
    with open(TEXT_FILE, "a", encoding="utf-8") as f:
        f.write(line)

def main():
    entry = {  # 1b
        "date": date.today().isoformat(),
        "course": get_subject(),
        "minutes": get_minutes(),
        "note": get_note(),
    }
    append_text_entry(entry)  # 1b


if __name__ == "__main__":
    main()