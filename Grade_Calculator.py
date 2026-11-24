def average(marks):
    return sum(marks) / len(marks)


def grade(avg):
    if avg >= 90:
        return "A+"
    if avg >= 80:
        return "A"
    if avg >= 70:
        return "B"
    if avg >= 60:
        return "C"
    if avg >= 40:
        return "D"
    return "F"


def is_pass(marks):
    return all(m >= 40 for m in marks)

def highest(marks):
    return max(marks)


def lowest(marks):
    return min(marks)


if __name__ == "__main__":
    marks = [76, 89, 90]

    avg = average(marks)
    print("Marks  :", marks)
    print(f"Average: {avg:.2f}")
    print("Highest:", highest(marks))
    print("Lowest:", lowest(marks))
    print("Grade  :", grade(avg))
    print("Result :", "PASS" if is_pass(marks) else "FAIL")
