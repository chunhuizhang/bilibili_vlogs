import tkinter as tk

root = tk.Tk()

test = tk.Label(root, text="Red", bg="red", fg="white")
test.pack(side=tk.BOTTOM)
test = tk.Label(root, text="Green", bg="green", fg="white")
test.pack(side=tk.BOTTOM)
test = tk.Label(root, text="Purple", bg="purple", fg="white")
test.pack(side=tk.BOTTOM)

tk.mainloop()