from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def otherPage(request):
    return HttpResponse("<h1>Hello, world.  You're at another page.</h1>"
    "<h2> This is how you do line breaks in python.</h2><br>Or this if is "
    " shorter I suppose.")