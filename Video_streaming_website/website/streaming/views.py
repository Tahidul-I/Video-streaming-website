from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from streaming.models import Item,comment

# Create your views here.

@login_required
def home(request):

    data = Item.objects.all()
    context={
        'data':data,
    }
    return render(request,'video.html',context)

def search(request):
    if request.method=='GET':
        key = request.GET.get('q')
        data = Item.objects.filter(name__icontains=key)
        context={
            'data':data,
        }

        return render(request,'video.html',context)
    

def user_registration(request):

    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass1')
        conf_password = request.POST.get('pass2')
        if password==conf_password:
            data = User.objects.create_user(username,email,password)
            data.save()
            return redirect('user_login')
        else:
            return redirect('user_registration')
    return render(request,'signup.html')

@login_required
def watch(request,id):
    data = Item.objects.get(id = id)
    recommended = Item.objects.all().exclude(id = id)
    comment_data = comment.objects.filter(content_id = id).order_by('-created').all()
    context={
        'data':data,
        'comment_data':comment_data,
        'recommended':recommended,
    }

    if request.method=='POST':
        comments = request.POST.get('comment')
        data_save = comment(
            content = data,
            user = request.user,
            commented = comments,
        )
        data_save.save()
        
        
        return redirect('watch',id = data.id)
    return render(request,'watch.html',context)

def user_login(request):

    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        user = authenticate(username =username, password = password )
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return redirect('user_login')
    return render(request,'user_login.html')

def user_logout(request):
    logout(request)
    return redirect('user_login')

