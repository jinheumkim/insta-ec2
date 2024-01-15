from django.urls import path
from .views import UploadFeed,Profile,UploadReply,Main,ToggleLike,ToggleBookmark,Follows,FeedDelete,Search_view

urlpatterns = [
    path('upload',UploadFeed.as_view()),
    path('reply', UploadReply.as_view()),
    path('profile/<int:id>',Profile.as_view(), name = 'profile'),
    path('bookmark',ToggleBookmark.as_view()),
    path('main',Main.as_view()),
    path('like',ToggleLike.as_view()),
    path('follow',Follows.as_view()),
    path('delete',FeedDelete.as_view()),
    path('search',Search_view, name = 'search')
]