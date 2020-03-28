from ..models import Post
from . import serializers
from rest_framework import generics, status
from rest_framework.response import Response


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def perform_create(self, serializer):  # 重写原来的方法
        serializer.save(owner=self.request.user)  # 储存当前用户信息
        super(PostCreateView, self).perform_create(serializer)  # 继承原来的方法
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Successfully created',
                    'result': self.request.data}
        return Response(response)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer

    def retrieve(self, request, *args, **kwargs):  # 重写原来读取方法
        super(PostDetailView, self).retrieve(request, args, kwargs)  # 继承原来的方法
        instance = self.get_object()  # 获得实例
        serializer = self.get_serializer(instance)  # 序列化
        data = serializer.data  # 变成数据
        response = {'status_code': status.HTTP_200_OK,
                    'message': "Successfully retrieved",
                    'result': data}
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super(PostDetailView, self).patch(request, args, kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Successfully updated',
                    'result': data}
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super(PostDetailView, self).delete(request, args, kwargs)
        response = {'status_code': status.HTTP_200_OK,
                    'message': 'Successfully deleted'}
        return Response(response)
