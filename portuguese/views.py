from django.shortcuts import render

# Create your views here.
def conjugate_pt(request):
    if 'verb' in request.GET and request.GET['verb']:
        verb = request.GET['verb']
        ending = verb[-2:]
        root = verb[:-2]
        present = {'eu': root + 'o',
                'tu': root + 'as',
                'ela': root + 'a',
                'nós': root + 'amos',
                'vós': root + 'ais',
                }
        return render(request, 'conjugate.html', {'verb': verb, 'ending': ending, 'root': root, 'present': present})

    return render(request, 'conjugate.html', {})

