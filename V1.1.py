import tkinter as tk

def update_label_hotdog():
    label_hotdog_amount.config(text=f"{hotdogAmount}")
def update_label_fries():
    label_fries_amount.config(text=f"{friesAmount}")

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
label_hotdog_amount = tk.Label(root, text="0")
label_hotdog_amount.place(x=212.5,y=60)
label_fries_amount = tk.Label(root, text="0")
label_fries_amount.place(x=612.5,y=60)
button_add_hotdog = tk.Button(root, text="+", width=4, height=2, command=add_hotdog).place(x=150,y=50)
button_remove_hotdog = tk.Button(root, text="-", width=4, height=2, command=remove_hotdog).place(x=250,y=50)
button_add_fries = tk.Button(root, text="+", width=4, height=2, command=add_fries).place(x=550,y=50)
button_remove_fries = tk.Button(root, text="-", width=4, height=2, command=remove_fries).place(x=650,y=50)


label_hotdog_ketchup = tk.Label(root, text="Ketchup")
label_hotdog_ketchup.place(x=50, y=125)
label_hotdog_mayo = tk.Label(root, text="Majo")
label_hotdog_mayo.place(x=50, y=150)
label_hotdog_mustard = tk.Label(root, text="Senf")
label_hotdog_mustard.place(x=50, y=175)
label_hotdog_ketchup = tk.Label(root, text="Zwiebeln")
label_hotdog_ketchup.place(x=50, y=200)
label_hotdog_mayo = tk.Label(root, text="Gurken")
label_hotdog_mayo.place(x=50, y=225)
label_hotdog_mustard = tk.Label(root, text="PLACEHOLDER")
label_hotdog_mustard.place(x=50, y=250)

hotdog_ketchup=tk.IntVar()
hotdog_mayo=tk.IntVar()
hotdog_mustard=tk.IntVar()
hotdog_onion=tk.IntVar()
hotdog_pickles=tk.IntVar()
hotdog_placeholder=tk.IntVar()


checkbox_hotdog_ketchup = tk.Checkbutton(root, onvalue=1, offvalue=0, variable=hotdog_ketchup)
checkbox_hotdog_ketchup.place(x=150, y=125)
checkbox_hotdog_mayo = tk.Checkbutton(root, onvalue=1, offvalue=0)
checkbox_hotdog_mayo.place(x=150, y=150)
checkbox_hotdog_mustard = tk.Checkbutton(root, onvalue=1, offvalue=0)
checkbox_hotdog_mustard.place(x=150, y=175)
checkbox_hotdog_onion = tk.Checkbutton(root, onvalue=1, offvalue=0)
checkbox_hotdog_onion.place(x=150, y=200)
checkbox_hotdog_pickles = tk.Checkbutton(root, onvalue=1, offvalue=0)
checkbox_hotdog_pickles.place(x=150, y=225)
checkbox_hotdog_PLACEHOLDER = tk.Checkbutton(root, onvalue=1, offvalue=0)
checkbox_hotdog_PLACEHOLDER.place(x=150, y=250)


label_fries_ketchup = tk.Label(root, text="Ketchup")
label_fries_ketchup.place(x=450, y=125)
label_fries_mayo = tk.Label(root, text="Majo")
label_fries_mayo.place(x=450, y=150)
label_fries_mustard = tk.Label(root, text="Senf")
label_fries_mustard.place(x=450, y=175)
label_fries_mustard = tk.Label(root, text="Keine")
label_fries_mustard.place(x=450, y=200)

fries_sauce = tk.StringVar()
fries_sauce.set("Keine")

fries_sauce_data=fries_sauce.get()

radiobutton_fries_sauce_ketchup = tk.Radiobutton(root, text="", variable=fries_sauce, value="Ketchup")
radiobutton_fries_sauce_ketchup.place(x=550, y=125)
radiobutton_fries_sauce_mayo = tk.Radiobutton(root, text="", variable=fries_sauce, value="Majo")
radiobutton_fries_sauce_mayo.place(x=550, y=150)
radiobutton_fries_sauce_mustard = tk.Radiobutton(root, text="", variable=fries_sauce, value="Senf")
radiobutton_fries_sauce_mustard.place(x=550, y=175)
radiobutton_fries_sauce_none = tk.Radiobutton(root, text="", variable=fries_sauce, value="Keine")
radiobutton_fries_sauce_none.place(x=550, y=200)



root.mainloop()
