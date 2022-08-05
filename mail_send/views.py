"""
smtp_app  views
"""
import logging
import smtplib
import ssl
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

import constants


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
        function to post the data
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
        context = ssl.create_default_context()
        try:
            mail_sends = smtplib.SMTP(host, port)
            mail_sends.ehlo()
            mail_sends.starttls(context=context)
            mail_sends.ehlo()
            mail_sends.login(email_from, password)
            data = "Subject:" + subject + "\n" + message + "\n" + username
            mail_sends.sendmail(email_from, email_to, data)
            messages.success(request, constants.ERROR['success']['success'])
            mail_sends.quit()
        except Exception as error:
            logging.error(error)
            messages.error(request, constants.ERROR['error']['error'])
        return JsonResponse({"msg": "true"})
