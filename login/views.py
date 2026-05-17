from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from requests import session
# Create your views here.
"""def login(request):
    response = HttpResponse("Login Page")
    response.set_cookie('username', 'john_doe',max_age=120) 
    request.session['username']='rounak'
    return response"""
class login(View):
    def get(self,request):
        username= request.session.get('name')
        if username:
            return HttpResponseRedirect('/main_page/')
        else:
            return render(request,'logpage/login_page.html')
    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.session['name']=username
        request.session['pass']=password
        return HttpResponseRedirect('/main_page/')
    
def getcookie(request):
    username= request.COOKIES.get('username','noname')
    username2 = request.session.get('username','noname')
    return HttpResponse(f"Username: {username} (from cookie), {username2} (from session)")
def logout(request):
    if request.method == 'POST':
        request.session.flush()
        return HttpResponseRedirect('/login/')
def main_page(request):
    username = request.session.get('name')
    if username:
        return render(request,'logpage/main_page.html',{'username': username})
    else:
        return HttpResponseRedirect('/login/')