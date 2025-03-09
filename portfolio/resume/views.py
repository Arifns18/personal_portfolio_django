from django.shortcuts import render

from .models import Experience


def index(request):
    experience_list = Experience.objects.order_by()
    context = {"experience_list": experience_list}
    return render(request, "resume/index.html", context)
