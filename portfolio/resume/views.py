from django.shortcuts import render

from .models import Experience, Education


def index(request):
    experience_list = Experience.objects.order_by("-start_date")
    education_list = Education.objects.order_by("-start_date")
    context = {"experience_list": experience_list, "education_list": education_list}
    return render(request, "resume/index.html", context)
