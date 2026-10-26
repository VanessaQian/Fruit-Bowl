# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define isBanana = False
define o = Character("Orange", color="#f67f35")
define s = Character("Strawberry", color = "#ff3333")
define w = Character("Watermelon", color = "#8aab2e")
define l = Character("Lemon", color="#fff700")
define yn = Character("[You]")

define zoom_factor = 1.5
image lemon happy:
    "images/chara/lemon happy.png"
    zoom zoom_factor
image lemon normal:
    "images/chara/lemon normal.png"
    zoom zoom_factor
image lemon upset:
    "images/chara/lemon upset.png"
    zoom zoom_factor
image orange happy:
    "images/chara/orange happy.png"
    zoom zoom_factor
image orange normal:
    "images/chara/orange normal.png"
    zoom zoom_factor
image orange upset:
    "images/chara/orange upset.png"
    zoom zoom_factor
image watermelon happy:
    "images/chara/watermelon happy.png"
    zoom zoom_factor
image watermelon extra happy:
    "images/chara/watermelon extra happy.png"
    zoom zoom_factor