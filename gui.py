from tkinter import *

win = Tk()  # This is to create a basic window
win.geometry("391x324")  # this is for the size of the window
win.resizable(False, False)  # this is to prevent from resizing the window
win.title("Calculator")


def conversion_action(mode):
    global expression
    x = int(expression)

    if mode:
        # degrees to rad
        input_text.set(f'{x}')
    else:
        # rad to degrees
        input_text.set(f'{x}')
    expression = x


def sign_action():
    # change sign_action
    global expression
    x = int(expression)

    input_text.set(f'{-x}')
    expression = -x


def log_action():
    # logarithm
    global expression
    x = int(expression)

    input_text.set(f'{x}')
    expression = x


def square_action(mode):
    global expression
    x = int(expression)

    if mode:
        # square_action
        input_text.set(f'{x}')
    else:
        # sqrt
        input_text.set(f'{x}')
    expression = x


def sin_action(mode):
    global expression
    x = int(expression)

    if mode:
        # sin_action
        input_text.set(f'{x}')
    else:
        # asin
        input_text.set(f'{x}')
    expression = x


def cos_action(mode):
    global expression
    x = int(expression)

    if mode:
        # cos_action
        input_text.set(f'{x}')
    else:
        # acos
        input_text.set(f'{x}')
    expression = x


def tan_action(mode):
    global expression
    x = int(expression)

    if mode:
        # tan_action
        input_text.set(f'{x}')
    else:
        # atan
        input_text.set(f'{x}')
    expression = x


def suma_action():
    global expression
    global operand
    global op
    op = print
    operand = int(expression)
    expression = ""
    input_text.set("")


def resta_action():
    global expression
    global operand
    global op
    op = print
    operand = int(expression)
    expression = ""
    input_text.set("")


def div_action():
    global expression
    global operand
    global op
    op = print
    operand = int(expression)
    expression = ""
    input_text.set("")


def mul_action():
    global expression
    global operand
    global op
    op = print
    operand = int(expression)
    expression = ""
    input_text.set("")


actions = {
    "suma_action": suma_action,
    "resta_action": resta_action,
    "mul_action": mul_action,
    "div_action": div_action,
    "conversion_action": lambda: conversion_action(True),
    "sign_action": sign_action,
    "square_action": lambda: square_action(True),
    "log_action": log_action,
    "sin_action": lambda: sin_action(True),
    "cos_action": lambda: cos_action(True),
    "tan_action": lambda: tan_action(True),
}

sec_actions = {
    "conversion_action": lambda: conversion_action(False),
    "square_action": lambda: square_action(False),
    "sin_action": lambda: sin_action(False),
    "cos_action": lambda: cos_action(False),
    "tan_action": lambda: tan_action(False),
}


# 'action_click' function :
# Executes the default action of a pressed
# button that matches with action dictionary members
def action_click(item):
    actions.get(item)()


# 'action_dClick function:
# Executes the secondary action of a pressed button
# that matches with sec_action dictionary members
def action_double_click(item):
    sec_actions.get(item)()


# 'btn_click' function :
# This Function continuously updates the
# input field whenever you enter a number

def btn_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)


# 'bt_clear' function :This is used to clear
# the input field

def bt_clear():
    global expression
    expression = ""
    input_text.set("")


# 'bt_equal':This method calculates the expression
# present in input field

def bt_equal():
    global expression
    global op
    global operand
    op(int(expression))
    input_text.set(str(operand))
    expression = ""


expression = ""
operand = 0
op = print

# 'StringVar()' :It is used to get the instance of input field

input_text = StringVar()

# Let us creating a frame for the input field

input_frame = Frame(win, width=322, height=50, bd=0, highlightbackground="black", highlightcolor="black",
                    highlightthickness=2)

input_frame.pack(side=TOP)

# Let us create a input field inside the 'Frame'

input_field = Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0,
                    justify=RIGHT)

input_field.grid(row=0, column=0)

input_field.pack(ipady=10)  # 'ipady' is internal padding to increase the height of input field

# Let us creating another 'Frame' for the button below the 'input_frame'

btns_frame = Frame(win, width=322, height=272.5, bg="grey")

btns_frame.pack()

# first row

