#Structure of the Program

#1. Import the necessary library.
#2. Create a main window with a specific theme.
#3. set the title of the window.
#4. define a function to retrieve and display a selected date.  
#5. creayte a DataEntry widget for selecting date and display it in the label widget.
#6. Create a button widget and a label widget to display the selected date.
#7. Start the GUI event loop (root.mainloop())

from tkinter import ttk
import ttkbootstrap
from ttkbootstrap.constants import *
from datetime import date

#setup the window
root = ttkbootstrap.Window(themename='cyborg')
root.title("Calendar")
root.geometry("400x300")
root.resizable(False, False)

#function to get the date
def see_date():
    selected_date = cal.entry.get()
    date_label.config(text=f"Selected Date: {selected_date}")
    status_label.config(text="Date retrieved successfully", bootstyle="success")

def set_today():
    today_str = date.today().strftime('%d-%m-%Y')
    cal.entry.delete(0, 'end')
    cal.entry.insert(0, today_str)
    see_date()

def clear_date():
    cal.entry.delete(0, 'end')
    date_label.config(text="No date selected")
    status_label.config(text="Date cleared", bootstyle="warning")

#frame for better layout
frame = ttk.Frame(root, padding=50)
frame.pack(fill=BOTH, expand=YES)

#DateEntry widget
cal = ttkbootstrap.DateEntry(frame, dateformat='%d-%m-%Y', bootstyle='info', firstweekday=6)
cal.grid(row=0, column=0, columnspan=3, pady=10)

#Buttons
show_btn = ttk.Button(frame, text='Show Date', bootstyle="light-outline", command=see_date)
show_btn.grid(row=1, column=0, padx=5, pady=10)

today_btn = ttk.Button(frame, text='Today', bootstyle="success-outline", command=set_today)
today_btn.grid(row=1, column=1, padx=5, pady=10)

clear_btn = ttk.Button(frame, text='Clear', bootstyle="danger-outline", command=clear_date)
clear_btn.grid(row=1, column=2, padx=5, pady=10)

#Label to display date
date_label = ttk.Label(frame, text='No date selected', font=("Helvetica", 12))
date_label.grid(row=2, column=0, columnspan=3, pady=20)

#Status bar
status_label = ttk.Label(root, text='Ready', anchor='w', bootstyle="info")
status_label.pack(fill=X, side=BOTTOM)

#Bind Enter key to show date
root.bind('<Return>', lambda e: see_date())

root.mainloop()
