import translator as tr

t = tr.Translator()

t.loadDictionary("dictionary.txt")
while(True):

    t.printMenu()

    txtIn = input()

    # Add input control here!

    if int(txtIn) == 1:
        print("Inserire la parola aliena associata alle sua/sue traduzione/i:")
        nuova_voce = input()
        t.handleAdd(nuova_voce)
        print()

    if int(txtIn) == 2:
        print("Parola da cercare:")
        parola_da_cercare = input()
        t.handleTranslate(parola_da_cercare)
        print()

    if int(txtIn) == 3:
        print("Inserire la parola da cercare con la wildcard (es. 'par?la'):")
        parola_wildcard = input()
        t.handleWildCard(parola_wildcard)
        print()

    if int(txtIn) == 4:
        t.handlePrintAll()
        print()

    if int(txtIn) == 5:
        print("Chiusura dizionario")
        break