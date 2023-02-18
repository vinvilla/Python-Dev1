#Hurdle 4
def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    turn_left()
    while (right_is_clear() is False):
        move()
    turn_right()
    move()
    turn_right()
    while (wall_in_front() is False):
        move()
    turn_left()


while (at_goal() is False):
    while front_is_clear() is True:
        move()
    while wall_in_front() is True:
        jump()
