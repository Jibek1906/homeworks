from decouple import config
from random import randint

def guess_number():

      min_num = config('MIN_NUM', cast=int)
      max_num = config('MAX_NUM', cast=int)
      attempts = config('ATTEMPTS', cast=int)
      start_capital = config('START_CAPITAL', cast=int)

      print(max_num, min_num, attempts, start_capital)
      number = randint(min_num, max_num)
      print(number)
      print(f"Игра: Угадай число"
            f"\nДиапазон от {min_num} - до {max_num}")
      print(f'Ваш капитал: {start_capital}')

      while attempts > 0:
            print(f'ATTEMPTS: {attempts}')
            player_num = input('Введите число: ')
            player_capital = input('Сделайте ставку: ')

            try:
                  player_num = int(player_num)
                  player_capital = int(player_capital)

                  if not (min_num <= player_num <= max_num):
                        print(f'Число должно быть в диапазоне от {min_num} до {max_num}. Попробуйте снова.')
                        continue

                  if player_capital > start_capital:
                        print('Ставка не может превышать ваш текущий капитал. Попробуйте снова.')
                        continue

                  if player_num == number:
                        start_capital += player_capital * 2
                        print(f'Вы угадали ваш капитал: {start_capital}')
                  else:
                        start_capital -= player_capital
                        print(f'Вы не угадли, ваш остаток: {start_capital}')
                  attempts = attempts - 1

            except ValueError:
                  print('Вводите только числа')

      if attempts == 0:
            print('Попытки закончились. Игра окончена:(')



