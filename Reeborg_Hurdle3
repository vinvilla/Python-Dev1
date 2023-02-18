#Hurdle 3
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


while ((at_goal() is False) and (front_is_clear() is True)):
    move()
    while (wall_in_front() is True):
        jump()
