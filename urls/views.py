from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from django.http import HttpResponse
from urls.models import URLItem
from urls.forms import UrlAddForm
import time
from rq import Queue
from redis import Redis


# Create your views here.
def index(request):
    # return HttpResponse("Страница ввода URL и key_word")
    all_urls = URLItem.objects.all()
    form = UrlAddForm()
    return render(request,'urls/index.html',{"form": form,'urls':all_urls})

class addUrl(View):
    def post(self, request, *args, **kwargs):
        form = UrlAddForm(request.POST)
        if form.is_valid():
            form.save()
            all_urls = URLItem.objects.all()
        return redirect('urls:index')
        # return render(request,'urls/index.html',{"form": form,'urls':all_urls})

    def get(self, request, *args, **kwargs):
        form = URLItem()
        return render(request, "urls/index.html")

def url_create(request):
    if request.method == "POST":
        form = UrlAddForm(request.POST)
        print("url_create")
        if form.is_valid():
            cd = form.cleaned_data
            url_new = cd["url"]
            key_word_new = cd["key_word"]
            t = URLItem(url=url_new, key_word=key_word_new )
            t.save()
            redis_job(cd["url"],cd["key_word"])
            return redirect("index.html")
    else:
        form = UrlAddForm()
    return render(request, "index.html", {"form": form})
# return redirect("index.html")


def redis_job(url,word):
    r = redis.Redis()
    r.publish(url,word)


