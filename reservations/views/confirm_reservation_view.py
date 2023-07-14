from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.http import HttpResponseBadRequest, HttpResponse

from reservations.models import ReservationModel


def confirm_reservation_view(request, reservation_id_b64, token):
    try:
        reservation_id = force_str(urlsafe_base64_decode(reservation_id_b64))
        # Obtiene el modelo de usuario personalizado (si se está utilizando)
        User = get_user_model()
        # Obtén el objeto User correspondiente al ID de la reserva
        Re = ReservationModel.objects.get(pk=reservation_id)
        user = Re.user

        if default_token_generator.check_token(user, token):

            reservation = ReservationModel.objects.get(id=reservation_id)
            reservation.status = 'Confirmed'
            reservation.save()
            # Retorna una respuesta exitosa
            html_content = render_to_string('confirmation_email.html')

            return HttpResponse(html_content)
        else:
            # El token no es válido, retorna una respuesta de error
            return HttpResponseBadRequest("Token de confirmación no válido.")
    except (TypeError, ValueError, OverflowError, ReservationModel.DoesNotExist):
        # Ocurrió un error al decodificar el ID o al obtener la reserva
        return HttpResponseBadRequest("Error al confirmar la reserva.")