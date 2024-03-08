# Todays lessons were on a site. I'll paste the project code below so that by Day15 I can come back
# to debug it.

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        

            