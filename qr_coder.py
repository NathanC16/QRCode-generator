import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk
import math

# Global variables to prevent garbage collection
qr_image_pil = None
qr_photo_tk = None

# Base width for responsive font scaling
BASE_WIDTH = 500

# ===================================================================
# APPLICATION FUNCTIONS
# ===================================================================

def on_resize(event):
    """
    Adjusts font sizes proportionally to the window width.
    """
    try:
        current_width = root.winfo_width()
        if current_width > 100:
            scale_factor = current_width / BASE_WIDTH
            
            for widget_info in widgets_to_adjust_font:
                widget = widget_info['widget']
                base_font_size = widget_info['base_size']
                new_size = int(base_font_size * scale_factor)

                if new_size < 8:
                    new_size = 8
                elif new_size > 24:
                    new_size = 24
                
                widget.config(font=("Arial", new_size, widget_info['style']))
    except Exception:
        pass

def generate_qr_code():
    """Generates the QR code and displays it."""
    global qr_image_pil, qr_photo_tk

    data = entry_text.get()
    if not data:
        messagebox.showwarning("Warning", "Please enter text or URL to generate a QR Code.")
        return

    try:
        fill_color = var_color.get()
        back_color = var_background.get()
        box_size = var_qr_size.get()

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=box_size,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        qr_image_pil = qr.make_image(fill_color=fill_color, back_color=back_color)

        max_size = int(root.winfo_width() * 0.8) if root.winfo_width() > 100 else 400
        if qr_image_pil.size[0] > max_size or qr_image_pil.size[1] > max_size:
            qr_image_pil = qr_image_pil.resize((max_size, max_size), Image.Resampling.LANCZOS)

        qr_photo_tk = ImageTk.PhotoImage(qr_image_pil)
        
        label_preview.config(image=qr_photo_tk)
        label_preview.image = qr_photo_tk
        
        messagebox.showinfo("Success", "QR Code generated successfully!")
        
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while generating the QR Code: {e}")

def save_qr_code():
    """Saves the QR code image to a file."""
    global qr_image_pil

    if qr_image_pil is None:
        messagebox.showwarning("Warning", "No QR Code generated to save.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("All files", "*.*")],
        title="Save QR Code as..."
    )

    if file_path:
        try:
            qr_image_pil.save(file_path)
            messagebox.showinfo("Success", f"QR Code saved to: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while saving the file: {e}")

def decrease_size():
    """Decreases the QR code size."""
    current_size = var_qr_size.get()
    if current_size > 5:
        var_qr_size.set(current_size - 1)

def increase_size():
    """Increases the QR code size."""
    current_size = var_qr_size.get()
    if current_size < 50:
        var_qr_size.set(current_size + 1)

# ===================================================================
# GRAPHICAL INTERFACE
# ===================================================================

# Main window configuration
root = tk.Tk()
root.title("Lightweight QR Code Generator")
root.geometry("500x700")
root.minsize(400, 550)
root.resizable(True, True) 

# Tkinter variables
var_qr_size = tk.IntVar(master=root, value=10)
var_color = tk.StringVar(master=root, value="black")
var_background = tk.StringVar(master=root, value="white")

# Colors and fonts
root.configure(bg="#f0f0f0")

# List of widgets for automatic font adjustment
widgets_to_adjust_font = []

def add_responsive_widget(widget, base_size, style="normal"):
    widgets_to_adjust_font.append({'widget': widget, 'base_size': base_size, 'style': style})

# Main frame
main_frame = tk.Frame(root, bg="#f0f0f0", padx=20, pady=20)
main_frame.grid(row=0, column=0, sticky="nsew")

# Configure the window grid to be responsive
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure((0,1), weight=1)
# Apenas a linha do preview terá peso para se expandir
main_frame.rowconfigure(5, weight=1) 


# Título
label_title = tk.Label(main_frame, text="QR Code Generator", font=("Arial", 18, "bold"), bg="#f0f0f0")
label_title.grid(row=0, column=0, columnspan=2, pady=(0, 20), sticky="nsew")
add_responsive_widget(label_title, 18, "bold")

# Campo de texto e seu frame
text_frame = tk.Frame(main_frame, bg="#f0f0f0")
text_frame.grid(row=1, column=0, columnspan=2, pady=(5, 10), sticky="ew")
text_frame.columnconfigure(1, weight=1)

