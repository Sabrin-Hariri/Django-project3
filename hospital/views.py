from django.shortcuts import render
from . import views 
from django.views.generic import *
from . import models
from .models import *
from django.urls import reverse_lazy
from .forms import CURDForm
from django.urls import reverse
##############################################################################################################

class HomePage(TemplateView):
     template_name = "home.html"

class Thanks(TemplateView):
     template_name = "thanks.html"


###############

class Create(CreateView):
     model= Patient
     # fields= "__all__"
     success_url=reverse_lazy("hospital:thanks")
     template_name = "create.html"
     form_class=CURDForm
     
#############

class Show(ListView):
     model = Patient
     context_object_name = "patient"
     # queryset= Patient.objects.order_by('age')
     template_name = "show.html"
     form_class=CURDForm


##############

class Detail(DetailView):
     model = Patient
     context_object_name = "patient"
     template_name = "details.html"
     form_class=CURDForm



##############

class Update(UpdateView):
     model = Patient
     # fields= "__all__"
     success_url=reverse_lazy("hospital:thanks")
     template_name = "update.html"
     form_class=CURDForm


##############
class Delete(DeleteView):
     model = Patient
     success_url=reverse_lazy("hospital:show")
     template_name = "delete.html"
     form_class=CURDForm



