from blog.models import Post 
from django.views.generic import ListView, DetailView
#from django.core.context_processors import csrf

class PostsListView(ListView): # представление в виде списка
    model = Post                   # модель для представления 

class PostDetailView(DetailView): # детализированное представление модели
	model = Post
	#c.update(csrf(request))   