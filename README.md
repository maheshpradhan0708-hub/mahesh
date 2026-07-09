# 🔲 Logic Box — Pattern Generator & Number Analyzer

A beginner-friendly Python console project that combines **nested loop pattern printing** with a simple **number range analyzer**, wrapped in an interactive menu-driven program.

---

## 🎯 Objective

To build a menu-driven Python application that demonstrates core programming concepts — loops, nested loops, conditionals, exception handling, and loop-control statements (`break`, `continue`, `pass`) — through two practical mini-tools:

1. A **pattern generator** that prints star (`*`) shapes.
2. A **number analyzer** that classifies numbers in a range as odd/even and sums them.

---

## 📋 Problem Statement

Design a program that:

- Runs continuously in a loop until the user chooses to exit.
- Offers the user a menu with 5 options.
- Generates three types of star patterns (Right-angled Triangle, Pyramid, Left-angled Triangle) based on a user-supplied row count, using **nested loops**.
- Analyzes a user-defined numeric range by:
  - Labeling each number as **Even** or **Odd**.
  - Calculating the **sum** of all numbers in that range.
- Handles invalid input gracefully (e.g., non-numeric entries, invalid ranges) without crashing.
- Demonstrates the use of `break`, `continue`, and `pass` statements as per assignment requirements.

---

## 🗺️ Program Flow

```
┌─────────────────────────────┐
│        START PROGRAM        │
└──────────────┬───────────────┘
               │
               ▼
      ┌──────────────────┐
      │  Show Main Menu   │◄────────────────────┐
      └────────┬──────────┘                      │
               │                                  │
               ▼                                  │
      ┌──────────────────┐                        │
      │  Get user choice  │                        │
      └────────┬──────────┘                        │
               │                                    │
   ┌───────────┼─────────────┬─────────────┐        │
   ▼           ▼             ▼             ▼        │
 1 / 2 / 3     4           5 (Exit)     Invalid      │
Pattern      Number        │            Choice       │
Generator    Analyzer      │              │           │
   │           │           ▼              │           │
   │           │      "Goodbye!"          │           │
   │           │         END              │           │
   │           │                          │           │
   ▼           ▼                          │           │
Ask rows   Ask start/end                  │           │
   │           │                          │           │
 Validate   Validate                      │           │
 (try/     (try/except,                   │           │
 except,    continue on                   │           │
 break on   error or                      │           │
 error)     end<start)                    │           │
   │           │                          │           │
   ▼           ▼                          │           │
Nested     Loop through                   │           │
loops →    range → Even/Odd               │           │
print      + running total                │           │
pattern        │                          │           │
   │           ▼                          │           │
   │      Print total sum                 │           │
   │           │                          │           │
   └───────────┴──────────────────────────┴───────────┘
                     (loop back to menu)
```

**Loop-control demonstrations:**
| Statement | Where used | Purpose |
|---|---|---|
| `break` | Invalid row count (≤ 0) | Stops the entire program |
| `break` | User selects option `5` | Exits the main `while True` loop |
| `continue` | Invalid number input (`ValueError`) | Skips back to show the menu again |
| `continue` | End of range < start of range | Skips back to show the menu again |
| `pass` | Placeholder check (`i == -99999`) | Demonstrates a no-op statement inside the loop |

---

## ⚙️ Features

| # | Option | Description |
|---|--------|-------------|
| 1 | Right-angled Triangle | Prints a triangle of stars aligned to the left |
| 2 | Pyramid | Prints a centered pyramid of stars |
| 3 | Left-angled Triangle | Prints a right-aligned triangle of stars |
| 4 | Analyze a Range of Numbers | Classifies each number as Even/Odd and prints the sum |
| 5 | Exit | Ends the program |

---

## 🖥️ Sample Output

```
Enter your choice: 3
Enter the number of rows for the pattern: 5

Pattern:
    *
   **
  ***
 ****
*****
```

```
Enter your choice: 4
Enter the start of the range: 2
Enter the end of the range: 10
Number 2 is Even
Number 3 is Odd
...
Sum of all numbers from 2 to 10 is: 54
```

---

## ▶️ How to Run

```bash
python py_prj2.py
```

Then follow the on-screen menu prompts (enter `1`–`5`).

---

## 🧠 Concepts Demonstrated

- `while True` main program loop
- Nested `for` loops for pattern generation
- Input validation using `try / except`
- Loop control: `break`, `continue`, `pass`
- String formatting with f-strings
- Basic arithmetic accumulation (running sum)

---

## 👤 Author

**Author:** Mahesh
**Project:** Project 2 — Logic Box – Pattern Generator and Number Analyzer
**Language:** Python 3.13
**Type:** Console Application / Beginner Assignment

---

## 📌 Notes

- Row count of `0` or less **terminates the program** (by design, per assignment rules).
- Non-numeric input for rows or range values is caught and handled without crashing.
- The number analyzer requires `end ≥ start`, otherwise it re-prompts the menu.
