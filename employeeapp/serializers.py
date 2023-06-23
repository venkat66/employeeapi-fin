from rest_framework import serializers
from .models import Employee
from django.core.files.uploadedfile import InMemoryUploadedFile
import base64
import io
from PIL import Image
from datetime import datetime

# def decodeImage(data):
#     try:
#         data = base64.b64decode(data.encode('UTF-8'))
#         buf = io.BytesIO(data)
#         img = Image.open(buf)
#         return img
#     except Exception as e:
#         return None

class EmployeeSerializer(serializers.ModelSerializer):
    # photo = serializers.CharField()
    class Meta:
        model = Employee
        fields = (
            'name',
            'email',
            'age',
            'gender',
            'phoneNo',
            'addressDetails',
            'workExperience',
            'qualifications',
            'projects',
            'photo',
        )

    # def create(self, validated_data):
    #     print(validated_data,'validdddd')
    #     print(type(validated_data),'typeeeeee')
    #     img = decodeImage(validated_data['photo'])
    #     img_io = io.BytesIO()
    #     img.save(img_io, format='JPEG')
    #     validated_data['photo'] =  InMemoryUploadedFile(img_io, field_name=None, name=validated_data["name"]+datetime.now()+".jpg", content_type='image/jpeg', size=img_io.tell, charset=None)        
    #     return super().create(validated_data)

class EmployeeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'regid',
            'name',
            'email',
            'age',
            'gender',
            'phoneNo',
            'addressDetails',
            'workExperience',
            'qualifications',
            'projects',
            'photo',
        )

class EmployeeUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'regid',
            'name',
            'email',
            'age',
            'gender',
            'phoneNo',
            'addressDetails',
            'workExperience',
            'qualifications',
            'projects',
            'photo'
        )


