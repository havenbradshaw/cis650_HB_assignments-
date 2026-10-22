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


def main():
    totals = total_minutes_per_course()
    print("Data Management:", totals["Data Management"], "minutes")
    course, sessions = most_active_course()
    print("Most active:", course, sessions, "sessions")

if __name__ == "__main__":
    main()