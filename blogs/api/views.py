from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from blogs.models import Blog
from blogs.api.serializers import BlogSerializer

@api_view(['GET',])
def api_detail_blog_view(request, slug):

    try:
        blog = Blog.objects.get(slug=slug)
    except Blog.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        serializer = BlogSerializer(blog)
        return Response(serializer.data)




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
