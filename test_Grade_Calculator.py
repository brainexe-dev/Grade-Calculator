from Grade_Calculator import average, grade, is_pass, highest, lowest

def test_average_normal():
    assert average([80, 90, 100]) == 90

def test_average_single_mark():
    assert average([75]) == 75

def test_grade_distinction():
    assert grade(90) == "A+"

def test_grade_first_class():
    assert grade(74.2) == "B"

def test_grade_second_class():
    assert grade(65) == "C"

def test_grade_fail():
    assert grade(35) == "F"

def test_is_pass_true():
    assert is_pass([45, 60, 75]) is True

def test_is_pass_false_when_one_subject_low():
    assert is_pass([85, 90, 39]) is False

def test_highest():
    assert highest([76, 89, 90]) == 90

def test_lowest():
    assert lowest([76, 89, 90]) == 76
