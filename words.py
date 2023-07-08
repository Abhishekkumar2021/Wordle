with open("words.txt", "r") as r:
    words = r.read()
    words = words.split()
    with open("raw.txt", 'w') as w:
        for word in words:
            w.write(f"'{word}', ")