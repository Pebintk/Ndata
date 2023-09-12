from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'M Pendar Bintang K',
        'class': 'PBP E',
        "app" : "Ndata",
        'npm' : '2206083174',
    }

    return render(request, "main.html", context)