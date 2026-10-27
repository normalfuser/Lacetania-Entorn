
qualificacions = [8.8, 9.5, 7.0, 10.0, 9.3, 8.5, 7.4, 9.9, 9.2, 7.8]

n = len(qualificacions)

hi_ha_canvis = True

while hi_ha_canvis:
    hi_ha_canvis = False
    for i in range(1, n):
        if qualificacions[i - 1] > qualificacions[i]:
            aux = qualificacions[i]
            qualificacions[i] = qualificacions[i - 1]
            qualificacions[i - 1] = aux
            hi_ha_canvis = True
    n = n - 1

print(qualificacions)
# comentari
