from django.forms import widgets
from rest_framework import serializers
from octo_nemesis.models import StateSet, LANGUAGE_CHOICES, STYLE_CHOICES

class StateSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateSet
        # fields = ('id', 'name', 'description', 'states_wrap')