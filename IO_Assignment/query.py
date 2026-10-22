import json

JSON_FILE = "study_log.json"


def load_entries():
    with open(JSON_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def total_minutes_per_course():
    totals = {}
    for entry in load_entries():
        totals[entry["course"]] = totals.get(entry["course"], 0) + entry["minutes"]
    return totals

def most_active_course():
    counts = {}
    for entry in load_entries():
        counts[entry["course"]] = counts.get(entry["course"], 0) + 1
    course = max(counts, key=counts.get)
    return course, counts[course]

def average_session_length(course):
    minutes = [e["minutes"] for e in load_entries() if e["course"] == course]
    if not minutes:
        return 0.0
    return round(sum(minutes) / len(minutes), 1)

def get_course_notes(course):
    matches = [(e["date"], e["note"]) for e in load_entries() if e["course"] == course]
    return sorted(matches, key=lambda pair: pair[0])  # ISO dates sort chronologically

def format_duration(total_minutes):
    hours, minutes = divmod(total_minutes, 60)
    return f"{hours} hr {minutes} min"


def get_valid_course():
    courses = list(total_minutes_per_course())
    while True:
        choice = input(f"Course ({', '.join(courses)}): ").strip().lower()
        for course in courses:
            if course.lower() == choice:
                return course
        print("Not a valid course. Try again.")


def show_totals():
    for course, minutes in total_minutes_per_course().items():
        print(f"{course}: {format_duration(minutes)}")


def show_most_active():
    course, sessions = most_active_course()
    print(f"Most active course: {course} ({sessions} sessions)")


def show_average():
    course = get_valid_course()
    print(f"Average session length for {course}: {average_session_length(course)} minutes")


def show_notes():
    course = get_valid_course()
    print(f"\nSessions for {course}:")
    for date, note in get_course_notes(course):
        print(f"{date} - {note}")


def main():
    actions = {
        "2a": show_totals,
        "2b": show_most_active,
        "2c": show_average,
        "2d": show_notes,
    }
    while True:
        print("\nStudy Log Queries - ")
        print("2a. Total time per course")
        print("2b. Most active course")
        print("2c. Average session length")
        print("2d. Dates and notes for a course")
        print("Q.  Quit")
        choice = input("Select an option: ").strip().lower()
        if choice == "q":
            break
        if choice in actions:
            actions[choice]()
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()