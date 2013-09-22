from django.forms import widgets
from rest_framework import serializers
from octo_nemesis.models import LANGUAGE_CHOICES, STYLE_CHOICES
from octo_nemesis.models.stateset_model import StateSet

class StateSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateSet
        # fields = ('id', 'name', 'description', 'states_wrap')