import customtkinter
from PIL import Image
import requests
from io import BytesIO


# На вход подаются аргументы которые нам не нужны, поэтому не используем их
def refresh_buttons(*args):
    search_term = search_var.get()
    current_tab = tabview.get()

    if current_tab == "Books":
        for button in tabview.tab("Books").winfo_children():
            button.destroy()
        get_books(search_term)
    elif current_tab == "Characters":
        for button in scrollable_frame_characters.winfo_children():
            button.destroy()
        get_characters(search_term)
    elif current_tab == "Houses":
        for button in tabview.tab("Houses").winfo_children():
            button.destroy()
        get_houses(search_term)
    elif current_tab == "Spells":
        for button in scrollable_frame_spells.winfo_children():
            button.destroy()
        get_spells(search_term)


def open_new_window(desc, image=None):
    new_window = customtkinter.CTkToplevel(app)
    new_window.title("Description")
    new_window.geometry("600x600")

    scrollable_frame = customtkinter.CTkScrollableFrame(new_window, width=580, height=580)
    scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

    if image:
        response = requests.get(image)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        image = Image.open(image_data)
        ctk_image = customtkinter.CTkImage(light_image=image, size=(300, 400))

        image_label = customtkinter.CTkLabel(scrollable_frame, image=ctk_image, text="")
        image_label.pack(pady=10)

    text_label = customtkinter.CTkLabel(scrollable_frame, text=f"{desc}", wraplength=550, justify="left")
    text_label.pack(pady=10)


def get_books(search_query=""):
    response = requests.get('https://potterapi-fedeperin.vercel.app/en/books',
                            params={"search": search_query} if search_query else {})
    books = response.json()
    for elem in books:
        description = (
            f"Title: {elem['title']}\n"
            f"Original Title: {elem['originalTitle']}\n"
            f"Release Date: {elem['releaseDate']}\n"
            f"Pages: {elem['pages']}\n"
            f"Description:\n{elem['description']}\n"
        )

        button = customtkinter.CTkButton(tabview.tab("Books"), text=elem['title'],
                                         command=lambda desc=description, image=elem['cover']: open_new_window(desc, image))
        button.pack(padx=20, pady=5)


def get_characters(search_query=""):
    response = requests.get('https://potterapi-fedeperin.vercel.app/en/characters',
                            params={"search": search_query} if search_query else {})
    characters = response.json()

    for elem in characters:
        description = (
            f"Full Name: {elem['fullName']}\n"
            f"Nickname: {elem['nickname']}\n"
            f"Hogwarts House: {elem['hogwartsHouse']}\n"
            f"Interpreted By: {elem['interpretedBy']}\n"
            f"Birthdate: {elem['birthdate']}\n"
            f"Children: {', '.join(elem['children']) if elem['children'] else 'None'}\n"
        )
        button = customtkinter.CTkButton(scrollable_frame_characters, text=elem['nickname'],
                                         command=lambda desc=description, image=elem['image']: open_new_window(desc, image))
        button.pack(padx=20, pady=5)


def get_houses(search_query=""):
    response = requests.get('https://potterapi-fedeperin.vercel.app/en/houses',
                            params={"search": search_query} if search_query else {})
    houses = response.json()

    for elem in houses:
        description = (
            f"House: {elem['house']} {elem['emoji']}\n"
            f"Founder: {elem['founder']}\n"
            f"Colors: {', '.join(elem['colors'])}\n"
            f"Animal: {elem['animal']}\n"
        )
        button = customtkinter.CTkButton(tabview.tab("Houses"), text=elem['house'],
                                         command=lambda desc=description: open_new_window(desc))
        button.pack(padx=20, pady=5)


def get_spells(search_query=""):
    response = requests.get('https://potterapi-fedeperin.vercel.app/en/spells',
                            params={"search": search_query} if search_query else {})
    spells = response.json()

    for elem in spells:
        description = (
            f"Spell: {elem['spell']}\n"
            f"Use: {elem['use']}\n"
        )
        button = customtkinter.CTkButton(scrollable_frame_spells, text=elem['spell'],
                                         command=lambda desc=description: open_new_window(desc))
        button.pack(padx=20, pady=5)


app = customtkinter.CTk()
app.title("Harry Potter")
app.geometry("400x600")

tabview = customtkinter.CTkTabview(app, fg_color='#decbb7')
tabview.pack(padx=20, pady=10, fill="both", expand=True)

tabview.add("Books")
tabview.add("Characters")
tabview.add("Houses")
tabview.add("Spells")
tabview.set("Books")

scrollable_frame_characters = customtkinter.CTkScrollableFrame(tabview.tab("Characters"), fg_color='#decbb7')
scrollable_frame_characters.pack(padx=10, pady=10, fill="both", expand=True)

scrollable_frame_spells = customtkinter.CTkScrollableFrame(tabview.tab("Spells"), fg_color='#decbb7')
scrollable_frame_spells.pack(padx=10, pady=10, fill="both", expand=True)

label = customtkinter.CTkLabel(app, text="Search:")
label.pack(padx=10, pady=5)

search_var = customtkinter.StringVar()
search_entry = customtkinter.CTkEntry(app, textvariable=search_var)
search_entry.bind("<Return>", refresh_buttons)
search_entry.pack(padx=20, pady=10, fill="x")

get_books()
get_characters()
get_houses()
get_spells()

app.mainloop()
