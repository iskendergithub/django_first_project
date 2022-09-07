from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.http import Http404
import random


# Create your views here.

def main_page(request):
    return HttpResponse('Hello, world !')


def test_view(request):
    print(request)
    my_object = Post.objects.all()
    len_of_objects = len(my_object)
    my_random_object_from_db = Post.objects.get(id=random.randint(1, len_of_objects))
    # list_ids = [1, 3, 2]
    # all_items_from_db = Post.objects.filter(id__in=list_ids)
    all_posts = Post.objects.all()
    context = {"my_first_object": my_random_object_from_db,
               "posts": all_posts}

    return render(request, 'posts/test.html', context=context)


def post_detail_view(request, id=None):
    post_object = None
    print(id)
    if id is not None:
        try:
            post_object = Post.objects.get(id=id)
        except:
            raise Http404

    context = {
        "post_object": post_object
    }
    return render(request, 'posts/post_detail.html', context=context)
