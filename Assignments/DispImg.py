from PIL import Image, ImageTk
import tkinter as tk

def display_image(image_path):
    root = tk.Tk()
    root.title("Taj Mahal")

    img = Image.open(image_path)
    img_tk = ImageTk.PhotoImage(img)

    label = tk.Label(root, image=img_tk)
    label.pack()

    root.mainloop()

display_image('T:/TajMahal.jpg')

