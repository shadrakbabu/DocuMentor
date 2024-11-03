from django.urls import path # type: ignore
from .import views
from .views import resources_view
from .views import refer_video
from .views import add_comment
from .views import community_view, community_detail
from django.urls import path # type: ignore
from .views import add_comment, community_view  # Import your views
from .views import file1_view
from .views import home_view
from .views import search
from django.urls import path # type: ignore

urlpatterns = [
    path('', views.landingpage, name='landingpage',),
    path('login/', views.login, name='login',),
    path('login/submit/',views.temp,name='temp',),
    path('login/logout/', views.logout, name="logout"),
    path('Signup/', views.Signup,name="Signup"),
    path('Signup/submit/',views.pemp1,name= 'pemp1'),

    path('search/', search, name='search'),


    path('community/', community_view, name='community'),
    path('community/<int:post_id>/', views.community_detail, name='community_detail'),
    path('home/', home_view, name='home'),



    path('ask/', views.ask, name='ar',),
    path('recommendations/', views.recommendations, name='recommendations',),

    # resources link changed
    path('resources/', resources_view, name='resources'),

    # ended changing the resources
    path('file1/', file1_view, name='file1'),
    path('upload/', views.upload, name='upload',),

    # changed the referring link
    path('refer-video/', refer_video, name='refer_video'),

    # endded changing
    path('log/', views.log, name='log',),
    path('comment/', views.comment, name='comment',),
    path('community/', views.community_view, name='community'),
    path('resources/', views.resources_view, name='resources'),


    path('tutorials/', views.list_tutorials, name='tutorials'),
    
    path('create-post/', views.create_post, name='create_post'),
    path('upload-document/', views.upload_document, name='upload_document'),
    path('refer-video/', views.refer_video, name='refer_video'),

    # comment button
    # path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),
    path('add_comment/<int:post_id>/', add_comment, name='add_comment'),

    path('add_comment/<int:post_id>/', views.add_comment, name='add_comment'),

    # resources

    path('resources/<int:resource_id>/', views.resource_detail, name='resource_detail'),
    path('tutorials/<int:tutorial_id>/', views.tutorial_detail, name='tutorial_detail'),

    path('terms-and-conditions/', views.terms_and_conditions, name='terms_and_conditions'),

    # community view
    path('community/', community_view, name='community'),
    path('add_comment/<int:post_id>/', add_comment, name='add_comment'),

]







