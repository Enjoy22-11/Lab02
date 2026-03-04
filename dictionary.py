class Dictionary:
    def __init__(self):
        self.parole= {}

    def addWord(self, aliena, italiana):
        aliena = aliena.lower()
        italiana = italiana.lower()
        if aliena not in self.parole:
            self.parole[aliena] = []
        if italiana not in self.parole[aliena]:
            self.parole[aliena].append(italiana)


    def translate(self,parola_aliena):
        parola_aliena = parola_aliena.lower()
        if parola_aliena in self.parole:
            return self.parole[parola_aliena]
        else:
            return None

    def translateWordWildCard(self, wildcard_query):
        wildcard_query = wildcard_query.lower()
        traduzioni_trovate = []
        for alien_word, traduzioni in self.parole.items():
            if len(alien_word) == len(wildcard_query):
                match = True
                for i in range(len(alien_word)):
                    if wildcard_query[i] != '?' and wildcard_query[i] != alien_word[i]:
                        match = False
                        break
                if match:
                    traduzioni_trovate.extend(traduzioni)
        return traduzioni_trovate




