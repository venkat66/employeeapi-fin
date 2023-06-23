from django.db import models

class Employee(models.Model):
    regid = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    phoneNo = models.CharField(max_length=20)
    addressDetails = models.JSONField()
    workExperience = models.JSONField()
    qualifications = models.JSONField()
    projects = models.JSONField()
    photo = models.ImageField(upload_to='employee_photos', null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.regid:
            last_employee = Employee.objects.order_by('-regid').first()
            if last_employee:
                last_regid = int(last_employee.regid[3:])  # Extract the numeric part
                new_regid = f'EMP{last_regid + 1:03}'  # Increment and format as "EMPXXX"
            else:
                new_regid = 'EMP001'
            self.regid = new_regid
        super().save(*args, **kwargs)
