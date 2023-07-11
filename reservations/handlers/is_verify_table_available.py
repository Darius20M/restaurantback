from reservations.models import TableModel


def is_verify_table_available(table_id):
    try:
        table = TableModel.objects.get(id=table_id)
        if table.status != 'available':
            return True
        else:
            return False
    except TableModel.DoesNotExist:
        return True
