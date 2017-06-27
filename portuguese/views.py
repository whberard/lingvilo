from django.shortcuts import render
from portuguese.models import Verb, Word
from portuguese.pt_tools import *
import datetime
from portuguese.forms import WordForm

# Create your views here.
def conjugate_pt(request):
    context = {}
    irreg = ["crer", "dar", "ir", "saber", "vir"]
    context['irreg'] = irreg
    dbverbs = Verb.objects.all()
    context['dbverbs'] = dbverbs

    if 'verb' in request.GET and request.GET['verb']:
        verb = request.GET['verb']
        context['verb'] = verb
        conj = get_conjugation_pt(verb)
        if conj:
            context['present'] = conj["present"]
            context['preterit'] = conj["preterit"]
            context['imperative'] = conj["imperative"]

            return render(request, 'conjugate.html', context)
        else: 
            errormsg = "I only know how to conjugate regular verbs that end in -ar, -er, or -ir."
            context['errormsg'] = errormsg
            return render(request, 'conjugate.html', context)

    else: 
        return render(request, 'conjugate.html', context)



def get_conjugation_pt(verb):
    conj = {}

    if verb == "crer":
        present = {'eu': 'creio',
                'tu': 'crês',
                'ela': 'crê',
                'nós': 'cremos',
                'elas': 'crêem'
                }
        conj['present'] = present
        preterit = {'eu': 'cri',
                'tu': 'crêste',
                'ela': 'creu',
                'nós': 'cremos',
                'elas': 'creram'
                }
        conj['preterit'] = preterit
        conj['imperative'] = {}
    elif verb == "dar":
        present = {'eu': 'dou',
                'tu': 'dás',
                'ela': 'dá',
                'nós': 'damos',
                'elas': 'dão'
                }
        conj['present'] = present
        preterit = {'eu': 'dei',
                'tu': 'deste',
                'ela': 'deu',
                'nós': 'demos',
                'elas': 'deram'
                }
        conj['preterit'] = preterit
        conj['imperative'] = {}
    elif verb == "ir":
        conj['present'] = {'eu': 'vou',
                'tu': 'vais',
                'ela': 'vai',
                'nós': 'vamos',
                }
        conj['preterit'] = {}
        conj['imperative'] = {'ela': 'vai'}

    elif verb == "saber":
        present = {'eu': 'sei',
                'tu': 'sabes',
                'ela': 'sabe',
                'nós': 'sabemos',
                'elas': 'sabem'
                }
        conj['present'] = present
        preterit = {'eu': 'soube',
                'tu': 'soubeste',
                'ela': 'soube',
                'nós': 'soubemos',
                'elas': 'souberam'
                }
        conj['preterit'] = preterit
    elif verb == "ter":
        conj['present'] = {'eu': 'tenho',
                'tu': 'tens',
                'ela': 'tem',
                'nós': 'temos',
                'elas': 'têm'
                }
        conj['preterit'] = {}
        conj['imperative'] = {}

    elif verb == "vir":
        present = {'eu': 'venho',
                'tu': 'vens',
                'ela': 'vem',
                'nós': 'vimos',
                'elas': 'vêm'
                }
        conj['present'] = present
        conj['preterit'] = {}
        conj['imperative'] = {'ela': 'vem'}

    elif verb[-3:] == "car":
        root = verb[:-3]
        imperative = {'ela': root + 'que'}
        conj['imperative'] = imperative
        conj['present'] = regular_present_pt(verb)
        conj['preterit'] = regular_preterit_pt(verb)
    

    else:
        conj['present'] = regular_present_pt(verb)
        conj['preterit'] = regular_preterit_pt(verb)
        conj['imperative'] = regular_imperative_pt(verb)
    
    return conj


def regular_present_pt(verb):
    root = verb[:-2]
    if verb.endswith("ar"):
        present = {'eu': root + 'o',
                'tu': root + 'as',
                'ela': root + 'a',
                'nós': root + 'amos',
                'elas': root + 'am',
                }
    elif verb.endswith("er"):
        present = {'eu': root + 'o',
                'tu': root + 'es',
                'ela': root + 'e',
                'nós': root + 'emos',
                'elas': root + 'em'
                }
    elif verb.endswith("ir"):
        present = {'eu': root + 'o',
                'tu': root + 'es',
                'ela': root + 'e',
                'nós': root + 'imos',
                'elas': root+ 'em'
                }
    else: 
        present = {}
    return present

def regular_preterit_pt(verb):
    root = verb[:-2]
    if verb.endswith("ar"):
        preterit = {'eu': root + 'ei',
                'tu': root + 'aste',
                'ela': root + 'ou',
                'nós': root + 'ámos',
                'elas': root + 'aram',
                }
    elif verb.endswith("er"):
        preterit = {'eu': root + 'i',
                'tu': root + 'este',
                'ela': root + 'eu',
                'nós': root + 'emos',
                'elas': root + 'eram',
                }
    elif verb.endswith("ir"):
        preterit = {'eu': root + 'i',
                'tu': root + 'iste',
                'ela': root + 'iu',
                'nós': root + 'imos',
                'elas': root + 'iram',
                }
    else:
        preterit = {}
    return preterit


def regular_imperative_pt(verb):
    root = verb[:-2]
    if verb.endswith("ar"):
        imperative = {'tu': root + 'a',
                'ela': root + 'e',
                'nós': root + 'emos',
                'elas': root + 'em',
                }
    elif verb.endswith("er"):
        imperative = {'tu': root + 'e',
                'ela': root + 'a',
                'nós': root + 'amos',
                'elas': root + 'am',
                }
    elif verb.endswith("ir"):
        imperative = {'tu': root + 'e',
                'ela': root + 'a',
                'nós': root + 'amos',
                'elas': root + 'am',
                }
    else:
        imperative = {}
    return imperative

        
def subjunctive_constructs(request):
    return render(request, 'subjunctive.html', {})


def my_vocabulary(request):
    #ptext1 = Text(machado.words('romance/marm05.txt'), name="Memórias Póstumas de Brás Cubas (1881)")
    #word_list = common_vocab(ptext1, 20)
    context = {}
    if request.method == 'POST':
        
        form = WordForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            w = Word.objects.get(id=cd['word_id'])
            w.translation = cd['translation']
            w.is_known = cd['is_known']
            w.last_review = datetime.date.today()
            w.save()

    startdate = datetime.date(1999, 1, 1)
    enddate = datetime.date.today() - datetime.timedelta(days=7)
    need_review = Word.objects.filter(last_review__range=[startdate, enddate])
    if len(need_review)>0:
        context['word_to_edit'] =  need_review[0]

        #Make a concordance
        mc = machado_concordance(need_review[0])
        context['concordance'] = mc

    known_words = Word.objects.filter(is_known=True).order_by('word')
    context['known_words'] = known_words
    unknown_words = Word.objects.filter(is_known=False).order_by('word')
    context['unknown_words'] = unknown_words
    return render(request, 'vocabulary.html', context)


def can_i_read_this(request):
    context = {}
    return render(request, 'canireadthis.html', context)


