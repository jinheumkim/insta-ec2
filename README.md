# Clone Instagram Project

### 기술 스택
----------------------
Python, Django, Mysql, Jquery, Ajax
### 프로젝트 설명
----------------------
Django를 기반으로 만든 유명한 소셜 네트워크 서비스를 Clone 해보기
### 구현 한 사이트 주소
----------------------
http://jinheum.duckdns.org/main
### 프로젝트 구조
----------------------
Project
 * Insta
Apps
 * Content
 * User

![insta tree 1](https://github.com/jinheumkim/insta-ec2/assets/126999253/b00db149-e357-4d12-bb22-b7a96a03f1d5)

### ERD
-------------------
![insta erd](https://github.com/jinheumkim/insta-ec2/assets/126999253/193e71e8-02dd-4c4f-8efa-ff07a3c49d72)

### 구현 기능
--------------------
##### 로그인
* 사이트 접속 시 로그인 창 및 회원가입과 로그인 구현
* 회원가입 시 make_password를 사용하여 패스워드 암호화

##### 메인
* 피드 올리기 및 팔로우/언팔로우 구현
* 피드에 좋아요 기능 구현 및 좋아요 개수 반영
* 피드에 북마크 기능 ajax로 새로코침 없이 바로 적용 가능
* 피드에 댓글달기 기능 ajax로 새로고침 없이 컨텐츠 업로드 가능
* 각각 유저의 사진 클릭 시 프로필에 접속
* 유저 검색 기능 구현
  
##### 프로필
* 접속한 프로필에만 프로필 사진 변경 기능 구현
* 개개인 유저 프로필마다 게시물 수, 팔로워 수, 팔로잉 수 표시
* 유저 프로필마다 게시물, 좋아요, 북마크 목록을 피드 이미지로 표시

### Aws로 ubuntu 서버 사용
* putty 사용
* nginx/uwsgi 사용하여 상시로 서버 띄워놓기
* docker 사용, mysql image 사용하여 mysql 연동
* vscode Database Client JDBC로 mysql database를 vscode로 보기
* ubuntu 서버의 uwsgi.ini에 database 정보 os.environ.get으로 숨겨두기

### Git Actions
---------------------
##### * Django CI로 VSCODE COMMIT시 파이썬 3.8 3.9버전으로 회원가입과 로그인 테스트 후 성공시 CD 진행시키기 자동화
##### * Django CD로 aws cloud 서비스로 띄워놓은 ubuntu 서버 접속 후
##### * cd /home/ubuntu/insta-ec2 ---> git pull ---> sudo systemctl restart uwsgi로 nginx/uwsgi로 상시 띄워놓은 서버에 자동 적용시키기

### settings.py database 정보 및 Actions 정보
--------------------
##### settings
DATABASES = {
    
    'default': {
        
        'ENGINE': 'django.db.backends.mysql',
        
        'NAME': 'insta',
        
        'HOST' : os.environ.get('MYSQL_HOST','localhost'),
        
        'USER' : os.environ.get('MYSQL_USER_NAME','admin'),
        
        'PASSWORD' : os.environ.get('MYSQL_PASSWORD','default_password'),
        
        'PORT' :'3306',
    
        'OPTIONS' : {'charset' : 'utf8mb4'},

    }

}
##### Actions
  host : ${{ secrets.HOST }}
  
  username : ${{ secrets.USERNAME }}
  
  key : ${{secrets.KEY}}

  port : 22

host, username,  key 정보를    Settings ---> Secrets and variabls ---> actions ---> Repository Secrets에 숨겨두기
