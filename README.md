# Clone Instagram Project

### 기술 스택
----------------------
Python, Django, Mysql, Jquery, Ajax, html, css, aws ec2
### 프로젝트 설명
----------------------
Django를 기반으로 만든 유명한 소셜 네트워크 서비스를 Clone 해보기
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
#### 로그인

* 사이트 접속 시 로그인 창 및 회원가입과 로그인 구현
  
  ![로그인 성공](https://github.com/jinheumkim/insta-ec2/assets/126999253/ba7bb728-ca28-431b-a3a3-dc2678c01aa7)
  
* 로그아웃 구현
  
  ![로그아웃](https://github.com/jinheumkim/insta-ec2/assets/126999253/124da3bc-5873-4215-ba65-6ee0cb99c399)

* 회원가입 시 make_password를 사용하여 패스워드 암호화
* 회원 가입 시 validate_email을 사용하여 email 형식에 맞지 않을 시 에러 반환
  
  ![이메일 틀림](https://github.com/jinheumkim/insta-ec2/assets/126999253/04d5f4fc-af86-4a59-b2d3-994e33db8ae0)

* 회원 가입 시validate_password를 사용하여 비밀번호가
  8자리 이상, 반복되는 비밀번호, 숫자/영어/특수문자 중 2가지 이상 포함되지 않을 시 에러 반환

  ![전부 숫자로 된 이메일](https://github.com/jinheumkim/insta-ec2/assets/126999253/11445ae4-2bdb-491b-9fd7-57de8feba179)


#### 메인 화면

* 팔로우/언팔로우 구현
  
 ![팔로우 언팔로우](https://github.com/jinheumkim/insta-ec2/assets/126999253/563e082e-b7f0-4246-9cd4-7c5313c2c627)

* 피드 업로드 구현
  
  ![피드 업로드](https://github.com/jinheumkim/insta-ec2/assets/126999253/5e15f742-0a28-4d8c-83b8-c03fe5a808cd)

* 피드에 좋아요 기능 구현 및 좋아요 개수 반영
  
  ![좋아요 북마크 프로필적용](https://github.com/jinheumkim/insta-ec2/assets/126999253/c48b818e-22a6-45c6-9260-00ca5a5af5a8)
  
* 피드에 북마크 기능 ajax로 새로고침 없이 바로 적용 가능
* 피드에 댓글달기 기능 ajax로 새로고침 없이 컨텐츠 업로드 가능
  
  ![댓글 달기](https://github.com/jinheumkim/insta-ec2/assets/126999253/f1f2977c-cad3-441c-9d2b-34c6602394bf)
  
* 피드의 '''누를 시 본인이 누르면 피드 삭제기능, 타인이 누르면 팔로우/언팔로우 기능
  
  ![로그인에 맞는 피드 메뉴 (2)](https://github.com/jinheumkim/insta-ec2/assets/126999253/fc16bd97-7bf9-4b06-9505-0c98cbc1c592)

* 각각 유저의 사진 클릭 시 프로필에 접속
  
 ![아이디 별 프로필 사이트](https://github.com/jinheumkim/insta-ec2/assets/126999253/4af755a4-83b1-4314-90f2-bb34834eed46)

* 유저 검색 기능 구현
  
  ![검색 창](https://github.com/jinheumkim/insta-ec2/assets/126999253/4cb990f8-db8c-4959-9ca6-04f37cd38caa)

* 피드 이미지 클릭 시 확대, 다시 클릭 시 축소 기능
  
  ![사진 클릭시 원본 확대](https://github.com/jinheumkim/insta-ec2/assets/126999253/22b45084-b153-4132-95ae-321501bc5f44)


#### 프로필 화면

* 본인 프로필만 프로필 사진 변경 가능
  
  ![로그인 된 프로필에만 프로필 사진 변경](https://github.com/jinheumkim/insta-ec2/assets/126999253/ba1ca149-a09b-402a-8a0a-fefa22b20cd5)
  
* 프로필 사진 변경
  
  ![프로필 사진 변경](https://github.com/jinheumkim/insta-ec2/assets/126999253/4d30a835-c183-49bf-848b-936c534be0ea)

* 개개인 유저 프로필마다 게시물 수, 팔로워 수, 팔로잉 수 표시
* 유저 프로필마다 내 게시물, 좋아요, 북마크 목록을 피드 이미지로 표시
* 개인의 피드 페이지 구현
* 각각의 피드 이미지 클릭 시 해당 게시물로 스크롤 자동이동
  
  ![해당 피드로 자동 스크롤](https://github.com/jinheumkim/insta-ec2/assets/126999253/7e5a74d4-9853-4746-b0e4-e8691a6ac211)


### Aws로 ubuntu 서버 사용
* putty 사용
* nginx/uwsgi 사용하여 상시로 서버 띄워놓기
* docker 사용, mysql image 사용하여 mysql 연동
* vscode Database Client JDBC로 mysql database를 vscode로 연동
* ubuntu 서버의 uwsgi.ini에 database 정보 os.environ.get으로 숨겨두기
* settings_local.py로 메인서버에 개입하지 않고 python manage.py runserver --settings=insta.settings_local로 로컬서버 접속하여 테스트 가능

### Git Actions
---------------------
##### * Django CI로 VSCODE COMMIT시 파이썬 3.8 3.9버전으로 회원가입과 로그인 테스트 후 성공시 CD 진행시키기 자동화
##### * Django CD로 aws cloud 서비스로 띄워놓은 ubuntu 서버 접속 후
##### * cd /home/ubuntu/insta-ec2 ---> git pull ---> sudo systemctl restart uwsgi로 nginx/uwsgi로 상시 띄워놓은 서버에 자동 적용시키기

### settings.py database 정보 및 Actions 정보
--------------------
#### settings
DATABASES = {
    
    'default': {
        
        'ENGINE': 'django.db.backends.mysql',
        
        'NAME': 'insta',
        
        'HOST' : os.environ.get,
        
        'USER' : os.environ.get,
        
        'PASSWORD' : os.environ.get,
        
        'PORT' :'3306',
    
        'OPTIONS' : {'charset' : 'utf8mb4'},

    }

}
#### Actions
  host : ${{ secrets.HOST }}
  
  username : ${{ secrets.USERNAME }}
  
  key : ${{secrets.KEY}}

  port : 22
