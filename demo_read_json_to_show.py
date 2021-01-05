import os, django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mblog.settings') # 需對應 wsgi.py
django.setup()
print(f'當前路徑: {os.getcwd()}')

from mainsite.models import Post, Branch, StoreIncome
# 更多操作請參考官方文檔: https://docs.djangoproject.com/en/3.1/topics/db/models/

import json
#=============================================================================#
with open('Post.json', 'r') as read_file:
    post_json = json.load(read_file)

for i, post_dict in enumerate(post_json):
    print(f'\n第 {i} 筆 Post 資料')
    title = post_dict['title']
    slug = post_dict['slug']
    body = post_dict['body']
    pub_date = post_dict['pub_date']
    print(f'title: {title} slug: {slug} pub_date: {pub_date}')
    print(f'body: {body}')
#=============================================================================#
with open('Branch.json', 'r') as read_file:
    stores_json = json.load(read_file)

for i, store_dict in enumerate(stores_json):
    print(f'\n第 {i} 筆 Branch 資料')
    title = store_dict['title']
    name = store_dict['name']
    print(f'title: {title} name: {name}')
#=============================================================================#
with open('StoreIncome.json', 'r') as read_file:
    store_income_json = json.load(read_file)

for i, store_income_dict in enumerate(store_income_json):
    print(f'\n第 {i} 筆 Post 資料')
    income_year = store_income_dict['income_year']
    income_month = store_income_dict['income_month']
    income = store_income_dict['income']
    branch_title = store_income_dict['branch.title']
    print(f'income_year: {income_year} income_month: {income_month} income: {income} branch.title: {branch_title}')
    