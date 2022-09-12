
total = float(input("What was the total bill in dollahs? $ "))

tip = int(input("What percentage would you tip? "))

amountOfPeeps = int(input("How many are you with? "))

pp = (total * (1 +(tip / 100))) / amountOfPeeps 
amountPerPerson = "{:.2f}".format(round(pp,2))

print(f"Each person should pay: $ {amountPerPerson }")
          