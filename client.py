import requests

HOST = "http://127.0.0.1:5000"

print("Создание пользователя:")
data = requests.post(
    f"{HOST}/user/",
    json={
        "user_name": "Dmitry Matveev",
        "email": "dmit812@mail.ru",
        "password": "qwerty123456789",
    },
)
print(data.json(), "\n")

print("Создание пользователя с коротким паролем:")
data = requests.post(
    f"{HOST}/user/",
    json={
        "user_name": "Michail Oblomov",
        "email": "misha@yandex.ru",
        "password": "1234",
    },
)
print(data.json(), "\n")

print("Создание пользователя с большим паролем:")
data = requests.post(
    f"{HOST}/user/",
    json={
        "user_name": "Vasilii Pupkin",
        "email": "pupkin@mail.ru",
        "password": "qwerty987654321",
        "asdfghj": "qwerty",
    },
)
print(data.json(), "\n")

print("Запрос пользователя по id:")
data = requests.get(f"{HOST}/user/1/")
print(data.json(), "\n")

print("Зайти под пользователем:")
data = requests.post(
    f"{HOST}/login/",
    json={
        "user_name": "Dmitry Matveev",
        "email": "dmit812@mail.ru",
        "password": "qwerty123456789",
    },
)
print(data.json(), "\n")

print("Зайти под пользователем, ошибка в пароле:")
data = requests.post(
    f"{HOST}/login/",
    json={
        "user_name": "Vasilii Pupkin",
        "email": "pupkin@mail.ru",
        "password": "123456789",
    },
)
print(data.json(), "\n")

print("Размещение объявления без авторизации:")
data = requests.post(
    f"{HOST}/advertisement/",
    json={
        "title": "Продаю автомобиль.",
        "description": "Состояние отличное, сел и поехал.",
    },
)
print(data.json(), "\n")

print("Размещение объявления c авторизацией:")
data = requests.post(
    f"{HOST}/advertisement/",
    json={
        "title": "Продаю автомобиль.",
        "description": "Состояние отличное, сел и поехал.",
    },
    headers={
        "user_name": "Dmitry Matveev",
        "token": "1c854b92-367b-4cd2-8451-6b92a942fa09",
    },
)
print(data.json(), "\n")

print("Запрос объявления по его id:")
data = requests.get(f"{HOST}/advertisement/1/")
print(data.json(), "\n")

print("Попытка изменить объявление, не верный пользователь и ключ:")
data = requests.put(
    f"{HOST}/advertisement/1/",
    json={"title": "Куплю квартиру в вашем районе.", "description": "Дорого и быстро!"},
    headers={
        "user_name": "Vasilii Pupkin",
        "token": "437a34f1-ecda-433b-8690-4a80a76c0936",
    },
)
print(data.json(), "\n")

print("Попытка изменить объявление, верный пользователь и ключ:")
data = requests.put(
    f"{HOST}/advertisement/1/",
    json={"title": "Куплю квартиру в вашем районе.", "description": "Дорого и быстро!"},
    headers={
        "user_name": "Dmitry Matveev",
        "token": "010d9ee6-e252-40b0-bcc1-f85aa64be3a0",
    },
)
print(data.json(), "\n")

print("Попытка удалить объявление, не верный пользователь и ключ:")
data = requests.delete(
    f"{HOST}/advertisement/1/",
    headers={
        "user_name": "Vasilii Pupkin",
        "token": "437a34f1-ecda-433b-8690-4a80a76c0936",
    },
)
print(data.json(), "\n")

print("Попытка удалить объявление, верный пользователь и ключ:")
data = requests.delete(
    f"{HOST}/advertisement/1/",
    headers={
        "user_name": "Dmitry Matveev",
        "token": "010d9ee6-e252-40b0-bcc1-f85aa64be3a0",
    },
)
print(data.json(), "\n")
