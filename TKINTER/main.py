import tkinter

window = tkinter.Tk()

window.title("First GUI")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

def button_clicked():
    my_label['text'] = 'Button clicked'  # input.get()
    print('Button clicked')
    print(input.get())

# Label
my_label = tkinter.Label(text="I am a label", font=('Arial', 24, 'bold'))
my_label.grid(row= 0, column= 0)
my_label.config(padx=10,pady=10 )


# Button
my_button = tkinter.Button(text='Click me', command=button_clicked)
my_button.grid(row=1, column=1)

my_button_1 = tkinter.Button(text='Click me', command=button_clicked)
my_button_1.grid(row=0, column=2)

# Entry
input = tkinter.Entry(width= 10)
input.grid(row=2, column=3)


window.mainloop()
