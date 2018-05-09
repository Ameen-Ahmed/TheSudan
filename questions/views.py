from django.shortcuts import render
from .forms import EmailPostForm
from django.core.mail import send_mail


def index(request):
    sent = False
    if request.method == "POST":
        # Form was submitted
        form = EmailPostForm(request.POST)
        sent = True

        # Capture all the valid data from each field into a dictionary
        cd = form.cleaned_data

        subject = '{} ({}) asks '.format(cd['name'], cd['email'])
        message = '?????????'.format(cd['email_body'])
        send_mail(subject, message, 'admin@mysite.com', [cd['to']])

    else:
        form = EmailPostForm()

    return render(request, 'questions/index.html', {'form':form,
                                                    'sent':sent})