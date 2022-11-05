# settings.py

# python manage.py runserver
- 서버 실행

# python manage.py migrate
- 데이터 베이스 초기화. 
- db.sqlite3 생성됨.

# python manage.py createsuperuser
- 관리자 계정 생성

# http://127.0.0.1:8000/admin/auth/user/
- 관리자 페이지 

# 블로그앱 python manage.py startapp blog

# 싱글 페이지 앱 python manage.py startapp single_pages

# 데이터 베이스 모델의 구조가 변경 되었을 때
- python manage.py makemigrations
- python manage.py migrate

# setting.py에 앱등록
```py
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.staticfiles',
'blog',
'single_pages',
]
```

# 관리자 페이지에 모델 추가(blog/admin.py) 

