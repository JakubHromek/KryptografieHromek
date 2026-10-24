def posunuti(x, key, cipher):
    if cipher == "+":
        return chr(65 + (((ord(x) - 65) + key) % 26))
    elif cipher == "-":
        return chr(65 + (((ord(x) - 65) - key) % 26))


def cypher(sentence, key, d="None"):
    cipher = ""
    for x in sentence:
        print(x)
        if x != " ":
            if d == "decipher":
                cipher += posunuti(x, key, "-")
            else:
                cipher += posunuti(x, key, "+")
        else:
            cipher += " "
    return cipher


print(cypher(cypher("DNES JE KRASNY DEN", 5), 5, "decipher"))
