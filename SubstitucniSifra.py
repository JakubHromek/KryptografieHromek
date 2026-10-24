def cypher(sentence, key, d="None"):
    cipher = ""
    for x in sentence:
        if x != " ":
            if d == "decipher":
                cipher += abeceda[key.find(x)]
            else:
                cipher += key[abeceda.find(x)]
        else:
            cipher += " "
    return cipher


abeceda = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

if __name__ == "__main__":
    print(cypher("DNES JE KRASNY DEN", key))
    print(cypher(cypher("DNES JE KRASNY DEN", key), key, "decipher"))
