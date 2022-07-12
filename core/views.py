from django.shortcuts import render

# Create your views here.


def Index(request):
    title = "Home"
    return render(request, 'index.html', {'title': title})
