from django.urls import path
from post import views

urlpatterns = [
    path('pub_post', views.PublicPostView.as_view(), name='pub_post'),
    path('post_detail/<int:pk>', views.PostDetailView.as_view(), name='post_detail'),
    path('comment/<int:post_id>', views.PostCommentView.as_view(), name='comment'),
    path('reply', views.ReplyView.as_view(), name='reply'),
]
