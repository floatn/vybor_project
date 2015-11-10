from django.shortcuts import render
from django.views import generic
from .models import Advisor


class AdvisorsPageView(generic.ListView):
    model = Advisor
    template_name = "advisors/index_advisors.html"
    context_object_name = "advisors"
