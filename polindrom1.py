print("Введи короткий текст")
Text1 = input()
Text2 = ""
Chain = len(Text1)
for Nr in range(Chain):
    Text2 += Text1[Chain - Nr - 1]
print(Text2)
if Text1 == Text2:
    print("Полиндром")
