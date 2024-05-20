from django.urls import path, include
from rest_framework import routers
from .views import blogApiView, categoryApiView, CategoryPostApiView, PopularPostApiView


router = routers.SimpleRouter()
#dang ki view voi router 
router.register('blogs', blogApiView, basename='blogs')
router.register('category', categoryApiView, basename='category')
router.register('catgoryBaseBlogs', CategoryPostApiView, basename='categoryBaseBlogs')
router.register('PopularPostApiView', PopularPostApiView, basename='PopularPostApiView')


#them URL cua router vao URL trong goc cua ung dung
urlpatterns = [
    path('', include(router.urls))
]