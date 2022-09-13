
year = int(input("Which year would you like to check? "))

isLeap = False

if year % 4 == 0:
    if year % 100 == 0:
        isLeap = False
        if year % 400 == 0:
            isLeap = True
    else:
        isLeap = True
    
    
    
if isLeap:
    print(f"{year} is a leap year.")
else :
    print(f"{year} is not a leap year.")
