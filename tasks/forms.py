from django import forms
from tasks.models import task

class taskform(forms.Form):
    title=forms.CharField(max_length=250,label='task title')
    description=forms.CharField(widget=forms.Textarea,label='task description')
    due_date=forms.DateField(widget=forms.SelectDateWidget,label='due date')
    assigned_to=forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=[])

    def __init__(self,*args, **kwargs):
        # print(args,kwargs)
        employees=kwargs.pop("employees",[])
        super().__init__(*args,**kwargs)
        self.fields["assigned_to"].choices=[(emp.id,emp.name) for emp in employees]
        

"""using mixin widget"""
class styledformmixin:
    default_classes="border-2 border-gray-300 w-full rounded-lg shadow-sm focus:border-rose-300 focus:ring-rose-500"
    def apply_styled_widgets(self):
        for field_name,field in self.fields.items():
            if isinstance(field.widget,forms.TextInput):
                field.widget.attrs.update({
                    'class':self.default_classes,
                    'placeholder':f"enter{field.label.lower()}"
                })

            elif isinstance(field.widget,forms.Textarea):
                field.widget.attrs.update({
                    'class':f"{self.default_classes} resize-none",
                    'placeholder':f"enter{field.label.lower()}",
                    'rows':5
                })
            elif isinstance(field.widget,forms.SelectDateWidget):
                field.widget.attrs.update({
                    'class':"border-2 border-gray-300 rounded-lg shadow-sm focus:border-rose-300 focus:ring-rose-500"
                })
            elif isinstance(field.widget,forms.CheckboxSelectMultiple):
                field.widget.attrs.update({
                    'class':"space-y-2"
                })
            else:
                field.widget.attrs.update({
                    'class':self.default_classes
                })





class taskmodelform(styledformmixin,forms.ModelForm):
    class Meta:
        model=task
        fields=['title','description','due_date','assigned_to'] 
        widgets={
            'due_date':forms.SelectDateWidget,
            'assigned_to':forms.CheckboxSelectMultiple
        }


        # exclude=['project','is_completed','created_at','updated_at']
        """manual widget"""
        # widgets={
        #     'title':forms.TextInput(attrs=
        # {'class':"border-2 border-gray-300 w-full rounded-lg shadow-sm focus:border-rose-300 focus:ring-rose-500",'placeholder':"enter your task"}),

        #     'description':forms.Textarea(attrs=
        # {'class':"border-2 border-gray-300 w-full rounded-lg shadow-sm focus:border-rose-300 focus:ring-rose-500",'placeholder':"describe your task"}),

        #     'due_date':forms.SelectDateWidget(attrs=
        # {'class':"border-2 border-gray-300 rounded-lg shadow-sm focus:border-rose-300 focus:ring-rose-500"}),

        #     'assigned_to':forms.CheckboxSelectMultiple(attrs=
        # {'class':"border-2 border-gray-300 w-full rounded-lg shadow-sm focus:border-rose-300 focus:ring-rose-500",'placeholder':"enter your query"})}
       
    def __init__(self,*arg,**kwarg):
        super().__init__(*arg,**kwarg)
        self.apply_styled_widgets()

