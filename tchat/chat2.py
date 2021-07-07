def chat():
    qts = {
        "salut":"bonjour",
        "comment tu vas": "très bien",
        "quel est ton age":"j'ai 20ans",

    }
    while True:
        qs=input()
        if(qs == "quitter"):
            break
        else:
            print(qts[qs])