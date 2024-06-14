from rest_framework import serializers
from mother.models import Mother,Child,Report
from teacher.models import Teacher
from mother.models import *
#تم الاضافة 
class SignUpSerializer(serializers.ModelSerializer):
     class Meta:
        model = User
        fields = ['email','username','password']
     extra_kwargs = {
         'email':{'required':True, 'allow_blank':False},
         'username':{'required':True, 'allow_blank':False},
         'password': {'required':True, 'allow_blank':False},
         
         
     }
class MotherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mother
        fields = ['username','email','phone','address']

class ChildSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['name','age','child_gender','featured_image','state_health']
       # fields = '__all__'
       # exclude = ['teach','mom']

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['username','email','phone','address']

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['learn','activities','attiude','mood','created']
        #تم الاضافة 

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['name','notes']
        #تم الاضافة 
class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['name','meal']
        #تم الاضافة 
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Child
        fields = ['name','location','Important_notes','created']


       