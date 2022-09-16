
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()
    
while not at_goal():
    if wall_in_front():
        if wall_on_right():
            turn_left()
        else:
            turn_right()
    else: 
        if right_is_clear():
            turn_right()

    
    if front_is_clear():
        move()