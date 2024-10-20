import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

def clear1():
    result_entry.delete(0, "end")
    entry.delete(0, "end")

def convert(*args):
    current = entry.get()
    from_base = from_var.get()

    try:
        # Splitting the input expression based on the operators
        operands = []
        operators = []
        current_operand = ""
        for char in current:
            if char in "+-*/":
                operands.append(current_operand)
                operators.append(char)
                current_operand = ""
            else:
                current_operand += char
        operands.append(current_operand)  # Add the last operand
        result = float(int(operands[0], from_base))  # Initialize result with the first operand

        # Performing calculations based on the operators
        for i in range(len(operators)):
            if operators[i] == "+":
                result += float(int(operands[i + 1], from_base))
            elif operators[i] == "-":
                result -= float(int(operands[i + 1], from_base))
            elif operators[i] == "*":
                result *= float(int(operands[i + 1], from_base))
            elif operators[i] == "/":
                result /= float(int(operands[i + 1], from_base))

        result_var1.set(f"Decimal: {result:.2f}")
        result_var2.set(f"Binary: {bin(int(result))[2:]}")
        result_var3.set(f"Octal: {oct(int(result))[2:]}")
        result_var4.set(f"Hexadecimal: {hex(int(result))[2:].upper()}")

    except ValueError:
        result_var1.set("Invalid input")

def exit11():
    close = messagebox.askyesno('EXIT', 'Are you sure that you want to exit?')
    if close:
        root.destroy()

def select_base(value):
    for button, base in radio_buttons:
        if base == value:
            button.config(bg="#6A89CC", fg="#FFFFFF")
        else:
            button.config(bg="#ECF0F1", fg="#2C3E50")

root = tk.Tk()
root.title("Number System Converter By LOGS")
root.geometry("750x680")
root.configure(bg="#2C3E50")
root.resizable(width=False, height=False)

# Add "LOGS TEAM" text beside the logo image
logs_team_label = tk.Label(root, text="LOGS TEAM", font=("Arial", 18), bg="#2C3E50", fg="#FFFFFF")
logs_team_label.pack(side="top")

# Load the logo image
try:
    logo_image = Image.open("logs.png")  # Replace "logo.png" with the path to your logo image
    logo_image = logo_image.resize((50, 50))  # Resize the image
    logo_photo = ImageTk.PhotoImage(logo_image)
    logo_label = tk.Label(root, image=logo_photo, bg="#2C3E50")
    logo_label.pack(side="top", padx=20)
except Exception as e:
    print("Error loading logo image:", e)

# Entry field
entry = tk.Entry(root, width=25, bg="#34495E", cursor='arrow', fg="#ECF0F1", font=("Arial", 30), bd=5)
entry.pack(pady=20)
entry.bind("<KeyRelease>", convert)

# Label for choosing base
from_var = tk.IntVar()

from_frame = tk.Frame(root, bg="#2C3E50")
from_frame.pack()
from_label = tk.Label(from_frame, text="Choose the system of the number you are entering:", cursor='arrow', font=("Helvetica", 20),
                      bg="#2C3E50", fg="#ECF0F1")
from_label.pack(side="top", pady=10)

radio_buttons = []

def create_radio_button(parent, text, value):
    button = tk.Radiobutton(parent, text=text, cursor='arrow', variable=from_var, value=value,
                            bg="#2C3E50", fg="#ECF0F1", font=("Helvetica", 15), indicatoron=False,
                            selectcolor="#6A89CC", width=15, relief="flat", highlightthickness=0,
                            command=lambda: select_base(value))
    button.pack(side="left", padx=10)
    radio_buttons.append((button, value))

create_radio_button(from_frame, "Decimal", 10)
create_radio_button(from_frame, "Binary", 2)
create_radio_button(from_frame, "Octal", 8)
create_radio_button(from_frame, "Hexadecimal", 16)

# Buttons frame
buttons_frame = tk.Frame(root, bg="#2C3E50")
buttons_frame.pack()

# Button to perform conversion and clear entries
convert_button = tk.Button(buttons_frame, text="Convert", font=("Helvetica", 18), command=convert, bg="#6A89CC", fg="#FFFFFF")
convert_button.pack(pady=20, padx=10, side="left")

clear_button = tk.Button(buttons_frame, text="Clear", font=("Helvetica", 18), command=clear1, bg="#6A89CC", fg="#FFFFFF")
clear_button.pack(pady=20, padx=10, side="left")

from_frame = tk.Frame(root, bg="#2C3E50")
from_frame.pack()
from_label = tk.Label(from_frame, text="Your number after convertion:", cursor='arrow', font=("Helvetica", 20),
                      bg="#2C3E50", fg="#ECF0F1")
from_label.pack(side="top", pady=10)

# Label for displaying results
result_var1 = tk.StringVar()
result_var1.set("Decimal: ")
result_label1 = tk.Label(root, textvariable=result_var1, font=("Helvetica", 18), bg="#2C3E50", fg="#FFFFFF")
result_label1.pack(pady=10)

result_var2 = tk.StringVar()
result_var2.set("Binary: ")
result_label2 = tk.Label(root, textvariable=result_var2, font=("Helvetica", 18), bg="#2C3E50", fg="#FFFFFF")
result_label2.pack(pady=10)

result_var3 = tk.StringVar()
result_var3.set("Octal: ")
result_label3 = tk.Label(root, textvariable=result_var3, font=("Helvetica", 18), bg="#2C3E50", fg="#FFFFFF")
result_label3.pack(pady=10)

result_var4 = tk.StringVar()
result_var4.set("Hexadecimal: ")
result_label4 = tk.Label(root, textvariable=result_var4, font=("Helvetica", 18), bg="#2C3E50", fg="#FFFFFF")
result_label4.pack(pady=10)

# Exit button
exit_button = tk.Button(root, text="Exit", font=("Helvetica", 18), command=exit11, bg="#6A89CC", fg="#FFFFFF")
exit_button.pack(pady=10)

root.mainloop()
