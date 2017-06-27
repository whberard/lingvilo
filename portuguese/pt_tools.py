# First 22 lines or so of this file were taken from: 
# http://www.nltk.org/_modules/nltk/examples/pt.html

from nltk.corpus import machado, mac_morpho, floresta, genesis
from nltk.text import Text, ConcordanceIndex
from nltk.probability import FreqDist
from nltk.util import bigrams
from nltk.misc import babelize_shell
from portuguese.models import Word
import datetime

print("Type: 'texts()' to list the materials.")

ptext1 = Text(machado.words('romance/marm05.txt'), name="Memórias Póstumas de Brás Cubas (1881)")
ptext2 = Text(machado.words('romance/marm08.txt'), name="Dom Casmurro (1899)")
ptext3 = Text(genesis.words('portuguese.txt'), name="Gênesis")
ptext4 = Text(mac_morpho.words('mu94se01.txt'), name="Folha de Sao Paulo (1994)")

machado_fileids = machado.fileids()
machado_words = machado.words('romance/marm05.txt')
machado_text = Text(machado_words)
machado_ci = ConcordanceIndex(machado_text)

def texts():
    print("ptext1:", ptext1.name)
    print("ptext2:", ptext2.name)
    print("ptext3:", ptext3.name)
    print("ptext4:", ptext4.name)

def common_vocab(text, n=50):
    words = [word.lower() for word in text if word.isalpha()]
    fdist = FreqDist(words)
    common = fdist.most_common(n)
    word_list = [w for (w,n) in common]
    return word_list

def vocab(text):
    distinct_words = set([word.lower() for word in text if word.isalpha()])
    return distinct_words


def add_words_to_db(word_list):
    added = []
    for w in word_list:
        obj, created = Word.objects.get_or_create(word=w, defaults={'is_known': False, 'last_review': datetime.date(2000, 1, 1)})
        if created:
            added.append(w)

    print("Added ", len(added), " words, out of ", len(word_list), " total words.")

    return added

def machado_concordance(word, width=75, lines=10):
    # This is edited from the concordance code to return 
    # a list of results instead of directly printing

    half_width = (width - len(word) - 2) // 2
    context = width // 4 # approx number of words of context

    offsets = machado_ci.offsets(word)
    concordance = []
    if offsets:
        lines = min(lines, len(offsets))
        #print("Displaying %s of %s matches:" % (lines, len(offsets)))
        for i in offsets:
            if lines <= 0:
                break
            
            left = (' ' * half_width + ' '.join(machado_ci.tokens()[i-context:i]))
            right = ' '.join(machado_ci.tokens()[i+1:i+context])
            left = left[-half_width:]
            right = right[:half_width]
            concordance.append(left + ' ' + machado_ci.tokens()[i] + ' ' + right)
            lines -= 1
            
    return concordance




