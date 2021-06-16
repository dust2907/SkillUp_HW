from pprint import pprint
# Задача №2

engfra = {
    "Beetroot": "Betterave",
    "Carrot": "Carotte",
    "Potatoes": "Pommes de terre",
    "Radish": "Un radis",
    "Onion": "Oignon",
}
# Добавление
engfra["Honest"] = "Honnete"
# Удаление
engfra.pop("Honest")
# Поиск
engfra.get("Radish")
pprint(engfra.get("RadishРедис"))
# Замена данных
pprint(engfra["Carrot"])
engfra["Carrot"] = "Rogger's carrot"

pprint(engfra)
# ===============================================================