# Clear Input
Button(btns_frame, text="C", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: bt_clear()).grid(row=0, column=0, padx=1, pady=1)

# Conversion between radians and degrees
conv_btn = Button(btns_frame, text="rad<->deg", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
                  command=lambda: action_click("conversion_action"))
conv_btn.bind('<Button-1>', lambda _: action_click('conversion_action'))
conv_btn.bind('<Button-3>', lambda _: action_double_click('conversion_action'))
conv_btn.grid(row=0, column=1, padx=1, pady=1)
# Change sign_action
Button(btns_frame, text="+/-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: action_click("sign_action")).grid(row=0, column=2, padx=1, pady=1)

# Division
Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: action_click("div_action")).grid(row=0, column=3, padx=1, pady=1)

# Square number
square_btn = Button(btns_frame, text="x\u00b2", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")

square_btn.bind('<Button-1>', lambda _: action_click('square_action'))
square_btn.bind('<Button-3>', lambda _: action_double_click('square_action'))
square_btn.grid(row=0, column=4, padx=1, pady=1)

# second row

# Seven
Button(btns_frame, text="7", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(7)).grid(row=1, column=0, padx=1, pady=1)

# Eight
Button(btns_frame, text="8", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(8)).grid(row=1, column=1, padx=1, pady=1)

# Nine
Button(btns_frame, text="9", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(9)).grid(row=1, column=2, padx=1, pady=1)

# Multiplication
Button(btns_frame, text="*", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: action_click("mul_action")).grid(row=1, column=3, padx=1, pady=1)

# Logarithm
log = Button(btns_frame, text="log_action", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
log.bind('<Button-1>', lambda _: action_click('log_action'))
log.bind('<Button-3>', lambda _: action_double_click('log_action'))
log.grid(row=1, column=4, padx=1, pady=1)

# third row
# Four
Button(btns_frame, text="4", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(4)).grid(row=2, column=0, padx=1, pady=1)

# Five
Button(btns_frame, text="5", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(5)).grid(row=2, column=1, padx=1, pady=1)

# Six
Button(btns_frame, text="6", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(6)).grid(row=2, column=2, padx=1, pady=1)

# Minus
Button(btns_frame, text="-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: action_click("resta_action")).grid(row=2, column=3, padx=1, pady=1)

# Sin
sin_btn = Button(btns_frame, text="sin_action", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
sin_btn.bind('<Button-1>', lambda _: action_click('sin_action'))
sin_btn.bind('<Button-3>', lambda _: action_double_click('sin_action'))
sin_btn.grid(row=2, column=4, padx=1, pady=1)

# fourth row

# One
Button(btns_frame, text="1", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(1)).grid(row=3, column=0, padx=1, pady=1)

# Two
Button(btns_frame, text="2", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(2)).grid(row=3, column=1, padx=1, pady=1)

# Three
Button(btns_frame, text="3", fg="black", width=10, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(3)).grid(row=3, column=2, padx=1, pady=1)

# Plus
Button(btns_frame, text="+", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: action_click("suma_action")).grid(row=3, column=3, padx=1, pady=1)

# Cosine
cos_btn = Button(btns_frame, text="cos_action", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
cos_btn.bind('<Button-1>', lambda _: action_click('cos_action'))
cos_btn.bind('<Button-3>', lambda _: action_double_click('cos_action'))
cos_btn.grid(row=3, column=4, padx=1, pady=1)
# fourth row

# Zero
Button(btns_frame, text="0", fg="black", width=21, height=3, bd=0, bg="#fff", cursor="hand2",
       command=lambda: btn_click(0)).grid(row=4, column=0, columnspan=2, padx=1, pady=1)

# Dot
Button(btns_frame, text=".", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: btn_click(".")).grid(row=4, column=2, padx=1, pady=1)

# Equals
Button(btns_frame, text="=", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: bt_equal()).grid(row=4, column=3, padx=1, pady=1)

# Tangent
tan_btn = Button(btns_frame, text="tan_action", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")

tan_btn.bind('<Button-1>', lambda _: action_click('tan_action'))
tan_btn.bind('<Button-3>', lambda _: action_double_click('tan_action'))
tan_btn.grid(row=4, column=4, padx=1, pady=1)
win.mainloop()
