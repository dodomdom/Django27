# -*- coding: utf-8 -*- 
from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,
	)
from django.shortcuts import render, redirect

from .forms import UserLoginForm, UserRegisterForm

def login_view(request):
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username=form.cleaned_data.get("username")
		password=form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		return redirect("/")
	context = {
		"form" : form,
		"title" : "Sign In",
		"subtitle": "Login to our site",
		"title2": "Welcome My Site",
		"subtitle2": "Enter your username, password",
		"controll" : '처음이십니까??',
		"controll_url" : "/register/",
	}

	return render(request, "accounts.html", context)

def register_view(request):
	print(request.user.is_authenticated())
	title = "Register"
	form = UserRegisterForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		return redirect("/")		
	context = {
		"form" : form,
		"title" : "Register",
		"subtitle": "Welcome My Site",
		"title2": "Register your account",
		"subtitle2": "Enter your Register",
		"controll" : '로그인',
		"controll_url" : "/login",
	}
	return render(request, "accounts.html", context)

def logout_view(request):
	logout(request)
	return redirect("/")
