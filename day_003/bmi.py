
height = float(input("What is your heigth in m? "))
weight = float(input("What is your weight in kg? "))

bmi = weight / height ** 2

print(f" {weight} / {height} * {height } = {bmi}")

if bmi < 18.5:
    print("You could use some cheesecake.")
elif bmi < 25:
    print("You look perfect to me.")
elif bmi < 30:
    print("You are slightly chubby")
elif bmi < 25:
    print("Still ok.")
else:
    print('Obese.')
    
