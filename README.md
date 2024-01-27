# Clone Instagram Project
----------------------
### 기술 스택
----------------------
Python, Django, Mysql, Jquery, Ajax
### 프로젝트 설명
----------------------
Django를 기반으로 만든 유명한 소셜 네트워크 서비스를 Clone 해보기
### 구현 한 사이트 주소
http://jinheum.duckdns.org/main
### 프로젝트 구조
----------------------
Project
 * Insta
Apps
 * Content
 * User
.
├── Insta
│   ├── template
│   │   └── content
│   │   │   └── profile.html
│   │   │   └── search.html
│   │   └── insta
│   │   │   └── main.html
│   │   └── user
│   │   │   └── join.html
│   │   │   └── login.html
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── settings_local.py
│   ├── urls.py
│   └── wsgi.py
├── media
├── content
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── user
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── requirements.txt
├── manage.py
├── venv
├── db.sqlite3
└── .github \ workflows
     ├── django_CI.yml
     └── django_CD.yml
### 구현 기능
--------------------
로그인 기능
