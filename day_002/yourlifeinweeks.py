
age = int(input("What is your current age in years: \n"))

# if you are lucky you have until you are 90:
# days, weeks or months left unitl 90

if age > 90:
    print("You have no days left....")
else:
    yearsLeft = 90 - age
    monthsleft = yearsLeft * 12
    weeksLeft = yearsLeft * 52
    daysLeft = yearsLeft * 365
    print(
        f"You have {monthsleft} months left, or {weeksLeft} weeks left. Or that's {daysLeft} days.."
    )
