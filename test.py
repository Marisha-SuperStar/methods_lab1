import customtkinter


def button_callback1():
    label = customtkinter.CTkLabel(scrollable_frame_right, text="button1")
    label.grid(row=0, column=1, sticky="n")


def button_callback2():
    label = customtkinter.CTkLabel(scrollable_frame_right, text="button2")
    label.grid(row=0, column=1, sticky="n")


def button_callback3():
    label = customtkinter.CTkLabel(scrollable_frame_right, text="button3")
    label.grid(row=0, column=1, sticky="n")


app = customtkinter.CTk()
app.title("test")
app.geometry("1000x750")

scrollable_frame_left = customtkinter.CTkScrollableFrame(app, width=300, height=700)
scrollable_frame_left.grid(row=0, column=0, padx=10, pady=10)

button = customtkinter.CTkButton(scrollable_frame_left, text="my button", command=button_callback1)
button.grid(row=0, padx=10, pady=10)

button = customtkinter.CTkButton(scrollable_frame_left, text="your button", command=button_callback2)
button.grid(row=1, padx=10, pady=10)

button = customtkinter.CTkButton(scrollable_frame_left, text="our button", command=button_callback3)
button.grid(row=2, padx=10, pady=10)

scrollable_frame_right = customtkinter.CTkScrollableFrame(app, width=600, height=700)
scrollable_frame_right.grid(row=0, column=1, padx=10, pady=10)
app.mainloop()