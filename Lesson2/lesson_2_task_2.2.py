def is_yesr_leap(year):
    if (year % 4 == 0):
        print("Год: " + str(year) + " True")
    else:
        print("Год: " + str(year) + " False")

is_yesr_leap(int(input("Ввести год: ")))