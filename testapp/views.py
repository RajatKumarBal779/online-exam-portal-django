from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from testapp.forms import SignupForm
from django.http import HttpResponseRedirect
# Create your views here.
def home_page_view(request):
    return render(request,'testapp/home.html')

def logout_view(request):
    return render(request,'testapp/logout.html')

def sign_up_view(request):
    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect('/accounts/login')
    return render(request,'testapp/signup.html',{"form":form})

@login_required
def java_exam_view(request):
    if request.method == 'POST':
        score = 0
        ans ={
            'q1':'b',
            'q2':'c',
            'q3':'b',
            'q4':'c',
            'q5':'b'
        }
        for key in ans:
            if request.POST.get(key) == ans[key]:
                score+=1
        return render (request,'testapp/result.html',{'score':score})
    return render(request,'testapp/javaexam.html')

@login_required
def python_exam_view(request):
    if request.method == 'POST':
        score = 0 
        ans = {
            'q1':'b',
            'q2':'c',
            'q3':'d',
            'q4':'c',
            'q5':'c'
        }
        for key in ans:
            if request.POST.get(key) == ans[key]:
                score+=1
        return render (request,'testapp/result.html',{'score':score})
    return render(request,'testapp/python.html')

@login_required
def cpp_view(request):
    if request.method == 'POST':
        score = 0
        ans = {
            'q1':'b',
            'q2':'c',
            'q3':'b',
            'q4':'b',
            'q5':'c'   
        }
        for key in ans:
            if request.POST.get(key) == ans[key]:
                score+=1
        return render (request,'testapp/result.html',{'score':score})
    return render(request,'testapp/cpp.html')
