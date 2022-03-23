from django.forms import ModelForm
from .models import Comentario
import requests


class FormComentario(ModelForm):
    def clean(self):
        raw_data = self.data
        recaptcha_response = raw_data.get('g-recaptcha-response')

        recaptcha_request = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data = {
                'secret': '6LenNf0eAAAAAKeHUr5pljh1gs3dKqBSD0_fSR4E',
                'response': recaptcha_response,
            }
        )
        recaptcha_result = recaptcha_request.json()

        if not recaptcha_result.get('success'):
            'comentario',
            'Desculpe Mr. Robot, você não passou na validação.'

        cleaned_data = self.cleaned_data
        nome = cleaned_data.get('nome_comentario')
        email = cleaned_data.get('email_comentario')
        comentario = cleaned_data.get('comentario')

        if len(nome) < 5:
            self.add_error(
                'nome_comentario',
                'Nome precisa ter mais de 5 caracteres'
            )


    class Meta:
        model = Comentario
        fields = ('nome_comentario', 'email_comentario', 'comentario')