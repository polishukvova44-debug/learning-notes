import random

while True:
    secret = random.randint(1, 100)
    print("Я загадав число від 1 до 100. У тебе є 7 спроб!")

    attempts = 7

    for i in range(1, attempts + 1):

        # Безпечний ввід
        while True:
            user_input = input(f"Спроба {i}: Введи число: ")
            if user_input.lstrip("-").isdigit():
                guess = int(user_input)
                break
            else:
                print("❗ Треба ввести ЦІЛЕ число!")

        # Логіка гри
        if guess == secret:
            print("🎉 Вітаю! Ти вгадав число!")
            break
        elif guess < secret:
            print("Більше!")
        else:
            print("Менше!")

        # Якщо спроби закінчились
        if i == attempts:
            print("❌ Спроби закінчились! Ти програв.")
            print(f"Загадане число було: {secret}")

    # Можна грати знову
    again = input("Хочеш зіграти ще? (так/ні): ").lower()
    if again != "так":
        print("Гру завершено.")
        break
