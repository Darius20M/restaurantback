from rest_framework.exceptions import APIException

class NotAvailableExceptcion(APIException):
    status_code = 420
    default_detail = 'Table not available'
    default_code = 'Not_available'
