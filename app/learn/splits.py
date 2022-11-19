from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os

root = Tk()
root.title('split')


def split_image():
    img_name = filedialog.askopenfilename(initialdir='./',
                                          title='Select A Image',
                                          filetypes=(('png files', '*.png'),))

    Label(root, text=img_name, ).grid(row=1, column=1)

    pil_img = Image.open(img_name)
    print(pil_img.size)
    width, height = pil_img.size
    cell_width = width // 3
    cell_height = height // 3
    for r in range(3):
        for c in range(3):
            cell_img = pil_img.crop((c * cell_width, r * cell_height, (c + 1) * cell_width, (r + 1) * cell_height))
            print(cell_img.size)
            tk_cell_image = ImageTk.PhotoImage(cell_img)
            cell_img.save('./{}_{}_{}.png'.format(os.path.basename(img_name).split('.')[0], r, c))
            label = Label(root, image=tk_cell_image)
            label.image = tk_cell_image
            label.grid(row=r+2, column=c)
            # label.pack()


Button(root, text='split', command=split_image).grid(row=0, column=1)

root.mainloop()
