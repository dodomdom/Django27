# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import PostForm

def post_main(request):
	query = request.GET.get("q")
	if not request.user.is_staff or not request.user.is_superuser:
		queryset_list = Post.objects.filter(~Q(classify__icontains = "문의"))
	else :
		queryset_list = Post.objects.all()
	if query:
		queryset_list = queryset_list.filter(
				Q(classify__icontains=query)|
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()

	paginator = Paginator(queryset_list, 30) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset,
		"page_request_var": page_request_var,
		"main":"메인",
		"computer":"컴퓨터",
		"chatting":"잡담",
		"drama":"드라마",
		"movie":"영화",
		"game":"게임",
		"suggest":"문의",
		"mylog":"내가쓴글",
		"value":"메인",
	}
	return render(request, "index.html", context)


def post_chat(request):
	query = request.GET.get("q")
	queryset_list = Post.objects.filter(Q(classify__icontains = "잡담"))
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset,
		"page_request_var": page_request_var,
		"main":"메인",
		"computer":"컴퓨터",
		"chatting":"잡담",
		"drama":"드라마",
		"movie":"영화",
		"game":"게임",
		"suggest":"문의",
		"mylog":"내가쓴글",
		"value":"잡담",
	}
	return render(request, "index.html", context)


def post_computer(request):
	query = request.GET.get("q")
	queryset_list = Post.objects.filter(Q(classify__icontains = "컴퓨터"))
	
	if query:
		queryset_list = queryset_list.filter(
				Q(classify__icontains=query_c)&
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()

	paginator = Paginator(queryset_list, 25) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset,
		"page_request_var": page_request_var,
		"main":"메인",
		"computer":"컴퓨터",
		"chatting":"잡담",
		"drama":"드라마",
		"movie":"영화",
		"game":"게임",
		"suggest":"문의",
		"mylog":"내가쓴글",
		"value":"컴퓨터",
	}
	
	return render(request, "index.html", context)


def post_movie(request):
	query = request.GET.get("q")
	queryset_list = Post.objects.filter(Q(classify__icontains = "영화"))
	query_c = "영화"
	if query:
		queryset_list = queryset_list.filter(
				Q(classify__icontains=query_c)&
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()

	paginator = Paginator(queryset_list, 25) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset,
		"page_request_var": page_request_var,
		"main":"메인",
		"computer":"컴퓨터",
		"chatting":"잡담",
		"drama":"드라마",
		"movie":"영화",
		"game":"게임",
		"suggest":"문의",
		"mylog":"내가쓴글",
		"value":"영화",
	}
	return render(request, "index.html", context)

def post_game(request):
	query = request.GET.get("q")
	queryset_list = Post.objects.filter(Q(classify__icontains = "게임"))
	query_c = "게임"
	if query:
		queryset_list = queryset_list.filter(
				Q(classify__icontains=query_c)&
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()

	paginator = Paginator(queryset_list, 25) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset,
		"page_request_var": page_request_var,
		"main":"메인",
		"computer":"컴퓨터",
		"chatting":"잡담",
		"drama":"드라마",
		"movie":"영화",
		"game":"게임",
		"suggest":"문의",
		"mylog":"내가쓴글",
		"value":"게임",
	}
	return render(request, "form.html", context)

def post_drama(request):
	query = request.GET.get("q")
	queryset_list = Post.objects.filter(Q(classify__icontains = "드라마"))
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)|
				Q(user__first_name__icontains=query) |
				Q(user__last_name__icontains=query)
				).distinct()

	paginator = Paginator(queryset_list, 25) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset,
		"page_request_var": page_request_var,
		"main":"메인",
		"computer":"컴퓨터",
		"chatting":"잡담",
		"drama":"드라마",
		"movie":"영화",
		"game":"게임",
		"suggest":"문의",
		"mylog":"내가쓴글",
		"value":"드라마",
	}
	return render(request, "form.html", context)

def post_mylog(request):
	query = request.GET.get("q")
	queryset_list = Post.objects.filter(Q(user=request.user))
	if query:
		queryset_list = queryset_list.filter(
				Q(title__icontains=query)|
				Q(content__icontains=query)
				).distinct()

	paginator = Paginator(queryset_list, 25) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		queryset = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		queryset = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		queryset = paginator.page(paginator.num_pages)
	context = {
		"object_list": queryset,
		"page_request_var": page_request_var,
		"main":"메인",
		"computer":"컴퓨터",
		"chatting":"잡담",
		"drama":"드라마",
		"movie":"영화",
		"game":"게임",
		"suggest":"문의",
		"mylog":"내가쓴글",
		"value":"내가쓴글",
	}
	return render(request, "index.html", context)

def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "저장되었습니다.")
		return HttpResponseRedirect(instance.get_absolute_url())
	context = {
		"form":form,
	}
	return render(request, "post_form.html", context)


def post_detail(request, id=None):
	instance = get_object_or_404(Post, id=id)
	initial_data = {
			"content_type":instance.get_content_type,
			"object_id":instance.id
	}

	context = {
		"title": instance.title,
		"Login": "Login",
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

def post_delete(request, id=None):
	instance = get_object_or_404(Post, id=id)
	if (request.user == instance.user) or request.user.is_staff or request.user.is_superuser:
		instance.delete()
		messages.success(request, "제거되었습니다.")
		return redirect("main:pmain")
	else:
		return redirect("/error")
	



	