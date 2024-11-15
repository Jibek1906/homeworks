from decouple import config
from random import randint

def guess_number():

    min_num = config('MIN_NUM', cast=int)
    max_num = config('MAX_NUM', cast=int)
    attempts = config('ATTEMPTS', cast=int)
    start_capital = config('START_CAPITAL', cast=int)

    print(f"Игра: Угадай число")
    print(f"Диапазон от {min_num} до {max_num}")

    while True:
        number = randint(min_num, max_num)
        print("\nНовая игра: ")
        print(f"Ваш начальный капитал: {start_capital}")

        current_attempts = attempts

        while current_attempts > 0:
            print(f"\nОсталось попыток: {current_attempts}")
            print(f"Ваш текущий капитал: {start_capital}")

            try:
                player_num = int(input("Введите число: "))
                player_bet = int(input("Сделайте ставку: "))

                if not (min_num <= player_num <= max_num):
                    print(f"Число должно быть в диапазоне от {min_num} до {max_num}.")
                    continue

                if player_bet > start_capital:
                    print("Ставка не может превышать ваш текущий капитал.")
                    continue

                if player_num == number:
                    start_capital += player_bet * 2
                    print(f"Поздравляем! Вы угадали число! Ваш текущий капитал: {start_capital}")

                    if input("Хотите начать новую игру? (y/n): ").lower() == 'y':
                        break
                    else:
                        return print(f"Игра завершена. Ваш итоговый капитал: {start_capital}")
                else:
                    start_capital -= player_bet
                    print(f"Вы не угадали! Остаток капитала: {start_capital}")

                if start_capital <= 0:
                    print("Недостаточно для ставки. Игра окончена :(")
                    return

                current_attempts -= 1

            except ValueError:
                print("Ошибка ввода. Пожалуйста, вводите только числа.")

        if current_attempts == 0:
            print("Попытки закончились. Хотите попробовать снова?")
            if input("(y/n): ").lower() != 'y':
                break

    print(f"Игра окончена. Ваш итоговый капитал: {start_capital}")
