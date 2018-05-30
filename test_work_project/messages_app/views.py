from django.shortcuts import render

# Create your views here.

def empty_page(request):
    return render(request, 'messages_app/empty_page.html', {})
