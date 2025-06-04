from django.shortcuts import render

# Create your views here.


def mainpage_view(request):

    return render(request, 'main.html')

def category_view(request):

    return render(request, 'category.html')