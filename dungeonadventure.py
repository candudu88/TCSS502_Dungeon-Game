from room import Room
from dungeon import Dungeon
import PySimpleGUI as psg
from dungeon import Dungeon

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

psg.theme('DarkAmber')
layout = [[(psg.Graph((360, 360), (0, 0), (360, 360), key='Graph'))],
          [psg.Button('OK')]]
window = psg.Window('Car Dashboard', layout, resizable=True, finalize=True, return_keyboard_events=True)



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


current_x = 0
current_y = 0
my_map.rooms[0][0]._pit = True

def draw_image(x, y):
    room = my_map.get_room()
    if 0 > x or x >= my_map.rows or 0 > y or y >= my_map.cols:
        return
    if room[x][y]._exit:
        window['Graph'].draw_image(filename='images/pit.png', location=(y * 60, 360 - x * 60))
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
    # elif room.south and room.west and room.east:
    #     window['Graph'].draw_image(filename='images/T1.png', location=(y * 60, 360 - x * 60))
    # elif room.north and room.west and room.east:
    #     window['Graph'].draw_image(filename='images/T2.png', location=(y * 60, 360 - x * 60))
    # elif room.north and room.south and room.east:
    #     window['Graph'].draw_image(filename='images/T3.png', location=(y * 60, 360 - x * 60))
    # elif room.north and room.south and room.west:
    #     window['Graph'].draw_image(filename='images/T4.png', location=(y * 60, 360 - x * 60))


while True:
    event, values = window.read()
    # if checkEvents(event) == 'Up':
    #     window['Graph'].draw_image(filename='images/map.png', location=(60, 120))
    old_x = current_x
    old_y = current_y
    if my_map.get_room()[current_x][current_y].north and checkEvents(event) == 'Up' and current_x - 1 >= 0:
        current_x = current_x - 1
    elif my_map.get_room()[current_x][current_y].south and checkEvents(event) == 'Down' and current_x + 1 < my_map.cols:
        current_x = current_x + 1
    elif my_map.get_room()[current_x][current_y].west and checkEvents(event) == 'Left' and current_y - 1 >= 0:
        current_y = current_y - 1
    elif my_map.get_room()[current_x][current_y].east and checkEvents(event) == 'Right' and current_y + 1 < my_map.rows:
        current_y = current_y + 1
    elif checkEvents(event) == 'V':
        draw_image(current_x, current_y + 1)
        draw_image(current_x, current_y - 1)
        draw_image(current_x + 1, current_y)
        draw_image(current_x - 1, current_y)
        draw_image(current_x + 1, current_y + 1)
        draw_image(current_x - 1, current_y + 1)
        draw_image(current_x + 1, current_y - 1)
        draw_image(current_x - 1, current_y - 1)

    # print(my_map.get_room()[current_x][current_y])
    draw_image(current_x, current_y)
    window['Graph'].draw_image(filename='images/Huntress.png', location=(current_y * 60, 360 - current_x * 60))
    if old_x != current_x or old_y != current_y:
        draw_image(old_x, old_y)
    if event == psg.WIN_CLOSED:
        break
window.close()


# width = 10
# col = 8
#



#
# def move(x, y, rooms, dungeon):
#     current_x = 0
#     current_y = 0
#     if rooms[current_x][current_y].north and checkEvents(event) == 'Up':
#         temp_y = current_y - 1
#     elif rooms[current_x][current_y].south and checkEvents(event) == 'Down':
#         temp_y = current_y + 1
#     elif rooms[current_x][current_y].west and checkEvents(event) == 'Left':
#         temp_x = current_x - 1
#     elif rooms[current_x][current_y].east and checkEvents(event) == 'Right':
#         temp_x = current_x + 1
#     if 0 <= temp_x < dungeon.cols:
#         next_x = temp_x
#     if 0 <= temp_y < dungeon.rows:
#         next_y = temp_y
#     window['Graph'].draw_image(filename='images/map.png', location=(current_x * 60, 360 - current_y * 60))
