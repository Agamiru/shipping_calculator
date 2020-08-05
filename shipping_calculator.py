from tkinter import *

# Loading the main window

mainWindow = Tk()
mainWindow.title("Shipping Calculator")
mainWindow.geometry("330x350+900+150")
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

inputLabel_IN1 = Label(inputFrame, text=" In", fg="red")
inputLabel_IN1.grid(row=1, column=1, sticky="w")

inputLabel_IN2 = Label(inputFrame, text=" In", fg="red")
inputLabel_IN2.grid(row=1, column=3, sticky="w")

inputLabel_IN3 = Label(inputFrame, text=" In", fg="red")
inputLabel_IN3.grid(row=1, column=5, sticky="w")

# radio_lbs = Radiobutton(inputFrame, text="lbs")
# radio_lbs.grid(row=1, column=0, sticky="w")
c_button = Button(inputFrame, text="C")
c_button.grid(row=3, column=0, sticky="ew")

radio_cm = Radiobutton(inputFrame, text="cm")
radio_cm.grid(row=3, column=2, sticky="w")

shippingConstant_entry = Entry(inputFrame, width=8)
shippingConstant_entry.grid(row=3, column=3)

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

warning_message = ["Please select a box below",
                   "Please input a number"]

#   Functions for clearing entry


def clear_entry_l(event):
    entry_text = entryL.get()
    if "L" in entry_text:
        entryL.delete(0, END)
    elif len(entry_text) == 0:
        entryL.insert(0, "L")
    elif ratchet == 0:
        entryL.delete(0, END)
    else:
        result_box.delete(0, END)


def clear_entry_w(event):
    entry_text = entryW.get()
    if "W" in entry_text:
        entryW.delete(0, END)
    elif len(entry_text) == 0:
        entryW.insert(0, "W")
    elif ratchet == 0:
        entryW.delete(0, END)
    else:
        result_box.delete(0, END)


def clear_entry_h(event):
    entry_text = entryH.get()
    if "H" in entry_text:
        entryH.delete(0, END)
    elif len(entry_text) == 0:
        entryH.insert(0, "H")
    elif ratchet == 0:
        entryH.delete(0, END)
    else:
        result_box.delete(0, END)


def clear_all_entry():
    global ratchet
    ratchet = 0
    global clank
    clank = ratchet
    entryL.focus_set()
    entryW.focus_set()
    entryH.focus_set()
    shippingConstant_entry.focus_set()
    ratchet += 1


def shipping_k_clear_result(event):
    result_box.delete(0, END)


def warning_message_f(event):
    result_box.insert(0, warning_message[0])


def calculate_shipping():
    length = (entryL.get())
    width = (entryW.get())
    height = (entryH.get())
    constant = (shippingConstant_entry.get())

    culprits = {
        "L": "L",
        "W": "W",
        "H": "H",
        "": "Constant"
    }

    entry_list = [length, width, height, constant]
    error_messages = []

    # Check for valid input
    for entry in entry_list:
        # Looking for L,W,H in entry boxes
        if entry in culprits.keys():
            error_messages.append(culprits[entry])
            # Test to see the new error message
            print(error_messages)

    if error_messages:
        result_box.delete(0, END)
        formatted_messages = ", ".join(error_messages).rstrip(',')
        readable_error_message = f"Please enter {formatted_messages}"
        result_box.insert(0, readable_error_message)

        return

    result_box.delete(0, END)
    volumetric_weight = (int(length) * int(width) * int(height)) // int(constant)
    result_box.insert(0, str(volumetric_weight) + " Kg")

#   Function for inserting numbers


def button_click(number):
    # Storing the names of the widget in focus
    entry_l_info = ".!frame2.!entry"
    entry_w_info = ".!frame2.!entry2"
    entry_h_info = ".!frame2.!entry3"
    shipping_constant_info = ".!frame2.!entry4"

    # focus_get() function helps us retrieve the id of widget in focus
    widget_focus = str(mainWindow.focus_get())
    print(widget_focus)

    # Condition for placing numbers in the right widget
    if widget_focus == entry_l_info:
        # print("in first widget")
        current_l = entryL.get()
        entryL.delete(0, END)
        entryL.insert(0, str(current_l) + str(number))
    elif widget_focus == entry_w_info:
        # print("in second widget")
        current_w = entryW.get()
        entryW.delete(0, END)
        entryW.insert(0, str(current_w) + str(number))
    elif widget_focus == entry_h_info:
        # print("in third widget")
        current_h = entryH.get()
        entryH.delete(0, END)
        entryH.insert(0, str(current_h) + str(number))
    elif widget_focus == shipping_constant_info:
        # print("in fourth widget")
        current_shipping_constant = shippingConstant_entry.get()
        shippingConstant_entry.delete(0, END)
        shippingConstant_entry.insert(0, str(current_shipping_constant) + str(number))
    else:
        # warning_message = "Please select a box below"
        result_box.delete(0, END)
        result_box.insert(0, warning_message[0])


def button_clear(event):
    # Storing the names of the widget in focus
    entry_l_info = ".!frame2.!entry"
    entry_w_info = ".!frame2.!entry2"
    entry_h_info = ".!frame2.!entry3"
    shipping_constant_info = ".!frame2.!entry4"

    widget_focus = str(mainWindow.focus_get())
    # print(widget_focus)

    # Condition for clearing numbers in the right widget
    if widget_focus == entry_l_info:
        # print("in first widget")
        # entryL.get()
        entryL.delete(len(entryL.get()) - 1)

    elif widget_focus == entry_w_info:
        # print("in second widget")
        entryW.delete(len(entryW.get()) - 1)

    elif widget_focus == entry_h_info:
        # print("in third widget")

        entryH.delete(len(entryH.get()) - 1)

    elif widget_focus == shipping_constant_info:
        # print("in fourth widget")
        shippingConstant_entry.delete(len(shippingConstant_entry.get()) - 1)

    else:
        result_box.delete(0, END)
        result_box.insert(0, warning_message[0])


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

# mainWindow.bind("<FocusIn>", print_hi)    # Check to see if its the mainWindow that gets focus on start up

# shippingConstant_entry.bind("<FocusIn>", shipping_k_clear_result)

# clearButton.bind("<1>", clear_all_entry)       # This is supposed to set focus to result box
c_button.bind("<1>", button_clear)
result_box.bind("<FocusIn>", warning_message_f)
gi

if __name__ == "__main__":
    run_calculator()
