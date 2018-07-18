from django.conf.urls import url
from my_app import views

app_name="my_app"

urlpatterns=[
    url(r'^$',views.PostListView.as_view(),name="post_list"),
    url(r'^about/$',views.AboutView.as_view(),name="about"),
    url(r'^post/(?P<pk>\d+)$',views.PostDetailView.as_view(),name="post_detail"),
    url(r'post/create/$',views.CreatePost,name="create_post"),
    url(r'^post/(?P<pk>\d+)/update$',views.UpdatePostView.as_view(),name="update_post"),
    url(r'^post/(?P<pk>\d+)/delete$',views.DeletePostView.as_view(),name="delete_post"),
    url(r'^draft/$',views.DraftPostView.as_view(),name="draft_post"),
    url(r'^post/(?P<pk>\d+)/publish/$',views.publish_post,name="publish_post"),
    url(r'^post/(?P<pk>\d+)/comment$',views.add_comment,name="comment_post"),
    url(r'^comment/(?P<pk>\d+)/update$',views.UpdateCommentView.as_view(),name="update_comment"),
    url(r'^comment/(?P<pk>\d+)/delete$',views.comment_remove,name="delete_comment"),
    url(r'^post/(?P<pk>\d+)/commentlist$',views.CommentListView.as_view(),name="comment_list"),
    url(r'^register/$',views.reg,name="register"),
    url(r'^accounts/profile/$',views.profile,name="profile"),
    url(r'^profile/$',views.ProfileView.as_view(),name="user_profile"),
    
    
]
