from django.shortcuts import render
from .models import List
from .models import Near_by

def task_view(request):
	a={'list':List.objects.all()}
	return render(request, 'List.html' , a)

def view_task(request , view_id):
	view=List.objects.get(id=view_id)
	a={'view': view,}
	return render(request, 'view_task.html' , a)