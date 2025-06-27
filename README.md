A lightweight, interactive calendar GUI application built using Python and ttkbootstrap. This project allows users to select a date using a stylish calendar widget, view the selected date, and perform quick actions like setting today's date or clearing the input.


📌 Features:

📅 Date picker with a modern themed DateEntry widget

✅ View and display selected date

🗓️ One-click “Today” button to auto-fill current date

❌ Clear selected date with feedback

🖤 Beautiful dark-themed UI (cyborg theme from ttkbootstrap)

🔁 Keyboard shortcut: Press Enter to show selected date


🛠️ Technologies Used:

1: Python 

2: Tkinter

3: ttkbootstrap for themed widgets

4: datetime module


🧱 Program Structure:

1: Import required libraries

2: Initialize the main window with a specific ttkbootstrap theme

3: Set title, dimensions, and layout

4: Define functions:

   see_date() to show selected date
   set_today() to auto-fill today’s date
   clear_date() to reset the input


5: Add widgets:

   DateEntry for selecting a date
   Buttons: Show Date, Today, Clear
   Labels to display date and app status

6: Start the GUI event loop


▶️ How to Run:

- Make sure Python 3 is installed.

- Install the required library:

   "pip install ttkbootstrap"
  

- Run the app:

   "gui_calendar.py"
