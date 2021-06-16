from pprint import pprint
# Задача №1

basketball_players = {
    "Леброн Джеймс": "2.06 м",
    "Энтони Дэвис": "2.08 м",
    "Яннис Адетокунбо": "2.11 м",
    "Лука Дончич": "2.01 м",
    "Кавай Леонард": "2.01 м",
    'Кевин Дюрант': "2.08 м",
}
# Добавление
basketball_players["Дэмьен Лиллард"] = "1.88 м"
# Удаление
basketball_players.pop("Дэмьен Лиллард")
# Поиск
pprint(basketball_players.get("Энтони Дэвис"))
pprint(basketball_players.get("Энтони Дэвисисис"))
# Замена данных
pprint(basketball_players["Энтони Дэвис"])
basketball_players["Энтони Дэвис"] = "2.111 м"

pprint(basketball_players)
# ===============================================================
