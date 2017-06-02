from django.shortcuts import render
from portuguese.models import Verb

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
    ending = verb[-2:]
    root = verb[:-2]
    if ending == "ar":
        present = {'eu': root + 'o',
                'tu': root + 'as',
                'ela': root + 'a',
                'nós': root + 'amos',
                'elas': root + 'am',
                }
    elif ending == "er":
        present = {'eu': root + 'o',
                'tu': root + 'es',
                'ela': root + 'e',
                'nós': root + 'emos',
                'elas': root + 'em'
                }
    elif ending == "ir":
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
    ending = verb[-2:]
    root = verb[:-2]
    if ending == "ar":
        preterit = {'eu': root + 'ei',
                'tu': root + 'aste',
                'ela': root + 'ou',
                'nós': root + 'ámos',
                'elas': root + 'aram',
                }
    elif ending == "er":
        preterit = {'eu': root + 'i',
                'tu': root + 'este',
                'ela': root + 'eu',
                'nós': root + 'emos',
                'elas': root + 'eram',
                }
    elif ending == "ir":
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
    ending = verb[-2:]
    root = verb[:-2]
    if ending == "ar":
        imperative = {'tu': root + 'a',
                'ela': root + 'e',
                'nós': root + 'emos',
                'elas': root + 'em',
                }
    elif ending == "er":
        imperative = {'tu': root + 'e',
                'ela': root + 'a',
                'nós': root + 'amos',
                'elas': root + 'am',
                }
    elif ending == "ir":
        imperative = {'tu': root + 'e',
                'ela': root + 'a',
                'nós': root + 'amos',
                'elas': root + 'am',
                }
    else:
        imperative = {}
    return imperative

        







