import pytest
from oop_exercises import *


def test_complex():
    assert Complex(1, 2) + Complex(3, 4) == Complex(4, 6)
    assert Complex(5, 5) - Complex(2, 1) == Complex(3, 4)


def test_person_gt():
    assert Person("A", 30, "F") > Person("B", 20, "M")
    assert not Person("A", 20, "F") > Person("B", 30, "M")


def test_vector_dot():
    assert Vector(1, 2, 3) * Vector(4, 5, 6) == 32


def test_circle_all_operators():
    a, b = Circle(1), Circle(2)
    assert a < b and b > a and a <= b and b >= a and a != b and a == Circle(1)


def test_point_distance_ordering():
    assert Point(1, 1) < Point(3, 4)
    assert Point(3, 4) == Point(5, 0)


def test_matrix_mul():
    assert Matrix([[1, 2], [3, 4]]) * Matrix([[5, 6], [7, 8]]) == Matrix([[19, 22], [43, 50]])
    with pytest.raises(ValueError):
        Matrix([[1, 2]]) * Matrix([[1, 2]])


def test_vehicles():
    assert Car().drive() != Bicycle().drive() != Vehicle().drive()


def test_person_hierarchy():
    assert "I study Maths" in Student("Raph", 20, "Paris", "Maths").introduce()
    assert "I work at ESSEC" in Employee("Ana", 30, "Lyon", "ESSEC").introduce()


def test_bank():
    a, b = BankAccount("A", 100), SavingsAccount("B", 100, 0.1)
    assert a.transfer(b, 50) is True and a.balance == 50 and b.balance == 150
    assert a.transfer(b, 500) is False
    b.add_interest()
    assert b.check_balance() == pytest.approx(165)
