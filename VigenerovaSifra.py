def posunuti(x, key, n, cipher):
    key = ord(key[n]) - 65
    if cipher == "+":
        return chr(65 + (((ord(x) - 65) + key) % 26))
    elif cipher == "-":
        return chr(65 + (((ord(x) - 65) - key) % 26))


def cypher(sentence, key, d="None"):
    cipher = ""
    n = 0
    for x in sentence:
        if x != " ":
            if d == "decipher":
                cipher += posunuti(x, key, n, "-")
            else:
                cipher += posunuti(x, key, n, "+")

            n = (n + 1) % 3
        else:
            cipher += " "
    return cipher


abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "PES"

if __name__ == "__main__":
    print(cypher("DNES JE KRASNY DEN", key))
    print(cypher(cypher("DNES JE KRASNY DEN", key), key, "decipher"))