label_text = tk.Label(text_frame, text="Text or URL:", font=("Arial", 12, "bold"), bg="#f0f0f0")
label_text.grid(row=0, column=0, padx=(0, 10), sticky="w")
add_responsive_widget(label_text, 12, "bold")
entry_text = tk.Entry(text_frame, font=("Arial", 10), bd=2, relief="groove")
entry_text.grid(row=0, column=1, sticky="ew")
add_responsive_widget(entry_text, 10)

# Options frame
options_frame = tk.Frame(main_frame, bg="#f0f0f0")
options_frame.grid(row=2, column=0, columnspan=2, pady=10, sticky="ew")
for i in range(8): options_frame.columnconfigure(i, weight=1)

# QR Code Color
label_color = tk.Label(options_frame, text="QR Color:", font=("Arial", 12, "bold"), bg="#f0f0f0")
label_color.grid(row=0, column=0, sticky="e")
add_responsive_widget(label_color, 12, "bold")
colors = ["black", "blue", "red", "green", "purple"]
menu_color = tk.OptionMenu(options_frame, var_color, *colors)
menu_color.config(font=("Arial", 9), relief="flat")
menu_color.grid(row=0, column=1, padx=(5, 10), sticky="ew")
add_responsive_widget(menu_color, 9)

# Background Color
label_background = tk.Label(options_frame, text="Background:", font=("Arial", 12, "bold"), bg="#f0f0f0")
label_background.grid(row=0, column=2, sticky="e")
add_responsive_widget(label_background, 12, "bold")
backgrounds = ["white", "yellow", "cyan", "lightgray"]
menu_background = tk.OptionMenu(options_frame, var_background, *backgrounds)
menu_background.config(font=("Arial", 9), relief="flat")
menu_background.grid(row=0, column=3, padx=(5, 10), sticky="ew")
add_responsive_widget(menu_background, 9)

# Size
label_size = tk.Label(options_frame, text="Size:", font=("Arial", 12, "bold"), bg="#f0f0f0")
label_size.grid(row=0, column=4, sticky="e")
add_responsive_widget(label_size, 12, "bold")
btn_decrease = tk.Button(options_frame, text='◄', command=decrease_size, font=("Arial", 10), relief="raised")
btn_decrease.grid(row=0, column=5, sticky="ew")
add_responsive_widget(btn_decrease, 10)
label_current_size = tk.Label(options_frame, textvariable=var_qr_size, font=("Arial", 10, "bold"), bg="#f0f0f0")
label_current_size.grid(row=0, column=6, sticky="ew")
add_responsive_widget(label_current_size, 10, "bold")
btn_increase = tk.Button(options_frame, text='►', command=increase_size, font=("Arial", 10), relief="raised")
btn_increase.grid(row=0, column=7, sticky="ew")
add_responsive_widget(btn_increase, 10)

# Main buttons frame
buttons_frame = tk.Frame(main_frame, bg="#f0f0f0")
buttons_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")
buttons_frame.columnconfigure((0, 1), weight=1)

btn_generate = tk.Button(buttons_frame, text="Generate QR Code", command=generate_qr_code, bg="#4CAF50", fg="white", font=("Arial", 10, "bold"), bd=0, relief="raised", padx=15, pady=8)
btn_generate.grid(row=0, column=0, padx=5, sticky="ew")
add_responsive_widget(btn_generate, 10, "bold")
btn_save = tk.Button(buttons_frame, text="Save QR Code", command=save_qr_code, bg="#008CBA", fg="white", font=("Arial", 10, "bold"), bd=0, relief="raised", padx=15, pady=8)
btn_save.grid(row=0, column=1, padx=5, sticky="ew")
add_responsive_widget(btn_save, 10, "bold")

# QR Code preview
label_preview = tk.Label(main_frame, bg="#f0f0f0")
label_preview.grid(row=5, column=0, columnspan=2, pady=20, sticky="nsew")

# Placeholder
placeholder_image = Image.new('RGB', (200, 200), 'white')
placeholder_tk = ImageTk.PhotoImage(placeholder_image)
label_preview.config(image=placeholder_tk)

# Bind the resize event
root.bind('<Configure>', on_resize)

# Start the application main loop
root.mainloop()
