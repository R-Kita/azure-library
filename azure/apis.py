from rest_framework import viewsets, routers
from .models import Post
from .serializers import PostSerializer
 
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
 
router = routers.DefaultRouter()
router.register(r'novels', PostViewSet)

