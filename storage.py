import json
from pathlib import Path
from datetime import date
from planner import Subject

DATA_FILE = Path("data/subjects.json")

def save_subjects(subjects):
    DATA_FILE.parent.mkdir(exist_ok=True)
    data = [
        {
            "name": s.name,
            "deadline": s.deadline.isoformat(),
            "hours_needed": s.hours_needed,
            "hours_completed": s.hours_completed,
        }
        for s in subjects
    ]
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

def load_subjects():
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE) as f:
        data = json.load(f)
    return [
        Subject(
            name=d["name"],
            deadline=date.fromisoformat(d["deadline"]),
            hours_needed=d["hours_needed"],
            hours_completed=d["hours_completed"],
        )
        for d in data
    ]