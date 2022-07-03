import random
def initGame():
    Secret = "Я загадал число от 1 до 1000"
    print(Secret)

def playGame(Attemp, Input):

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
    return Attemp

def endGame(Attemp):
    print("Ты попробовал", Attemp, "раз.")


initGame()
Game = playGame(0, 0)
endGame(Game)
