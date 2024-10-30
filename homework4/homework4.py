import random
def searcher(number):
  while True:
    number_inp = input(f"Введите цифру X: ")
    if number_inp.isdigit() and len(number_inp) == 1 and number_inp!='0':
      x = int(number_inp)
      break
    else:
      print("Некорректный ввод. Введите цифру.")
  numbers = [random.randint(0, 200) for _ in range(10)]
  multiples = list(filter(lambda number: number % x == 0, numbers))
  print(f"Список чисел: {numbers}")
  print(f"Числа, кратные {x}: {multiples}")
searcher(0)