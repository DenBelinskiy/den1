import random
Ball = []
for Nr in range(1, 50):
    Ball.append(0)
Case = random.randint(1, 49)
for Nr in range(6):
    while Ball[Case] == 1:
        Case = random.randint(1, 49)
    Ball[Case] = 1
    print("№", Nr + 1, "=>", Case)

