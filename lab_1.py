import customtkinter
import requests
from bs4 import BeautifulSoup

def get_description(url):

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        desc = soup.find_all("div", class_="desc-text")

        label.configure(text=desc[0].text)
        print(desc[0].text.replace('\n', "").replace('\t', '').replace('\r', ''))
    else:
        label.configure(text="Не удалось получить описание игры с сайта. Упси")

url = "https://hobbygames.ru/hardkor"

response = requests.get(url)
result = {}
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    games = soup.find_all("div", class_="product-card-title")
    for game in games:
        result[game.contents[1].attrs['title']] = game.contents[1].attrs['href']
    print(result)
else:
    print(f"Не удалось получить игры с сайта. Упси")
    exit(-1)

app = customtkinter.CTk()
app.title("Каталог настольных игр")
app.geometry("1000x750")


scrollable_frame_left = customtkinter.CTkScrollableFrame(app, width=300, height=700, fg_color='#decbb7')
scrollable_frame_left.grid(row=0, column=0, padx=10, pady=10)

i=0
for elem in result.keys():
    button = customtkinter.CTkButton(scrollable_frame_left, text=elem,
                                     command=lambda url=result[elem]: get_description(url),
                                     width=280, height=50, fg_color="#f7f0f5", text_color='#433633')
    button.grid(row=i, padx=5, pady=10)
    i += 1

scrollable_frame_right = customtkinter.CTkScrollableFrame(app, width=600, height=700, fg_color='#decbb7')
scrollable_frame_right.grid(row=0, column=1, padx=10, pady=10)

label = customtkinter.CTkLabel(scrollable_frame_right, text="", wraplength=560,  justify="left",
                               font=("Times New Roman", 18), text_color='#433633')
label.grid(row=0, column=0, padx=25, pady=25)

app.mainloop()
