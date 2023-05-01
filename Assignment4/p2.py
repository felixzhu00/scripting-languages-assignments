#!/usr/bin/python3
# gui-database.py

from tkinter import *

from tkinter import messagebox

# Main window definition
root = Tk()
root.geometry("1280x720")
root.title("Contact List")
root.configure(bg = "cyan")

# Constants
FIRST_NAME = 0
LAST_NAME = 1
STREET = 2
TOWN = 3
STATE = 4
ZIP = 5
PHONE = 6
EMAIL = 7

# Global variables
current_view = 1
contact_fields = dict()
contact_list = [{'fn' : 'Liara', 'ln' : 'T\'soni', 'str' : '113 Prothean Way',
                  'twn' : 'Sparta Base', 'st' : 'Mars', 'zip' : '11223',
                  'phn' : '555-229-0447', 'eml' : 'liara@mail.edu'},
                {'fn' : 'John', 'ln' : 'Shepard', 'str' : '91 Main Street', 'twn' : 'Los Angeles',
                 'st' : 'CA', 'zip' : '26774', 'phn' : '555-977-2231', 'eml' : 'js@mail.edu'},
                {'fn' : 'Jane', 'ln' : 'Shepard', 'str' : '111 Station Concourse', 'twn' : 'Terminus',
                 'st' : 'L3 Langrangian', 'zip' : '11008', 'phn' : '555-224-2442', 'eml' : 'bestshepard@mail.edu'},
                {'fn' : 'Garrus', 'ln' : 'Vakarian', 'str' : '10 Turian Blvd.', 'twn' : 'Sector 7',
                 'st' : 'The Citadel', 'zip' : '77663', 'phn' : '555-854-3321', 'eml' : 'csecrocks@mail.edu'},
                {'fn' : 'Urdnot', 'ln' : 'Wrex', 'str' : '21 Ruins Ave.', 'twn' : 'The Ruins',
                 'st' : 'Tuchanka', 'zip' : '46654', 'phn' : '555-993-6442', 'eml' : 'wrexisbest@mail.edu'}]
search_txt = StringVar()
search_txt.set("First Name")
search_value = FIRST_NAME
my_font = ("Times", 22)

list_index = []


# Callback functions
def save_contact():
    global contact_list
    contact_dict = dict()
    for field in contact_fields:
        contact_dict[field] = contact_fields[field].get()
    contact_list.append(contact_dict)
    for field in contact_fields:
        contact_fields[field].set("")
# end save_contact()

def clear_contact():
    for field in contact_fields:
        contact_fields[field].set("")
# end clear_contact()

def find_contact():
    if current_view == 3:
        query = d_search_str.get()
    else:
        query = search_str.get()
    results = []
    if search_value == FIRST_NAME:
        for c in enumerate(contact_list):
            s = c[1]
            if s['fn'] == query:
                results.append(c)
    elif search_value == LAST_NAME:
        for c in enumerate(contact_list):
            s = c[1]
            if s['ln'] == query:
                results.append(c)
    elif search_value == PHONE:
        for c in enumerate(contact_list):
            s = c[1]
            if s['phn'] == query:
                results.append(c)
    elif search_value == EMAIL:
        for c in enumerate(contact_list):
            s = c[1]
            if s['eml'] == query:
                results.append(c)

    if current_view == 3:
        global list_index
        list_index = []
        d_result_lb.delete(0, END)
        for c in results:
            list_index.append(c[0])
            d_result_lb.insert(END, space_stringify_contact(c[1])) 
    else:
        result_field.delete(1.0, END)
        for c in results:
            result_field.insert(END, stringify_contact(c[1])) 
# end find_contact()

def delete_list():
    selected = d_result_lb.curselection()
    first = contact_list[list_index[selected[0]]]['fn']
    last = contact_list[list_index[selected[0]]]['ln']

    contact_list.pop(list_index[selected[0]])
    messagebox.showinfo("Contact Deleted", "%s %s has been removed from the contact list." %(first , last))

    print()
    pass    
