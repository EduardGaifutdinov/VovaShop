from django.core.mail import EmailMessage
from django.shortcuts import render


def index(request):
    msg = EmailMessage(request.POST.get('select'),
                       'Here is the message.', to=['razor3538@mail.ru'])
    msg.send()
    return render(request, 'base.html', {})
