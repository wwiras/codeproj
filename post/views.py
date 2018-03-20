
# Create your views here.
from django.urls import reverse_lazy
from django.core import serializers
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, DetailView
# from flashcard.models import FlashSet, FlashCard, Category
# from quiz.models import Revision
from post.models import Post
from django.contrib import messages
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponse
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Count, Sum, Q, Case, Value, When, IntegerField
# from django.db.models import CharField, Case, Value, When, Count
import re, json

class HomeView(TemplateView):
    template_name = "post/home.html"