from django.shortcuts import render

# Create your views here.
def conjugate_pt(request):
    return render(request, 'conjugate.html', {})

