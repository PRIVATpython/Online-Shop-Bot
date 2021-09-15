from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView


class AdminPageView(TemplateView):
    template_name = "index.html"
