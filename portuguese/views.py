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

        elif ending == "er":
            cando = True
            present = {'eu': root + 'o',
                    'tu': root + 'es',
                    'ela': root + 'e',
                    'nós': root + 'emos',
                    'elas': root + 'em'
                    }

        elif ending == "ir":
            cando = True
            present = {'eu': root + 'o',
                    'tu': root + 'es',
                    'ela': root + 'e',
                    'nós': root + 'imos',
                    'elas': root+ 'em'
                    }

        if cando:
            return render(request, 'conjugate.html', {'verb': verb, 'ending': ending, 'root': root, 'present': present})
        else: 
            errormsg = "I only know how to conjugate regular verbs that end in -ar, -er, or -ir."
            return render(request, 'conjugate.html', {'verb': verb, 'error': errormsg})

    else: 
        return render(request, 'conjugate.html', {})

