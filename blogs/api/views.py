from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView

from django.http import Http404

from blogs.models import Blog
from blogs.api.serializers import BlogSerializer 
from rest_framework.pagination import PageNumberPagination
# @api_view(['GET',])
# def api_detail_blog_view(request, slug):

#     try:
#         blog = Blog.objects.get(slug=slug)
#     except Blog.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method =='GET':
#         serializer = BlogSerializer(blog)
#         return Response(serializer.data)



#paginations classes
class SmallPagesPagination(PageNumberPagination):
    page_size = 5




#View classes

class BLogDetail(APIView):

    def get_object(self, slug):
        try:
            return Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            raise Http404

    def get(self, request, slug, format=None):
        Blog = self.get_object(slug)
        serializer = BlogSerializer(Blog)
        return Response(serializer.data)

    def put(self, request, slug, format=None):
        Blog = self.get_object(slug)
        serializer = BlogSerializer(Blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, slug, format=None):
        Blog = self.get_object(slug)
        Blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CreateBlog(CreateAPIView):

    def post(self, request, format=None):
    	serializer = BlogSerializer(data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AllBlogs(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = SmallPagesPagination

#
# class BlogList(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAdminUser]
#
#     def list(self, request):
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         queryset = self.get_queryset()
#         serializer = UserSerializer(queryset, many=True)
#         return Response(serializer.data)
