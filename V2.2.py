import tkinter as tk
import mysql.connector

with open("D:\Daten\Tim Hochstrasser\Desktop\RFT Food\Python\RFT Food\Python\Versions\config.txt", "r") as f:
    for line in f:
        parts = line.strip().split('=')
        if len(parts) == 2:
            key, value = parts
            if key == 'hotdog_upper':
                hotdog_upper = value
            elif key == 'hotdog_lower':
                hotdog_lower = value
            elif key == 'fries_upper':
                fries_upper = value
            elif key == 'fries_lower':
                fries_lower = value
            elif key == 'username':
                username = value
            elif key == 'passwd':
                passwd = value
            elif key == 'hostname':
                hostname = value
            elif key == 'database':
                db_name = value

conn = mysql.connector.connect(
   user=username, password=passwd, host=hostname, database=db_name)


def update_label_hotdog():
    label_hotdog_amount.config(text=f"{hotdogAmount}")
def update_label_fries():
    label_fries_amount.config(text=f"{friesAmount}")

def add_hotdog():
    global hotdogAmount
    if(hotdogAmount < hotdog_upper) :
        hotdogAmount += 1
    update_label_hotdog()

def remove_hotdog():
    global hotdogAmount
    if(hotdogAmount > hotdog_lower) :
        hotdogAmount -= 1
    update_label_hotdog()

def add_fries():
    global friesAmount
    if(friesAmount < fries_upper) :
        friesAmount += 1
    update_label_fries()

def remove_fries():
    global friesAmount
    if(friesAmount > fries_lower) :
        friesAmount -= 1
    update_label_fries()

def order_not_correct():
    order_correct_boalean = order_correct.get()
    if(order_correct_boalean == False) :
        order_correct_status = "Bitte bestätigen Sie, dass alle Felder richtig ausgefüllt sind."
    label_order_correct.config(text=f"{order_correct_status}")
    order_correct_status = ""

def submit():
    order_correct_boalean = order_correct.get()
    label_order_correct.config(text="")
    if(order_correct_boalean == True) :
        cursor = conn.cursor()
        # Preparing SQL query to INSERT a record into the database.
        insert_stmt = (
            "INSERT INTO orders(name, phone, hotdog, hotdog_ketchup, hotdog_mayo, hotdog_mustard, hotdog_onions, hotdog_pickles, fries, fries_sauce, data_consent)"
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        )
        data = (name.get(), phone.get(), hotdogAmount, checkbox_hotdog_ketchup.get(), checkbox_hotdog_mayo.get(), checkbox_hotdog_mustard.get(), checkbox_hotdog_onion.get(), checkbox_hotdog_pickles.get(), friesAmount, fries_sauce.get(), data_consent.get())
        try:
            #executing the sql command
            cursor.execute(insert_stmt,data)
            #commit changes in database
            conn.commit()
        except Exception as e:
            conn.rollback()
            print(e)
    else :
        order_not_correct()


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

name = tk.StringVar()
name.set("")
phone = tk.StringVar()
phone.set("")
entry_name = tk.Entry(root, textvariable=name)
entry_name.place(x=550, y=225)
entry_phone = tk.Entry(root, textvariable=phone)
entry_phone.place(x=550, y=250)
label_name=tk.Label(root, text="Name")
label_name.place(x=450, y=225)
label_phone=tk.Label(root, text="Telefonnummer")
label_phone.place(x=450, y=250)

label_hotdog_ketchup = tk.Label(root, text="Ketchup")
label_hotdog_ketchup.place(x=50, y=125)
checkbox_hotdog_ketchup = tk.BooleanVar()
checkbox_hotdog_ketchup.set(False)
checkbutton_hotdog_ketchup = tk.Checkbutton(root, variable=checkbox_hotdog_ketchup)
checkbutton_hotdog_ketchup.place(x=150, y=125)

label_hotdog_mayo = tk.Label(root, text="Majo")
label_hotdog_mayo.place(x=50, y=150)
checkbox_hotdog_mayo = tk.BooleanVar()
checkbox_hotdog_mayo.set(False)
checkbutton_hotdog_mayo = tk.Checkbutton(root, variable=checkbox_hotdog_mayo)
checkbutton_hotdog_mayo.place(x=150, y=150)

label_hotdog_mustard = tk.Label(root, text="Senf")
label_hotdog_mustard.place(x=50, y=175)
checkbox_hotdog_mustard = tk.BooleanVar()
checkbox_hotdog_mustard.set(False)
checkbutton_hotdog_mustard = tk.Checkbutton(root, variable=checkbox_hotdog_mustard)
checkbutton_hotdog_mustard.place(x=150, y=175)

label_hotdog_onion = tk.Label(root, text="Zwiebeln")
label_hotdog_onion.place(x=50, y=200)
checkbox_hotdog_onion = tk.BooleanVar()
checkbox_hotdog_onion.set(False)
checkbutton_hotdog_onion = tk.Checkbutton(root, variable=checkbox_hotdog_onion)
checkbutton_hotdog_onion.place(x=150, y=200)

label_hotdog_pickles = tk.Label(root, text="Gurken")
label_hotdog_pickles.place(x=50, y=225)
checkbox_hotdog_pickles = tk.BooleanVar()
checkbox_hotdog_pickles.set(False)
checkbutton_hotdog_pickles = tk.Checkbutton(root, variable=checkbox_hotdog_pickles)
checkbutton_hotdog_pickles.place(x=150, y=225)

label_hotdog_placeholder1 = tk.Label(root, text="PLACEHOLDER")
label_hotdog_placeholder1.place(x=50, y=250)
checkbox_hotdog_PLACEHOLDER = tk.BooleanVar()
checkbox_hotdog_PLACEHOLDER.set(False)
checkbutton_hotdog_PLACEHOLDER = tk.Checkbutton(root, variable=checkbox_hotdog_PLACEHOLDER)
checkbutton_hotdog_PLACEHOLDER.place(x=150, y=250)

fries_sauce = tk.StringVar()
fries_sauce.set("")
entry_fries_sauce = tk.Entry(root, textvariable=fries_sauce)
entry_fries_sauce.place(x=550, y=125)
label_fries_sauce = tk.Label(root, text="Sauce")
label_fries_sauce.place(x=450, y=125)

data_consent = tk.BooleanVar()
data_consent.set(False)
checkbutton_data_consent = tk.Checkbutton(root, text="Ich stimme zu, dass meine Daten verwendet werden, um mich zu kontaktieren.", variable=data_consent)
checkbutton_data_consent.place(x=50, y=300)

order_correct = tk.BooleanVar()
#order_correct.set(False)
checkbutton_order_correct = tk.Checkbutton(root, text="Ich bestätige, dass alle Angaben korrekt sind. Ich erkläre mich damit einverstanden, dass diese Bestellung verbindlich ist.", variable=order_correct)
checkbutton_order_correct.place(x=50, y=325)

label_order_correct = tk.Label(root, text="")
label_order_correct.place(x=50,y=400)

button_submit = tk.Button(root, bg="orange", text="Submit", command=submit)
button_submit.place(x=550, y=300)

root.mainloop()