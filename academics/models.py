from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    is_hod=models.BooleanField(default=False)
    is_faculty=models.BooleanField(default=False)


class Course(models.Model):
    course_id=models.AutoField(primary_key=True)
    hod=models.CharField(max_length=50)
    faculty=models.CharField(max_length=50)
    academic_year=models.CharField(max_length=50)
    programme=models.CharField(max_length=50)
    class_sem=models.CharField(max_length=50)
    course_code=models.CharField(max_length=50)
    course_name=models.CharField(max_length=50)
    course_type=models.CharField(max_length=50)
    credits=models.CharField(max_length=50) 

    desired_requsite=models.CharField(max_length=50 ,null=True)
    
    lecture=models.CharField(max_length=50 ,null=True)
    tutorial=models.CharField(max_length=50 ,null=True)
    practical=models.CharField(max_length=50 ,null=True)
    interaction=models.CharField(max_length=50 ,null=True)
    
    courseobjective1=models.CharField(max_length=500 ,null=True)
    courseobjective2=models.CharField(max_length=500 ,null=True)
    courseobjective3=models.CharField(max_length=500 ,null=True)
    courseobjective4=models.CharField(max_length=500 ,null=True)
    courseobjective5=models.CharField(max_length=500 ,null=True)
    
    courseoutcome1=models.CharField(max_length=500 ,null=True)
    courseoutcome2=models.CharField(max_length=500 ,null=True)
    courseoutcome3=models.CharField(max_length=500 ,null=True)
    courseoutcome4=models.CharField(max_length=500 ,null=True)
    courseoutcome5=models.CharField(max_length=500 ,null=True)
    
    courseoutcomelevel1=models.CharField(max_length=50 ,null=True)
    courseoutcomelevel2=models.CharField(max_length=50 ,null=True)
    courseoutcomelevel3=models.CharField(max_length=50 ,null=True)
    courseoutcomelevel4=models.CharField(max_length=50 ,null=True)
    courseoutcomelevel5=models.CharField(max_length=50 ,null=True)

    courseoutcomeverb1=models.CharField(max_length=50 ,null=True)
    courseoutcomeverb2=models.CharField(max_length=50 ,null=True)
    courseoutcomeverb3=models.CharField(max_length=50 ,null=True)
    courseoutcomeverb4=models.CharField(max_length=50 ,null=True)
    courseoutcomeverb5=models.CharField(max_length=50 ,null=True)

    module1=models.CharField(max_length=500 ,null=True)
    module2=models.CharField(max_length=500 ,null=True)
    module3=models.CharField(max_length=500 ,null=True)
    module4=models.CharField(max_length=500 ,null=True)
    module5=models.CharField(max_length=500 ,null=True)
    module6=models.CharField(max_length=500 ,null=True)

    modulehour1=models.CharField(max_length=50 ,null=True,default=0)
    modulehour2=models.CharField(max_length=50 ,null=True,default=0)
    modulehour3=models.CharField(max_length=50 ,null=True,default=0)
    modulehour4=models.CharField(max_length=50 ,null=True,default=0)
    modulehour5=models.CharField(max_length=50 ,null=True,default=0)
    modulehour6=models.CharField(max_length=50 ,null=True,default=0)

    labexperiment=models.CharField(max_length=500 ,null=True)

    textbook1=models.CharField(max_length=500 ,null=True)
    textbook2=models.CharField(max_length=500 ,null=True)
    textbook3=models.CharField(max_length=500 ,null=True)
    textbook4=models.CharField(max_length=500 ,null=True)

    reference1=models.CharField(max_length=500 ,null=True)
    reference2=models.CharField(max_length=500 ,null=True)
    reference3=models.CharField(max_length=500 ,null=True)
    reference4=models.CharField(max_length=500 ,null=True)

    usefullink1=models.CharField(max_length=500 ,null=True)
    usefullink2=models.CharField(max_length=500 ,null=True)
    usefullink3=models.CharField(max_length=500 ,null=True)
    usefullink4=models.CharField(max_length=500 ,null=True)

    co1po1=models.CharField(max_length=10 ,null=True,default=0)
    co1po2=models.CharField(max_length=10 ,null=True,default=0)
    co1po3=models.CharField(max_length=10 ,null=True,default=0)
    co1po4=models.CharField(max_length=10 ,null=True,default=0)
    co1po5=models.CharField(max_length=10 ,null=True,default=0)
    co1po6=models.CharField(max_length=10 ,null=True,default=0)
    co1po7=models.CharField(max_length=10 ,null=True,default=0)
    co1po8=models.CharField(max_length=10 ,null=True,default=0)
    co1po9=models.CharField(max_length=10 ,null=True,default=0)
    co1po10=models.CharField(max_length=10 ,null=True,default=0)
    co1po11=models.CharField(max_length=10 ,null=True,default=0)
    co1po12=models.CharField(max_length=10 ,null=True,default=0)
    co1pso1=models.CharField(max_length=10 ,null=True,default=0)
    co1pso2=models.CharField(max_length=10 ,null=True,default=0)
    co1pso3=models.CharField(max_length=10 ,null=True,default=0)


    co2po1=models.CharField(max_length=10 ,null=True,default=0)
    co2po2=models.CharField(max_length=10 ,null=True,default=0)
    co2po3=models.CharField(max_length=10 ,null=True,default=0)
    co2po4=models.CharField(max_length=10 ,null=True,default=0)
    co2po5=models.CharField(max_length=10 ,null=True,default=0)
    co2po6=models.CharField(max_length=10 ,null=True,default=0)
    co2po7=models.CharField(max_length=10 ,null=True,default=0)
    co2po8=models.CharField(max_length=10 ,null=True,default=0)
    co2po9=models.CharField(max_length=10 ,null=True,default=0)
    co2po10=models.CharField(max_length=10 ,null=True,default=0)
    co2po11=models.CharField(max_length=10 ,null=True,default=0)
    co2po12=models.CharField(max_length=10 ,null=True,default=0)
    co2pso1=models.CharField(max_length=10 ,null=True,default=0)
    co2pso2=models.CharField(max_length=10 ,null=True,default=0)
    co2pso3=models.CharField(max_length=10 ,null=True,default=0)

    co3po1=models.CharField(max_length=10 ,null=True,default=0)
    co3po2=models.CharField(max_length=10 ,null=True,default=0)
    co3po3=models.CharField(max_length=10 ,null=True,default=0)
    co3po4=models.CharField(max_length=10 ,null=True,default=0)
    co3po5=models.CharField(max_length=10 ,null=True,default=0)
    co3po6=models.CharField(max_length=10 ,null=True,default=0)
    co3po7=models.CharField(max_length=10 ,null=True,default=0)
    co3po8=models.CharField(max_length=10 ,null=True,default=0)
    co3po9=models.CharField(max_length=10 ,null=True,default=0)
    co3po10=models.CharField(max_length=10 ,null=True,default=0)
    co3po11=models.CharField(max_length=10 ,null=True,default=0)
    co3po12=models.CharField(max_length=10 ,null=True,default=0)
    co3pso1=models.CharField(max_length=10 ,null=True,default=0)
    co3pso2=models.CharField(max_length=10 ,null=True,default=0)
    co3pso3=models.CharField(max_length=10 ,null=True,default=0)

    co4po1=models.CharField(max_length=10 ,null=True,default=0)
    co4po2=models.CharField(max_length=10 ,null=True,default=0)
    co4po3=models.CharField(max_length=10 ,null=True,default=0)
    co4po4=models.CharField(max_length=10 ,null=True,default=0)
    co4po5=models.CharField(max_length=10 ,null=True,default=0)
    co4po6=models.CharField(max_length=10 ,null=True,default=0)
    co4po7=models.CharField(max_length=10 ,null=True,default=0)
    co4po8=models.CharField(max_length=10 ,null=True,default=0)
    co4po9=models.CharField(max_length=10 ,null=True,default=0)
    co4po10=models.CharField(max_length=10 ,null=True,default=0)
    co4po11=models.CharField(max_length=10 ,null=True,default=0)
    co4po12=models.CharField(max_length=10 ,null=True,default=0)
    co4pso1=models.CharField(max_length=10 ,null=True,default=0)
    co4pso2=models.CharField(max_length=10 ,null=True,default=0)
    co4pso3=models.CharField(max_length=10 ,null=True,default=0)

    co5po1=models.CharField(max_length=10 ,null=True,default=0)
    co5po2=models.CharField(max_length=10 ,null=True,default=0)
    co5po3=models.CharField(max_length=10 ,null=True,default=0)
    co5po4=models.CharField(max_length=10 ,null=True,default=0)
    co5po5=models.CharField(max_length=10 ,null=True,default=0)
    co5po6=models.CharField(max_length=10 ,null=True,default=0)
    co5po7=models.CharField(max_length=10 ,null=True,default=0)
    co5po8=models.CharField(max_length=10 ,null=True,default=0)
    co5po9=models.CharField(max_length=10 ,null=True,default=0)
    co5po10=models.CharField(max_length=10 ,null=True,default=0)
    co5po11=models.CharField(max_length=10 ,null=True,default=0)
    co5po12=models.CharField(max_length=10 ,null=True,default=0)
    co5pso1=models.CharField(max_length=10 ,null=True,default=0)
    co5pso2=models.CharField(max_length=10 ,null=True,default=0)
    co5pso3=models.CharField(max_length=10 ,null=True,default=0)
    
    remembert1=models.CharField(max_length=10 ,null=True,default=0)
    remembert2=models.CharField(max_length=10 ,null=True,default=0)
    rememberese=models.CharField(max_length=10 ,null=True,default=0)
    remembertotal=models.CharField(max_length=10 ,null=True,default=0)

    understandt1=models.CharField(max_length=10 ,null=True,default=0)
    understandt2=models.CharField(max_length=10 ,null=True,default=0)
    understandese=models.CharField(max_length=10 ,null=True,default=0)
    understandtotal=models.CharField(max_length=10 ,null=True,default=0)

    analyzet1=models.CharField(max_length=10 ,null=True,default=0)
    analyzet2=models.CharField(max_length=10 ,null=True,default=0)
    analyzeese=models.CharField(max_length=10 ,null=True,default=0)
    analyzetotal=models.CharField(max_length=10 ,null=True,default=0)

    applyt1=models.CharField(max_length=10 ,null=True,default=0)
    applyt2=models.CharField(max_length=10 ,null=True,default=0)
    applyese=models.CharField(max_length=10 ,null=True,default=0)
    applytotal=models.CharField(max_length=10 ,null=True,default=0)

    evaluatet1=models.CharField(max_length=10 ,null=True,default=0)
    evaluatet2=models.CharField(max_length=10 ,null=True,default=0)
    evaluateese=models.CharField(max_length=10 ,null=True,default=0)
    evaluatetotal=models.CharField(max_length=10 ,null=True,default=0)

    createt1=models.CharField(max_length=10 ,null=True,default=0)
    createt2=models.CharField(max_length=10 ,null=True,default=0)
    createese=models.CharField(max_length=10 ,null=True,default=0)
    createtotal=models.CharField(max_length=10 ,null=True,default=0)

    finalsubmit=models.BooleanField(default=False)