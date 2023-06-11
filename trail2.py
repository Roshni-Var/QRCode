import qrcode
from tkinter import *
from tkinter import filedialog

def generate_qr_code():
    # Get the user input from the text entry field
    text = text_entry.get()

    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(text)
    qr.make(fit=True)

    # Create an image from the QR code
    qr_image = qr.make_image(fill='black', back_color='white')

    # Prompt the user to save the image file
    save_file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[('PNG Image', '*.png')])
    if save_file_path:
        qr_image.save(save_file_path)
        status_label.config(text="QR code saved successfully!")
    else:
        status_label.config(text="QR code generation cancelled.")

# Create the GUI window
window = Tk()
window.title("QR Code Generator")
window.geometry("400x200")  # Set window size (width x height)

# Create the input label and text entry field
input_label = Label(window, text="Enter text or URL:", font=("Arial", 14))  # Increase font size
input_label.pack()
text_entry = Entry(window, font=("Arial", 12))  # Increase font size
text_entry.pack()

# Create the generate button
generate_button = Button(window, text="Generate QR Code", command=generate_qr_code, font=("Arial", 14))  # Increase font size
generate_button.pack()

# Create the status label
status_label = Label(window, text="", font=("Arial", 12))  # Increase font size
status_label.pack()

# Run the GUI main loop
window.mainloop()
