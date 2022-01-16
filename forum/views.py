from django.shortcuts import render

posts = [
    {
        'author': 'Gustav',
        'title': 'Forum Post 1',
        'content': 'First post content',
        'date_posted': 'January 16, 2022'
    },
    {
        'author': 'Daniel',
        'title': 'Forum Post 2',
        'content': 'Second post content',
        'date_posted': 'January 16, 2022'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'forum/home.html', context)


def about(request):
    return render(request, 'forum/about.html', {'title': 'About'})