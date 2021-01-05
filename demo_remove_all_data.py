import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings') # 需對應 wsgi.py
django.setup()
print(f'當前路徑: {os.getcwd()}')

from mainsite.models import Post, Branch, StoreIncome
# 更多操作請參考官方文檔: https://docs.djangoproject.com/en/3.1/topics/db/models/

#=============================================================================#
Post.objects.all().delete()

#=============================================================================#
Branch.objects.all().delete()

#=============================================================================#
StoreIncome.objects.all().delete()


