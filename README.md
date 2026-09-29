# 📚 Study Planner

## 1. About the Project

**Study Planner** is a simple Python project made to help students organize their studies.

A student can add subjects, set deadlines, enter the number of hours needed for each subject, and check their progress.

The main idea of the project is to help answer:

> **What should I study and how much time should I give to each subject?**

The project is a command-line application, so it runs directly in the terminal.

---

## 2. Features

The project is designed to provide the following features:

- Add a new subject.
- Set a deadline for a subject.
- Enter the total study hours required.
- Track completed study hours.
- Calculate remaining study hours.
- Calculate progress percentage.
- Calculate days left until a deadline.
- Save subject data in a JSON file.
- Load saved subjects when the program starts.
- Generate a daily study schedule based on urgency.

Some of the planning features are still marked as `TODO` in the current code and can be completed as future work.

---

## 3. Technologies Used

The project is made using:

- **Python**
- **JSON** for storing data
- **Rich** for better terminal output
- **PyFiglet** for the Study Planner heading

---

## 4. Project Files

The project contains these main files:

```text
Study Planner
│
├── main.py
├── planner.py
├── storage.py
├── ui.py
├── requirements.txt
└── README.md
```

### `main.py`

This is the main file of the project.

It:

- Starts the program.
- Loads saved subjects.
- Shows the menu.
- Takes input from the user.
- Adds subjects.
- Shows progress.
- Saves the data before exiting.

To run the project, we run this file.

### `planner.py`

This file contains the main study-planning logic.

It has two main classes:

- `Subject`
- `Planner`

`Subject` stores information such as:

```text
Subject name
Deadline
Hours needed
Hours completed
```

It can also calculate:

- Hours remaining
- Progress percentage
- Days left
- Urgency score

`Planner` stores all the subjects and is meant to handle planning-related operations.

### `storage.py`

This file is used to save and load subjects.

The data is stored in:

```text
data/subjects.json
```

The `data` folder is created automatically when the program saves the data.

### `ui.py`

This file handles the terminal display.

It uses **Rich** and **PyFiglet** to make the terminal output easier to read.

It contains:

- Study Planner banner
- Menu
- Subject table
- Schedule display function

### `requirements.txt`

This file contains the external Python package required by the project.

---

# 5. Requirements

Before running the project, make sure you have:

- Python installed
- pip installed
- A terminal or Command Prompt

The project uses packages mentioned in `requirements.txt`.

---

# 6. How to Install and Run

Follow these steps if you are running the project for the first time.

## Step 1: Open the project folder

Open Command Prompt or Terminal and go to the project folder.

Example:

```bash
cd path/to/study-planner
```

Make sure the folder contains:

```text
main.py
planner.py
storage.py
ui.py
requirements.txt
README.md
```

---

## Step 2: Create a virtual environment

A virtual environment keeps the project's packages separate from other Python projects.

### Windows

```bash
python -m venv .venv
```

Then activate it:

```bash
.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv
```

Then:

```bash
source .venv/bin/activate
```

---

## Step 3: Install the required packages

Run:

```bash
python -m pip install -r requirements.txt
```

---

## Step 4: Run the project

Run:

```bash
python main.py
```

If your computer uses `python3`, use:

```bash
python3 main.py
```

The Study Planner will start in the terminal.

---

# 7. How to Use the Project

After running the program, the menu looks like:

```text
[1] Add Subject
[2] Mark Progress
[3] View Schedule
[4] View Progress
[5] Save & Exit
```

## Add Subject

Choose:

```text
1
```

The program asks for:

### Subject name

Example:

```text
Mathematics
```

### Deadline

Enter the date in this format:

```text
YYYY-MM-DD
```

Example:

```text
2026-10-05
```

### Total hours needed

Example:

```text
12
```

The subject is then added to the planner.

---

## View Progress

Choose:

```text
4
```

The program shows a table with:

```text
Name
Deadline
Days Left
Progress
```

This helps the student quickly check their subjects.

---

## Save and Exit

Choose:

```text
5
```

The subjects are saved in:

```text
data/subjects.json
```

The saved information can be loaded again when the program is run.

---

# 8. How Data is Stored

The project uses a JSON file instead of a database.

For example, the data can look like:

```json
[
  {
    "name": "Mathematics",
    "deadline": "2026-10-05",
    "hours_needed": 12,
    "hours_completed": 0.0
  }
]
```

This makes the project simple and easy to understand.

---

# 9. How the Study Planner Works

For every subject, the planner keeps track of:

```text
Total hours needed
        ↓
Hours already completed
        ↓
Hours remaining
```

It also checks:

```text
Today's date
      +
Subject deadline
      ↓
Days left
```

The planner can use the remaining hours and days left to decide how urgent a subject is.

The planned scheduling process is:

```text
Subjects
   ↓
Check days left
   ↓
Check remaining hours
   ↓
Find urgency
   ↓
Give study time
   ↓
Create daily schedule
```

The final urgency formula and schedule-generation code are currently marked as `TODO` in the project.

---

# 10. Project Documentation

## Main Classes

### Subject

The `Subject` class represents one subject.

It stores:

```text
name
deadline
hours_needed
hours_completed
```

It also calculates:

```text
hours_remaining
progress_percent
days_left
urgency_score
```

### Planner

The `Planner` class stores the subjects.

It is designed to:

- Add subjects
- Remove subjects
- Update progress
- Calculate priorities
- Generate a daily schedule

---

## Data Flow

The basic flow of the project is:

```text
User
 ↓
main.py
 ↓
Planner
 ↓
Subject
 ↓
storage.py
 ↓
subjects.json
```

The `ui.py` file is used to display the information to the user.

---

# 11. Current Status of the Project

