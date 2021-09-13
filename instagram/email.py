from email.mime import text
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
def  register_email(name,recipient):
 
 subject='Registration Email'
 sender='izzieapptest@gmail.com'
 text_content=render_to_string('templates/register.html',{'name':name})
 html_content=render_to_string('templates/register.txt',{'name':name})
 message=EmailMultiAlternatives(subject,text_content,sender,[recipient])
 message.attach_alternative(html_content,'text/html')
 message.send()