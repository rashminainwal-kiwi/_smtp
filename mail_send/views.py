"""
smtp_app  views
"""
import logging
import smtplib
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


class Sender(View):
    """
    create a class for sending mail dynamically
    """

    @staticmethod
    def get(request):
        """
        function to render home template
        :param request: wsgi request
        :return: home.html
        """
        return render(request, 'home.html')

    @staticmethod
    def post(request):
        """
        function to post and get the data at once
        function to render home template
        :param request: wsgi request
        :return: home.html
        """

        port = request.POST.get('port')
        username = request.POST.get('username')
        password = request.POST.get('password')
        email_from = request.POST.get('email_from')
        email_to = request.POST.get('email_to')
        host = request.POST.get('host')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        try:
            mail_sends = smtplib.SMTP(host, port)
            mail_sends.ehlo()
            mail_sends.starttls()
            mail_sends.ehlo()
            mail_sends.login(email_from, password)
            message = 'Subject: {}\n\n{}'.format(subject, message, username)
            mail_sends.sendmail(email_from, email_to, message)
            messages.success(request, 'mail sent Successfully.')
            mail_sends.quit()

        except Exception as error:
            logging.error(error)
            messages.error(request, 'Invalid credentials ')
            # messages.error(request, form.errors)
        return JsonResponse({"msg": "true"})

            # return render(request, 'home.html')
