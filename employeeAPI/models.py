from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class CustomAutoField(models.CharField):
    def __init__(self, prefix, *args, **kwargs):
        self.prefix = prefix
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['prefix'] = self.prefix
        return name, path, args, kwargs

    def pre_save(self, model_instance, add):
        if add:
            last_instance = model_instance._meta.model.objects.last()
            if last_instance:
                last_id = last_instance.regid
                sequence_number = int(last_id.split(self.prefix)[-1]) 
            else:
                sequence_number = 0
            sequence_number += 1
            return f"{self.prefix}{sequence_number:03d}"
        return super().pre_save(model_instance, add)
    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return value


class employee(models.Model):
    GENDER_CHOICES = {
        "M" : "MALE",
        "F" : "FEMALE",
        "Other" : "Other"
    }
    regid = CustomAutoField(prefix='EMP', max_length=6, editable = False)
    name = models.CharField(max_length = 100)
    email = models.EmailField(unique = True)
    age = models.IntegerField()
    gender = models.CharField(max_length = 5,choices = GENDER_CHOICES)
    phoneNo = models.CharField(max_length = 10)
    photo = models.ImageField(upload_to="media/" ,blank=True)
    

    def __str__(self) -> str:
        return self.name
    
class addressDetails(models.Model):
    employee = models.OneToOneField(employee,on_delete = models.CASCADE,related_name = 'addressDetails')
    hno = models.CharField(max_length = 100)
    street = models.CharField(max_length = 100)
    city = models.CharField(max_length = 20)
    state = models.CharField(max_length = 30)
    

    def __str__(self) -> str:
        return self.street

class workExperience(models.Model):
    employee = models.ForeignKey(employee,on_delete=models.CASCADE,related_name = 'workExperience')
    companyName = models.CharField(max_length = 100)
    fromDate = models.DateField()
    toDate = models.DateField()
    address = models.CharField(max_length = 200)
    
    
    def __str__(self) -> str:
        return self.companyName

class qualifications(models.Model):
    employee = models.ForeignKey(employee,on_delete=models.CASCADE,related_name = 'qualifications')
    qualificationName = models.CharField(max_length = 20)
    fromDate = models.DateField()
    toDate = models.DateField()
    percentage = models.FloatField()
    

    def __str__(self) -> str:
        return self.qualificationName

class projects(models.Model):
    employee = models.ForeignKey(employee,on_delete=models.CASCADE,related_name = 'projects')
    title = models.CharField(max_length = 50)
    description = models.TextField()
    

    def __str__(self) -> str:
        return self.title

