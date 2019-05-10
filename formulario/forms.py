from django import forms
from . import models
from .models import AULA
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit

class CAtividade(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'nome_autor',
            'email_autor',
            'titulo_aula',
            'descricao_aula',
            
            Submit('submit', 'Criar aula', css_class='btn-primary, my-3')
        )
    
    class Meta:
        model = AULA
        fields = ['nome_autor', 'email_autor', 'titulo_aula', 'descricao_aula']
        