# DVD Logos game
# How this program works
# This project simulates the animation in the terminal
# it moves this text one step at a time accross your terminal
# when the text reaches the edge of the terminal the direction of it will reverse
# it keeps track how many times the logo lands exactly in a corner and each time
# the logo hit the any corner the corner counter increase
#
#  why we use bext module?
# because it lets python move the cursor around in the terminal (move text in the terminal)
# it allows colored text to make the animation colorful
# How the project works:
# DVD has a position (x,y)
#  Every frame the program moves the DVD in it's direction
# if DVD hits the left or right edge -> it flips it's x-direction
# if DVD hits the top or bottom edge -> it flips it's y-direction
# if it hits both(left with up or right with bottom or...)-> that's a corner hit.

##########################################################################

import sys, time, random

try:
    import bext
except ModuleNotFoundError:
    sys.exit()

Width, Height = bext.size()
Width -= 1

Num_of_Logos = 5
pause_amount = 0.2
LogoWidth = 3
LogoHeight = 1
Colors = ["white", "green", "blue", "yellow", "magenta", "cyan", "red"]


Up_Right = "ur"
Up_left = "ul"
Down_Right = "dr"
Down_Left = "dl"
Directions = [Up_Right, Up_left, Down_Right, Down_Left]


Color = "color"
Dir = "direction"
X = "x"
Y = "y"

# bext.clear()

logos = []
for i in range(Num_of_Logos):
    logos.append(
        {
            Dir: random.choice(Directions),
            Color: random.choice(Colors),
            X: random.randint(1, Width - 4),
            Y: random.randint(1, Height - 4),
        }
    )

    if logos[-1][X] % 2 == 1:  # make sure that x direction is odd
        logos[-1][X] -= 1  # convert here into even num by subtract one from it.
print(logos)
bext.clear()

counterBounces = 0
while True:
    for logo in logos:
        bext.goto(logo[X], logo[Y])
        print("   ", end="")

        OriginalDir = logo[Dir]

        # Checks for corner Bounces
        if logo[X] == 0 and logo[Y] == 0:
            logo[Dir] = Down_Right
            counterBounces += 1
        elif logo[X] == 0 and logo[Y] == Height - 1:
            logo[Dir] = Up_Right
            counterBounces += 1
        elif logo[X] == Width - 3 and logo[Y] == Height - 1:
            logo[Dir] = Up_left
            counterBounces += 1
        elif logo[X] == Height - 3 and logo[Y] == 0:
            logo[Dir] = Down_Left
            counterBounces += 1
        # see the bounces of left corner
        elif logo[X] == 0 and logo[Dir] == Up_left:
            logo[Dir] = Up_Right
            counterBounces += 1
        elif logo[X] == 0 and logo[Dir] == Down_Left:
            logo[Dir] = Down_Right
            counterBounces += 1
        # see the bounces of right corner
        elif logo[X] == Width - 3 and logo[Dir] == Up_Right:
            logo[Dir] = Up_left
            counterBounces += 1
        elif logo[X] == Width - 3 and logo[Dir] == Down_Right:
            logo[Dir] = Down_Left
            counterBounces += 1
        # See if the bounces at top corner
        elif logo[Y] == 0 and logo[Dir] == Up_left:
            logo[Dir] = Down_Left
            counterBounces += 1
        elif logo[Y] == 0 and logo[Dir] == Up_Right:
            logo[Dir] = Down_Right
            counterBounces += 1
        # see if the bounces off the bottom corner
        elif logo[Y] == Height - 1 and logo[Dir] == Down_Left:
            logo[Dir] = Up_left
            counterBounces += 1
        elif logo[Y] == Height - 1 and logo[Dir] == Down_Right:
            logo[Dir] = Up_Right
            counterBounces += 1
        # if the logo crashes the corner -> color change
        if OriginalDir != logo[Dir]:
            logo[Color] = random.choice(Colors)

        if logo[Dir] == Up_left:
            logo[X] -= 2
            logo[Y] -= 1
        if logo[Dir] == Up_Right:
            logo[X] += 2
            logo[Y] -= 1
        if logo[Dir] == Down_Left:
            logo[X] -= 2
            logo[Y] += 1
        if logo[Dir] == Down_Right:
            logo[X] += 2
            logo[Y] += 1

    bext.goto(5, 0)
    bext.fg("white")
    print("CornerBounces:", counterBounces, end="")
    for logo in logos:
        bext.goto(logo[X], logo[Y])
        bext.fg(logo[Color])
        print("DVD", end="")

    bext.goto(0, 0)
    sys.stdout.flush()
    time.sleep(pause_amount)
