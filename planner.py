from dataclasses import dataclass, field
from datetime import date

@dataclass
class Subject:
    name: str
    deadline: date          # study deadline
    hours_needed: float      # total hours required
    hours_completed: float = 0.0

    @property
    def hours_remaining(self):
        return max(0, self.hours_needed - self.hours_completed)

    @property
    def progress_percent(self):
        if self.hours_needed == 0:
            return 100
        return round((self.hours_completed / self.hours_needed) * 100, 1)

    @property
    def days_left(self):
        return (self.deadline - date.today()).days

    @property
    def urgency_score(self):
        # TODO: design your own formula.
        # Idea: higher score = more urgent.
        # Consider: hours_remaining vs days_left.
        # e.g. hours_remaining / max(days_left, 1)
        pass


class Planner:
    def __init__(self):
        self.subjects: list[Subject] = []

    def add_subject(self, subject: Subject):
        self.subjects.append(subject)

    def remove_subject(self, name: str):
        # TODO
        pass

    def mark_progress(self, name: str, hours: float):
        # TODO: find subject by name, add hours to hours_completed
        pass

    def generate_daily_schedule(self, available_hours_per_day: float):
        """
        TODO: This is the core logic you'll design.
        Ideas to consider:
        - Sort subjects by urgency_score (most urgent first)
        - Allocate available_hours_per_day across subjects,
          giving more time to higher urgency subjects
        - Return a dict: {subject_name: hours_allocated}
        """
        pass