import customtkinter
from tkinter import messagebox

# Set appearance mode and color theme
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# Create the root window
root = customtkinter.CTk()
root.geometry("500x400")  # Set window size

# Define the calculation methods
def calculate_method(selected_method):
    if selected_method == "Bisection Method":
        messagebox.showinfo("Calculation", "Bisection Method selected")
    elif selected_method == "Newton-Raphson Method":
        messagebox.showinfo("Calculation", "Newton-Raphson Method selected")
    elif selected_method == "Runge-Kutta Method":
        messagebox.showinfo("Calculation", "Runge-Kutta Method selected")
    elif selected_method == "Simpson's Rule":
        messagebox.showinfo("Calculation", "Simpson's Rule selected")
    elif selected_method == "Euler Method":
        messagebox.showinfo("Calculation", "Euler Method selected")
    else:
        messagebox.showerror("Error", "No method selected")

# Create the frame
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

# Create the label
label = customtkinter.CTkLabel(master=frame, text="Select Calculation Method", font=("Roboto", 18))
label.pack(pady=12, padx=10)

# Create the entry fields (for future user inputs if needed)
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Input First Number")
entry1.pack(pady=12, padx=10)

entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Input Second Number")
entry2.pack(pady=12, padx=10)

# OptionMenu for selecting methods
method_options = ["Bisection Method", "Newton-Raphson Method", "Runge-Kutta Method", "Simpson's Rule", "Euler Method"]
optionmenu = customtkinter.CTkOptionMenu(master=frame, values=method_options)
optionmenu.pack(pady=12, padx=10)
optionmenu.set("Select Method")  # Default placeholder

# Create the calculate button
button = customtkinter.CTkButton(master=frame, text="Calculate",
                                 command=lambda: calculate_method(optionmenu.get()))
button.pack(pady=12, padx=10)

# Run the application
root.mainloop()
