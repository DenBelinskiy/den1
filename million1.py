import random
Capital = random.randint(2, 10) * 10000
print("Ты выйграл в лотерею", Capital, "рублей!")
print("Ты можеш не забирать выйгрыш сразу, ", end="")
print("а вложить деньги и заработать на этом!")
print("Процентная ставка: ", end="")
Percent = float(input())
Term = 0
while Capital < 1000000:
    Free = Capital * Percent / 100
    Capital = Capital + Free
    Term += 1
print("Чтобы стать миллионером, тебе понадобится", Term, "лет.")

