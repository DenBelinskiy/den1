print("Какаую сумму ты хочешь инвестировать: ")
Capital = float(input())
print("Процентная ставка: ", end="")
Persent = float(input())
Term = 0
while Capital < 1000000:
    Free = Capital * Persent / 100
    Capital = Capital + Free
    Term += 1
if Term > 0:
    print("Чтобы превратиться в миллионера, твои деньги в течении", Term,\
          "лет должны храниться в банкею")
else:
    print("Добро пожаловать в клуб милионеров")
