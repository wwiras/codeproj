
from django.urls import reverse_lazy
from django.core import serializers
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView, ListView, DetailView
from post.models import Post
from .forms import PostForm
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponse
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.db.models import Count, Sum, Q, Case, Value, When, IntegerField
from datetime import date
# from django.db.models import CharField, Case, Value, When, Count
import re, json

class HomeView(TemplateView):
    template_name = "post/post_home.html"

# FlashSet JSON list filtering 
class PostListJson(BaseDatatableView):
    order_columns = ['name', 'content','pk','link']

    def get_initial_queryset(self):
        # return queryset used as base for futher sorting/filtering
        return Post.objects.filter(date_exp__gte=date.today())

    def filter_queryset(self, qs):
        # use request parameters to filter queryset

        # Getting advanced filtering indicators for dataTables 1.10.13
        search = self.request.GET.get(u'search[value]', "")
        iSortCol_0 = self.request.GET.get(u'order[0][column]', "") # Column number 0,1,2,3,4
        sSortDir_0 = self.request.GET.get(u'order[0][dir]', "") # asc, desc

        # Choose which column to sort
        if iSortCol_0 == '1':
          sortcol = 'name'
        else:
          sortcol = 'content'

        # Choose which sorting direction : asc or desc
        if sSortDir_0 == 'asc':
          sortdir = ''
        else:
          sortdir = '-'

        # Filtering if search value is key-in
        if search:
          # Initial Q parameter value
          qs_params = None

          # Filtering other fields
          q = Q(name__icontains=search)|Q(content__icontains=search)
          qs_params = qs_params | q if qs_params else q
   
          # Completed Q queryset
          # print qs_params
          qs = qs.filter(qs_params)

        return qs.order_by(sortdir + sortcol)

    def prepare_results(self, qs):
        # prepare list with output column data
        json_data = []
        for item in qs:
          json_data.append([
              item.name,
              item.content,
              item.pk,
              reverse_lazy('post_home')
          ])
        return json_data

def post_new(request):
    if request.method == "POST":
        # form = LetterForm(request.POST)
        form = PostForm(request.POST)
        if form.is_valid():
            newpost = form.save(commit=False)
            newpost.save()
            messages.success(request, "New Post : " + str(newpost.name) + " has been created ! ")
            return redirect(reverse_lazy('post_home'))
    else:
        form = PostForm()
    return render(request, 'post/post_new.html', {'form': form})

def post_edit(request,pk):
    editpost = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,instance=editpost)
        if form.is_valid():
            editpost = form.save(commit=False)
            editpost.save()
            messages.success(request, "Post : " + str(editpost.name) + " has been updated! ")
            # return redirect(reverse_lazy('letter_detail',kwargs={'pk': editletter.pk }))
            return redirect(reverse_lazy('post_home'))
    else:
        editpost.date_exp = date.strftime(editpost.date_exp, "%d-%m-%Y")
        form = PostForm(instance=editpost)
    return render(request, 'post/post_edit.html', {'form': form})

def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post/post_detail.html', {'post': post})


def post_remove(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        if request.POST.get("submit_yes", ""):
            post.delete()
            messages.success(request, "Post : " + str(post.name) + " has been removed! ")
            return redirect(reverse_lazy('post_home'))
    return render(request, 'post/post_confirm_delete.html', {'post': post, 'pk':pk})

