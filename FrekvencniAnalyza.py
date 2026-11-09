def smazat_nechtene_znaky(text):
    new_text = ""
    for n in text:
        if ord(n) >= 65 and ord(n) <= 90:
            new_text += n
    return new_text
            
def analyza(text):
    text = smazat_nechtene_znaky(text)
    slovnik = {}

    for i in range(65, 91):
        slovnik[chr(i)] = 0
        
    for n in text:
        slovnik[n] = slovnik.get(n, 0) + 1
    for n in range(1, len(text)):
        slovnik[f"{text[n-1]}{text[n]}"] = slovnik.get(f"{text[n-1]}{text[n]}", 0) + 1

    for n in range(2, len(text)):
        slovnik[f"{text[n-2]}{text[n-1]}{text[n]}"] = slovnik.get(f"{text[n-2]}{text[n-1]}{text[n]}", 0) + 1
    return slovnik

for klic, hodnota in analyza("AHOJ, jak se MAS? Dnes je 9. listopadu 2026! Python je SUPER!!! AAA BBB ABC ABC.").items():
    print(f"{klic}: {hodnota}")