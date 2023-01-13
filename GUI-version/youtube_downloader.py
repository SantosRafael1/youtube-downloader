import tkinter as tk

root = tk.Tk()

root.geometry('350x300')
root.title("YouTube Downloader")
root.resizable(False, False)

top_label = tk.Label(root, text="Enter URL:").pack()
url = tk.Entry(root, width=40).pack()

root.mainloop()