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
* 피드에 좋아요 기능 구현
* 피드에 북마크 기능 ajax로 새로코침 없이 바로 적용 가능
* 피드에 댓글달기 기능 ajax로 새로고침 없이 컨텐츠 업로드 가능
* 각각 유저의 사진 클릭 시 프로필에 접속
* 유저 검색 기능 구현
  
##### 프로필
* 접속한 프로필에 대해 프로필 사
