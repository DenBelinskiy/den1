import random
Min = 1
Max = 1000
Secret = "Я загадал число от 1 до 1000"
Case = random.randint(Min, Max)
print(Case)
print(Secret)
Attemp = 0
print("Угадай число: ",end="")
Input = random.randint(Min, Max)
while Input != Case :

#    Input = random.randint()
    if Input == 0:
        print("Правильное число было", Case)
        break
    Attemp = Attemp + 1
    if Input < Case:
        Min = Input
        Input = random.randint(Min, Max)
        print(Input, "Слишко маленькое")
    if Input > Case:
        Max = Input
        Input = random.randint(Min, Max)
        print(Input, "Слишком большое")
    if Input == Case:
        print(Input, "Правильно")
print("Ты попробовал",Attemp,"раз.")
# print("Ты попробовал" + str(Attemp) + "раз.")