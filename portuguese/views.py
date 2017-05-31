from django.shortcuts import render

# Create your views here.
def conjugate_pt(request):
    if 'verb' in request.GET and request.GET['verb']:
        cando = False
        verb = request.GET['verb']
        ending = verb[-2:]
        root = verb[:-2]
        if ending == "ar" or ending == "ir" or ending == "er":
            cando = True
            conj = get_conjugation_pt(verb)
            present = conj["present"]
            preterit = conj["preterit"]

            return render(request, 'conjugate.html', {'verb': verb, 'ending': ending, 'root': root, 'present': present, 'preterit': preterit})
        else: 
            errormsg = "I only know how to conjugate regular verbs that end in -ar, -er, or -ir."
            return render(request, 'conjugate.html', {'verb': verb, 'error': errormsg})

    else: 
        return render(request, 'conjugate.html', {})



def get_conjugation_pt(verb):
    conj = {}
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



    

