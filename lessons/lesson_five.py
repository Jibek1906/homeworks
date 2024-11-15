# import random # импортировали модуль рандом

# print(random.randint(1, 10))

import calculator as calc
from random import randint,choice as select_random_element # choice = select_random_element alias В Python алиасы (или псевдонимы) часто используются для сокращения имен модулей, библиотек или переменных. Это упрощает код и делает его более читаемым. Алиасы создаются с помощью ключевого слова as.

from utilities.templates import Person
from termcolor import colored, cprint # python3 -m pip install termcolor для установки модуля или pip install termcolor==2.0.1
# pip uninstall termcolor - для удаления модуля
from decouple import config

print(randint(1,6)) # в этом случае не нужно прописовать префикс random
print(select_random_element(['Apple','Banana','Orange']))

print(calc.addition(10,2))
# python package - добавляется файл инициализации __init__.py
# python file - модуль

# выведется только из эотого файла через __name__ == '__main__' передалось название пакета и модуля
friend = Person('Jim', 25)
print(friend)

# virtual environment - это папка venv
# pip - python install package
# cd.. - назад
# mkdir - создание папки
# python3 -m venv .venv - создаем виртуальную среду
# deactivate - декативируем виртуальную среду
# source bin/activate или source .venv/bin/activate - активируем другую среду
# python lesson_five.py запускаем модуль

cprint("Hello, World!", "green", "on_red")

# decouple - нужна для считывания настройек из стороннего файла используем python-decouple 3.8

print(config('SECRET_KEY'))
commented = config('COMMENTED', default=0, cast = int )  # cast = int конвертирует
print(commented)

# requirements - зависимости
# pip freeze - покажет какие есть билиотеки и какие у них версии python-decouple==3.8 termcolor==2.0.1
# pip freeze > reqs.txt - создаст файл с библиотеками и их версиями
# pip install -r reqs.txt - установит все билиотеки и их версии через файл
# merge - соединяется
# git branch name_of_branch - создаем ветку
# git checkout name_of_branch - переключаемся между ветками