#end delete_list()

def stringify_contact(c):
    s = ""
    s += "Name: " + c['fn'] + " " + c['ln'] + "\n"
    s += "Phone: " + c['phn'] + "\n"
    s += "Email: " + c['eml'] + "\n\n"
    return s
# end stringify_contact()

def space_stringify_contact(c):
    s = ""
    s += "Name: " + c['fn'] + " " + c['ln'] + " "
    s += "Phone: " + c['phn'] + " "
    s += "Email: " + c['eml']
    return s
# end space_stringify_contact()


def clear_search():
    search_str.set("")
    d_search_str.set("")

# end clear_contact()

def search_by_fn():
#   print("Search by FN")
    global search_value
    search_txt.set("First Name")
    search_value = FIRST_NAME
# end search_by_fn()

def search_by_ln():
    print("Search by LN")
    global search_value
    search_txt.set("Last Name")
    search_value = LAST_NAME
# end search_by_ln()

def search_by_phn():
    print("Search by PHN")
    global search_value
    search_txt.set("Phone Number")
    search_value = PHONE
# end search_by_phn()

def search_by_eml():
    print("Search by EML")
    global search_value
    search_txt.set("Email")
    search_value = EMAIL
# end search_by_eml()

def change_view():
    global current_view
    if radio_var.get() == current_view:
        print(radio_var.get(), current_view)
    elif radio_var.get() == 1:
        find_container_frame.pack_forget()
        d_container_frame.forget()
        current_view = 1
        build_add_view()
    elif radio_var.get() == 2:
        container_frame.pack_forget()
        d_container_frame.forget()
        current_view = 2
        build_find_view()
    elif radio_var.get() == 3:
        container_frame.pack_forget()
        find_container_frame.pack_forget()
        current_view = 3
        build_delete_view()
# end change_view()

# Widget Definitions
topspace_frame = Frame(root, height = 100, bg = "cyan")
midspace_frame = Frame(root, height = 40, bg = "cyan")

radio_frame = Frame(root, bg = "cyan")
radio_var = IntVar()
radio_lbl = Label(radio_frame, font = my_font, width = 16, anchor = W, text = "Select View:", bg = "cyan")
radio_add = Radiobutton(radio_frame, text = "Add contact", variable = radio_var,
                          value = 1, command = change_view, font = my_font, bg = "cyan")
radio_add.select()
radiomid = Frame(radio_frame, width = 32, bg = "cyan")
radio_find = Radiobutton(radio_frame, text = "Find contact", variable = radio_var,
                         value = 2, command = change_view, font = my_font, bg = "cyan")
radiomid2 = Frame(radio_frame, width = 32, bg = "cyan")
radio_remove = Radiobutton(radio_frame, text = "Remove contact", variable = radio_var,
                           value = 3, command = change_view, font = my_font, bg = "cyan")

# Add Contact Widgets
# These are the widgets that make up the add contact view
container_frame = Frame(root, bg = "cyan")

fname_frame = Frame(container_frame, bg = "cyan")
fname_lbl = Label(fname_frame, font = my_font, width = 16, anchor = W, text = "First Name:", bg = "cyan")
fname_str = StringVar()
contact_fields["fn"] = fname_str
fname_field = Entry(fname_frame, font = my_font, width = 32, textvariable = fname_str)

lname_frame = Frame(container_frame, bg = "cyan")
lname_lbl = Label(lname_frame, font = my_font, width = 16, anchor = W, text = "Last Name:", bg = "cyan")
lname_str = StringVar()
contact_fields["ln"] = lname_str
lname_field = Entry(lname_frame, font = my_font, width = 32, textvariable = lname_str)

