import random

def user():
  while True:
    choice = input("Выберите камень, ножницы или бумагу: ").lower()
    if choice in ["камень", "ножницы", "бумага"]:
      return choice
    else:
      print("Некорректный ввод. Пожалуйста, введите камень, ножницы или бумагу.")

def computer():
  choices = ["камень", "ножницы", "бумага"]
  return random.choice(choices)

def win(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "Ничья!"
  elif (user_choice == "камень" and computer_choice == "ножницы") or \
     (user_choice == "ножницы" and computer_choice == "бумага") or \
     (user_choice == "бумага" and computer_choice == "камень"):
    return "Вы победили!"
  else:
    return "Компьютер победил!"
  
def game():
  while True:
    user_choice = user()
    computer_choice = computer()
    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")
    winner = win(user_choice, computer_choice)
    print(winner)
game()