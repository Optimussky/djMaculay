from msilib.schema import ListView
from django.shortcuts import render
from .models import Resume, Post
#from django.views.generic import ListView
# Create your views here.

# Vistas basadas en funciones
def home(request):
    return render(request,'resume/home.html')

# Vistas basadas en funciones
def about(request):
    resume = Resume.objects.get(pk=1)
    return render(request,'resume/about.html', {'resume':resume})
"""
# Vistas basadas en funciones
def blog(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'resume/blog.html', context)
"""
def blog(request):
    post_objects = Post.objects.all().order_by('-date')
    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        post_objects = post_objects.filter(title__icontains=item_name).order_by('-date')

    return render(request,'resume/blog.html',{'post_objects':post_objects})


"""
class PostListView(ListView):
    model = Post
    template_name = 'resume/blog.html'
    context_object_name = 'posts'

    ordering= ['-date']
"""