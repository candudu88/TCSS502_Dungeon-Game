import random
from imp import reload

from room import Room

import math
import PySimpleGUI as psg
from dungeon import Dungeon
from adventurer import Adventurer

global my_map
global window

ad = Adventurer("warrior")
my_map = Dungeon(6, 6)  # assume the rows and columns must be greater than 1
my_map.generate()
my_map.print()
my_map.draw()

my_map.rooms[0][0].draw_top()
print()
my_map.rooms[0][0].draw_middle()
print()
my_map.rooms[0][0].draw_bottom()
print()

print(my_map.rooms[0][0])

# def intro():
#     print("Welcome to Dungeon Adventure!\n"
#           "\n"
#           "We need you to explore the dungeon and find the four pillars of OOP.\n"
#           "Your goal:\n"
#           "\t1) Collect all the four pillars of OOP\n"
#           "\t2) Get to the exit safely.\n"
#           "\n"
#           "Items randomly placed in each room:\n"
#           "\t1) Healing potion(random heal amount),\n"
#           "\t2) Vision potion(reveal, adjacent rooms)\n"
#           "\t3) Pit(random damage to adventurer),\n"
#           "\t4) OOP pillars(\"A\",\"P\",\"I\",\"E\"\n"
#           "\n"
#           "Are you ready to play?!!!\n"
#           "\n"
#           "\'c\' : for continue\n"
#           "\'q\' : for quit\n"
#           "\n")
#
#
# def ask_to_play():
#     choice = input("Your choice: ")
#     while not (choice.startswith("c") or choice.startswith("q")):
#         print("Sorry not an option, please type one of the options.\n"
#               "\'c\' : for continue\n"
#               "\'q\' : for quit\n"
#               "\n")
#         choice = input("Your choice: ")
#     if choice.startswith("c"):
#         return True
#     else:
#         return False


# def ask_for_name():
#     player_name = input("What is your name? ")
#     return player_name


# intro()
# should_play = ask_to_play()
# if should_play:
#     name = ask_for_name()
#     adventurer = Adventurer(name)
#     print(f"Good luck {name}!")
#     print(adventurer)


AppFont = 'Any 16'
psg.theme('DarkAmber')
layout = [[(psg.Graph((360, 360), (0, 0), (360, 360), key='Graph'))],
          [psg.Text('Player: ' + str(ad.hit_point), key='-P1-', text_color='red')],
          [psg.Text('Hit point: ', key='-P1-', text_color='white')],
          [psg.Text('Healing potion: ', key='-P1-', text_color='white'), psg.Button('NewMaze', font=AppFont)],
          [psg.Text('vision potion:        ', key='-P1-', text_color='white'),
           psg.Text('', key='-P5-', text_color='white')],
          ]
window = psg.Window('Dungeon Adventure', layout, resizable=True, finalize=True, return_keyboard_events=True)

# current_x = 1
# current_y = 1


def checkEvents(event):
    move = ''
    if len(event) == 1:
        if ord(event) == 63232:  # UP
            move = 'Up'
        elif ord(event) == 63233:  # DOWN
            move = 'Down'
        elif ord(event) == 63234:  # LEFT
            move = 'Left'
        elif ord(event) == 63235:  # RIGHT
            move = 'Right'
        elif ord(event) == 86 or ord(event) == 118:  # V
            move = 'V'
        elif ord(event) == 72 or ord(event) == 104:  # H
            move = 'H'
    # Filter key press Windows :
    else:
        if event.startswith('Up'):
            move = 'Up'
        elif event.startswith('Down'):
            move = 'Down'
        elif event.startswith('Left'):
            move = 'Left'
        elif event.startswith('Right'):
            move = 'Right'
        elif event.startswith('V'):
            move = 'V'
        elif event.startswith('H'):
            move = 'H'
    return move


exit_count = 1
entrance_count = 1
A_count = 1
E_count = 1
I_count = 1
P_count = 1
healing_potion_count = math.floor(0.1 * 6 * 6)
vision_potion_count = math.floor(0.1 * 6 * 6)
pit_count = math.floor(0.1 * 6 * 6)
total_count = exit_count + entrance_count + A_count + E_count + I_count + P_count + healing_potion_count + vision_potion_count + pit_count
random_list = random.sample(range(0, 35), total_count)
print(random_list)

