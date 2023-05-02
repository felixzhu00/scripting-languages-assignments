from tkinter import *


root = Tk()
root.geometry("300x400")
root.title("Calculator")
root.configure(bg = "gray80")

my_font = ('Times', 15)
display_str = StringVar()
error_message = ""

input_number = 0
def button_construct(text, command):
    btn = Button(root, font = my_font, text = text, bg = "gray80", command = command ,relief=RAISED)
    # btn.pack()
    return btn
def num_press(num):
    global display_str
    display_str.set(display_str.get() + num)
def clear():
    display_str.set("")
def delete():
    display_str.set(display_str.get()[0:-1])
def calc():
    try:
        global display_str
        display_str.set(eval(display_str.get()))
    except Exception as e:
        display_str.set("ERROR")
        print("Error: " + str(e))

main_frame = Frame(root)

txt = Entry(root, font = my_font, bg = "gray80" ,textvariable = display_str)


num0 = button_construct("0", lambda : num_press("0"))
num1 = button_construct("1", lambda : num_press("1"))
num2 = button_construct("2", lambda : num_press("2"))
num3 = button_construct("3", lambda : num_press("3"))
num4 = button_construct("4", lambda : num_press("4"))
num5 = button_construct("5", lambda : num_press("5"))
num6 = button_construct("6", lambda : num_press("6"))
num7 = button_construct("7", lambda : num_press("7"))
num8 = button_construct("8", lambda : num_press("8"))
num9 = button_construct("9", lambda : num_press("9"))

left_brkt = button_construct("(", lambda : num_press("("))
right_brkt = button_construct(")", lambda : num_press(")"))
add = button_construct("+", lambda : num_press("+"))
sub = button_construct("-", lambda : num_press("-"))
mul = button_construct("*", lambda : num_press("*"))
div = button_construct("/", lambda : num_press("/"))

clear_btn = button_construct("clear", clear)
calc_btn = button_construct("calc", calc)
del_btn = button_construct("del", delete)


txt.grid(row = 0 , column = 1, columnspan = 12 , padx = 20, pady = 20)

num0.grid(row = 1 , column = 1, sticky="ew", columnspan = 3)
num1.grid(row = 1 , column = 4, sticky="ew", columnspan = 3)
num2.grid(row = 1 , column = 7, sticky="ew", columnspan = 3)
num3.grid(row = 1 , column = 10, sticky="ew", columnspan = 3)
num4.grid(row = 2 , column = 1, sticky="ew", columnspan = 3)
num5.grid(row = 2 , column = 4, sticky="ew", columnspan = 3)
num6.grid(row = 2 , column = 7, sticky="ew", columnspan = 3)
num7.grid(row = 2 , column = 10, sticky="ew", columnspan = 3)
num8.grid(row = 3 , column = 1, sticky="ew", columnspan = 3)
num9.grid(row = 3 , column = 4, sticky="ew", columnspan = 3)


left_brkt.grid(row = 3 , column = 7, sticky="ew", columnspan = 3)
right_brkt.grid(row = 3 , column = 10, sticky="ew", columnspan = 3)
add.grid(row = 4 , column = 1, sticky="ew", columnspan = 3)
sub.grid(row = 4 , column = 4, sticky="ew", columnspan = 3)
mul.grid(row = 4 , column = 7, sticky="ew", columnspan = 3)
div.grid(row = 4 , column = 10, sticky="ew", columnspan = 3)

clear_btn.grid(row = 5 , column = 1, sticky="ew", columnspan = 4)
calc_btn.grid(row = 5 , column = 5, sticky="ew", columnspan = 4)
del_btn.grid(row = 5 , column = 9, sticky="ew", columnspan = 4)

root.grid_columnconfigure((0,13), weight=1)

root.mainloop()





# txt.grid(row = 0 , column = 0, columnspan = 4 , padx = 20, pady = 20)

# num0.grid(row = 1 , column = 0)
# num1.grid(row = 1 , column = 1)
# num2.grid(row = 1 , column = 2)
# num3.grid(row = 1 , column = 3)
# num4.grid(row = 2 , column = 0)
# num5.grid(row = 2 , column = 1)
# num6.grid(row = 2 , column = 2)
# num7.grid(row = 2 , column = 3)
# num8.grid(row = 3 , column = 0)
# num9.grid(row = 3 , column = 1)


# left_brkt.grid(row = 3 , column = 2)
# right_brkt.grid(row = 3 , column = 3)
# add.grid(row = 4 , column = 0)
# sub.grid(row = 4 , column = 1)
# mul.grid(row = 4 , column = 2)
# div.grid(row = 4 , column = 3)

# # root.grid_columnconfigure((0, 1, 2, 3), weight=1)
# root.grid_columnconfigure((0,4), weight=1)
