from uuid import uuid4
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed, Reply, Like, Bookmark
from user.models import User,Follow
import os
from insta.settings import MEDIA_ROOT
import random


# Create your views here.
class Main(APIView):
    def get(self, request):
        email = request.session.get('email',None)
        if email is None:
            return render(request, "user/login.html")
        
        feed_object_list = Feed.objects.all().order_by('-id')
        feed_list = []
        for feed in feed_object_list:
            user = User.objects.filter(email = feed.email).first()
            login = User.objects.filter(email = email).first()
            reply_object_list = Reply.objects.filter(feed_id = feed.id)
            reply_list = []
            for reply in reply_object_list:
                user = User.objects.filter(email = reply.email).first()
                reply_list.append(dict(reply_content = reply.reply_content,
                                       nickname = user.nickname))
            like_count = Like.objects.filter(feed_id = feed.id, is_like = True).count()
            Feed.objects.filter(email = feed.email, id = feed.id).update(like_count = like_count)
            is_liked = Like.objects.filter(feed_id = feed.id, email = email, is_like = True).exists()
            is_marked = Bookmark.objects.filter(feed_id = feed.id, email = email, is_marked = True).exists()
            login = User.objects.filter(email = email).first()
            delete = Feed.objects.filter(email = login.email, nickname = feed.nickname).exists()
            followed = Follow.objects.filter(user_id = login.id, following_id = user.id).exists()
            feed_list.append(dict(id = feed.id,
                                  image = feed.image,
                                  like_count = like_count,
                                  content = feed.content,
                                  profile_image = user.profile_image,
                                  nickname = user.nickname,
                                  reply_list = reply_list,
                                  is_liked = is_liked,
                                  is_marked = is_marked,
                                  delete = delete,
                                  user = user,
                                  followed = followed
                                  ))
            
        follow_object_list = User.objects.exclude(email = email)
        follow_list = []
        for follow in follow_object_list:
            login = User.objects.filter(email = email).first()
            followed = Follow.objects.filter(user_id = login.id, following_id = follow.id).exists()
            user = User.objects.filter(email = follow.email).first()
            follow_list.append(dict(id = login.id,
                                    profile_image = follow.profile_image,
                                    nickname = follow.nickname,
                                    name = follow.name,
                                    following_id = follow.id,
                                    followed = followed,
                                    user= user
                                    ))
                     
        user = User.objects.filter(email = email).first()
        
        if user is None:
                return render(request, "user/login.html")
            
            
        
        
        return render(request, "insta/main.html",context = dict(feeds = feed_list, user = user, follows = follow_list))
    
    
    
    

class UploadFeed(APIView):
    def post(self, request):
        
        file = request.FILES['file']
        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT,uuid_name)
        
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        image = uuid_name
        content = request.data.get('content')
        email = request.session.get('email',None)
        user = User.objects.filter(email = email).first()
        
        Feed.objects.create(image = image, content = content, email = email, nickname = user.nickname ,user_id = user.id)
        
        return Response(status=200)
    
class Profile(APIView):
    def get(self, request, id):
        email = request.session.get('email',None)
        
        if email is None:
            return render(request, "user/login.html")
        
        
        user = User.objects.filter(email = email).first()
        
        if user is None:
            return render(request, "user/login.html")
        
        
        user = User.objects.get(id = id)
        
        feed_list = Feed.objects.filter(email = user.email)
        like_list = list(Like.objects.filter(email = user.email, is_like = True).values_list('feed_id', flat = True))
        like_feed_list = Feed.objects.filter(id__in = like_list)
        bookmark_list = list(Bookmark.objects.filter(email = user.email, is_marked = True).values_list('feed_id',flat = True))
        bookmark_feed_list = Feed.objects.filter(id__in = bookmark_list)
        feed_list_count = Feed.objects.filter(email = user.email).count()
        following_count = Follow.objects.filter(user_id = user.id).count()
        follower_count = Follow.objects.filter(following_id = user.id).count()
        return render(request, "content/profile.html" , context = dict(user = user, 
                                                                       feed_list = feed_list,
                                                                       like_feed_list = like_feed_list,
                                                                       bookmark_feed_list = bookmark_feed_list,
                                                                       following_count = following_count,
                                                                       feed_list_count = feed_list_count,
                                                                       follower_count = follower_count,
                                                                       ))
    