street_frame = Frame(container_frame, bg = "cyan")
street_lbl = Label(street_frame, font = my_font, width = 16, anchor = W, text = "Street Address:", bg = "cyan")
street_str = StringVar()
contact_fields["str"] = street_str
street_field = Entry(street_frame, font = my_font, width = 32, textvariable = street_str)

town_frame = Frame(container_frame, bg = "cyan")
town_lbl = Label(town_frame, font = my_font, width = 16, anchor = W, text = "Town:", bg = "cyan")
town_str = StringVar()
contact_fields["twn"] = town_str
town_field = Entry(town_frame, font = my_font, width = 32, textvariable = town_str)

state_frame = Frame(container_frame, bg = "cyan")
state_lbl = Label(state_frame, font = my_font, width = 16, anchor = W, text = "State:", bg = "cyan")
state_str = StringVar()
contact_fields["st"] = state_str
state_field = Entry(state_frame, font = my_font, width = 32, textvariable = state_str)

zip_frame = Frame(container_frame, bg = "cyan")
zip_lbl = Label(zip_frame, font = my_font, width = 16, anchor = W, text = "Zip Code:", bg = "cyan")
zip_str = StringVar()
contact_fields["zip"] = zip_str
zip_field = Entry(zip_frame, font = my_font, width = 32, textvariable = zip_str)

phone_frame = Frame(container_frame, bg = "cyan")
phone_lbl = Label(phone_frame, font = my_font, width = 16, anchor = W, text = "Phone:", bg = "cyan")
phone_str = StringVar()
contact_fields["phn"] = phone_str
phone_field = Entry(phone_frame, font = my_font, width = 32, textvariable = phone_str)

email_frame = Frame(container_frame, bg = "cyan")
email_lbl = Label(email_frame, font = my_font, width = 16, anchor = W, text = "Email:", bg = "cyan")
email_str = StringVar()
contact_fields["eml"] = email_str
email_field = Entry(email_frame, font = my_font, width = 32, textvariable = email_str)

save_frame = Frame(container_frame, bg = "cyan")
save_btn = Button(save_frame, font = my_font, text = "SAVE", bg = "green", command = save_contact)
clear_btn = Button(save_frame, font = my_font, text = "CLEAR", bg = "red", command = clear_contact)

# Find Contact Widgets
# These are the widgets that make up the find contact view
find_container_frame = Frame(root, bg = "cyan")

search_frame = Frame(find_container_frame, bg = "cyan")
search_lbl = Label(search_frame, font = my_font, width = 8, anchor = W, text = "Search by:", bg = "cyan")

search_menu = Menubutton(search_frame, font = my_font, textvariable = search_txt, width = 12, bg = "cyan")
search_options = Menu(search_menu)
search_options.add_command(label = "First Name", command = search_by_fn)
search_options.add_command(label = "Last Name", command = search_by_ln)
search_options.add_command(label = "Phone", command = search_by_phn)
search_options.add_command(label = "Email", command = search_by_eml)
search_menu.configure(menu = search_options)

search_str = StringVar()
search_field = Entry(search_frame, font = my_font, width = 32, textvariable = search_str)

search_btn = Button(search_frame, font = my_font, text = "FIND", bg = "green", command = find_contact)
clear_search_btn = Button(search_frame, font = my_font, text = "CLEAR", bg = "red", command = clear_search)

result_frame = Frame(find_container_frame, bg = "cyan")
result_lbl = Label(result_frame, font = my_font, width = 16, anchor = W, text = "Results:", bg = "cyan")
result_field = Text(result_frame, width = 80, height = 25)

#Delete Contact Widgets
d_container_frame = Frame(root, bg = "cyan")

d_search_frame = Frame(d_container_frame, bg = "cyan")
d_search_lbl = Label(d_search_frame, font = my_font, width = 8, anchor = W, text = "Search by:", bg = "cyan")

