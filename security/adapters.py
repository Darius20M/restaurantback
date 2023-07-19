from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        # Obtiene el enlace de confirmación generado por Allauth
        url = super().get_email_confirmation_url(request, emailconfirmation)

        # Reemplaza "/account-confirm-email/" por "/verification-email/"
        custom_url = url.replace("/account-confirm-email/", "/verify-email/")

        return custom_url