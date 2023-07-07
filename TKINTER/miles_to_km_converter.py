import tkinter


window = tkinter.Tk()
window.title("Miles to Km converter")
# window.minsize(width=200, height=100)
window.config(padx=10, pady=10)


def miles_to_km():
    miles=float(miles_input.get())
    km=1.61*miles
    km_value_label.config(text=f"{km}")

# Input box for miles value
miles_input = tkinter.Entry(width=10)
miles_input.grid(row=0, column=1)

# Labels
miles_label = tkinter.Label(text="Miles")
miles_label.grid(row=0, column=2)
equal_to_label = tkinter.Label(text="is equal to")
equal_to_label.grid(row=1,column=0)
km_value_label = tkinter.Label(text='0')
km_value_label.grid(row=1,column=1)
km_label = tkinter.Label(text="Km")
km_label.grid(row=1,column=2)

# Button
calculate_button = tkinter.Button(text="Calculate",command=miles_to_km)
calculate_button.grid(row=2,column=1)

window.mainloop()
