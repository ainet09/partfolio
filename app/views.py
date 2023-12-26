from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import TemplateView, CreateView
from .models import *


class HomeTemplateView(TemplateView):
    template_name = 'home.html'

    # override get context date method
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  # first, call super get context data
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        return context


def contact(request):
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        name = request.POST['name']
        send_mail(
            'Contact Form',
            message,
            settings.EMAIL_HOST_USER,
            [email, 'asadbekinomov3@gmail.com'],
            fail_silently=False)
        return render(request, 'home.html')


# class ContactModelView(CreateView):
#     template_name = 'home.html'
#     model = ContactModel
#     fields = ['name', 'email', 'comment']
#     success_url = '/'
#
#     def form_valid(self, form):
#         chat_ids = ['1491929245', '2108885380']
#         name = form.cleaned_data.get('name')
#         email = form.cleaned_data.get('email')
#         comment = form.cleaned_data.get('comment')
#
#         send_mail(name, email, comment, chat_ids)
#         return super().form_valid(form)
