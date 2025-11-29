while True:
    user_input = input("Введіть число (або 'stop' щоб вийти): ")

    if user_input.lower() == "stop":
        print("Програму завершено.")
        break

    # Перевіряємо, чи ввели число
    if not user_input.lstrip("-").isdigit():
        print("Потрібно ввести ціле число!")
        continue

    n = int(user_input)

    # Виводимо таблицю множення
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

    print()  # Порожній рядок для зручності
