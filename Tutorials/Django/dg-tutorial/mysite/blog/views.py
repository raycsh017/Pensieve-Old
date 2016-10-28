from django.shortcuts import render
from django.utils import timezone
from .models import Post			# Imports Post from models.py in the cur dir

# Create your views here.
def post_list(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	# render post_list.html
	return render(request, 'blog/post_list.html', {'posts': posts})