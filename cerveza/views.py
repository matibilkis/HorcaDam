from django.shortcuts import render

def index(request):
    cervecerias = ['anteares','amsterdam']
    template_name="index.html"
    return render(
        request,
        'index.html',
        context={'cervecerias':cervecerias},
    )
