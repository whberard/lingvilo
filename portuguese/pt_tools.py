# First 22 lines or so of this file were taken from: 
# http://www.nltk.org/_modules/nltk/examples/pt.html


from nltk.corpus import machado, mac_morpho, floresta, genesis
from nltk.text import Text
from nltk.probability import FreqDist
from nltk.util import bigrams
from nltk.misc import babelize_shell

print("Type: 'texts()' to list the materials.")

ptext1 = Text(machado.words('romance/marm05.txt'), name="Memórias Póstumas de Brás Cubas (1881)")
ptext2 = Text(machado.words('romance/marm08.txt'), name="Dom Casmurro (1899)")
ptext3 = Text(genesis.words('portuguese.txt'), name="Gênesis")
ptext4 = Text(mac_morpho.words('mu94se01.txt'), name="Folha de Sao Paulo (1994)")

def texts():
    print("ptext1:", ptext1.name)
    print("ptext2:", ptext2.name)
    print("ptext3:", ptext3.name)
    print("ptext4:", ptext4.name)

def common_vocab(text, n=50):
    words = [word.lower() for word in text if word.isalpha()]
    fdist = FreqDist(words)
    common = fdist.most_common(n)
    return common

def vocab(text):
    distinct_words = set([word.lower() for word in text if word.isalpha()])
    return distinct_words


