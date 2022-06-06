from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import models
from .models import Course,Account


# Create your views here.
def loginuser(request):
    if request.method=="POST":
        username= request.POST['username']
        password=request.POST['password']

        user = authenticate(username=username,password=password)
        
        if user is not None and user.account.is_faculty:
            login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect('faculty')

        elif user is not None and user.account.is_hod:
            login(request,user)
            messages.success(request,"Logged in successfully")
            return redirect('hod')
        else:
            messages.error(request,"Invalid User credentials ")
            return redirect('loginuser')
    
    return render(request,'login.html')

def logoutuser(request):
    if request.user.is_anonymous:
        return redirect('loginuser')
        
    logout(request)
    messages.success(request,"Logged out successfully")
    return redirect('loginuser')


def faculty(request):
    if request.user.account.is_faculty is not True:
        return redirect('loginuser')

    courses=Course.objects.filter(faculty=request.user.username)
    context={'courses':courses}
    return render(request,'faculty.html',context)


def hod(request):
    if request.user.account.is_hod is not True:
        return redirect('loginuser')
    
    courses=Course.objects.filter(hod=request.user.username)
    context={'courses':courses}
    return render(request,'hod.html',context)



def addcoursecontent(request):
    if request.user.account.is_faculty is not True:
        return redirect('loginuser')
    
    if request.method=="POST":
        
            

        if "save" in request.POST:
            course_id=request.POST["cid"]
            course=Course.objects.filter(course_id=course_id)
            course=course[0]

            ctype=course.course_type

            dreq=request.POST['dreq']

            courseobjective1=request.POST['courseobjective1']
            courseobjective2=request.POST['courseobjective2']
            courseobjective3=request.POST['courseobjective3']
            courseobjective4=request.POST['courseobjective4']
            courseobjective5=request.POST['courseobjective5']
    
            courseoutcome1=request.POST['courseoutcome1']
            courseoutcome2=request.POST['courseoutcome2']
            courseoutcome3=request.POST['courseoutcome3']
            courseoutcome4=request.POST['courseoutcome4']
            courseoutcome5=request.POST['courseoutcome5']
    
            courseoutcomelevel1=request.POST['co1level']
            courseoutcomelevel2=request.POST['co2level']
            courseoutcomelevel3=request.POST['co3level']
            courseoutcomelevel4=request.POST['co4level']
            courseoutcomelevel5=request.POST['co5level']

            courseoutcomeverb1=request.POST['co1verb']
            courseoutcomeverb2=request.POST['co2verb']
            courseoutcomeverb3=request.POST['co3verb']
            courseoutcomeverb4=request.POST['co4verb']
            courseoutcomeverb5=request.POST['co5verb']

            if(ctype=="Theory"):
                module1=request.POST['module1']
                module2=request.POST['module2']
                module3=request.POST['module3']
                module4=request.POST['module4']
                module5=request.POST['module5']
                module6=request.POST['module6']

                modulehour1=request.POST['modulehour1']
                modulehour2=request.POST['modulehour2']
                modulehour3=request.POST['modulehour3']
                modulehour4=request.POST['modulehour4']
                modulehour5=request.POST['modulehour5']
                modulehour6=request.POST['modulehour6']

            
                #totalmodulehours=int(modulehour1)+int(modulehour2)+int(modulehour3)+int(modulehour4)+int(modulehour5)+int(modulehour6)
                #if(totalmodulehours!=40):
                #    messages.error(request," Total of Module hours should be equal 40")
                #    return redirect("addcoursecontent")
            
            if(ctype=="Laboratory"):
                labexperiment=request.POST['labexperiment']

            textbook1=request.POST['textbook1']
            textbook2=request.POST['textbook2']
            textbook3=request.POST['textbook3']
            textbook4=request.POST['textbook4']

            reference1=request.POST['reference1']
            reference2=request.POST['reference2']
            reference3=request.POST['reference3']
            reference4=request.POST['reference4']

            usefullink1=request.POST['usefullink1']
            usefullink2=request.POST['usefullink2']
            usefullink3=request.POST['usefullink3']
            usefullink4=request.POST['usefullink4']

            co1po1=request.POST['co1po1']
            co1po2=request.POST['co1po2']
            co1po3=request.POST['co1po3']
            co1po4=request.POST['co1po4']
            co1po5=request.POST['co1po5']
            co1po6=request.POST['co1po6']
            co1po7=request.POST['co1po7']
            co1po8=request.POST['co1po8']
            co1po9=request.POST['co1po9']
            co1po10=request.POST['co1po10']
            co1po11=request.POST['co1po11']
            co1po12=request.POST['co1po12']
            co1pso1=request.POST['co1pso1']
            co1pso2=request.POST['co1pso2']
            co1pso3=request.POST['co1pso3']

            co2po1=request.POST['co2po1']
            co2po2=request.POST['co2po2']
            co2po3=request.POST['co2po3']
            co2po4=request.POST['co2po4']
            co2po5=request.POST['co2po5']
            co2po6=request.POST['co2po6']
            co2po7=request.POST['co2po7']
            co2po8=request.POST['co2po8']
            co2po9=request.POST['co2po9']
            co2po10=request.POST['co2po10']
            co2po11=request.POST['co2po11']
            co2po12=request.POST['co2po12']
            co2pso1=request.POST['co2pso1']
            co2pso2=request.POST['co2pso2']
            co2pso3=request.POST['co2pso3']

            co3po1=request.POST['co3po1']
            co3po2=request.POST['co3po2']
            co3po3=request.POST['co3po3']
            co3po4=request.POST['co3po4']
            co3po5=request.POST['co3po5']
            co3po6=request.POST['co3po6']
            co3po7=request.POST['co3po7']
            co3po8=request.POST['co3po8']
            co3po9=request.POST['co3po9']
            co3po10=request.POST['co3po10']
            co3po11=request.POST['co3po11']
            co3po12=request.POST['co3po12']
            co3pso1=request.POST['co3pso1']
            co3pso2=request.POST['co3pso2']
            co3pso3=request.POST['co3pso3']

            co4po1=request.POST['co4po1']
            co4po2=request.POST['co4po2']
            co4po3=request.POST['co4po3']
            co4po4=request.POST['co4po4']
            co4po5=request.POST['co4po5']
            co4po6=request.POST['co4po6']
            co4po7=request.POST['co4po7']
            co4po8=request.POST['co4po8']
            co4po9=request.POST['co4po9']
            co4po10=request.POST['co4po10']
            co4po11=request.POST['co4po11']
            co4po12=request.POST['co4po12']
            co4pso1=request.POST['co4pso1']
            co4pso2=request.POST['co4pso2']
            co4pso3=request.POST['co4pso3']

            co5po1=request.POST['co5po1']
            co5po2=request.POST['co5po2']
            co5po3=request.POST['co5po3']
            co5po4=request.POST['co5po4']
            co5po5=request.POST['co5po5']
            co5po6=request.POST['co5po6']
            co5po7=request.POST['co5po7']
            co5po8=request.POST['co5po8']
            co5po9=request.POST['co5po9']
            co5po10=request.POST['co5po10']
            co5po11=request.POST['co5po11']
            co5po12=request.POST['co5po12']
            co5pso1=request.POST['co5pso1']
            co5pso2=request.POST['co5pso2']
            co5pso3=request.POST['co5pso3']


            remembert1=request.POST['remembert1']
            remembert2=request.POST['remembert2']
            rememberese=request.POST['rememberese']
            remembertotal=request.POST['remembertotal']

            understandt1=request.POST['understandt1']
            understandt2=request.POST['understandt2']
            understandese=request.POST['understandese']
            understandtotal=request.POST['understandtotal']

            analyzet1=request.POST['analyzet1']
            analyzet2=request.POST['analyzet2']
            analyzeese=request.POST['analyzeese']
            analyzetotal=request.POST['analyzetotal']

            applyt1=request.POST['applyt1']
            applyt2=request.POST['applyt2']
            applyese=request.POST['applyese']
            applytotal=request.POST['applytotal']

            evaluatet1=request.POST['evaluatet1']
            evaluatet2=request.POST['evaluatet2']
            evaluateese=request.POST['evaluateese']
            evaluatetotal=request.POST['evaluatetotal']

            createt1=request.POST['createt1']
            createt2=request.POST['createt2']
            createese=request.POST['createese']
            createtotal=request.POST['createtotal']
            
            #t1la1total=int(remembert1)+int(understandt1)+int(analyzet1)+int(applyt1)+int(evaluatet1)+int(createt1)
            #t2la2total=int(remembert2)+int(understandt2)+int(analyzet2)+int(applyt2)+int(evaluatet2)+int(createt2)
            #esetotal=int(rememberese)+int(understandese)+int(analyzeese)+int(applyese)+int(evaluateese)+int(createese)
            #totaltotal=int(remembertotal)+int(understandtotal)+int(analyzetotal)+int(applytotal)+int(evaluatetotal)+int(createtotal)

            #if(ctype=="Theory"):
            #    if(t1la1total!=20):
            #           messages.error(request,"Total of T1 all levels should be equal to 20")
            #           return redirect("faculty")

            #    if(t2la2total!=20):
            #           messages.error(request,"Total of T2 all levels should be equal to 20")
            #           return redirect("faculty")

            #    if(esetotal!=60):
            #           messages.error(request,"Total of ESE all levels should be equal to 60")
            #           return redirect("faculty")

            #    
            #    if(totaltotal!=100):
            #           messages.error(request,"Total of Total all levels should be equal to 100")
            #           return redirect("faculty")
            #
            #else:
            #    if(t1la1total!=30):
            #           messages.error(request,"Total of LA1 all levels should be equal to 30")
            #           return redirect("faculty")

            #    if(t2la2total!=30):
            #           messages.error(request,"Total of LA2 all levels should be equal to 30")
            #           return redirect("faculty")

            #    if(esetotal!=40):
            #           messages.error(request,"Tatal of ESE all levels should be equal to 40")
            #           return redirect("faculty")

            #    
            #    if(totaltotal!=100):
            #           messages.error(request,"Total of Total all levels should be equal to 100")
            #           return redirect("faculty")

            
                
            course.desired_requsite=dreq
            
            course.courseobjective1=courseobjective1
            course.courseobjective2=courseobjective2
            course.courseobjective3=courseobjective3
            course.courseobjective4=courseobjective4
            course.courseobjective5=courseobjective5
    
            course.courseoutcome1=courseoutcome1
            course.courseoutcome2=courseoutcome2
            course.courseoutcome3=courseoutcome3
            course.courseoutcome4=courseoutcome4
            course.courseoutcome5=courseoutcome5
    
            course.courseoutcomelevel1=courseoutcomelevel1
            course.courseoutcomelevel2=courseoutcomelevel2
            course.courseoutcomelevel3=courseoutcomelevel3
            course.courseoutcomelevel4=courseoutcomelevel4
            course.courseoutcomelevel5=courseoutcomelevel5

            course.courseoutcomeverb1=courseoutcomeverb1
            course.courseoutcomeverb2=courseoutcomeverb2
            course.courseoutcomeverb3=courseoutcomeverb3
            course.courseoutcomeverb4=courseoutcomeverb4
            course.courseoutcomeverb5=courseoutcomeverb5

            if(ctype=="Theory"):
                course.module1=module1
                course.module2=module2
                course.module3=module3
                course.module4=module4
                course.module5=module5
                course.module6=module6

                course.modulehour1=modulehour1
                course.modulehour2=modulehour2
                course.modulehour3=modulehour3
                course.modulehour4=modulehour4
                course.modulehour5=modulehour5
                course.modulehour6=modulehour6

            if(ctype=="Laboratory"):
                course.labexperiment=labexperiment

            course.textbook1=textbook1
            course.textbook2=textbook2
            course.textbook3=textbook3
            course.textbook4=textbook4

            course.reference1=reference1
            course.reference2=reference2
            course.reference3=reference3
            course.reference4=reference4

            course.usefullink1=usefullink1
            course.usefullink2=usefullink2
            course.usefullink3=usefullink3
            course.usefullink4=usefullink4

            course.co1po1=co1po1
            course.co1po2=co1po2
            course.co1po3=co1po3
            course.co1po4=co1po4
            course.co1po5=co1po5
            course.co1po6=co1po6
            course.co1po7=co1po7
            course.co1po8=co1po8
            course.co1po9=co1po9
            course.co1po10=co1po10
            course.co1po11=co1po11
            course.co1po12=co1po12
            course.co1pso1=co1pso1
            course.co1pso2=co1pso2
            course.co1pso3=co1pso3

            course.co2po1=co2po1
            course.co2po2=co2po2
            course.co2po3=co2po3
            course.co2po4=co2po4
            course.co2po5=co2po5
            course.co2po6=co2po6
            course.co2po7=co2po7
            course.co2po8=co2po8
            course.co2po9=co2po9
            course.co2po10=co2po10
            course.co2po11=co2po11
            course.co2po12=co2po12
            course.co2pso1=co2pso1
            course.co2pso2=co2pso2
            course.co2pso3=co2pso3

            course.co3po1=co3po1
            course.co3po2=co3po2
            course.co3po3=co3po3
            course.co3po4=co3po4
            course.co3po5=co3po5
            course.co3po6=co3po6
            course.co3po7=co3po7
            course.co3po8=co3po8
            course.co3po9=co3po9
            course.co3po10=co3po10
            course.co3po11=co3po11
            course.co3po12=co3po12
            course.co3pso1=co3pso1
            course.co3pso2=co3pso2
            course.co3pso3=co3pso3

            course.co4po1=co4po1
            course.co4po2=co4po2
            course.co4po3=co4po3
            course.co4po4=co4po4
            course.co4po5=co4po5
            course.co4po6=co4po6
            course.co4po7=co4po7
            course.co4po8=co4po8
            course.co4po9=co4po9
            course.co4po10=co4po10
            course.co4po11=co4po11
            course.co4po12=co4po12
            course.co4pso1=co4pso1
            course.co4pso2=co4pso2
            course.co4pso3=co4pso3

            course.co5po1=co5po1
            course.co5po2=co5po2
            course.co5po3=co5po3
            course.co5po4=co5po4
            course.co5po5=co5po5
            course.co5po6=co5po6
            course.co5po7=co5po7
            course.co5po8=co5po8
            course.co5po9=co5po9
            course.co5po10=co5po10
            course.co5po11=co5po11
            course.co5po12=co5po12
            course.co5pso1=co5pso1
            course.co5pso2=co5pso2
            course.co5pso3=co5pso3


            course.remembert1=remembert1
            course.remembert2=remembert2
            course.rememberese=rememberese
            course.remembertotal=remembertotal

            course.understandt1=understandt1
            course.understandt2=understandt2
            course.understandese=understandese
            course.understandtotal=understandtotal

            course.analyzet1=analyzet1
            course.analyzet2=analyzet2
            course.analyzeese=analyzeese
            course.analyzetotal=analyzetotal

            course.applyt1=applyt1
            course.applyt2=applyt2
            course.applyese=applyese
            course.applytotal=applytotal

            course.evaluatet1=evaluatet1
            course.evaluatet2=evaluatet2
            course.evaluateese=evaluateese
            course.evaluatetotal=evaluatetotal

            course.createt1=createt1
            course.createt2=createt2
            course.createese=createese
            course.createtotal=createtotal

            course.save()
            
            messages.success(request,"Course content added successfully")
        
        if "finalsubmit" in request.POST:
            course_id=request.POST["cid"]
            course=Course.objects.filter(course_id=course_id)
            course=course[0]
            error=False
            ctype=course.course_type

            dreq=request.POST['dreq']

            courseobjective1=request.POST['courseobjective1']
            courseobjective2=request.POST['courseobjective2']
            courseobjective3=request.POST['courseobjective3']
            courseobjective4=request.POST['courseobjective4']
            courseobjective5=request.POST['courseobjective5']
    
            courseoutcome1=request.POST['courseoutcome1']
            courseoutcome2=request.POST['courseoutcome2']
            courseoutcome3=request.POST['courseoutcome3']
            courseoutcome4=request.POST['courseoutcome4']
            courseoutcome5=request.POST['courseoutcome5']
    
            courseoutcomelevel1=request.POST['co1level']
            courseoutcomelevel2=request.POST['co2level']
            courseoutcomelevel3=request.POST['co3level']
            courseoutcomelevel4=request.POST['co4level']
            courseoutcomelevel5=request.POST['co5level']

            courseoutcomeverb1=request.POST['co1verb']
            courseoutcomeverb2=request.POST['co2verb']
            courseoutcomeverb3=request.POST['co3verb']
            courseoutcomeverb4=request.POST['co4verb']
            courseoutcomeverb5=request.POST['co5verb']

            if(ctype=="Theory"):
                module1=request.POST['module1']
                module2=request.POST['module2']
                module3=request.POST['module3']
                module4=request.POST['module4']
                module5=request.POST['module5']
                module6=request.POST['module6']

                modulehour1=request.POST['modulehour1']
                modulehour2=request.POST['modulehour2']
                modulehour3=request.POST['modulehour3']
                modulehour4=request.POST['modulehour4']
                modulehour5=request.POST['modulehour5']
                modulehour6=request.POST['modulehour6']

            
                totalmodulehours=int(modulehour1)+int(modulehour2)+int(modulehour3)+int(modulehour4)+int(modulehour5)+int(modulehour6)
                if(totalmodulehours!=40):
                    messages.error(request," Total of Module hours should be equal 40")
                    error=True
            
            if(ctype=="Laboratory"):
                labexperiment=request.POST['labexperiment']

            textbook1=request.POST['textbook1']
            textbook2=request.POST['textbook2']
            textbook3=request.POST['textbook3']
            textbook4=request.POST['textbook4']

            reference1=request.POST['reference1']
            reference2=request.POST['reference2']
            reference3=request.POST['reference3']
            reference4=request.POST['reference4']

            usefullink1=request.POST['usefullink1']
            usefullink2=request.POST['usefullink2']
            usefullink3=request.POST['usefullink3']
            usefullink4=request.POST['usefullink4']

            co1po1=request.POST['co1po1']
            co1po2=request.POST['co1po2']
            co1po3=request.POST['co1po3']
            co1po4=request.POST['co1po4']
            co1po5=request.POST['co1po5']
            co1po6=request.POST['co1po6']
            co1po7=request.POST['co1po7']
            co1po8=request.POST['co1po8']
            co1po9=request.POST['co1po9']
            co1po10=request.POST['co1po10']
            co1po11=request.POST['co1po11']
            co1po12=request.POST['co1po12']
            co1pso1=request.POST['co1pso1']
            co1pso2=request.POST['co1pso2']
            co1pso3=request.POST['co1pso3']

            co2po1=request.POST['co2po1']
            co2po2=request.POST['co2po2']
            co2po3=request.POST['co2po3']
            co2po4=request.POST['co2po4']
            co2po5=request.POST['co2po5']
            co2po6=request.POST['co2po6']
            co2po7=request.POST['co2po7']
            co2po8=request.POST['co2po8']
            co2po9=request.POST['co2po9']
            co2po10=request.POST['co2po10']
            co2po11=request.POST['co2po11']
            co2po12=request.POST['co2po12']
            co2pso1=request.POST['co2pso1']
            co2pso2=request.POST['co2pso2']
            co2pso3=request.POST['co2pso3']

            co3po1=request.POST['co3po1']
            co3po2=request.POST['co3po2']
            co3po3=request.POST['co3po3']
            co3po4=request.POST['co3po4']
            co3po5=request.POST['co3po5']
            co3po6=request.POST['co3po6']
            co3po7=request.POST['co3po7']
            co3po8=request.POST['co3po8']
            co3po9=request.POST['co3po9']
            co3po10=request.POST['co3po10']
            co3po11=request.POST['co3po11']
            co3po12=request.POST['co3po12']
            co3pso1=request.POST['co3pso1']
            co3pso2=request.POST['co3pso2']
            co3pso3=request.POST['co3pso3']

            co4po1=request.POST['co4po1']
            co4po2=request.POST['co4po2']
            co4po3=request.POST['co4po3']
            co4po4=request.POST['co4po4']
            co4po5=request.POST['co4po5']
            co4po6=request.POST['co4po6']
            co4po7=request.POST['co4po7']
            co4po8=request.POST['co4po8']
            co4po9=request.POST['co4po9']
            co4po10=request.POST['co4po10']
            co4po11=request.POST['co4po11']
            co4po12=request.POST['co4po12']
            co4pso1=request.POST['co4pso1']
            co4pso2=request.POST['co4pso2']
            co4pso3=request.POST['co4pso3']

            co5po1=request.POST['co5po1']
            co5po2=request.POST['co5po2']
            co5po3=request.POST['co5po3']
            co5po4=request.POST['co5po4']
            co5po5=request.POST['co5po5']
            co5po6=request.POST['co5po6']
            co5po7=request.POST['co5po7']
            co5po8=request.POST['co5po8']
            co5po9=request.POST['co5po9']
            co5po10=request.POST['co5po10']
            co5po11=request.POST['co5po11']
            co5po12=request.POST['co5po12']
            co5pso1=request.POST['co5pso1']
            co5pso2=request.POST['co5pso2']
            co5pso3=request.POST['co5pso3']


            remembert1=request.POST['remembert1']
            remembert2=request.POST['remembert2']
            rememberese=request.POST['rememberese']
            remembertotal=request.POST['remembertotal']

            understandt1=request.POST['understandt1']
            understandt2=request.POST['understandt2']
            understandese=request.POST['understandese']
            understandtotal=request.POST['understandtotal']

            analyzet1=request.POST['analyzet1']
            analyzet2=request.POST['analyzet2']
            analyzeese=request.POST['analyzeese']
            analyzetotal=request.POST['analyzetotal']

            applyt1=request.POST['applyt1']
            applyt2=request.POST['applyt2']
            applyese=request.POST['applyese']
            applytotal=request.POST['applytotal']

            evaluatet1=request.POST['evaluatet1']
            evaluatet2=request.POST['evaluatet2']
            evaluateese=request.POST['evaluateese']
            evaluatetotal=request.POST['evaluatetotal']

            createt1=request.POST['createt1']
            createt2=request.POST['createt2']
            createese=request.POST['createese']
            createtotal=request.POST['createtotal']
            
            t1la1total=int(remembert1)+int(understandt1)+int(analyzet1)+int(applyt1)+int(evaluatet1)+int(createt1)
            t2la2total=int(remembert2)+int(understandt2)+int(analyzet2)+int(applyt2)+int(evaluatet2)+int(createt2)
            esetotal=int(rememberese)+int(understandese)+int(analyzeese)+int(applyese)+int(evaluateese)+int(createese)
            totaltotal=int(remembertotal)+int(understandtotal)+int(analyzetotal)+int(applytotal)+int(evaluatetotal)+int(createtotal)

            if(ctype=="Theory"):
                if(t1la1total!=20):
                       messages.error(request,"Total of T1 all levels should be equal to 20")
                       error=True

                if(t2la2total!=20):
                       messages.error(request,"Total of T2 all levels should be equal to 20")
                       error=True

                if(esetotal!=60):
                       messages.error(request,"Total of ESE all levels should be equal to 60")
                       error=True
                
                if(totaltotal!=100):
                       messages.error(request,"Total of Total all levels should be equal to 100")
                       error=True
            else:
                if(t1la1total!=30):
                       messages.error(request,"Total of LA1 all levels should be equal to 30")
                       error=True

                if(t2la2total!=30):
                       messages.error(request,"Total of LA2 all levels should be equal to 30")
                       error=True

                if(esetotal!=40):
                       messages.error(request,"Tatal of ESE all levels should be equal to 40")
                       error=True
                
                if(totaltotal!=100):
                       messages.error(request,"Total of Total all levels should be equal to 100")
                       error=True
            
                
            course.desired_requsite=dreq
            
            course.courseobjective1=courseobjective1
            course.courseobjective2=courseobjective2
            course.courseobjective3=courseobjective3
            course.courseobjective4=courseobjective4
            course.courseobjective5=courseobjective5
    
            course.courseoutcome1=courseoutcome1
            course.courseoutcome2=courseoutcome2
            course.courseoutcome3=courseoutcome3
            course.courseoutcome4=courseoutcome4
            course.courseoutcome5=courseoutcome5
    
            course.courseoutcomelevel1=courseoutcomelevel1
            course.courseoutcomelevel2=courseoutcomelevel2
            course.courseoutcomelevel3=courseoutcomelevel3
            course.courseoutcomelevel4=courseoutcomelevel4
            course.courseoutcomelevel5=courseoutcomelevel5

            course.courseoutcomeverb1=courseoutcomeverb1
            course.courseoutcomeverb2=courseoutcomeverb2
            course.courseoutcomeverb3=courseoutcomeverb3
            course.courseoutcomeverb4=courseoutcomeverb4
            course.courseoutcomeverb5=courseoutcomeverb5

            if(ctype=="Theory"):
                course.module1=module1
                course.module2=module2
                course.module3=module3
                course.module4=module4
                course.module5=module5
                course.module6=module6

                course.modulehour1=modulehour1
                course.modulehour2=modulehour2
                course.modulehour3=modulehour3
                course.modulehour4=modulehour4
                course.modulehour5=modulehour5
                course.modulehour6=modulehour6

            if(ctype=="Laboratory"):
                course.labexperiment=labexperiment

            course.textbook1=textbook1
            course.textbook2=textbook2
            course.textbook3=textbook3
            course.textbook4=textbook4

            course.reference1=reference1
            course.reference2=reference2
            course.reference3=reference3
            course.reference4=reference4

            course.usefullink1=usefullink1
            course.usefullink2=usefullink2
            course.usefullink3=usefullink3
            course.usefullink4=usefullink4

            course.co1po1=co1po1
            course.co1po2=co1po2
            course.co1po3=co1po3
            course.co1po4=co1po4
            course.co1po5=co1po5
            course.co1po6=co1po6
            course.co1po7=co1po7
            course.co1po8=co1po8
            course.co1po9=co1po9
            course.co1po10=co1po10
            course.co1po11=co1po11
            course.co1po12=co1po12
            course.co1pso1=co1pso1
            course.co1pso2=co1pso2
            course.co1pso3=co1pso3

            course.co2po1=co2po1
            course.co2po2=co2po2
            course.co2po3=co2po3
            course.co2po4=co2po4
            course.co2po5=co2po5
            course.co2po6=co2po6
            course.co2po7=co2po7
            course.co2po8=co2po8
            course.co2po9=co2po9
            course.co2po10=co2po10
            course.co2po11=co2po11
            course.co2po12=co2po12
            course.co2pso1=co2pso1
            course.co2pso2=co2pso2
            course.co2pso3=co2pso3

            course.co3po1=co3po1
            course.co3po2=co3po2
            course.co3po3=co3po3
            course.co3po4=co3po4
            course.co3po5=co3po5
            course.co3po6=co3po6
            course.co3po7=co3po7
            course.co3po8=co3po8
            course.co3po9=co3po9
            course.co3po10=co3po10
            course.co3po11=co3po11
            course.co3po12=co3po12
            course.co3pso1=co3pso1
            course.co3pso2=co3pso2
            course.co3pso3=co3pso3

            course.co4po1=co4po1
            course.co4po2=co4po2
            course.co4po3=co4po3
            course.co4po4=co4po4
            course.co4po5=co4po5
            course.co4po6=co4po6
            course.co4po7=co4po7
            course.co4po8=co4po8
            course.co4po9=co4po9
            course.co4po10=co4po10
            course.co4po11=co4po11
            course.co4po12=co4po12
            course.co4pso1=co4pso1
            course.co4pso2=co4pso2
            course.co4pso3=co4pso3

            course.co5po1=co5po1
            course.co5po2=co5po2
            course.co5po3=co5po3
            course.co5po4=co5po4
            course.co5po5=co5po5
            course.co5po6=co5po6
            course.co5po7=co5po7
            course.co5po8=co5po8
            course.co5po9=co5po9
            course.co5po10=co5po10
            course.co5po11=co5po11
            course.co5po12=co5po12
            course.co5pso1=co5pso1
            course.co5pso2=co5pso2
            course.co5pso3=co5pso3


            course.remembert1=remembert1
            course.remembert2=remembert2
            course.rememberese=rememberese
            course.remembertotal=remembertotal

            course.understandt1=understandt1
            course.understandt2=understandt2
            course.understandese=understandese
            course.understandtotal=understandtotal

            course.analyzet1=analyzet1
            course.analyzet2=analyzet2
            course.analyzeese=analyzeese
            course.analyzetotal=analyzetotal

            course.applyt1=applyt1
            course.applyt2=applyt2
            course.applyese=applyese
            course.applytotal=applytotal

            course.evaluatet1=evaluatet1
            course.evaluatet2=evaluatet2
            course.evaluateese=evaluateese
            course.evaluatetotal=evaluatetotal

            course.createt1=createt1
            course.createt2=createt2
            course.createese=createese
            course.createtotal=createtotal
            if not error:
                course.finalsubmit=True
            course.save()

            if not error:
                messages.success(request,"Course Final Submitted")
                return redirect("faculty")      

        course_id=request.POST["cid"]
        course=Course.objects.filter(course_id=course_id)
        course=course[0]
        context={'course':course}
        return render(request,"addcoursecontent.html",context)

    
    return redirect("faculty")