The basic project structure is ready, but some functions are still incomplete.

The following parts are currently `TODO`:

- `urgency_score`
- `remove_subject()`
- `mark_progress()`
- `generate_daily_schedule()`
- `show_schedule()`

The menu options for **Mark Progress** and **View Schedule** also need to be connected to these functions.

These can be completed as the next step of the project.

---

# 12. Future Improvements

The project can be improved in many ways in the future.

### 1. Complete Progress Tracking

The user should be able to enter how many hours they studied and update their progress.

Example:

```text
Mathematics
Studied today: 2 hours
```

The completed hours would then increase automatically.

### 2. Complete Daily Schedule

The planner can automatically divide the available study hours between subjects.

For example:

```text
Today's Schedule

Mathematics    2 hours
Chemistry      1 hour
C++            2 hours
```

### 3. Better Urgency System

The urgency can be calculated using:

- Days left
- Hours remaining

Subjects with less time and more work remaining can receive more attention.

### 4. Input Validation

The program can check for incorrect input such as:

- Invalid dates
- Negative hours
- Empty subject names
- Letters entered where numbers are expected

### 5. Remove and Edit Subjects

Users could be given options to:

- Remove a subject
- Change a deadline
- Change required hours

### 6. Weekly Schedule

Instead of only creating a daily plan, the project could generate a complete weekly study plan.

### 7. Study History

The project could save individual study sessions.

For example:

```text
Date        Subject       Hours
28/09/2026  Mathematics   2
28/09/2026  Chemistry     1
29/09/2026  C++           2
```

### 8. Progress Statistics

The planner could show:

- Total hours studied
- Total hours remaining
- Overall progress
- Most urgent subject
- Weekly study time

### 9. Better User Interface

The terminal interface can be improved with:

- Better progress bars
- Clearer menus
- More colors
- Better schedule display
- Confirmation messages

### 10. GUI Version

In the future, the same project could be converted into a desktop or web application with buttons, calendars and visual progress charts.

---

# 13. Troubleshooting

### Problem: `ModuleNotFoundError`

Install the required packages again:

```bash
python -m pip install -r requirements.txt
```

Also make sure your virtual environment is activated.

### Problem: `python` is not recognized

Try:

```bash
python3 main.py
```

If that also does not work, make sure Python is installed correctly.

### Problem: Saved data is missing

Make sure you selected:

```text
5 - Save & Exit
```

The saved file should be:

```text
data/subjects.json
```

---


# 13. Testing

The project can be tested by running the program and entering sample subject details.

The following is one example of how the current working parts of the program can be tested.

## Test Case 1: Add a Subject

### Step 1

Run the program:

```bash
python main.py
```

### Step 2

Choose option:

```text
1
```

### Step 3

Enter the following sample input:

```text
Enter subject name: Mathematics
Enter deadline (YYYY-MM-DD): 2026-10-05
Enter total hours needed: 12
```

### Expected Output

The program should display:

```text
Added 'Mathematics'!
```

The subject is now added to the planner.

---

## Test Case 2: View Added Subject

After adding the subject, choose:

```text
4
```

### Expected Output

The subject table should contain information similar to:

```text
Your Subjects

Name         Deadline      Days Left     Progress
Mathematics  2026-10-05    [number]      0.0%
```

The exact **Days Left** value depends on the date on which the program is tested.

---

## Test Case 3: Save the Subject

Choose:

```text
5
```

### Expected Output

```text
Saved. Bye!
```

The program should create:

```text
data/subjects.json
```

The file should contain the saved subject information, similar to:

```json
[
  {
    "name": "Mathematics",
    "deadline": "2026-10-05",
    "hours_needed": 12.0,
    "hours_completed": 0.0
  }
]
```

---

## Test Case 4: Check Saved Data

Run the program again:

```bash
python main.py
```

The program loads the previously saved subjects.

Choose:

```text
4
```

The previously added `Mathematics` subject should appear in the table.

This confirms that the **save and load functionality** is working.

---

## Test Case 5: Multiple Subjects

The planner can also be tested with more than one subject.

Example inputs:

```text
1
Enter subject name: Mathematics
Enter deadline (YYYY-MM-DD): 2026-10-05
Enter total hours needed: 12
```

Then add another subject:

```text
1
Enter subject name: Chemistry
Enter deadline (YYYY-MM-DD): 2026-10-10
Enter total hours needed: 8
```

Then choose:

```text
4
```

### Expected Result

The progress table should show both subjects:

```text
Your Subjects

Name         Deadline      Days Left     Progress
Mathematics  2026-10-05    [number]      0.0%
Chemistry    2026-10-10    [number]      0.0%
```

---

## Testing Summary

| Test | Input / Action | Expected Result |
|---|---|---|
| Add subject | Enter subject details | Subject is added |
| View progress | Choose `4` | Subject appears in table |
| Save data | Choose `5` | Data is saved to JSON |
| Load data | Restart program | Saved subjects are loaded |
| Multiple subjects | Add two or more subjects | All subjects appear in the table |

> **Note:** The `Mark Progress` and `View Schedule` options are not included as completed test cases because their related functions are still marked as `TODO` in the current project code.

# 14. Project Goal

The main goal of this project is to make studying easier to organize.

Instead of simply making a list of subjects, the Study Planner is designed to consider:

```text
Subjects
   +
Deadlines
   +
Study Hours
   +
Progress
   ↓
Study Plan
```

This project also helps demonstrate basic Python concepts such as:

- Classes and objects
- Functions
- Lists
- File handling
- JSON
- User input
- Date handling
- External Python libraries

---

## 👨‍💻 Project

**Study Planner**

A first-year engineering Python project designed to help students organize their study time and keep track of their progress.
