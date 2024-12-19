# --- PARTIE 2 ---

persons = [
    ("Melanie", 25, 1.6),
    ("Paul", 29, 1.8),
    ("Jacques", 35, 1.75),
    ("Martin", 16, 1.65),
]

def obtain_info(name, _list):
    for i in _list:
        if i[0] == name:
            return i
    return None

# Jacques
#infos = obtain_info("Jacques", persons)
# print(infos)
persons_dict = {
    "Melanie" : (25, 1.6),
    "Paul" : (29, 1.8),
    "Jacques" : (35, 1.75),
    "Martin" : (16, 1.65),

}
infos = persons_dict.get("Claire")
if not infos:
    print("La personnes n'existe pas dans la liste")
else:
    print(infos)
