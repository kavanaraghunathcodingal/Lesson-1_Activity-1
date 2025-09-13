import tkinter as tk
from datetime import date
root = tk.Tk()
root.title("Age Calculator")
root.geometry("300x250")
def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        today = date.today()
        age = today.year - year
       if (today.month, today.day) < (month, day):
            age -= 1

        result_label.config(text=f"Your Age: {age} years")
    except ValueError:
        result_label.config(text="Please enter valid numbers")
tk.Label(root, text="Enter Birth Day:").pack()
day_entry = tk.Entry(root)
day_entry.pack()
tk.Label(root, text="Enter Birth Month:").pack(pady=5)
month_entry = tk.Entry(root)
month_entry.pack()
tk.Label(root, text="Enter Birth Year:").pack(pady=5)
year_entry = tk.Entry(root)
year_entry.pack()
calc_button = tk.Button(root, text="Calculate Age", command=calculate_age)
calc_button.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
