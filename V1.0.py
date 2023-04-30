import tkinter as tk

def update_label_hotdog():
    print("Hotdogs: " + str(hotdogAmount))
def update_label_fries():
    print("Pommes: " + str(friesAmount) )

def add_hotdog():
    global hotdogAmount
    if(hotdogAmount < 4) :
        hotdogAmount += 1
    update_label_hotdog()

def remove_hotdog():
    global hotdogAmount
    if(hotdogAmount > 0) :
        hotdogAmount -= 1
    update_label_hotdog()

def add_fries():
    global friesAmount
    if(friesAmount < 4) :
        friesAmount += 1
    update_label_fries()

def remove_fries():
    global friesAmount
    if(friesAmount > 0) :
        friesAmount -= 1
    update_label_fries()

root = tk.Tk()
root.title("Order")
root.geometry("800x480")
friesAmount = 0
hotdogAmount = 0
label_hotdog = tk.Label(root, text="Hotdogs:")
label_hotdog.place(x=50,y=60)
label_fries = tk.Label(root, text="Pommes:")
label_fries.place(x=450,y=60)
button_add_hotdog = tk.Button(root, text="+", width=4, height=2, command=add_hotdog).place(x=150,y=50)
button_remove_hotdog = tk.Button(root, text="-", width=4, height=2, command=remove_hotdog).place(x=250,y=50)
button_add_fries = tk.Button(root, text="+", width=4, height=2, command=add_fries).place(x=550,y=50)
button_remove_fries = tk.Button(root, text="-", width=4, height=2, command=remove_fries).place(x=650,y=50)


root.mainloop()
