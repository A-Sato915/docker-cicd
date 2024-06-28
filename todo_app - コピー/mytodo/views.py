from django.shortcuts import render, redirect
from django.views import View
from .models import Task
from .forms import TaskForm

# Create your views here.
class IndexView(View):
    def get(self, request):
        #todolist
        todo_list = Task.objects.all()
        
        context = {
            "todo_list": todo_list
        }
        
        #テンプレートレンダリング
        return render(request, "mytodo/index.html", context)
    
class AddView(View):
    def get(self, request):
        form = TaskForm()
        
        #テンプレートレンダリング
        return render(request, "mytodo/add.html", {"form": form})
        
    def post(self, request, *args, **kwargs):
        #登録処理
        #入力データ、フォームへ
        form = TaskForm(request.POST)
        #入力データに誤りないか
        is_valid = form.is_valid()
        
        #正常
        if is_valid:
            #モデル登録
            form.save()
            return redirect('/')
        
        #異常
        return render(request, 'mytodo/add.html', {"form": form})
    
class Update_task_complete(View):
    def post(self, request, *args, **kwargs):
        task_id = request.POST.get("task_id")
        
        task = Task.objects.get(id=task_id)
        task.complete = not task.complete
        task.save()
        
        return redirect('/')
    
#インスタンス化
index = IndexView.as_view()
add = AddView.as_view() 
Update_task_complete = Update_task_complete.as_view()