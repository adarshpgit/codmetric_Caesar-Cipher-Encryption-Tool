import tkinter as tk
from tkinter import messagebox

# Caesar Cipher Functions
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def process_text():
    text = input_entry.get()
    shift = shift_entry.get()

    if not text:
        messagebox.showwarning("Input Needed", "Please enter some text.")
        return

    if not shift.lstrip('-').isdigit():
        messagebox.showwarning("Invalid Shift", "Shift must be a number.")
        return

    shift = int(shift)
    if mode.get() == "Encrypt":
        result = encrypt(text, shift)
    else:
        result = decrypt(text, shift)

    result_label.config(text=f"Result:\n{result}")

# GUI Setup
root = tk.Tk()
root.title("Caesar Cipher Tool")
root.geometry("420x300")
root.configure(bg="#eafaf1")
root.resizable(False, False)

frame = tk.Frame(root, bg="#eafaf1", padx=20, pady=20)
frame.pack(fill="both", expand=True)

tk.Label(frame, text="Enter Text:", font=("Segoe UI", 11), bg="#eafaf1").pack(anchor="w")
input_entry = tk.Entry(frame, font=("Segoe UI", 11), width=35)
input_entry.pack(pady=5)

tk.Label(frame, text="Shift Value:", font=("Segoe UI", 11), bg="#eafaf1").pack(anchor="w")
shift_entry = tk.Entry(frame, font=("Segoe UI", 11), width=10)
shift_entry.pack(pady=5)

mode = tk.StringVar(value="Encrypt")
tk.Radiobutton(frame, text="Encrypt", variable=mode, value="Encrypt", font=("Segoe UI", 10), bg="#eafaf1").pack(anchor="w")
tk.Radiobutton(frame, text="Decrypt", variable=mode, value="Decrypt", font=("Segoe UI", 10), bg="#eafaf1").pack(anchor="w")

tk.Button(frame, text="Process", command=process_text,
          bg="#28a745", fg="white", font=("Segoe UI", 10, "bold")).pack(pady=10)

result_label = tk.Label(frame, text="", font=("Segoe UI", 10, "bold"), bg="#eafaf1", justify="left", wraplength=380)
result_label.pack(pady=5)

root.mainloop()
