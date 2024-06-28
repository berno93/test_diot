# main/views.py
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect

from django.conf import settings
from .models import BlogPost
from .forms import BlogPostForm
import openai 
from django.views.decorators.csrf import csrf_exempt


def blog_post_list(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_post_list.html', {'posts': posts})

def blog_post_detail(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    return render(request, 'blog_post_detail.html', {'post': post})

def blog_post_new(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog_post_detail', pk=post.pk)
    else:
        form = BlogPostForm()
    return render(request, 'blog_post_edit.html', {'form': form})

def blog_post_edit(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog_post_detail', pk=post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blog_post_edit.html', {'form': form})

def blog_post_delete(request, pk):
    post = get_object_or_404(BlogPost, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('blog_post_list')
    return render(request, 'main/blog_post_confirm_delete.html', {'post': post})

openai.api_key = settings.OPENAI_API_KEY

def chatbot_index(request):
    return render(request, 'chatbot_index.html')

@csrf_exempt 
def get_chatbot_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        if user_message:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=user_message,
                max_tokens=150
            )
            chatbot_response = response.choices[0].text.strip()
            return JsonResponse({'response': chatbot_response})
        return JsonResponse({'response': 'No message provided'}, status=400)
    return JsonResponse({'response': 'Invalid request'}, status=400)