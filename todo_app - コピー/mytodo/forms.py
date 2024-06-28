from typing import Any
from django import forms
from .models import Task
from django.utils import timezone
from django.core.exceptions import ValidationError

#taskテーブル入力
class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'start_date', 'end_date')
        widgets = {
            'start_date': forms.DateTimeInput(attrs={"type": "datetime-local"}), 
            'end_date': forms.DateTimeInput(attrs={"type": "datetime-local"}), 
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["title"].widget.attrs = {"placeholder": "タスク名"}
        self.fields["description"].widget.attrs = {"placeholder": "詳細"} 
      
    #項目別バリデーション  
    def clean_start_date(self):
        start_date = self.cleaned_data.get('start_date')
        if start_date and start_date < timezone.now():
            raise ValidationError("開始日過去不可")
        
        return start_date
    
    def clean_end_date(self):
        end_date = self.cleaned_data.get('start_date')
        if end_date and end_date < timezone.now():
            raise ValidationError("終了日過去不可")
        
        return end_date
    
    #全体バリデーション
    def clean(self):
        cleaned_date = super().clean()
        start_date = cleaned_date.get("start_date")
        end_date = cleaned_date.get("end_date")
        
        if start_date and end_date and end_date < start_date:
            self.add_error("end_date", "終了日開始日後日付設定")