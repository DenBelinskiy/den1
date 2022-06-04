print("Какаую сумму ты хочешь инвестировать: ")
Capital = float(input())
print("Процентная ставка: ")
Percent = float(input())
print("На какой срок вкладываеш деньги: ")
Term = int(input())
for N in range(Term):
    Free = Capital * Percent / 100
    Capital = Capital + Free
print("Ты получиш", Capital, "рублей")
if Capital < 1000000:
    print("Но так ты не станеш миллионером")
else:
    print("Добро пожаловать в клуб миллионеров")