from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def story(request):
    """ A view to return the story page """
    return render(request, 'home/story.html')


def contact(request):
    """ A view to return the contact page """
    return render(request, 'home/contact.html')
