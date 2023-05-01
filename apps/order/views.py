from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user.pk)
    
    @action(methods=['GET'], detail=True)
    def confirm(self, request, pk):
        order = Order.objects.get(pk=pk)
        order.status = 'in_process'
        order.save()
        return Response({'message': 'Zakaz v prosesse obrabotki'}, status=200)
    
    def get_permissions(self):
        if self.action == 'confirm':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]
        return super().get_permissions()


# class UserViewSet(viewsets.ViewSet):
#     # With cookie: cache requested url for each user for 2 hours
#     @method_decorator(cache_page(60*60*2))
#     @method_decorator(vary_on_cookie)
#     def list(self, request, format=None):
#         content = {
#             'user_feed': request.user.get_user_feed()
#         }
#         return Response(content)


# class ProfileView(APIView):
#     # With auth: cache requested url for each user for 2 hours
#     @method_decorator(cache_page(60*60*2))
#     @method_decorator(vary_on_headers("Authorization",))
#     def get(self, request, format=None):
#         content = {
#             'user_feed': request.user.get_user_feed()
#         }
#         return Response(content)


# class PostView(APIView):
#     # Cache page for the requested url
#     @method_decorator(cache_page(60*60*2))
#     def get(self, request, format=None):
#         content = {
#             'title': 'Post title',
#             'body': 'Post content'
#         }
#         return Response(content)