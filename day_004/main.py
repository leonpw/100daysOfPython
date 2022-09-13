from xml.sax.handler import property_interning_dict
import random

numb = 0
while(numb != 4):
    numb = int((random.random() * 4).__round__(0)) 
    print(numb)