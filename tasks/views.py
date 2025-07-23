from django.shortcuts import render
from django.http import HttpResponse
from tasks.forms import taskform,taskmodelform
from tasks.models import employee,task


# Create your views here.
# def home(request):
#     # return HttpResponse('welcome to the world')
#     return render(request,'home.html')
# def contact(request):
#     return HttpResponse("<h2 style='color:green'>this is the contact page</h2>")
# def showtask(request):
#     return HttpResponse("show your task")

def admindashboard(request):
    return render(request,"dashboard/common.html")
    
def text(request):
   context={
      "name":["ragib","oyon"]
   }

   return render(request,'text.html',context)

def create_task(request):
   #  employees=employee.objects.all()
    form=taskmodelform() #for get method

    if request.method =="POST":
        form=taskmodelform(request.POST)
        if form.is_valid():
            """for model form"""
            form.save()
            return render(request,"task_form.html",{"form":form,"message":"task added successfully"})

            """for django form data"""

            # data=form.cleaned_data
            # title=data.get('title')
            # description=data.get('description')
            # due_date=data.get('due_date')
            # assigned_to=data.get('assigned_to')
            
            # taskk=task.objects.create(title=title,description=description,due_date=due_date)
            
            # for emp_id in assigned_to:
            #     employeess=employee.objects.get(id=emp_id)
            #     taskk.assigned_to.add(employeess)

            # return HttpResponse("task added successfully")

    context={"form":form}
    return render(request,"task_form.html",context)


def view_task(request):
    taskk=task.objects.all()
    task_1=task.objects.get(pk=1)
    return render(request,"show_task.html",{"taskk":taskk,"task1":task_1})