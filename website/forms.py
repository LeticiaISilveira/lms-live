from django import forms


class ContatoForm(forms.Form):

    nome = forms.CharField(max_length=120, label='Nome Completo')
    email = forms.EmailField(label='E-mail')
    texto = forms.CharField(
        label='Mensagem',
        max_length=500,
        widget=forms.Textarea
    )

    def enviar_email(self):
        print('Enviando e-mail!!!!')