def viewcourse(request):
    if request.user.is_anonymous:
        return redirect('loginuser')

    if request.method=="POST":
        course_id=request.POST["cid"]
        course=Course.objects.filter(course_id=course_id)
        course=course[0]
        context={'course':course}
        return render(request,"viewcourse.html",context)


def deletecourse(request):
    if request.user.account.is_hod is not True:
        return redirect('loginuser')

    if request.method=="POST":
        course_id=request.POST["cid"]
        course=Course.objects.filter(course_id=course_id)
        course=course[0]
        course.delete()
        messages.success(request,"Course deleted successfully")
        return redirect("hod")
        


    
def addcourse(request):
    if request.user.account.is_hod is not True:
        return redirect('loginuser')

    if request.method=="POST":
        ay=request.POST['ay']
        hod=request.POST['hod']
        faculty=request.POST['faculty']
        programme=request.POST['programme']
        classsem=request.POST['classsem']
        cname=request.POST['cname']
        ccode=request.POST['ccode']
        ctype=request.POST['ctype']
        credits=request.POST['credits']

        lecture=request.POST['lecture']
        tutorial=request.POST['tutorial']
        practical=request.POST['practical']
        interaction=request.POST['interaction']

        ins= Course(
            
            academic_year=ay,
            hod=hod,
            faculty=faculty,
            programme=programme,
            class_sem=classsem,
            course_code=ccode,
            course_name=cname,
            course_type=ctype,
            credits=credits,
            lecture=lecture,
            tutorial=tutorial,
            practical=practical,
            interaction=interaction,
        )
        ins.save()
        messages.success(request,"Course Added successfully")
        return redirect("addcourse")


    faculties=[]
    users=User.objects.all()
    for user in users:
        if user.account.is_faculty:
            faculties.append(user)

    context={'faculties':faculties,
             'user':request.user.username}
    return render(request,"addcourse.html",context)
    
 
def modifycourse(request):
    if request.user.account.is_hod is not True:
        return redirect('loginuser')
    
    if request.method=="POST":
   
        if "save" in request.POST:
            course_id=request.POST["cid"]
            course=Course.objects.filter(course_id=course_id)
            course=course[0]

            course.academic_year=request.POST['ay']
            course.hod=request.POST['hod']
            course.faculty=request.POST['faculty']
            course.programme=request.POST['programme']
            course.class_sem=request.POST['classsem']
            course.course_name=request.POST['cname']
            course.course_code=request.POST['ccode']
            course.course_type=request.POST['ctype']
            course.credits=request.POST['credits']

            course.lecture=request.POST['lecture']
            course.tutorial=request.POST['tutorial']
            course.practical=request.POST['practical']
            course.interaction=request.POST['interaction']

            course.save()
            messages.success(request,"Course modified successfully")
        
        faculties=[]
        users=User.objects.all()
        for user in users:
            if user.account.is_faculty:
                faculties.append(user)

        course_id=request.POST["cid"]
        course=Course.objects.filter(course_id=course_id)
        course=course[0]
        context={'course':course,'faculties':faculties}

        return render(request,"modifycourse.html",context)

    return redirect("hod")