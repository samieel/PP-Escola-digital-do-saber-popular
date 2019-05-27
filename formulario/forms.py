from django import forms
from . import models
from .models import AULA, TEXTO_AULA
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
            'number',
            
            Submit('submit', 'Criar aula', css_class='btn-primary, my-3')
        )
    
    class Meta:
        model = AULA
        fields = ['nome_autor', 'email_autor', 'titulo_aula', 'descricao_aula', 'number']

class CPTexto(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'codigo_aula',
            'topico',
            'texto',

            Submit('submit', 'Criar texto', css_class='btn-primary, my-3')
        )

    class Meta:
        model = TEXTO_AULA
        fields = ['codigo_aula', 'topico', 'texto']