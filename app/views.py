from django.shortcuts import render
from .models import *
from .form import ResultForm
from django.contrib import messages


def test(request):
    num = request.POST.get("number")
    if request.POST:
        if not Result.objects.filter(number=num):
            print("d")
            messages.error(request, "not found")

    context = {
        "results": Result.objects.filter(number=num),
        "form": ResultForm

    }
    return render(request, "index.html", context)