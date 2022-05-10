for Nr in range(0, 100, 2):
    print(Nr, end=" ")
print()
for Nr in range(1, 100, 2):
    print(Nr, end=" ")
print()
Week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Восскресенье"]
WeekCn = ["星其一", "星其二", "星其三", "星其四", "星其五", "星其六", "星其七"]
for Day in Week:
    print(Day, end=" ")
for CnDay in WeekCn:
    print(CnDay, end="  ")
