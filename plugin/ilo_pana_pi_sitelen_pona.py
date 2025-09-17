import pyperclip
from flox import Flox

import dictionary_tok

class IloPanaPiSitelenPona(Flox): 
    def query(self, query):
        self.add_item(
            title = ("Convert2SitelenPona: {}".format(('Your query is: ' + query , query)[query == ''])),
            subtitle =  ("Copy sitelen pona sentence to clipboard."),
            # icon = ("Images/icon.png"),
            # "ContextData": ["foo", "bar"]
            method = ("convert_tok"),
            parameters = [query]
        )
    
    def convert_tok(self, query):
        q = query
        q = q.strip()
        q = q.replace(".", " . ")
        q = q.replace(",", " , ")
        q = q.replace("?", " ? ")
        q = q.replace("!", " ! ")
        q = q.replace(":", " : ")
        q = q.replace(";", " ; ")
        q = q.replace("(", " ( ")
        q = q.replace(")", " ) ")
        q = q.replace("[", " [ ")
        q = q.replace("]", " ] ")
        words = q.split(' ')
        # TODO: convert sentence
        dict_sp = dictionary_tok.ascii2sitelenpona
        converted_words = [dict_sp.get(w, w) for w in words]

        pyperclip.copy("".join(converted_words))
        return

if __name__ == "__main__":
    IloPanaPiSitelenPona()