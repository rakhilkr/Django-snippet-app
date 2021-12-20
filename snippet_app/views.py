from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer, SnippetSerializer, TagSerializer
from django.contrib.auth.models import User
from rest_framework import viewsets, serializers, status
from .models import Snippet


class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })


class HelloView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'Hello, Welcome to snippet app.'}
        return Response(content)

class SnippetView(APIView):
	permission_classes = (IsAuthenticated, )
	serializer_class = SnippetSerializer

	def get(self, request, format=None):
		snippets = Snippet.objects.all()
		serializer = self.serializer_class(snippets, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request):
		serializer = SnippetSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({
				"status": status.HTTP_201_CREATED,
				"data": serializer.data,
				"message": 'Snippet created successfully'
	    	})


class SnippetDetailView(APIView):
	permission_classes = (IsAuthenticated, )
	serializer_class = SnippetSerializer

	def get(self, request, id=None, format=None):
		snippets = Snippet.objects.filter(id=id).first()
		serializer = self.serializer_class(snippets)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, id=None):
		snippets = Snippet.objects.filter(id=id).first()
		serializer = SnippetSerializer(snippets, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response({
				"status": status.HTTP_201_CREATED,
				"data": serializer.data,
				"message": 'Snippet updated successfully'
	    	})

	def delete(self, request, id=None):
		snippets = Snippet.objects.filter(id=id).first()
		serializer = self.serializer_class(snippets)
		snippets.delete()
		return Response({
			"status": status.HTTP_201_CREATED,
			"data": serializer.data,
			"message": 'Snippet updated successfully'
    	})


class TagListView(APIView):
	permission_classes = (IsAuthenticated, )
	serializer_class = TagSerializer

	def get(self, request, format=None):
		tags = Tag.objects.all()
		serializer = self.serializer_class(tags, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)


class SnippetByTagView(APIView):
	permission_classes = (IsAuthenticated, )
	serializer_class = SnippetSerializer

	def get(self, request, id=None, format=None):
		snippets = Snippet.objects.filter(tag_id=id).all()
		serializer = self.serializer_class(snippets, many=True)
		return Response(serializer.data, status=status.HTTP_200_OK)
