import random
def initGame():
    Secret = "Я загадал число от 1 до 1000"
    print(Secret)
    Input = 0
    Attemp = 0

def playGame():
    Case = random.randint(1, 1000)
    while Input != Case:
        print("Угадай число: ", end="")
        Input = int(input())
        if Input == 0:
            print("Правильное число было", Case)
            break
        Attemp = Attemp + 1
        if Input < Case:
            print("Слишко маленькое")
        if Input > Case:
            print("Слишком большое")
        if Input == Case:
            print("Правильно")
def endGame():
    print("Ты попробовал", Attemp, "раз.")


initGame()
playGame()
endGame()
