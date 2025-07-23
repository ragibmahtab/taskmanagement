from django.db import models

# Create your models here.

class employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)

    def __str__(self):
        return self.name



class task(models.Model):
    status_options=[
        ('Pending','pending'),
        ('IN_progress','in_progress'),
        ('Completed','completed'),
    ]
    project=models.ForeignKey("project",on_delete=models.CASCADE,default="1")
    assigned_to=models.ManyToManyField(employee)
    title=models.CharField(max_length=250)
    description=models.TextField()
    due_date=models.TextField()
    status=models.CharField(max_length=250,choices=status_options,default='Pending')
    is_completed=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    
    def __str__(self):
        return self.title

class task_detail(models.Model):
    HIGH='H'
    MEDIUM='M'
    LOW='L'
    PRIORITY_OPTIONS=(
        (HIGH,'high'),
        (MEDIUM,'medium'),
        (LOW,'low')
    )
    task=models.OneToOneField(task, on_delete=models.CASCADE)
    assigned_to =models.CharField(max_length=100)
    priority=models.CharField(max_length=1,choices=PRIORITY_OPTIONS,default='LOW')
    notes=models.TextField(blank=True,null=True)

    
    def __str__(self):
        return F"details from task {self.task.title}"


class project(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    start_date=models.DateField()

    def __str__(self):
        return self.name