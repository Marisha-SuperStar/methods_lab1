from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import List

app = FastAPI()

class BoardGame(BaseModel):
    title: str
    duration: str
    player_count: int
    genre: str
    description: str

class User(BaseModel):
    name: str
    games: List[BoardGame]

board_games = []
users = []

@app.get("/board_games")
def get_board_games():
    return board_games

@app.get("/board_games/{title}")
def get_board_game_by_title(title: str):
    for board_game in board_games:
        if board_game.title == title:
            return board_game
    return "Такой игры нет"

@app.post("/board_games")
def add_board_game(board_game: BoardGame):
    board_games.append(board_game)
    return "Игра добавлена"

@app.put("/board_games/{title}")
def change_info_board_game(new_board_game: BoardGame, title: str):
    flag = False
    for board_game in board_games:
        if board_game.title == title:
            board_game.title = new_board_game.title
            board_game.duration = new_board_game.duration
            board_game.description = new_board_game.description
            board_game.genre = new_board_game.genre
            board_game.player_count = new_board_game.player_count
            flag = True

    if not flag:
        return "Такой игры нет"

    for user in users:
        for board_game in user.games:
            if board_game.title == title:
                board_game.title = new_board_game.title
                board_game.duration = new_board_game.duration
                board_game.description = new_board_game.description
                board_game.genre = new_board_game.genre
                board_game.player_count = new_board_game.player_count
    return "Информация обновлена"

@app.delete("/board_games/{title}")
def delete_board_game(title):
    for i in range(len(board_games)):
        if board_games[i].title == title:
            board_games.pop(i)
            for user in users:
                for j in range(len(user.games)):
                    if user.games[j].title == title:
                        user.games.pop(j)
            return "Игра удалена"
    return "Такой игры нет"

@app.get("/users")
def get_users():
    return users

@app.get("/users/{name}")
def get_user_by_name(name: str):
    for user in users:
        if user.name == name:
            return user
    return "Такого пользователя нет"

@app.post("/users")
def add_user(name: str):
    user = User(name=name, games=[])
    users.append(user)
    return "Пользователь добавлен"

@app.post("/users/{name}/{title}")
def add_board_game_to_user(name: str, title: str):
    for user in users:
        if user.name == name:
            for board_game in board_games:
                if board_game.title == title:
                    user.games.append(board_game)
                    return f'Пользователю {user.name} добавлена игра "{board_game.title}"'
            return "Такой игры нет"
    return "Такого пользователя нет"

@app.delete("/users/{name}/{title}")
def delete_board_game_from_user(name: str, title: str):
    for user in users:
        if user.name == name:
            for i in range(len(user.games)):
                if user.games[i].title == title:
                    user.games.pop(i)
                    return f'У пользователя {user.name} удалена игра "{user.games[i].title}"'
            return "Такой игры нет"
    return "Такого пользователя нет"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)