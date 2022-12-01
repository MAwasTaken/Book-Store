# ======================================================== FrontEnd ====================================================
#tKinter
from tkinter import *

#BackEnd
import BackEnd

# ======================================================== OOPs ========================================================
#clear list texts
def clear_list():
    list1.delete(0, END)

#show books in list
def fill_list(books):
    for book in books:
        list1.insert(END, book)

# ===================================================== tKinter Configs ================================================
#tKinter Prototyping
window = Tk()

#tkinter Title
window.title("Book Store")

# ======================================================== Labels ======================================================
#Title Text
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

#Authour Text
l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

#Year Text
l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

# ISBN Text
l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# ======================================================= Entries ======================================================
#Title Entries
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

#Author Entries
author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

#Year Entries
year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

#ISBN Entries
isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

#List
list1 = Listbox(window, width=35, height=6)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

#Scroll Bar
sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

#Scroll connection
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#Select Detector
def get_selected_row(event):
    global selected_book

    index = list1.curselection()[0]
    selected_book = list1.get(index)

    # Select into Labels
    if len(list1.curselection()) > 0:
        e1.delete(0, END)
        e1.insert(END, selected_book[1])
        e2.delete(0, END)
        e2.insert(END, selected_book[1])
        e3.delete(0, END)
        e3.insert(END, selected_book[2])
        e4.delete(0, END)
        e4.insert(END, selected_book[3])

#Event Listener
list1.bind("<<ListboxSelect>>", get_selected_row)

# ======================================================= Buttons ======================================================
#View Function
def view_Command():
    clear_list()
    books = BackEnd.view()
    fill_list(books)

#View Button
b1 = Button(window, text="View All", width=12, command=lambda: view_Command())
b1.grid(row=2, column=3)

# Search Function
def Search_Command():
    clear_list()
    books = BackEnd.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    fill_list(books)

#Search Button
b2 = Button(window, text="Search Entry", width=12, command= lambda: Search_Command())
b2.grid(row=3, column=3)

#Add Function
def Add_Command():
    BackEnd.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_Command()

#Add Button
b3 = Button(window, text="Add Entry", width=12, command= lambda: Add_Command())
b3.grid(row=4, column=3)

# Update Function
def Update_Command():
    BackEnd.update(selected_book[0] ,title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_Command()

#Update Button
b4 = Button(window, text="Update Selected", width=12, command= lambda: Update_Command())
b4.grid(row=5, column=3)

#Delete Function
def Delete_Command():
    BackEnd.delete(selected_book[0])
    view_Command()

#Delete Button
b5 = Button(window, text="Delete Selected", width=12, command=lambda: Delete_Command())
b5.grid(row=6, column=3)

#Close Button
b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

#Result show in list
view_Command()

# ============================================= tKinter Main Loop ======================================================
#tKinter Runner
window.mainloop()