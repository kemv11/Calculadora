# Universidad Politécnica Internacional
# Tarea 1 - calculadora
# Tecnicas de programación
# Kevin Morales valverde

from tkinter import *
import math

Window = Tk()
Window.title("Calculator")
Window.geometry("350x400")
Window.configure(background = "Black")
color_button = ("Lawn green")
index = 0

# Functions 

def Click_button(value):
    global index
    TextEntry.insert(index, value)
    index += 1
    
def delete_data():
    TextEntry.delete(0,END)
    index = 0

def Execute_Operations():
    value = TextEntry.get()
    result = eval(value)
    TextEntry.delete(0,END)
    TextEntry.insert(0,result)
    index = 0

def Prime_Number():
    number = TextEntry.get()
    value = int(number)
    if value < 2:
        TextEntry.delete(0,END)
        TextEntry.insert(0,number + " isn't prime")
    square_root = int (math.sqrt(value))+1
    for index in range (2, square_root):
        if value % index == 0:
            TextEntry.delete(0,END)
            TextEntry.insert(0,number + " isn't prime")
        else:
            TextEntry.delete(0,END)
            TextEntry.insert(0,number + " is prime")

def Palindrome_Number():
    number = TextEntry.get()
    reverse_number = number[::-1]
    if number == reverse_number:
        TextEntry.delete(0,END)
        TextEntry.insert(0, number + " is Palindrome")
    else:
        TextEntry.delete(0,END)
        TextEntry.insert(0, number + " isn't Palindrome")
        

# Entry method and Buttons

TextEntry = Entry(Window, font = ("Calibri 20"), bg = "LemonChiffon2", bd = 20)
TextEntry.grid(row = 0, column = 0, columnspan = 4, padx = 13, pady = 8)

button1= Button(Window, text = "1", bg = color_button, width = 5, height = 2, command = lambda: Click_button(1))
button2= Button(Window, text = "2", bg = color_button, width = 5, height = 2, command = lambda: Click_button(2))
button3= Button(Window, text = "3", bg = color_button, width = 5, height = 2, command = lambda: Click_button(3))
button4= Button(Window, text = '4', bg = color_button, width = 5, height = 2, command = lambda: Click_button(4))
button5= Button(Window, text = "5", bg = color_button, width = 5, height = 2, command = lambda: Click_button(5))
button6= Button(Window, text = "6", bg = color_button, width = 5, height = 2, command = lambda: Click_button(6))
button7= Button(Window, text = "7", bg = color_button, width = 5, height = 2, command = lambda: Click_button(7))
button8= Button(Window, text = "8", bg = color_button, width = 5, height = 2, command = lambda: Click_button(8))
button9= Button(Window, text = "9", bg = color_button, width = 5, height = 2, command = lambda: Click_button(9))
button0= Button(Window, text = "0", bg = color_button, width = 18, height = 2, command = lambda: Click_button(0))

button_Erase = Button(Window, text = "AC", bg = color_button, width = 5, height = 2, command = lambda: delete_data())
button_OpenParenthesis = Button(Window, text = "(", bg = color_button, width = 5, height = 2, command = lambda: Click_button("("))
button_CloseParenthesis = Button(Window, text = ")", bg = color_button, width = 5, height = 2, command = lambda: Click_button(")"))
button_dot = Button(Window, text = ".", width = 5, bg = color_button, height = 2, command = lambda: Click_button("."))

button_Sum = Button(Window, text = "+", width = 5, bg = color_button, height = 2, command = lambda: Click_button("+"))
button_Subtraction = Button(Window, text = "-", bg = color_button, width = 5, height = 2, command = lambda: Click_button("-"))
button_Multiplication = Button(Window, text = "/", bg = color_button, width = 5, height = 2, command = lambda: Click_button("/"))
button_Division = Button(Window, text = "*", bg = color_button, width = 5, height = 2, command = lambda: Click_button("*"))
button_Equal = Button(Window, text = "=", bg = color_button, width = 5, height = 2, command = lambda: Execute_Operations())
button_Prime = Button(Window, text = "Prime Number", bg = color_button, width = 18, height = 2, command = lambda: Prime_Number())
button_Palindrome = Button(Window, text = "Palindrome Number", bg = color_button, width = 18, height = 2, command = lambda: Palindrome_Number())

# Buttons in graphical interface

button_Erase.grid(row = 1, column = 0, padx = 5, pady = 5)
button_OpenParenthesis.grid(row = 1, column = 1, padx = 5, pady = 5)
button_CloseParenthesis.grid(row = 1, column = 2, padx = 5, pady = 5)
button_Division.grid(row = 1, column = 3, padx = 5, pady = 5)

button7.grid(row = 2, column = 0, padx = 5, pady = 5)
button8.grid(row = 2, column = 1, padx = 5, pady = 5)
button9.grid(row = 2, column = 2, padx = 5, pady = 5)
button_Multiplication.grid(row =2 , column = 3, padx = 5, pady = 5)

button4.grid(row = 3, column = 0, padx = 5, pady = 5)
button5.grid(row = 3, column = 1, padx = 5, pady = 5)
button6.grid(row = 3, column = 2, padx = 5, pady = 5)
button_Sum.grid(row = 3 , column = 3, padx = 5, pady = 5)

button1.grid(row = 4, column = 0, padx = 5, pady = 5)
button2.grid(row = 4, column = 1, padx = 5, pady = 5)
button3.grid(row = 4, column = 2, padx = 5, pady = 5)
button_Subtraction.grid(row = 4 , column = 3, padx = 5, pady = 5)

button0.grid(row = 5, column = 0, columnspan = 2, padx = 5, pady = 5)
button_dot.grid(row = 5, column = 2, padx = 5, pady = 5)
button_Equal.grid(row = 5, column = 3, padx = 5, pady = 5)

button_Prime.grid(row = 6, column = 0, columnspan = 2, padx = 5, pady = 5)
button_Palindrome.grid(row = 6, column = 2, columnspan = 2, padx = 5, pady = 5)


Window.mainloop()
