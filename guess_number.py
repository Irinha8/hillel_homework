from random import randint
counter = 0
numbers = []
while len(numbers) < 100:
    x = randint(1, 100)
    if x not in numbers:
        numbers.append(x) # список случайных чисел от 0 до 100, которые не повторяются
answer = "N"
while answer != "Y":
    print(f"Is {x} guessed number?")
    x = numbers[0]
    answer = input()
    counter += 1
    numbers.pop(0)
    if answer == "Y":
        print(f"You've used {counter} tries!")