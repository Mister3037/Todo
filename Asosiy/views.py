from django.shortcuts import render, redirect

from .models import *

def home(request):
    content = {
        'rejalar': Reja.objects.all()
    }
    return render(request, 'todo.html', content)

def rejaochir(request, son):
    Reja.objects.get(id=son).delete()
    return redirect("bosh_sahifa")


def rejaqoshish(request):

    if request.method == 'POST':
        Reja.objects.create(
            sarlavha = request.POST['s'],
            matn = request.POST['m'],
            vaqt = request.POST['v'],
            holat = request.POST['h']
        )
        return redirect("bosh_sahifa")
    return render(request, "todo.html",)



