from django import forms
from django.contrib import admin
from orders.models.orders_model import OrdersModel
from reservations.models.reservation_model import ReservationModel

from reservations.models.tables_model import TableModel
from .models import InvoiceModel

class TuModeloForm(forms.ModelForm):
    Nombre = forms.CharField()
    Apellido = forms.CharField()
    table = forms.ModelChoiceField(queryset=None, required=False)
    place = forms.MultipleChoiceField(
        required=True,
        widget=forms.SelectMultiple(attrs={'style': 'color: black;', 'size': 8}),
        choices=[
            ('A1', '1'),
            ('A2', '2'),
            ('A3', '3'),
            ('A4', '4'),
            ('A5', '5'),
            ('A6', '6'),
            ('A7', '7'),
            ('A8', '8'),
        ]
    )

    class Meta:
        model = InvoiceModel
        fields = ('table', 'place', 'is_individual',)  # Agrega el campo 'table_id' al formulario

    def clean_place(self):
        selected_places = self.cleaned_data.get('place', [])
        if len(selected_places) != len(set(selected_places)):
            raise forms.ValidationError('No se pueden seleccionar puestos duplicados.')
        return selected_places
        
    def __init__(self, *args, **kwargs):
        super(TuModeloForm, self).__init__(*args, **kwargs)

        # Filtrar las mesas reservadas y asignar el queryset al campo table_id
        tables_reservadas = TableModel.objects.filter(status='reserved')
        self.fields['table'].queryset = tables_reservadas

        table_id = self.initial.get('table') if self.instance.pk else None

        # Filtrar los lugares (places) relacionados con las reservas de la table_id seleccionada
        if table_id:
            places_reservados = ReservationModel.objects.filter(table_id=table_id).values_list('place', flat=True).distinct()
            self.fields['place'].queryset = TableModel.objects.filter(place__in=places_reservados)
        else:
            self.fields['place'].queryset = TableModel.objects.none()

        
        
    