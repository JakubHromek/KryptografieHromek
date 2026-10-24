from EukliduvAlgoritmus import eukliduv_algoritmus
from EulerovaFunkce import euklidova_funkce


def posunuti(x, a, b, cipher):
    x = ord(x) - 65
    if cipher == "+":
        return chr(((a*x + b) % 26) + 65)
    elif cipher == "-":
        inverze = (a ** (euklidova_funkce(26) - 1)) % 26
        return chr(((inverze * (x - b)) % 26) + 65)


def cypher(sentence, a, b, d="None"):
    if eukliduv_algoritmus(a, 26)[0] != 1:
        return "není injektivní"
    cipher = ""
    for x in sentence:
        if x != " ":
            if d == "decipher":
                cipher += posunuti(x, a, b, "-")
            else:
                cipher += posunuti(x, a, b, "+")
        else:
            cipher += " "
    return cipher


if __name__ == "__main__":
    print(cypher("DNES JE KRASNY DEN", 5, 8))
    print(cypher(cypher("DNES JE KRASNY DEN", 5, 8), 5, 8, "decipher"))
