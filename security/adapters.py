from allauth.account.adapter import DefaultAccountAdapter
from allauth.account.models import EmailConfirmation
from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    
    def send_mail(self, template_prefix, email, context, subject=None):
        context['EMAIL_TO'] = email
        msg = self.render_mail(template_prefix, email, context)
        subject = "Bienvenido a Delicias a la Brasa"

        if subject:
            msg.subject = subject

        msg.send()