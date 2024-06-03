from rest_framework import serializers
from .models import *

class AddressDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = addressDetails
        fields = ['id','hno','street','city','state']

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = workExperience
        fields = ['id','companyName','fromDate','toDate','address']

class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = qualifications
        fields = ['id','qualificationName','fromDate','toDate','percentage']

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = projects
        fields = ['id','title','description']

class EmployeeSerializer(serializers.ModelSerializer):
    addressDetails = AddressDetailsSerializer()
    workExperience = WorkExperienceSerializer(many=True)
    qualifications = QualificationSerializer(many = True)
    projects = ProjectsSerializer(many = True)
    class Meta:
        model = employee
        fields = ['id','regid','name','email','age','gender','phoneNo','addressDetails','workExperience','qualifications','projects']

    def create(self, validated_data):
        """
    Method to create a new employee instance along with related data.

    Args:
        validated_data (dict): Validated data for creating the employee instance and related models.
        
    Returns:
        employeData (Employee): Created employee instance.
    """
        addressDetailsData = validated_data.pop('addressDetails')
        qualificationsData = validated_data.pop('qualifications')
        projectsData = validated_data.pop('projects')
        workExperienceData = validated_data.pop('workExperience')

        employeData = employee.objects.create(**validated_data)

        addressDetails.objects.create(employee = employeData,**addressDetailsData)

        for qualificationData in qualificationsData:
            qualifications.objects.create(employee = employeData,**qualificationData)

        for project_data in projectsData:
            projects.objects.create(employee = employeData,**project_data)

        for workExperienceDataItem in workExperienceData:
            workExperience.objects.create(employee=employeData,**workExperienceDataItem)
        
        return employeData
    
    def update(self, instance, validated_data):
        """
    Method to update an existing employee instance along with related data.

    Args:
        instance (Employee): Existing employee instance to be updated.
        validated_data (dict): Validated data for updating the employee instance and related models.

    Returns:
        instance (Employee): Updated employee instance.
        """
        addressDetailsData = validated_data.pop('addressDetails')
        qualificationsData = validated_data.pop('qualifications')
        projectsData = validated_data.pop('projects')
        workExperienceData = validated_data.pop('workExperience')

        instance.name = validated_data.get('name',instance.name)
        instance.email = validated_data.get('email',instance.email)
        instance.age = validated_data.get('age',instance.age)
        instance.gender = validated_data.get('gender',instance.gender)
        instance.phoneNo = validated_data.get('phoneNo',instance.phoneNo)
        instance.save()

        addressDetailsInstance = instance.addressDetails
        addressDetailsInstance.hno = addressDetailsData.get('hno',addressDetailsInstance.hno)
        addressDetailsInstance.street = addressDetailsData.get('street',addressDetailsInstance.street)
        addressDetailsInstance.city = addressDetailsData.get('city',addressDetailsInstance.city)
        addressDetailsInstance.state = addressDetailsData.get('state',addressDetailsInstance.state)

        qualificationsInstances = list(instance.qualifications.all())
        print(qualificationsInstances)
        for qualificationData in qualificationsData:
            qualificationsInstance = qualificationsInstances.pop(0)
            qualificationsInstance.qualificationName = qualificationData.get('qualificationName',qualificationsInstance.qualificationName)
            qualificationsInstance.fromDate = qualificationData.get('fromDate',qualificationsInstance.fromDate)
            qualificationsInstance.toDate = qualificationData.get('toDate',qualificationsInstance.toDate)
            qualificationsInstance.percentage = qualificationData.get('percentage',qualificationsInstance.percentage)
            qualificationsInstance.save()
        
        workExperienceInstances = list(instance.workExperience.all())
        for workExperienceDataItem in workExperienceData:
            workExperienceInstance = workExperienceInstances.pop(0)
            workExperienceInstance.companyName = workExperienceDataItem.get('companyName',workExperienceInstance.companyName)
            workExperienceInstance.fromDate = workExperienceDataItem.get('fromDate',workExperienceInstance.fromDate)
            workExperienceInstance.toDate = workExperienceDataItem.get('toDate',workExperienceInstance.toDate)
            workExperienceInstance.address = workExperienceDataItem.get('address',workExperienceInstance.address)
            workExperienceInstance.save()

        projectsDataInstances = list(instance.projects.all())
        for projectsDataItem in projectsData:
            projectsDataInstance = projectsDataInstances.pop(0)
            projectsDataInstance.title = projectsDataItem.get('title',projectsDataInstance.title)
            projectsDataInstance.description = projectsDataItem.get('description',projectsDataInstance.description)
            projectsDataInstance.save()

        return instance
