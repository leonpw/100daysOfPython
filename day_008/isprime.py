#Write your code below this line 👇

import math


def prime_checker(number):
    for i in range(2, math.ceil(math.sqrt(number))+1):
        if number % i == 0:
            print(f" {number} is NOT a prime!")
            return

    print(f" {number} is a prime!")
    

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number = n)