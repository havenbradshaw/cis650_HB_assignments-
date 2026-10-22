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


def main():
    totals = total_minutes_per_course()
    print("Data Management:", totals["Data Management"], "minutes")


if __name__ == "__main__":
    main()