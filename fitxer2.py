
participants = [
    ["Joan", 22],
    ["Maria", 45],
    ["Carlos", 38],
    ["Anna", 19],
    ["Pere", 56],
    ["Laura", 24],
    ["Enric", 12],
    ["Sònia", 27],
    ["David", 31],
    ["Elena", 18],
    ["Ricard", 42]
]

n = len(participants)

hi_ha_canvis = True

while hi_ha_canvis:
    hi_ha_canvis = False

    for i in range(1, n):
        if participants[i - 1][1] > participants[i][1]:
            aux = participants[i]
            participants[i] = participants[i - 1]
            participants[i - 1] = aux
            hi_ha_canvis = True

    n = n - 1

print(participants)
