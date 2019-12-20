from django.urls import path
# from blogs.api.views import api_detail_blog_view
from blogs.api import views

app_name = 'blog'

urlpatterns = [
    # path('<slug>/',api_detail_blog_view,name='detail'),
    path('<slug>/',views.BLogDetail.as_view(),name='detail'),
    path('create',views.CreateBlog.as_view(),name="create"),
    path('',views.AllBlogs.as_view(),name="all-blogs")


]
