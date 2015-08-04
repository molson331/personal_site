from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):

	template_name = "index.html"

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		return context


class EventView(TemplateView):

	template_name = "event.html"

	def get_context_data(self, **kwargs):
		context = super(EventView, self).get_context_data(**kwargs)
		return context


class ResumeView(TemplateView):

	template_name = "resume.html"

	def get_context_data(self, **kwargs):
		context = super(ResumeView, self).get_context_data(**kwargs)
		return context
