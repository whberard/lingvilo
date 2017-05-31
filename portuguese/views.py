from django.shortcuts import render

# Create your views here.
def conjugate_pt(request):
    if 'verb' in request.GET and request.GET['verb']:
        cando = False
        verb = request.GET['verb']
        ending = verb[-2:]
        root = verb[:-2]
        if ending == "ar":
            cando = True
            present = {'eu': root + 'o',
                    'tu': root + 'as',
                    'ela': root + 'a',
                    'nós': root + 'amos',
                    'elas': root + 'am',
                    }

            preterit = {'eu': root + 'ei',
                    'tu': root + 'aste',
                    'ela': root + 'ou',
                    'nós': root + 'ámos',
                    'elas': root + 'aram',
                    }

        elif ending == "er":
            cando = True
            present = {'eu': root + 'o',
                    'tu': root + 'es',
                    'ela': root + 'e',
                    'nós': root + 'emos',
                    'elas': root + 'em'
                    }
            preterit = {'eu': root + 'i',
                    'tu': root + 'este',
                    'ela': root + 'eu',
                    'nós': root + 'emos',
                    'elas': root + 'eram',
                    }

        elif ending == "ir":
            cando = True
            present = {'eu': root + 'o',
                    'tu': root + 'es',
                    'ela': root + 'e',
                    'nós': root + 'imos',
                    'elas': root+ 'em'
                    }
            preterit = {'eu': root + 'i',
                    'tu': root + 'iste',
                    'ela': root + 'iu',
                    'nós': root + 'imos',
                    'elas': root + 'iram',
                    }

        if cando:
            return render(request, 'conjugate.html', {'verb': verb, 'ending': ending, 'root': root, 'present': present})
        else: 
            errormsg = "I only know how to conjugate regular verbs that end in -ar, -er, or -ir."
            return render(request, 'conjugate.html', {'verb': verb, 'error': errormsg})

    else: 
        return render(request, 'conjugate.html', {})