for n in random_list:
    if exit_count > 0:
        my_map.rooms[n // 6][n % 6].set_exit(True)
        exit_count -= 1
    elif entrance_count > 0:
        my_map.rooms[n // 6][n % 6].set_entrance(True)
        entrance_count -= 1
    elif A_count > 0:
        my_map.rooms[n // 6][n % 6].set_pillar("Abstraction")
        A_count -= 1
    elif E_count > 0:
        my_map.rooms[n // 6][n % 6].set_pillar("Encapsulation")
        E_count -= 1
    elif I_count > 0:
        my_map.rooms[n // 6][n % 6].set_pillar("Inheritance")
        I_count -= 1
    elif P_count > 0:
        my_map.rooms[n // 6][n % 6].set_pillar("Polymorphism")
        P_count -= 1
    elif healing_potion_count > 1:
        my_map.rooms[n // 6][n % 6].set_health_potion(True)
        healing_potion_count -= 1
    elif healing_potion_count == 1:
        my_map.rooms[n // 6][n % 6].set_health_potion(True)
        my_map.rooms[n // 6][n % 6].set_vision_potion(True)
        healing_potion_count -= 1
        vision_potion_count -= 1
    elif vision_potion_count > 0:
        my_map.rooms[n // 6][n % 6].set_vision_potion(True)
        vision_potion_count -= 1
    elif pit_count > 0:
        my_map.rooms[n // 6][n % 6].set_pit(True)
        pit_count -= 1


def draw_image(x, y, my_map):
    room = my_map.get_room()
    if 0 > x or x >= my_map.rows or 0 > y or y >= my_map.cols:
        return
    if room[x][y]._exit:
        window['Graph'].draw_image(filename='images/exit.png', location=(y * 60, 360 - x * 60))
    elif room[x][y]._pit:
        window['Graph'].draw_image(filename='images/pit.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].south and room[x][y].west and room[x][y].east:
        window['Graph'].draw_image(filename='images/T1.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].north and room[x][y].south and room[x][y].west:
        window['Graph'].draw_image(filename='images/T2.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].north and room[x][y].south and room[x][y].east:
        window['Graph'].draw_image(filename='images/T3.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].north and room[x][y].west and room[x][y].east:
        window['Graph'].draw_image(filename='images/T4.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].north and room[x][y].west:
        window['Graph'].draw_image(filename='images/L1.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].north and room[x][y].east:
        window['Graph'].draw_image(filename='images/L2.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].north and room[x][y].south:
        window['Graph'].draw_image(filename='images/L3.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].west and room[x][y].east:
        window['Graph'].draw_image(filename='images/L4.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].west and room[x][y].south:
        window['Graph'].draw_image(filename='images/L5.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].east and room[x][y].south:
        window['Graph'].draw_image(filename='images/L6.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].south:
        window['Graph'].draw_image(filename='images/S1.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].west:
        window['Graph'].draw_image(filename='images/S2.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].north:
        window['Graph'].draw_image(filename='images/S3.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].east:
        window['Graph'].draw_image(filename='images/S4.png', location=(y * 60, 360 - x * 60))
    if room[x][y].get_health_potion() and room[x][y].get_vision_potion():
        window['Graph'].draw_image(filename='images/H.png', location=(y * 60, 360 - x * 60))
        window['Graph'].draw_image(filename='images/V.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].get_health_potion():
        window['Graph'].draw_image(filename='images/H.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].get_vision_potion():
        window['Graph'].draw_image(filename='images/V.png', location=(y * 60, 360 - x * 60))
        room[x][y].set_vision_potion(False)
    elif room[x][y].get_pillar() == "Abstraction":
        window['Graph'].draw_image(filename='images/A.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].get_pillar() == "Encapsulation":
        window['Graph'].draw_image(filename='images/E.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].get_pillar() == "Inheritance":
        window['Graph'].draw_image(filename='images/I.png', location=(y * 60, 360 - x * 60))
    elif room[x][y].get_pillar() == "Polymorphism":
        window['Graph'].draw_image(filename='images/P.png', location=(y * 60, 360 - x * 60))


def dungeonadventure_test():
    current_x = 1
    current_y = 1
    draw_image(current_x, current_y, my_map)
    window['Graph'].draw_image(filename='images/Huntress.png', location=(current_y * 60, 360 - current_x * 60))
    while True:
        event, values = window.read()
        old_x = current_x
        old_y = current_y
        if my_map.get_room()[current_x][current_y].north and checkEvents(event) == 'Up' and current_x - 1 >= 0:
            current_x = current_x - 1
        elif my_map.get_room()[current_x][current_y].south and checkEvents(
                event) == 'Down' and current_x + 1 < my_map.cols:
            current_x = current_x + 1
            ad.hit_point -= 1
            window['-P1-'].update(str(ad.hit_point))
            window['-P5-'].update("Abstraction")
        elif my_map.get_room()[current_x][current_y].west and checkEvents(event) == 'Left' and current_y - 1 >= 0:
            current_y = current_y - 1
        elif my_map.get_room()[current_x][current_y].east and checkEvents(
                event) == 'Right' and current_y + 1 < my_map.rows:
            current_y = current_y + 1
        elif checkEvents(event) == 'V':
            draw_image(current_x, current_y + 1, my_map)
            draw_image(current_x, current_y - 1, my_map)
            draw_image(current_x + 1, current_y, my_map)
            draw_image(current_x - 1, current_y, my_map)
            draw_image(current_x + 1, current_y + 1, my_map)
            draw_image(current_x - 1, current_y + 1, my_map)
            draw_image(current_x + 1, current_y - 1, my_map)
            draw_image(current_x - 1, current_y - 1, my_map)

        draw_image(current_x, current_y, my_map)
        window['Graph'].draw_image(filename='images/Huntress.png', location=(current_y * 60, 360 - current_x * 60))
        if old_x != current_x or old_y != current_y:
            draw_image(old_x, old_y, my_map)
        if event == 'NewMaze':
            window['Graph'].erase()
            dungeonadventure_test()
        if event == psg.WIN_CLOSED:
            break
    window.close()


if __name__ == "__main__":
    dungeonadventure_test()
