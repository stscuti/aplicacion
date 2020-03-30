from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import FormStepOne, FormStepTwo, SolicitudesStep1_Form, SolicitudesStep1b_Form, SolicitudesStep2_Form
from formtools.wizard.views import SessionWizardView
from django.contrib.auth.mixins import LoginRequiredMixin


#Para API
from rest_framework import generics
from .models import Solicitud143_Step1
from .serializers import SolicitudesSerializer


# Create your views here.
class FormWizardView(LoginRequiredMixin, SessionWizardView):
    template_name = "solicitudes.html"
    form_list = [SolicitudesStep1_Form, SolicitudesStep1b_Form, SolicitudesStep2_Form]

    #def done(self, form_list, **kwargs):
    def done(self, form_list, form_dict, **kwargs):
    	#SolicitudesStep1 = SolicitudesStep1_Form.save(commit=False)
    	#SolicitudesStep1.save()
    	#[form.save(commit=True) for form in form_list]
    	for form in form_list:
    		form.save(commit=False)
    		form.instance.uc = self.request.user
    		form.save()
    	#SolicitudesStep1b = SolicitudesStep1b_Form.save(commit=False)
    	#SolicitudesStep1b.user = self.request.user
    	#SolicitudesStep1b.SolicitudesStep1 = SolicitudesStep1
    	#SolicitudesStep1b.save()

    	return render(self.request, 'solicitud_ok.html', {
    		'form_data': [form.cleaned_data for form in form_list],
		})


class SolicitudesList(generics.ListCreateAPIView):
	queryset = Solicitud143_Step1.objects.all()
	serializer_class = SolicitudesSerializer

	def get_object(self):
		queryset = self.get_queryset()
		obj = get_object_or_404(
			queryset,
			pk = self.kwargs['pk'],
		)
		return obj