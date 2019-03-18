from django.shortcuts import render

# Create your views here.


def home(request):

    args = dict()

    args["page_title"] = "Django Docker"

    return render(request, "home.html", args)