d_search_menu = Menubutton(d_search_frame, font = my_font, textvariable = search_txt, width = 12, bg = "cyan")
d_search_options = Menu(d_search_menu)
d_search_options.add_command(label = "First Name", command = search_by_fn)
d_search_options.add_command(label = "Last Name", command = search_by_ln)
d_search_options.add_command(label = "Phone", command = search_by_phn)
d_search_options.add_command(label = "Email", command = search_by_eml)
d_search_menu.configure(menu = d_search_options)

d_search_str = StringVar()
d_search_field = Entry(d_search_frame, font = my_font, width = 32, textvariable = d_search_str)

d_search_btn = Button(d_search_frame, font = my_font, text = "FIND", bg = "green", command = find_contact)
d_clear_search_btn = Button(d_search_frame, font = my_font, text = "CLEAR", bg = "red", command = clear_search)

d_bigger_result_frame = Frame(d_container_frame, bg = "cyan")
d_result_frame = Frame(d_bigger_result_frame, bg = "cyan")
d_font = ("Times", 15)
d_result_lbl = Label(d_result_frame, font = my_font, width = 16, anchor = W, text = "Results:",bg = "cyan")
d_result_lb = Listbox(d_result_frame, width = 80, height = 17, font=d_font)

del_btn = Button(d_bigger_result_frame , font = my_font, text = "DELETE", bg = "gray", command = delete_list)


# Geometry Management
# Here we describe the layout of the GUI widgets
topspace_frame.pack()

radio_frame.pack()
radio_lbl.pack(side = LEFT)
radio_add.pack(side = LEFT)
radiomid.pack(side = LEFT)
radio_find.pack(side = LEFT)
radiomid2.pack(side = LEFT)
radio_remove.pack(side = LEFT)

midspace_frame.pack()

def build_add_view():
    container_frame.pack()

    fname_frame.pack()
    fname_lbl.pack(side = LEFT)
    fname_field.pack(side = LEFT)
    
    lname_frame.pack()
    lname_lbl.pack(side = LEFT)
    lname_field.pack(side = LEFT)
    
    street_frame.pack()
    street_lbl.pack(side = LEFT)
    street_field.pack(side = LEFT)
    
    town_frame.pack()
    town_lbl.pack(side = LEFT)
    town_field.pack(side = LEFT)
    
    state_frame.pack()
    state_lbl.pack(side = LEFT)
    state_field.pack(side = LEFT)
    
    zip_frame.pack()
    zip_lbl.pack(side = LEFT)
    zip_field.pack(side = LEFT)
    
    phone_frame.pack()
    phone_lbl.pack(side = LEFT)
    phone_field.pack(side = LEFT)

    email_frame.pack()
    email_lbl.pack(side = LEFT)
    email_field.pack(side = LEFT)
    
    save_frame.pack()
    save_btn.pack(side = LEFT)
    clear_btn.pack(side = LEFT)
# end build_add_view()

def build_find_view():
    find_container_frame.pack()

    search_frame.pack()
    search_lbl.pack(side = LEFT)
    search_menu.pack(side = LEFT)
    search_field.pack(side = LEFT)
    search_btn.pack(side = LEFT)
    clear_search_btn.pack(side = LEFT)

    result_frame.pack()
    result_lbl.pack(side = LEFT)
    result_field.pack(side = LEFT)
# end build_find_view()

def build_delete_view():
    d_container_frame.pack()

    d_search_frame.pack()
    d_search_lbl.pack(side = LEFT)
    d_search_menu.pack(side = LEFT)
    d_search_field.pack(side = LEFT)
    d_search_btn.pack(side = LEFT)
    d_clear_search_btn.pack(side = LEFT)

    d_result_frame.pack()
    d_result_lbl.pack(side = LEFT)
    d_result_lb.pack(side = LEFT)
    del_btn.pack()
    d_bigger_result_frame.pack()
    # d_result_field.pack(side = LEFT)

    # lb.pack()



build_add_view()

root.mainloop()
