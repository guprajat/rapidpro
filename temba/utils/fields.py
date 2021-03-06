
from django import forms
from django.forms import widgets


class Select2Field(forms.Field):
    default_error_messages = {}
    widget = widgets.TextInput(attrs={"class": "select2_field", "style": "width:520px"})

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def to_python(self, value):
        return value