class UploadReply(APIView):
    def post(self, request):
        
        feed_id = request.data.get('feed_id', None)
        reply_content = request.data.get('reply_content', None)
        email = request.session.get('email',None)
        
        Reply.objects.create(feed_id=feed_id, reply_content=reply_content, email=email)
        
        return Response(status=200) 
    
    
class ToggleLike(APIView):
    def post(self, request):
        # 좋아요, 해제 반복하면 id 숫자 늘어남
        feed_id = request.data.get('feed_id', None)
        favorite_text = request.data.get('favorite_text', True)
        
        # email = request.session.get('email', None)
        
        # if favorite_text == 'favorite_border':
        #     Like.objects.create(feed_id = feed_id, is_like = True, email = email)
            
        # else :
        #     Like.objects.filter(feed_id =feed_id, email = email).delete()
        
        # id 숫자 줄이기
        
        if favorite_text == 'favorite_border':
            is_like = True
        else :
            is_like = False
            
        email = request.session.get('email',None)
        
        like = Like.objects.filter(feed_id=feed_id , email = email).first()
        
        
        if like:
            like.is_like = is_like
            like.save()
        else:
            Like.objects.create(feed_id=feed_id, is_like=is_like, email = email)
        
        return Response(status=200)
    
class ToggleBookmark(APIView):
    def post(self, request):
        # 북마크, 해제 반복하면 id 숫자 늘어남
        
        email = request.session.get('email', None)
        
        feed_id = request.data.get('feed_id', None)
        bookmark_text = request.data.get('bookmark_text', True)
        
        if bookmark_text == 'bookmark_border':
            Bookmark.objects.create(feed_id = feed_id, is_marked = True, email = email)
            
        else :
            Bookmark.objects.filter(feed_id =feed_id, email = email).delete()
        
        # id 숫자 줄이기
        
        # if bookmark_text == 'bookmark_border':
        #     is_marked = True
        # else :
        #     is_marked = False
            
        # email = request.session.get('email',None)
        
        # bookmark = Bookmark.objects.filter(feed_id=feed_id , email = email).first()
        
        # if bookmark:
        #     bookmark.is_marked = is_marked
        #     bookmark.save()
        # else:
        #     Bookmark.objects.create(feed_id=feed_id, is_marked=is_marked, email = email)
        
        return Response(status=200)
    
class Follows(APIView):    
    def post(self,request):
        follow_text = request.data.get('follow_text', None)
        user_id = request.data.get('user_id',None)
        following_id = request.data.get('following_id', None)
        
        if follow_text == '언팔로우':
            Follow.objects.filter(user_id = user_id, following_id = following_id).delete()
        else :
            Follow.objects.create(user_id = user_id, following_id = following_id)
        
            
        return Response(status = 200)
    
class FeedDelete(APIView):
    def post(self,request):
        email = request.session.get('email', None)
        feed_id = request.data.get('feed_id', None)
        
        if Feed.objects.filter(email = email, id = feed_id).exists():
            Feed.objects.filter(email = email, id = feed_id).delete()
            Like.objects.filter(email = email, feed_id = feed_id).delete()
            Reply.objects.filter(email = email, feed_id = feed_id ).delete()
            Bookmark.objects.filter(email = email, feed_id = feed_id).delete()
            
        return Response(status=200)
    

def Search_view(request):
    email  = request.session.get('email',None)
    if email is None:
        return render(request, 'user/login.html')
    
    query = request.GET.get('q', '')  # 검색어를 가져옴

    # 검색어가 존재하는 경우, 해당하는 모델을 필터링
    if query:
        results = User.objects.filter(nickname__icontains=query)
    else:
        results = User.objects.all()


    user = User.objects.filter(email = email).first()
    if user is None:
        return render(request, 'user/login.html')

    
    return render(request, 'content/search.html', context = dict(user = user,results = results, query = query))
