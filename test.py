import customtkinter

def update_label(content):  # обновляем текст
    label.configure(text=content)


def button_callback1():  # тык на кнопку 1
    with open('base1.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
        update_label(content)


def button_callback2():  # тык на кнопку 2
    with open('base2.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
        update_label(content)


def button_callback3():  # тык на кнопку 3
    with open('base3.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
        update_label(content)

app = customtkinter.CTk()
app.title("test")
app.geometry("1000x750")


scrollable_frame_left = customtkinter.CTkScrollableFrame(app, width=300, height=700) # создаем фрейм 1
scrollable_frame_left.grid(row=0, column=0, padx=10, pady=10)


button = customtkinter.CTkButton(scrollable_frame_left, text="my button", command=button_callback1, width=280, height=50) # создаем кнопку 1
button.grid(row=0, padx=10, pady=10)

button = customtkinter.CTkButton(scrollable_frame_left, text="your button", command=button_callback2, width=280, height=50) # создаем кнопку 2
button.grid(row=1, padx=10, pady=10)

button = customtkinter.CTkButton(scrollable_frame_left, text="our button", command=button_callback3, width=280, height=50) # создаем кнопку 3
button.grid(row=2, padx=10, pady=10)


scrollable_frame_right = customtkinter.CTkScrollableFrame(app, width=600, height=700) # создаем фрейм 2
scrollable_frame_right.grid(row=0, column=1, padx=10, pady=10)

label = customtkinter.CTkLabel(scrollable_frame_right, text="", wraplength=560,  justify="left", font=("Times New Roman", 18)) # выводим текст
label.grid(row=0, column=0, padx=25, pady=25)

app.mainloop()
