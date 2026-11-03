# PS 91 – Classroom Timetable Generator

**Course:** Bachelor of Computer Application – Rungta International Skills University
**Language:** Python 3  |  **Concepts:** Lists, Dictionaries, Constraints, Scheduling

## 1. Project Overview
A console program that generates a weekly class timetable. The user enters the number of
days, the periods per day and the weekly periods for each subject. The program checks the
input, then fills every slot using the rule "choose the subject with the most periods left".

## 2. Objectives
- Practise lists and dictionaries to store and update scheduling data.
- Apply constraints while scheduling (slot count, maximum periods per subject per day).
- Validate numeric input and show clear error messages.
- Print a readable day-by-day timetable.

## 3. Features
- Supports 1 to 6 days (Mon, Tue, Wed, Thu, Fri, Sat, in that order).
- Validates that days, periods per day and subject periods are positive whole numbers.
- Checks that total subject periods equal `days x periods per day`.
- A subject can appear at most **2 times in one day**.
- Each slot is filled with the subject that has the most periods left; on a tie, the subject
  entered first is chosen.
- Rejects duplicate subjects and badly formatted subject entries.

## 4. Requirements
- Python 3.6 or later. Only the standard library is used, so nothing needs to be installed.

## 5. How to Run
```
python one.py
```
(or click **Run Python File** in VS Code). Enter the three inputs when asked:

1. Days (1-6), e.g. `3`
2. Periods per day, e.g. `3`
3. Subjects with weekly periods in the form `Subject:Periods`, separated by commas,
   e.g. `Maths:3, Physics:2, Programming:3, English:1`

## 6. How It Works
| Step | Function | What it does |
|------|----------|--------------|
| 1 | `parse_positive_int`, `parse_subjects` | Convert typed text into numbers and a dictionary `{subject: periods}` |
| 2 | `validate` | Checks the rules and returns a list of error messages |
| 3 | `generate_timetable` | For every slot, picks the subject with the most periods left (max 2 per day) |
| 4 | `run` / `main` | Reads input, calls the steps above and prints the result |

A dictionary (`remaining`) tracks the periods still to be placed for each subject, and a second
dictionary (`used_today`) counts how many times a subject has been used on the current day.

## 7. Input / Output Details (Test Cases)
| Test | Input | Output |
|------|-------|--------|
| 1 Normal | Days 3, Periods/day 3, Maths:3, Physics:2, Programming:3, English:1 | Mon: Maths, Programming, Maths<br>Tue: Physics, Programming, Maths<br>Wed: Physics, Programming, English |
| 2 Boundary | Days 1, Periods/day 2, Maths:2 | Mon: Maths, Maths |
| 3(a) Invalid | Days 3, Periods/day 3, Maths:3, Physics:2, Programming:3 (total 8) | Error: Total weekly periods (8) must equal available slots (9). |
| 3(b) Invalid | Days 1, Periods/day 3, Maths:3 | Error: Timetable cannot be generated: Maths needs 3 periods in 1 day, but the limit is 2 per day. |
| 4 Different | Days 2, Periods/day 2, Programming:2, English:2 | Mon: Programming, English<br>Tue: Programming, English |

Screenshots of every test case are in `PS91_Test_Case_Screenshots.pdf`.

## 8. Files
- `one.py` – complete source code
- `README.md` – this documentation
- `PS91_Test_Case_Screenshots.pdf` – input and output screenshots of all test cases

## 9. Limitations
- Subject names are printed exactly as typed (`maths` and `Maths` look different in the output).
- A maximum of 6 days is supported (Mon to Sat).
- The "2 periods per day" limit is fixed in the code (`MAX_PER_DAY = 2`).
