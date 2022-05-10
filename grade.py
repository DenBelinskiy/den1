print("Введи число: ", end="")
Score = int(input())
print("Это ", end="")
if (Score >= 0) and (Score < 25):
    print("ужасно (6)")
if (Score >= 25) and (Score < 45):
    print("Плохо (6)")
if (Score >= 45) and (Score < 65):
    print("сойдет (6)")
if (Score >= 65) and (Score < 80):
    print("средне (6)")
if (Score >= 80) and (Score < 90):
    print("хорошо (6)")
if (Score >= 90) and (Score < 100):
    print("очень хорошо (6)")
if (Score > 100) or (Score < 0):
    print("неправильно")

