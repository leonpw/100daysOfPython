size = input("What size pizza do you want? S/M/L: ")
add_pepperoni = input("Do you want Peperoni? Y/N: ")
extra_cheese = input("Do you want extra cheese? Y/N: ")


bill = 15

if size == "M":
    bill += 5
elif size == "L":
    bill += 10

if add_pepperoni == "Y":
    if size == "M" or size == "L":
        bill += 3
    else:
        bill += 2
        
    
if extra_cheese == "Y":
        bill += 1

print(f"Your total bill for the pizza: $ {bill}")

