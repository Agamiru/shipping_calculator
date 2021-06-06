from tkinter import *

"""
A simple Volumetric Weight calculator, mostly used in the shipping/freight industry.
Basically, box dimensions (length, width, and height), all in inches, are given along with a
shipping constant (usually unique to the shipping/freight company) and the
volumetric weight of the item is calculated and returned using the provided values.  
"""

# Loading the main window

mainWindow = Tk()
mainWindow.title("Shipping Calculator")
mainWindow.geometry("330x350+800+150")
mainWindow["padx"] = 10
mainWindow["pady"] = 5

result_frame = Frame(mainWindow, borderwidth=2)
result_frame.grid(row=0, column=0, rowspan=3, columnspan=5, sticky="ew")
result_frame.rowconfigure(0, minsize=5)
result_frame.rowconfigure(1, minsize=30)
result_frame.rowconfigure(2, minsize=10)

result_box = Entry(result_frame, disabledbackground="white", width=50, justify=CENTER, insertbackground="white", borderwidth=2, relief="sunken")
result_box.grid(row=1, column=0, rowspan=1, sticky="nsew")

inputFrame = Frame(mainWindow, relief="sunken", borderwidth=1)


#   Configuring inputFrame rows and columns
for col_num in range(0, 5):
    inputFrame.columnconfigure(col_num, minsize=50)

inputFrame.columnconfigure(5, minsize=10)
inputFrame.rowconfigure(0, minsize=3)
inputFrame.rowconfigure(2, minsize=5)

inputFrame.grid(row=3, column=0, columnspan=5, rowspan=5, sticky="ew")


# Creating entry boxes for Length, Width and Height

entryL = Entry(inputFrame, width=8, borderwidth=2)
entryW = Entry(inputFrame, width=8, borderwidth=2)
entryH = Entry(inputFrame, width=8, borderwidth=2)

entryL.insert(0, 'L')
entryW.insert(0, 'W')
entryH.insert(0, 'H')

# Arranging the entry boxes on a grid

entryL.grid(row=1, column=0)
entryW.grid(row=1, column=2)
entryH.grid(row=1, column=4)

# Set aliases for entry boxes
setattr(entryL, "alias", "L")
setattr(entryW, "alias", "W")
setattr(entryH, "alias", "H")

inputLabel_IN1 = Label(inputFrame, text=' in', fg="red")
inputLabel_IN1.grid(row=1, column=1, sticky="w")

inputLabel_IN2 = Label(inputFrame, text=' in', fg="red")
inputLabel_IN2.grid(row=1, column=3, sticky="w")

inputLabel_IN3 = Label(inputFrame, text=' in', fg="red")
inputLabel_IN3.grid(row=1, column=5, sticky="w")


c_button = Button(inputFrame, text="C")
c_button.grid(row=3, column=0, sticky="ew")


shippingConstant_entry = Entry(inputFrame, width=8)
shippingConstant_entry.grid(row=3, column=3)

# set alias for shipping constant entry box
setattr(shippingConstant_entry, "alias", "Constant")

shippingConstant_label = Label(inputFrame, text="  shipping\n  constant", fg="blue", anchor=CENTER)
shippingConstant_label.grid(row=3, column=4, sticky="w")

inputFrame["padx"] = 3

buttonsFrame = Frame(mainWindow, borderwidth=2)

#   Configuring buttonsFrame rows and columns
for i in range(0, 3):
    columnNumber = int(i)
    buttonsFrame.columnconfigure(columnNumber, minsize=102)

for j in range(0, 4):
    rownumber = int(j)
    buttonsFrame.rowconfigure(rownumber, minsize=50)

buttonsFrame.grid(row=8, column=0, rowspan=4, columnspan=3, sticky="nsew")

numeric = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

warning_messages = [
    "Please select a box below",
    "Please input a number",
    "Entry '%s' contains an non-digit",
    "'%s' cannot be Zero",
]


