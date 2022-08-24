from rest_framework import serializers
from .models import Project, Technologie
from .validations import *


class TechnologieSerializar(serializers.ModelSerializer):
  type_technologie = serializers.SerializerMethodField()
  def get_type_technologie(self, obj):
    return obj.get_type_technologie_display() 
  class Meta:
    model = Technologie
    fields = '__all__'

  
  def validate(self, data):
    if not validate_name(data['name']):
      raise serializers.ValidationError({'name': 'the name informed is not valid'})
    return data

class ProjectSerializer(serializers.ModelSerializer):
  technologie = serializers.ReadOnlyField(source='technologie.name')
  class Meta:
    model = Project
    fields = '__all__'
  def validate(self, data):
    if not validate_name(data['name']):
      raise serializers.ValidationError({'name': 'the name informed is not valid'})
    if not validate_date(data['date_init'], data['date_end']):
      raise serializers.ValidationError({'date_init':'date is not valid'})
    return data

class ProjectByTechnologieSerializer(serializers.ModelSerializer):
  technologie = serializers.ReadOnlyField(source='technologie.name')
  print(serializers.ModelSerializer)
  class Meta:
    model = Project
    fields =['name', 'technologie']