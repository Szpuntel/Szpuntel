from tkinter import *

window = Tk()
x = IntVar()
whos_turn = 0


icon = PhotoImage(file='C:\\Users\\szpun\\Desktop\\Python\\GUI\\pv\\k_i_k\\icon.png')
iconx = PhotoImage(file='C:\\Users\\szpun\\Desktop\\Python\\GUI\\pv\\k_i_k\\iconx.png')
icono = PhotoImage(file='C:\\Users\\szpun\\Desktop\\Python\\GUI\\pv\\k_i_k\\icono.png')

game_dict = {
        "1":"None","2":"None","3":"None",
        "4":"None","5":"None","6":"None",
        "7":"None","8":"None","9":"None",
            }

def restart():
    window.destroy()

def check_clicked_button():
    global game_dict
    if game_dict["1"] == "X":
        global icon 
        icon = PhotoImage(file='C:\\Users\\szpun\\Desktop\\Python\\GUI\\pv\\k_i_k\\iconx.png')

def where_to_put(place,value):
    if value == "x":
        button = Checkbutton(window,image=iconx)
    if value == "o":
        button = Checkbutton(window,image=icono)

    if place == 1: button.grid(column=0,row=0)
    if place == 2: button.grid(column=1,row=0)
    if place == 3: button.grid(column=2,row=0)
    if place == 4: button.grid(column=0,row=1)
    if place == 5: button.grid(column=1,row=1)
    if place == 6: button.grid(column=2,row=1)
    if place == 7: button.grid(column=0,row=2)
    if place == 8: button.grid(column=1,row=2)
    if place == 9: button.grid(column=2,row=2)

def put_o(place):
    where_to_put(place,"o")
        
def put_x(place):
    where_to_put(place,"x")


def check_winner():
    if game_dict["1"] == "X" and game_dict["2"] == "X" and game_dict["3"] == "X" or \
       game_dict["4"] == "X" and game_dict["5"] == "X" and game_dict["6"] == "X" or \
       game_dict["7"] == "X" and game_dict["8"] == "X" and game_dict["9"] == "X" or \
       game_dict["1"] == "X" and game_dict["4"] == "X" and game_dict["7"] == "X" or \
       game_dict["2"] == "X" and game_dict["5"] == "X" and game_dict["8"] == "X" or \
       game_dict["1"] == "X" and game_dict["5"] == "X" and game_dict["9"] == "X" or \
       game_dict["7"] == "X" and game_dict["5"] == "X" and game_dict["3"] == "X" or \
       game_dict["3"] == "X" and game_dict["6"] == "X" and game_dict["9"] == "X":
        label_x_winner.grid(column=1, row=3)
        restartbutton.grid(column=1,row=4)

    if game_dict["1"] == "O" and game_dict["2"] == "O" and game_dict["3"] == "O" or \
       game_dict["4"] == "O" and game_dict["5"] == "O" and game_dict["6"] == "O" or \
       game_dict["7"] == "O" and game_dict["8"] == "O" and game_dict["9"] == "O" or \
       game_dict["1"] == "O" and game_dict["4"] == "O" and game_dict["7"] == "O" or \
       game_dict["2"] == "O" and game_dict["5"] == "O" and game_dict["8"] == "O" or \
       game_dict["1"] == "O" and game_dict["5"] == "O" and game_dict["9"] == "O" or \
       game_dict["7"] == "O" and game_dict["5"] == "O" and game_dict["3"] == "O" or \
       game_dict["3"] == "O" and game_dict["6"] == "O" and game_dict["9"] == "O":
        label_o_winner.grid(column=1, row=3)
        restartbutton.grid(column=1,row=4)

    if whos_turn == 9:
        label.grid(column=1, row=3)
        restartbutton.grid(column=1,row=4)

def place_value():
    global whos_turn
    place = x.get()

    if whos_turn % 2 == 0:
        game_dict.update({f"{place}":"X"})
        put_x(place)
    else:
        game_dict.update({f"{place}":"O"})
        put_o(place)

    if whos_turn % 2 == 1:
        print("Ruch gracza X")
    else:
        print("Ruch gracza O")

    whos_turn += 1

    if whos_turn >= 5:
        check_winner()


label = Label(window, text="Remis", font=('Arial', 15),fg="red")
label_x_winner = Label(window, text="X Won!", font=('Arial', 15),fg="red")
label_o_winner = Label(window, text="O Won!", font=('Arial', 15),fg="red")

restartbutton = Button(window,text="EXIT", font=('Arial',15),command=restart)
Checkbutton_1 = Checkbutton(window,command = place_value,variable=x,onvalue=1, image=icon)
Checkbutton_2 = Checkbutton(window,command = place_value,variable=x,onvalue=2, image=icon)
Checkbutton_3 = Checkbutton(window,command = place_value,variable=x,onvalue=3, image=icon)
Checkbutton_4 = Checkbutton(window,command = place_value,variable=x,onvalue=4, image=icon)
Checkbutton_5 = Checkbutton(window,command = place_value,variable=x,onvalue=5, image=icon)
Checkbutton_6 = Checkbutton(window,command = place_value,variable=x,onvalue=6, image=icon)
Checkbutton_7 = Checkbutton(window,command = place_value,variable=x,onvalue=7, image=icon)
Checkbutton_8 = Checkbutton(window,command = place_value,variable=x,onvalue=8, image=icon)
Checkbutton_9 = Checkbutton(window,command = place_value,variable=x,onvalue=9, image=icon)

Checkbutton_1.grid(column=0,row=0)
Checkbutton_2.grid(column=1,row=0)
Checkbutton_3.grid(column=2,row=0)
Checkbutton_4.grid(column=0,row=1)
Checkbutton_5.grid(column=1,row=1)
Checkbutton_6.grid(column=2,row=1)
Checkbutton_7.grid(column=0,row=2)
Checkbutton_8.grid(column=1,row=2)
Checkbutton_9.grid(column=2,row=2)

window.mainloop()