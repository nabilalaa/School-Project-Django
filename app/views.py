from django.shortcuts import render
from .models import *
from .form import ResultForm


def test(request):

    num = request.POST.get("number")

    context = {
        "results": Result.objects.filter(number=num),
        "form": ResultForm

    }
    return render(request, "index.html", context)