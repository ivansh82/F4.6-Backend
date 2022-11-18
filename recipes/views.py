from rest_framework.views import APIView
from rest_framework import viewsets, permissions, generics  # new
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .models import Category, Recipe
from .serializers import CategorySerializer, RecipeSerializer


class RecipeAPIView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    filterset_fields = ['category']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CategoryAPIView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#
# class RecipePhotoUpload(APIView):
#     permission_classes = (permissions.IsAuthenticated,)
#     parser_classes = [MultiPartParser, FormParser]
#     serializer_class = RecipeSerializer
#
#     def post(self, request, format=None):
#         serializer = RecipeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def perform_create(self, serializer):
#         serializer.save(id=self.request.id)
