# -*- coding: utf-8 -*-
from django.forms import ModelForm
#from django import newforms as forms
from django.utils.translation import ugettext_lazy as _

from django import forms
from django.contrib.auth.models import User


#en esta parte se van a inportar los modelos con los que se va a trabajar
from apps.comentarios.models.comentario import Comentario_promocion



class ComentarPromocionForm(forms.ModelForm):
    class Meta:
        model = Comentario_promocion
    