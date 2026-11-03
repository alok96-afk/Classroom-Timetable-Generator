"""
PS 91 - Classroom Timetable Generator
Language : Python 3
Concepts : Lists, Dictionaries, Constraints, Scheduling

Rules
-----
1. Total periods of all subjects must equal  days x periods_per_day.
2. A subject can appear at most 2 times in one day.
3. Each slot is filled with the subject that has the MOST periods left.
   If two subjects tie, the one entered first wins.
"""

DAY_NAMES = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]   # day names, in order
MAX_PER_DAY = 2                                           # limit per subject per day


# STEP 1: PARSING (typed text -> Python data)
def parse_positive_int(text):
    """'3' -> 3.  Returns None for 'abc', '0', '-2', '2.5'."""
    try:
        value = int(text.strip())
    except ValueError:
        return None
    return value if value > 0 else None


def parse_subjects(text):
    """'Maths:3, Physics:2' -> ({'Maths': 3, 'Physics': 2}, [errors])."""
    subjects = {}
    errors = []
    for part in text.split(","):
        part = part.strip()
        if not part:
            continue
        if ":" not in part:
            errors.append(f"Invalid entry '{part}'. Use the format Subject:Periods (e.g. Maths:3).")
            continue
        name, periods_text = part.split(":", 1)
        name = name.strip()
        periods = parse_positive_int(periods_text)
        if not name or periods is None:
            errors.append(f"Invalid entry '{part}'. Periods must be a positive whole number.")
        elif name.lower() in [s.lower() for s in subjects]:
            errors.append(f"Duplicate subject: {name}.")
        else:
            subjects[name] = periods
    if not subjects and not errors:
        errors.append("At least one subject is required.")
    return subjects, errors


# STEP 2: VALIDATION
def validate(days_text, ppd_text, subject_text):
    """Return (errors, days, periods_per_day, subjects)."""
    errors = []

    days = parse_positive_int(days_text)
    if days is None or days > len(DAY_NAMES):
        errors.append(f"Days must be a whole number between 1 and {len(DAY_NAMES)}.")

    ppd = parse_positive_int(ppd_text)
    if ppd is None:
        errors.append("Periods per day must be a positive whole number.")

    subjects, subject_errors = parse_subjects(subject_text)
    errors += subject_errors

    if errors:
        return errors, days, ppd, subjects

    # Rule 1: total periods must equal available slots
    total = sum(subjects.values())
    slots = days * ppd
    if total != slots:
        errors.append(f"Error: Total weekly periods ({total}) must equal available slots ({slots}).")
        return errors, days, ppd, subjects

    # Rule 2: a subject cannot need more than MAX_PER_DAY x days periods
    for name, periods in subjects.items():
        if periods > MAX_PER_DAY * days:
            unit = "day" if days == 1 else "days"
            errors.append(f"Error: Timetable cannot be generated: {name} needs {periods} "
                          f"periods in {days} {unit}, but the limit is {MAX_PER_DAY} per day.")
            break

    return errors, days, ppd, subjects


# STEP 3: SCHEDULING
def generate_timetable(days, ppd, subjects):
    """Return a list of (day_name, [subjects]) or None if impossible."""
    remaining = dict(subjects)       # periods still to place for each subject
    order = list(subjects)           # entry order, used to break ties
    timetable = []

    for d in range(days):
        used_today = {}
        slots = []
        for _ in range(ppd):
            best = None
            for name in order:
                can_use = remaining[name] > 0 and used_today.get(name, 0) < MAX_PER_DAY
                # '>' keeps the first-entered subject when there is a tie
                if can_use and (best is None or remaining[name] > remaining[best]):
                    best = name
            if best is None:
                return None
            slots.append(best)
            remaining[best] -= 1
            used_today[best] = used_today.get(best, 0) + 1
        timetable.append((DAY_NAMES[d], slots))

    return timetable


def print_timetable(timetable):
    print("\nClassroom Timetable")
    print("-" * 30)
    for day_name, slots in timetable:
        print(f"{day_name}: {', '.join(slots)}")


# STEP 4: RUN
def run(days_text, ppd_text, subject_text):
    errors, days, ppd, subjects = validate(days_text, ppd_text, subject_text)
    if errors:
        for message in errors:
            print(message)
        return False

    timetable = generate_timetable(days, ppd, subjects)
    if timetable is None:
        print("Error: Timetable cannot be generated with the given constraints.")
        return False

    print_timetable(timetable)
    return True


def main():
    print("=== Classroom Timetable Generator ===")
    days_text = input("Days (1-6): ")
    ppd_text = input("Periods per day: ")
    subject_text = input("Subjects with weekly periods (e.g. Maths:3, Physics:2): ")
    run(days_text, ppd_text, subject_text)


if __name__ == "__main__":
    main()