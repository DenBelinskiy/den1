import random, time
Attemp = 0
MyNumber = 0
YouNumber = 0
print("Давай бросим кубики")

while Attemp < 5 :
    Attemp = Attemp + 1
    print(Attemp, ". раунд",sep='')
    print("Твой бросок")
    Shoot1 = random.randint(1, 6)
    time.sleep(1)
    print(Shoot1)
    print("Мой бросок")
    Shoot2 = random.randint(1, 6)
    time.sleep(1)
    print(Shoot2)
    if Shoot1 > Shoot2 :
        YouNumber = YouNumber + 1
    if Shoot2 > Shoot1 :
        MyNumber = MyNumber +1
    print(YouNumber, " и ", MyNumber)
    time.sleep(3)
    print()

if YouNumber > MyNumber :
    print("You Win")
elif YouNumber < MyNumber :
    print("I win")
else:
    print("Ничя")
