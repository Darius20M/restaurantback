from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings

def send_reservation_email(user, reservation_id, reservation_date, reservation_time, table_name, table_capacity):
    # Configura los detalles del correo electrónico
    sender_email = 'dariusjosedelacruzhilario@gmail.com'
    receiver_email = user.email
    subject = 'Confirmación de reserva'

    # Renderiza el contenido del correo electrónico a partir de una plantilla
    email_template = 'reservation_email.html'  # Nombre de la plantilla HTML para el correo electrónico

    token = default_token_generator.make_token(user)

    # Decodifica el ID de la reserva en base64 para generar el enlace
    reservation_id_b64 = urlsafe_base64_encode(force_bytes(reservation_id))

    # Crea el enlace de confirmación utilizando el token y la ruta de confirmación en tu API
    confirm_url = reverse('confirm_reservation', args=[reservation_id_b64, token])
    redirect_url = f"{settings.BASE_URL}{confirm_url}"

    context = {
        'user': user,
        'reservation_id': reservation_id,
        'reservation_date': reservation_date,
        'reservation_time': reservation_time,
        'table_name': table_name,
        'table_capacity': table_capacity,
        'redirect_url': redirect_url
    }
    html_content = render_to_string(email_template, context)

    # Convierte el contenido HTML a texto sin formato para el correo electrónico
    text_content = strip_tags(html_content)

    # Crea un objeto EmailMultiAlternatives para el correo electrónico
    email = EmailMultiAlternatives(subject, text_content, sender_email, [receiver_email])

    # Agrega el contenido HTML al correo electrónico
    email.attach_alternative(html_content, "text/html")

    # Envía el correo electrónico
    email.send()
