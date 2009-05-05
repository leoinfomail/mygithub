#coding=utf8
import hashlib
import ymgconst
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from ymg.auth import build_ymg_cookie
from ymg.auth import login_required
from ymgweb.user.forms import UserEditForm
from ymgweb.user.forms import UserLoginForm
from ymgweb.user.forms import UserRegForm
from ymgweb.user.models import User

@login_required
def join(request):
    if request.method == 'POST':
        form = UserRegForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user_exist = User.all().filter('email', user.email)
            if user_exist.count():
                return render_to_response('user/join.html', {'form':form, 'error_msg':u'该email已经注册'}, context_instance=RequestContext(request))
            user.password = hashlib.sha1(user.password).hexdigest()
            user.put()
            # auto login
            response = HttpResponseRedirect('/user/join_success/')
            response.set_cookie(ymgconst.YMG_COOKIE, build_ymg_cookie(user.email, user.password))
            return response
    else:
        form = UserRegForm()
    return render_to_response('user/join.html', {'form':form}, context_instance=RequestContext(request))

@login_required
def join_success(request):
    user = request.web_user.get_user()
    ymg_id = user.email
    return render_to_response('user/join_success.html', {'ymg_id': ymg_id}, context_instance=RequestContext(request))

@login_required
def edit(request):
    user = request.web_user.get_user()
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            edit_user = form.save(commit=False)
            #if not edit_user.password == edit_user.password_2:
            #    return render_to_response('user/edit.html', {'form':form, 'error_msg':u'两次输入的密码不同'})
            if not edit_user.password == 'ZW1haWw9YUBjLmNvbTtwYXNzd2':
                user.password = hashlib.sha1(edit_user.password).hexdigest()
            user.nick_name = edit_user.nick_name
            user.birthday = edit_user.birthday
            user.gender = edit_user.gender
            user.career = edit_user.career
            user.residence = edit_user.residence
            user.introduction = edit_user.introduction
            user.put()
            response = render_to_response('user/edit.html', {'form':form, 'success_msg':u'成功修改用户信息'}, context_instance=RequestContext(request))
            response.set_cookie(ymgconst.YMG_COOKIE, build_ymg_cookie(user.email, user.password))
            return response
        return render_to_response('user/edit.html', {'form':form}, context_instance=RequestContext(request))
    # if edit, change the password
    user.password = 'ZW1haWw9YUBjLmNvbTtwYXNzd2'
    form = UserEditForm(instance=user)
    return render_to_response('user/edit.html', {'form':form}, context_instance=RequestContext(request))
    
def login(request):
    redirect_to = request.GET.get('redirect_to', None)
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            exist_user = User.all().filter('email', user.email)
            if exist_user.count() == 1 and exist_user[0].password == hashlib.sha1(user.password).hexdigest():
                response = HttpResponseRedirect('/')
                redirect_to = request.POST.get('redirect_to', None)
                if redirect_to:
                    response = HttpResponseRedirect(redirect_to)
                response.set_cookie(ymgconst.YMG_COOKIE, build_ymg_cookie(exist_user[0].email, exist_user[0].password))
                return response
            else:
                return render_to_response('user/login.html', {'form':form, 'error_msg':u'错误的用户名或密码'},
                    context_instance=RequestContext(request))
    else:
        form = UserLoginForm()
    return render_to_response('user/login.html', {'form':form, 'redirect_to':redirect_to})
    
def logout(request):
    response = HttpResponseRedirect('/')
    try:
        response.delete_cookie(ymgconst.YMG_COOKIE)
    except KeyError:
        pass
    return response
