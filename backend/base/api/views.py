from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MeterSerializer
from base.models import Meter
from simple_history.utils import update_change_reason


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]

    return Response(routes)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getMeter(request):
    user = request.user
    meters = Meter.objects.filter(user=user)
    serializer = MeterSerializer(meters, many=True)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def paidBill(request):
    user = request.user
    try:
        meter = Meter.objects.filter(user=user)
        for i in meter:
            if i.Last_recorded_reading != i.Last_billed_reading:
                old_value = i.Last_recorded_reading
                i.Last_billed_reading = old_value
                i.save()
                update_change_reason(Meter, "Paid Bill")
        meters = Meter.objects.filter(user=user)
        serializer = MeterSerializer(meters, many=True)
        return Response(serializer.data)

    except Meter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getMeterId(request, pk):
    try:
        meter = Meter.objects.get(id=pk)
    except Meter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MeterSerializer(meter)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAdminUser])
def getMeterCount(request):
    count = Meter.objects.all().count()
    response = {'count': count}
    return JsonResponse(response)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def UpdateMeter(request, pk):
    try:
        meter = Meter.objects.get(id=pk)
    except Meter.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = MeterSerializer(meter, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        update_change_reason(Meter, "Update Meter")
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
