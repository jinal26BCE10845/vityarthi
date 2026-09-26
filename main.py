from planner import Planner, Subject
from storage import save_subjects, load_subjects
from datetime import date
import ui

def main():
    planner = Planner()
    planner.subjects = load_subjects()
    ui.show_banner()

    while True:
        ui.show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Enter subject name: ")
            deadline_str = input("Enter deadline (YYYY-MM-DD): ")
            hours_needed = float(input("Enter total hours needed: "))

            deadline = date.fromisoformat(deadline_str)
            new_subject = Subject(name=name, deadline=deadline, hours_needed=hours_needed)
            planner.add_subject(new_subject)

            print(f"Added '{name}'!")
        elif choice == "2":
            # TODO: mark progress
            pass
        elif choice == "3":
            # TODO: call planner.generate_daily_schedule(...)
            # then ui.show_schedule(...)
            pass
        elif choice == "4":
            ui.show_subjects_table(planner.subjects)
        elif choice == "5":
            save_subjects(planner.subjects)
            print("Saved. Bye!")
            break

if __name__ == "__main__":
    main()