#   Functions for clearing entry, based on events
#   Event type 9 = FocusIn, type 10 = FocusOut
def clear_entry_l(event):
    entry_text = entryL.get()
    if "L" in entry_text:
        if event.type == str(9):    # has focus
            entryL.delete(0, END)
            result_box.delete(0, END)
        pass
    elif len(entry_text) == 0:
        entryL.insert(0, "L")
    else:
        result_box.delete(0, END)


def clear_entry_w(event):
    entry_text = entryW.get()
    if "W" in entry_text:
        if event.type == str(9):    # has focus
            entryW.delete(0, END)
            result_box.delete(0, END)
        pass
    elif len(entry_text) == 0:
        entryW.insert(0, "W")
    else:
        result_box.delete(0, END)


def clear_entry_h(event):
    entry_text = entryH.get()
    if "H" in entry_text:
        if event.type == str(9):    # has focus
            entryH.delete(0, END)
            result_box.delete(0, END)
        pass
    elif len(entry_text) == 0:
        entryH.insert(0, "H")
    else:
        result_box.delete(0, END)


def clear_entry_no_event(entry_alias: str):
    names = {
        "L": entryL, "W": entryW, "H": entryH
    }
    widget = names[entry_alias]
    entry_text = widget.get()

    if widget.alias == entry_text:
        pass
    elif len(entry_text) == 0:
        widget.insert(0, widget.alias)
    else:
        widget.delete(0, END)
        widget.insert(0, widget.alias)


def clear_all_entry():
    clear_entry_no_event("L")
    clear_entry_no_event("W")
    clear_entry_no_event("H")
    result_box.delete(0, END)
    # Direct focus to a non focusable widget, makes all focusable widget lose focus
    mainWindow.focus()


def warning_message_f(event):
    result_box.insert(0, warning_messages[0])


def calculate_shipping():
    result_box.delete(0, END)
    length = (entryL.get())
    width = (entryW.get())
    height = (entryH.get())
    constant = (shippingConstant_entry.get())

    culprits = ("L", "W", "H")

    entry_list = [length, width, height, constant]
    error_messages = []

    # Check for valid input
    idx = 0
    for entry in entry_list:
        # Looking for L,W,H in entry boxes
        if idx > 2:     # Condition out constant first
            if entry == "":
                error_messages.append("Constant")
        else:
            if entry in culprits or entry == "":
                error_messages.append(culprits[idx])

        idx += 1

    if error_messages:
        formatted_messages = ", ".join(error_messages).rstrip(',')
        readable_error_message = f"Please enter {formatted_messages}"
        result_box.insert(0, readable_error_message)

        return

    # Check for non digits or zeros
    val_widget = {
        length: entryL, width: entryW, height: entryH, constant: shippingConstant_entry,
    }
    l_w_h_c_list = []
    for val, widget in val_widget.items():
        try:
            _val = float(val)
            if _val <= 0:
                result_box.insert(0, warning_messages[3] % widget.alias)
                return
            l_w_h_c_list.append(_val)
        except ValueError:
            result_box.insert(0, warning_messages[2] % widget.alias)
            return

    print(l_w_h_c_list)
    length, width, height, constant = l_w_h_c_list
    volumetric_weight = length * width * height // constant
    result_box.insert(0, str(volumetric_weight) + " Kg")


#   Function for inserting numbers
def button_click(number):
    result_box.delete(0, END)

    # Storing the names of the widget in focus
    entry_l_info = ".!frame2.!entry"
    entry_w_info = ".!frame2.!entry2"
    entry_h_info = ".!frame2.!entry3"
    shipping_constant_info = ".!frame2.!entry4"

    # focus_get() function helps us retrieve the id of widget in focus
    widget_focus = str(mainWindow.focus_get())
    # print(widget_focus)

    # Condition for placing numbers in the right widget
    if widget_focus == entry_l_info:
        current_l = entryL.get()
        entryL.delete(0, END)
        entryL.insert(0, str(current_l) + str(number))
    elif widget_focus == entry_w_info:
        current_w = entryW.get()
        entryW.delete(0, END)
        entryW.insert(0, str(current_w) + str(number))
    elif widget_focus == entry_h_info:
        current_h = entryH.get()
        entryH.delete(0, END)
        entryH.insert(0, str(current_h) + str(number))
    elif widget_focus == shipping_constant_info:
        current_shipping_constant = shippingConstant_entry.get()
        shippingConstant_entry.delete(0, END)
        shippingConstant_entry.insert(0, str(current_shipping_constant) + str(number))
    else:
        # warning_message = "Please select a box below"
        result_box.delete(0, END)
        result_box.insert(0, warning_messages[0])


