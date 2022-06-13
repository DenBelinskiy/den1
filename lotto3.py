import random
Ball = []
for Nr in range(1, 50):
    Ball.append(False)
Case = random.randint(1, 49)
for Nr in range(6):
    while Ball[Case]:
        Case = random.randint(1, 49)
    Ball[Case] = True
    print("№", Nr + 1, "=>", Case)
