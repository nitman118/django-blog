from django.shortcuts import render
# from django.http import HttpResponse - not used anymore since we use render

posts = [
    {'author':'Nitish',
     'content':'Post Content 1',
     'date_posted':'August 11'},

     {'author':'Bhooms',
     'content':'Post Content 2',
     'date_posted':'August 12'}

    ]



# Create your views here.
def home(request):
    context={
        'posts':posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title':'About'})