#   The "C" button
def button_clear(event):
    # Storing the names of the widget in focus
    entry_l_info = ".!frame2.!entry"
    entry_w_info = ".!frame2.!entry2"
    entry_h_info = ".!frame2.!entry3"
    shipping_constant_info = ".!frame2.!entry4"

    widget_focus = str(mainWindow.focus_get())

    # Condition for clearing numbers in the right widget
    if widget_focus == entry_l_info:
        entryL.delete(len(entryL.get()) - 1)

    elif widget_focus == entry_w_info:
        entryW.delete(len(entryW.get()) - 1)

    elif widget_focus == entry_h_info:
        entryH.delete(len(entryH.get()) - 1)

    elif widget_focus == shipping_constant_info:
        shippingConstant_entry.delete(len(shippingConstant_entry.get()) - 1)

    else:
        result_box.delete(0, END)
        result_box.insert(0, warning_messages[0])


def run_calculator():
    mainWindow.mainloop()


# Creating and arranging the buttons on a grid

#   Row 1

num7 = Button(buttonsFrame, text='7', command=lambda: button_click(7))
num7.grid(row=0, column=0, sticky="nsew")

num8 = Button(buttonsFrame, text='8', command=lambda: button_click(8))
num8.grid(row=0, column=1, sticky="nsew")

num9 = Button(buttonsFrame, text='9', command=lambda: button_click(9))
num9.grid(row=0, column=2, sticky="nsew")

#   Row 2
num4 = Button(buttonsFrame, text='4', command=lambda: button_click(4))
num4.grid(row=1, column=0, sticky="nsew")

num5 = Button(buttonsFrame, text='5', command=lambda: button_click(5))
num5.grid(row=1, column=1, sticky="nsew")

num6 = Button(buttonsFrame, text='6', command=lambda: button_click(6))
num6.grid(row=1, column=2, sticky="nsew")

#   Row 3
num1 = Button(buttonsFrame, text='1', command=lambda: button_click(1))
num1.grid(row=2, column=0, sticky="nsew")

num2 = Button(buttonsFrame, text='2', command=lambda: button_click(2))
num2.grid(row=2, column=1, sticky="nsew")

num3 = Button(buttonsFrame, text='3', command=lambda: button_click(3))
num3.grid(row=2, column=2, sticky="nsew")

#   Row4
num0 = Button(buttonsFrame, text='0', command=lambda: button_click(0))
num0.grid(row=3, column=1, sticky="nsew")

clearButton = Button(buttonsFrame, text='Clear All', bg="red", command=clear_all_entry)
clearButton.grid(row=3, column=0, sticky="nsew")

calcShipping = Button(buttonsFrame, text='Calculate\nShipping', bg="green", command=calculate_shipping)
calcShipping.grid(row=3, column=2, sticky="nsew")


#   All event bindings
entryL.bind("<FocusIn>", clear_entry_l)
entryL.bind("<FocusOut>", clear_entry_l)


entryW.bind("<FocusIn>", clear_entry_w)
entryW.bind("<FocusOut>", clear_entry_w)

entryH.bind("<FocusIn>", clear_entry_h)
entryH.bind("<FocusOut>", clear_entry_h)

c_button.bind("<1>", button_clear)


if __name__ == "__main__":
    run_calculator()
