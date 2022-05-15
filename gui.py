from tkinter import *
from ctypes import *

cdll.LoadLibrary("libcalculadora.so")

calculadora = CDLL("libcalculadora.so")

signo = calculadora.signo
signo.restype = c_double

suma = calculadora.suma
suma.argtypes = [c_double, c_double]
suma.restype = c_double

resta = calculadora.resta
resta.argtypes = [c_double, c_double]
resta.restype = c_double

mul = calculadora.multi
mul.argtypes = [c_double, c_double]
mul.restype = c_double

div = calculadora.divi
div.argtypes = [c_double, c_double]
div.restype = c_double

seno = calculadora.senox
seno.restype = c_double

cos = calculadora.cosenox
cos.restype = c_double

tan = calculadora.tangx
tan.restype = c_double

arcoTan = calculadora.arcoTan
arcoTan.restype = c_double

arcoSeno = calculadora.arcoSeno
arcoSeno.restype = c_double

convRaG = calculadora.convRaG
convRaG.restype = c_double

convGaR = calculadora.convGaR
convGaR.restype = c_double

logarcm = calculadora.logarcm
logarcm.restype = c_double

dosalan = calculadora.dosalan
dosalan.restype = c_double

raizdos = calculadora.raizdos
raizdos.restype = c_double

win = Tk()  # This is to create a basic window
win.geometry("591x385")  # this is for the size of the window
win.resizable(False, False)  # this is to prevent from resizing the window
win.title("Calculator")


def conversion_action(mode):
    global expression
    x = float(expression)

    if mode:
        # degrees to rad
        x = convGaR(byref(c_double(x)))
        input_text.set(f'{x}')
    else:
        # rad to degrees
        x = convRaG(byref(c_double(x)))
        input_text.set(f'{x}')
    expression = str(x)


def sign_action():
    # change sign_action
    global expression
    x = float(expression)
    x = signo(byref(c_double(x)))
    input_text.set(f'{x}')
    expression = str(x)


def log_action():
    # logarithm
    global expression
    x = float(expression)
    x = logarcm(byref(c_double(x)))
    input_text.set(f'{x}')
    expression = str(x)


def square_action(mode):
    global expression
    x = float(expression)

    if mode:
        # square_action
        x = mul(x, x)
        input_text.set(f'{x}')
    else:
        # sqrt
        x = raizdos(byref(c_double(x)))
        input_text.set(f'{x}')
    expression = str(x)


def sin_action(mode):
    global expression
    x = float(expression)

    if mode:
        # sin_action
        x = seno(byref(c_double(x)))
        input_text.set(f'{x}')
    else:
        # asin
        x = arcoSeno(byref(c_double(x)))
        input_text.set(f'{x}')
    expression = str(x)


def cos_action(mode):
    global expression
    x = float(expression)

    if mode:
        # cos_action
        x = cos(byref(c_double(x)))
        input_text.set(f'{x}')
    else:
        # acos
        input_text.set(f'{x}')
    expression = str(x)


def tan_action(mode):
    global expression
    x = float(expression)

    if mode:
        # tan_action
        x = tan(byref(c_double(x)))
        input_text.set(f'{x}')
    else:
        # atan
        x = arcoTan(byref(c_double(x)))
        input_text.set(f'{x}')
    expression = str(x)


def suma_action():
    global expression
    global operand
    global op
    op = suma
    operand = float(expression)
    expression = ""
    input_text.set("")


def resta_action():
    global expression
    global operand
    global op
    op = resta
    operand = float(expression)
    expression = ""
    input_text.set("")


def div_action():
    global expression
    global operand
    global op
    op = div
    operand = float(expression)
    expression = ""
    input_text.set("")


def mul_action():
    global expression
    global operand
    global op
    op = mul
    operand = float(expression)
    expression = ""
    input_text.set("")


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
    res = op(operand, float(expression))
    input_text.set(res)
    expression = str(res)


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
conv_btn = Button(btns_frame, text="rad<->deg", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
conv_btn.bind('<Button-1>', lambda _: conversion_action(True))
conv_btn.bind('<Button-3>', lambda _: conversion_action(False))
conv_btn.grid(row=0, column=1, padx=1, pady=1)
# Change sign_action
Button(btns_frame, text="+/-", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: sign_action()).grid(row=0, column=2, padx=1, pady=1)

# Division
Button(btns_frame, text="/", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: div_action()).grid(row=0, column=3, padx=1, pady=1)

# Square number
square_btn = Button(btns_frame, text="x\u00b2", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")

square_btn.bind('<Button-1>', lambda _: square_action(True))
square_btn.bind('<Button-3>', lambda _: square_action(False))
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
       command=lambda: mul_action()).grid(row=1, column=3, padx=1, pady=1)

# Logarithm
Button(btns_frame, text="log", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2",
       command=lambda: log_action()).grid(row=1, column=4, padx=1, pady=1)

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
       command=lambda: resta_action()).grid(row=2, column=3, padx=1, pady=1)

# Sin
sin_btn = Button(btns_frame, text="sin", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
sin_btn.bind('<Button-1>', lambda _: sin_action(True))
sin_btn.bind('<Button-3>', lambda _: sin_action(False))
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
       command=lambda: suma_action()).grid(row=3, column=3, padx=1, pady=1)

# Cosine
cos_btn = Button(btns_frame, text="cos", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")
cos_btn.bind('<Button-1>', lambda _: cos_action(True))
cos_btn.bind('<Button-3>', lambda _: cos_action(False))
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
tan_btn = Button(btns_frame, text="tan", fg="black", width=10, height=3, bd=0, bg="#eee", cursor="hand2")

tan_btn.bind('<Button-1>', lambda _: tan_action(True))
tan_btn.bind('<Button-3>', lambda _: tan_action(False))
tan_btn.grid(row=4, column=4, padx=1, pady=1)
win.mainloop()
