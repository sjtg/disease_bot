# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render

from django.views import generic

from django.http.response import HttpResponse



# Create your views here.


class diseaseview(generic.View):
	def get(self, request, *args, **kwargs):
		return HttpResponse("Hello world")
