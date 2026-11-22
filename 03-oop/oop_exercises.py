"""Exo OOP (slide 67) : surcharge d'operateurs et heritage."""
import math


# ---------------------------------------------------------------- Operator overloading
class Complex:
    def __init__(self, real, imag):
        self.real, self.imag = real, imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

    def __repr__(self):
        return f"({self.real}{self.imag:+}i)"


class Person:
    def __init__(self, name, age, gender):
        self.name, self.age, self.gender = name, age, gender

    def __gt__(self, other):
        return self.age > other.age


class Vector:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __mul__(self, other):  # produit scalaire
        return self.x * other.x + self.y * other.y + self.z * other.z


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __lt__(self, o): return self.radius < o.radius
    def __gt__(self, o): return self.radius > o.radius
    def __le__(self, o): return self.radius <= o.radius
    def __ge__(self, o): return self.radius >= o.radius
    def __eq__(self, o): return self.radius == o.radius
    def __ne__(self, o): return self.radius != o.radius


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def _d(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __lt__(self, o): return self._d() < o._d()
    def __gt__(self, o): return self._d() > o._d()
    def __le__(self, o): return self._d() <= o._d()
    def __ge__(self, o): return self._d() >= o._d()
    def __eq__(self, o): return self._d() == o._d()
    def __ne__(self, o): return self._d() != o._d()


class Matrix:
    def __init__(self, rows):
        self.rows = rows

    def __mul__(self, other):
        if len(self.rows[0]) != len(other.rows):
            raise ValueError("dimensions incompatibles")
        cols = list(zip(*other.rows))
        return Matrix([[sum(a * b for a, b in zip(r, c)) for c in cols] for r in self.rows])

    def __eq__(self, other):
        return self.rows == other.rows

    def __repr__(self):
        return f"Matrix({self.rows})"


# ---------------------------------------------------------------- Inheritance
class Vehicle:
    def drive(self):
        return "Driving a vehicle"


class Car(Vehicle):
    def drive(self):
        return "Driving a car"


class Bicycle(Vehicle):
    def drive(self):
        return "Riding a bicycle"


class PersonInfo:
    def __init__(self, name, age, address):
        self.name, self.age, self.address = name, age, address

    def introduce(self):
        return f"I am {self.name}, {self.age} years old, living at {self.address}."


class Student(PersonInfo):
    def __init__(self, name, age, address, field_of_study):
        super().__init__(name, age, address)
        self.field_of_study = field_of_study

    def introduce(self):
        return super().introduce() + f" I study {self.field_of_study}."


class Employee(PersonInfo):
    def __init__(self, name, age, address, company):
        super().__init__(name, age, address)
        self.company = company

    def introduce(self):
        return super().introduce() + f" I work at {self.company}."


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number, self.balance = account_number, balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

    def transfer(self, other, amount):
        if not self.withdraw(amount):
            return False
        other.deposit(amount)
        return True


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate

    def check_balance(self):
        return self.balance
