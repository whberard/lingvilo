from django.shortcuts import render

# Create your views here.
def conjugate_pt(request):
    irreg = ["crer", "dar", "saber"]
    if 'verb' in request.GET and request.GET['verb']:
        verb = request.GET['verb']
        ending = verb[-2:]
        root = verb[:-2]
        conj = get_conjugation_pt(verb)
        if conj:
            present = conj["present"]
            preterit = conj["preterit"]

            return render(request, 'conjugate.html', {'verb': verb, 'ending': ending, 'root': root, 'present': present, 'preterit': preterit, 'irreg': irreg})
        else: 
            errormsg = "I only know how to conjugate regular verbs that end in -ar, -er, or -ir."
            return render(request, 'conjugate.html', {'verb': verb, 'error': errormsg, 'irreg': irreg})

    else: 
        return render(request, 'conjugate.html', {'irreg': irreg})



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


    else:
        ending = verb[-2:]
        root = verb[:-2]
        if ending == "ar":
            present = {'eu': root + 'o',
                    'tu': root + 'as',
                    'ela': root + 'a',
                    'nós': root + 'amos',
                    'elas': root + 'am',
                    }
            conj['present'] = present
    
    
            preterit = {'eu': root + 'ei',
                    'tu': root + 'aste',
                    'ela': root + 'ou',
                    'nós': root + 'ámos',
                    'elas': root + 'aram',
                    }
            conj['preterit'] = preterit
    
        elif ending == "er":
    
            present = {'eu': root + 'o',
                    'tu': root + 'es',
                    'ela': root + 'e',
                    'nós': root + 'emos',
                    'elas': root + 'em'
                    }
            conj['present'] = present
    
            preterit = {'eu': root + 'i',
                    'tu': root + 'este',
                    'ela': root + 'eu',
                    'nós': root + 'emos',
                    'elas': root + 'eram',
                    }
            conj['preterit'] = preterit
    
    
        elif ending == "ir":
            present = {'eu': root + 'o',
                    'tu': root + 'es',
                    'ela': root + 'e',
                    'nós': root + 'imos',
                    'elas': root+ 'em'
                    }
            conj['present'] = present
            preterit = {'eu': root + 'i',
                    'tu': root + 'iste',
                    'ela': root + 'iu',
                    'nós': root + 'imos',
                    'elas': root + 'iram',
                    }
            conj['preterit'] = preterit
    
    return conj



    

