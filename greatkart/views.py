from django.shortcuts import  render  # goi thu vien

def home(request):
    #return HttpResponse("Home page")
    return render(request, 'home.html') # cách gọi template