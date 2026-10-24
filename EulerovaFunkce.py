def prvocislo(n):
    m = 2
    if n < 2:
        return False
    else:
        while n > m:
            s = n % m 
            if s == 0:
                return False
            m += 1
    return True

def rozklad_cisla(p):
    m = 2
    pole_rozdeleni = set()
    while m < p:
        if p % m == 0:
            pole_rozdeleni.add(m)
            p = p/m
        else:
            m += 1
    if p > 1:
        pole_rozdeleni.add(p)
    return pole_rozdeleni


def euklidova_funkce(p):
    if prvocislo(p):
        return p - 1
    else:
        pole = rozklad_cisla(p)
        vysledek = p
        for n in pole:
            vysledek *= 1 - 1/n
        return round(vysledek)

print(euklidova_funkce(360))