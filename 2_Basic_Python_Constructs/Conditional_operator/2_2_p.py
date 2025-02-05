petya_speed = int(input())
vasya_speed = int(input())
tolya_speed = int(input())

if petya_speed > vasya_speed and petya_speed > tolya_speed:
    winner = "Петя"
    if vasya_speed > tolya_speed:
        second = "Вася"
        third = "Толя"
    else:
        second = "Толя"
        third = "Вася"
elif vasya_speed > petya_speed and vasya_speed > tolya_speed:
    winner = "Вася"
    if petya_speed > tolya_speed:
        second = "Петя"
        third = "Толя"
    else:
        second = "Толя"
        third = "Петя"
else:
    winner = "Толя"
    if petya_speed > vasya_speed:
        second = "Петя"
        third = "Вася"
    else:
        second = "Вася"
        third = "Петя"

# print(f"{winner:^24}")
# print(f"{second:^8}")
# print(f"{third:>24}")
# print("   II      I      III   ")

print("{:^8}{:^8}{:^8}".format(" ", winner, " "))
print("{:^8}{:^8}{:^8}".format(second, " ", " "))
print("{:^8}{:^8}{:^8}".format(" ", " ", third))
print("{:^8}{:^8}{:^8}".format("II", "I", "III"))