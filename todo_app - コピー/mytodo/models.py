from django.db import models

# Create your models here.
class Task(models.Model):
    class Meta:
        db_table = "tasks"
        
    #task名　テキスト(短い)データ notnull
    title = models.CharField(verbose_name="タスク名", max_length=255)
    
    #詳細　テキスト(長い)データ　
    description = models.TextField(verbose_name="詳細", null=True, blank=True)
    
    #完了　数値(1=完了　0=未完) def 0
    complete = models.IntegerField(verbose_name="完了フラグ", default=0)
    
    #開始　
    start_date = models.DateTimeField(verbose_name="開始日", null=True, blank=True)
    
    #終了
    end_date = models.DateTimeField(verbose_name="終了日", null=True, blank=True)
    
    def __str__(self):
        return self.title