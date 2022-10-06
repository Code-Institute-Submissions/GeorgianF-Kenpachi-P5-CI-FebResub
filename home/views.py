from django.shortcuts import render
from django.contrib import messages
from .forms import GetInTouch
# from django.http import HttpResponseRedirect


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def story(request):
    """ A view to return the story page """
    return render(request, 'home/story.html')


def contact(request):
    """
    A view to return the contact page
    """
    if request.method == 'POST':
        form = GetInTouch(request.POST)
        if form.is_valid():
            form.save()
            form = GetInTouch()
            messages.success(
                request,
                'Message away!')
    else:
        form = GetInTouch()

    context = {'form': form}
    return render(request, 'home/contact.html', context)
