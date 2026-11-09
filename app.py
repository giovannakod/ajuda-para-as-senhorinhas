meme_dict = {
            "PPRT": "Papo reto",
            "BIFE": "Pessoa que voce acha bonito(a)",
"BISCOITAR": "postar algo apenas para chamar a atenção",
    "SLK": "abreviação da palavra 'se é louco'",
            }

for i in range(5):
    word = input("Seja bem vindo(a) !Digite uma palavra moderna que você não entende (escreva todo a palavra em letras maiúsculas): ")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("não encontrada..")
