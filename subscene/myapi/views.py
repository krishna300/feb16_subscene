from django.shortcuts import render

# Create your views here.
from .models import Post
from .to_data import to_data

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

class PostListView(ListView):
    model = Post
    template_name = 'myapi/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'posts'


def detail(request,post_id):
    post=Post.objects.get(pk=post_id)
    entitle=str(post.document)
    data1=to_data(entitle)
    dr=[i[2:]for i in data1]
    index1=range(1,(len(dr)+1))
    context={
        "data1":dr,
        "entitle":entitle,
		"post":post,
        "mapped":zip(dr,index1),
	}
    return render(request,'myapi/test.html',context)


