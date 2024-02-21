# Задания 1-3
from datetime import datetime

from application.salary import calculate_salary
from application.db.people import get_employees

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print("Программа работает! Точное время запуска: ", datetime.now())

# 4ое задание, модуль импортирует случайную шутку, в данном случае на английском
import pyjokes

My_joke = pyjokes.get_joke(language="en", category="neutral")
print(My_joke)