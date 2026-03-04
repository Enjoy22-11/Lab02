from dictionary import Dictionary
class Translator:

    def __init__(self):
        self.diz = Dictionary()

    def printMenu(self):
        print("-----------------------------")
        print("   Translator Alien-Italian  ")
        print("-----------------------------")
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca una wildcard")
        print("4. Stampa tutto il dizionario")
        print("5. Exit")
        print("-----------------------------")

    def loadDictionary(self, dict):
        try:
            with open(dict, 'r', encoding='utf-8') as file:
                for line in file:
                    parts = line.strip().split(" ")
                    if len(parts) == 2:
                        parola_aliena = parts[0]
                        parola_italiana = parts[1]
                        self.diz.addWord(parola_aliena, parola_italiana)
            print("Dizionario caricato con successo!")

        except FileNotFoundError:
            print("Errore: il file del dizionario non è stato trovato")


    def handleAdd(self, entry):
        if not entry.replace(" ", "").isalpha():
            print("Errore: è possibile inserire solo lettere dell'alfabeto")
            return
        parts = entry.lower().split(" ")
        if len(parts) < 2:
            print("Errore: devi inserire una parola aliena e almeno una traduzione")
            return
        parola_aliena = parts[0]
        traduzione = parts[1:]
        for trad in traduzione:
            self.diz.addWord(parola_aliena, trad)
        print("Aggiunta")
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>

    def handleTranslate(self, query):
        traduzione = self.diz.translate(query)
        if traduzione is not None:
            print(f"La traduzione di {query} è: {traduzione}")
        else:
            print(f"La parola cercata {query} non è presente nel dizionario")

        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        query = query.lower()
        if query.count('?')!=1:
            print("Errore: la parola da cercare può contenere solo un punto interrogativo '?'")
            return
        risultati = self.diz.translateWordWildCard(query)
        if risultati:
            print(f"Le traduzioni trovate per '{query}' sono: {risultati}")
        else:
            print(f"Nessuna corrispondenza trovata per '{query}'")
    def handlePrintAll(self):
        if not self.diz.parole:
            print("Il dizionario è vuoto")
            return
        print("Dizionario completo:")
        for parola_aliena, traduzioni in self.diz.parole.items():
            print(f"{parola_aliena}: {traduzioni}")
        # Scorriamo tutto il dizionario usando .items()
