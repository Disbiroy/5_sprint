import random
import string


def generate_email(cohort_number="99"):
    names = ["pasha", "petr", "dimon", "polina", "galina", "jeny"]
    surnames = ["ivanov", "petrov", "sidorov", "smirnov", "popov"]

    name = random.choice(names)
    surname = random.choice(surnames)
    random_digits = ''.join(random.choices(string.digits, k=3))

    return f"{name}_{surname}_{cohort_number}_{random_digits}@yandex.ru"


def generate_password(length=6):
    if length < 6:
        length = 6

    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))


def generate_name():

    names = ["Паша", "Петр", "Димон", "Полина", "Галина", "Женя"]
    return random.choice(names)