# Grade Calculator

A Student Grade Calculator in Python, built as a DevOps practical (Git, GitHub, Jenkins, Docker).

Author: Shifa

## Functions
- `average(marks)` – average of all marks
- `grade(avg)` – grade for the average (A+, A, B, C, D, F)
- `is_pass(marks)` – True only when every mark is 40 or above
- `highest(marks)` / `lowest(marks)` – maximum / minimum mark

## Run
```
python Grade_Calculator.py
```

## Test
```
python -m pip install pytest
python -m pytest -v
```

## Docker
```
docker build -t grade_calculator-image .
docker run grade_calculator-image
```

## Jenkins
Repository URL: `https://github.com/brainexe-dev/Grade-Calculator.git`, branch `*/main`, build periodically `H/5 * * * *`, Windows batch command:
```
python -m pip install pytest
python -m pytest -v
```
