import datetime
def calculation_age():
    while True:
        date_birth = input("Введите дату рождения в формате ДД/ММ/ГГГГ: ")
        part = date_birth.split('/')
        if len(part) != 3:
            print("Некорректный формат даты. Введите дату в формате ДД/ММ/ГГГГ.")
            continue
        for part in part:
            if not part.isdigit():
                print("Дата рождения должна состоять только из цифр.")
                continue
        day, month, year = map(int, part)
        if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= datetime.date.today().year):
            print("Некорректная дата рождения.")
            continue
        break
    birth = datetime.date(year, month, day)
    today = datetime.date.today()
    age = today.year - birth.year - ((today.month, today.day) < (birth.month, birth.day))
    print(f"Ваш возраст: {age} лет")
calculation_age()