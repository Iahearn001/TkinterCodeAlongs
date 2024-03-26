import tkinter as tk

window = tk.Tk()
window.title("My Google")

label1 = tk.Label(
    window,
    text="GOOGLE",
    foreground="yellow",
    background="green",
    width=15,
    height=3
    
)
label1.pack()

button1 = tk.Button(
    window,
    text="Submit",
    fg="white",
    bg="black"
)
button1.pack()

entry1 = tk.Entry(
    window,
)
entry1.pack()

entry1.insert(0, "Search")

some_text = entry1.get()
print(some_text)


window.mainloop()