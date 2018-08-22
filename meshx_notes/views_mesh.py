from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import FormView
from django.contrib import messages

###

from django.http import HttpResponse
from django.views.generic.base import TemplateView
 
#importing loading from django template 
from django.template import loader


from django.views.generic import TemplateView


#from .forms import valida


class PacientePageView(TemplateView):
	template_name = 'index.html'


	def get_context_data(self, **kwargs):
		context = super(PacientePageView, self).get_context_data(**kwargs)

		#context['data'] =  m['DATA EVOL']

		return context
