
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

root = Tk()
root.title('image splits')

img_name = filedialog.askopenfilename(initialdir='./',
                                      title='please select an image',
                                      filetypes=(('png files', '*.png'), ('jpg files', '*.jpg')))

Label(root, text=img_name).grid(row=0, column=1)

img = Image.open(img_name)
tk_img = ImageTk.PhotoImage(img)

l1 = Label(root, image=tk_img)
l1.image = tk_img
l1.grid(row=1, column=1)

width, height = img.size
cell_width = width//3
cell_height = height//3

for r in range(3):
    for c in range(3):
        cell_image = img.crop((c*cell_width, r*cell_height, (c+1)*cell_width, (r+1)*cell_height))
        cell_image.save('./{}_{}_{}.png'.format(os.path.basename(img_name).split('.')[0], r, c))
        tk_cell_image = ImageTk.PhotoImage(cell_image)
        label = Label(root, image=tk_cell_image)
        label.image = tk_cell_image
        label.grid(row=r+2, column=c)

root.mainloop()