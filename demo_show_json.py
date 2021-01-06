import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings') # 需對應 wsgi.py
django.setup()
# 更多操作請參考官方文檔: https://docs.djangoproject.com/en/3.1/topics/db/models/
from mainsite.models import Post, Branch, StoreIncome
import json
#=============================================================================#
with open('Post.json', 'r') as read_file:
    post_json = json.load(read_file)

for i, post_dict in enumerate(post_json):
    print(f'\n第 {i+1} 筆 Post 資料')
    title = post_dict['title']
    slug = post_dict['slug']
    body = post_dict['body']
    pub_date = post_dict['pub_date']
    print(f'title: {title} slug: {slug} pub_date: {pub_date}')
    print(f'body: {body}')
    posts = Post.objects.filter(title=title, slug=slug, body=body)
    print(f'已存在 {len(posts)} 筆相同 Post 資料')
#=============================================================================#
with open('Branch.json', 'r') as read_file:
    stores_json = json.load(read_file)

for i, store_dict in enumerate(stores_json):
    print(f'\n第 {i+1} 筆 Branch 資料')
    title = store_dict['title']
    name = store_dict['name']
    print(f'title: {title} name: {name}')
    stores = Branch.objects.filter(title=title, name=name)
    print(f'已存在 {len(stores)} 筆相同 Branch 資料')
#=============================================================================#
with open('StoreIncome.json', 'r') as read_file:
    store_income_json = json.load(read_file)

for i, store_income_dict in enumerate(store_income_json):
    print(f'\n第 {i+1} 筆 Post 資料')
    income_year = store_income_dict['income_year']
    income_month = store_income_dict['income_month']
    income = store_income_dict['income']
    branch_title = store_income_dict['branch.title']
    print(f'income_year: {income_year} income_month: {income_month} income: {income} branch.title: {branch_title}')
    
    stores = Branch.objects.filter(title=branch_title)
    data = StoreIncome.objects.filter(income_year=income_year, income_month=income_month, income=income, branch=stores[0])
    print(f'已存在 {len(stores)} 筆相同 Branch 資料 {len(data)} 筆相 StoreIncome 同資料')
    