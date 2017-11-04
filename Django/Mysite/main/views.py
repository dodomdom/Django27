# -*- coding: utf-8 -*- 
from __future__ import unicode_literals

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post

def post_list(request):
	queryset_list = Post.objects.all()#.order_by("-timestamp")
	query = request.GET.get("q")
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
		"pass":"문의"
	}
	#if request.user.is_authenticated():
	#	context = {
	#		"Login":"Login"
	#	}
	#else:
	#	context = {
	#		"Login":"LogOut"
	#	}
	return render(request, "index.html", context)