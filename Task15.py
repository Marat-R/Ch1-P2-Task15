age = int(input("Input your age: "))
# for age_even in range(0, age):
#     print(age_even, end = " ")

if age % 2 == 0:
    for age_even in range(0, age):
        if age_even % 2 == 0:
            print(age_even, end = " ")
else:
    for age_odd in range(0, age):
        if age_odd % 2 != 0:
            print(age_odd, end = " ")
