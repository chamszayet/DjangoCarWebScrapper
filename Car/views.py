from django.http import HttpResponse, JsonResponse
from .models import Car
from .serializers import CarSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.db.models import Q


class CarAPIView(APIView):
    #auth_classes = [SessionAuthentication,BasicAuthentication]
  #  auth_classes = (TokenAuthentication,)
   #  permission_calss = (IsAuthenticated,)
    def get(self,request):
        cars = Car.objects.all()
        serializer = CarSerializer(cars,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = CarSerializer(data = request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class CarDetails(APIView):
    auth_classes = (TokenAuthentication,)
    permission_calss = (IsAuthenticated,)
    
    def get_object(self,id):
 
        try:
            return Car.objects.get(id=id)
        except Car.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,id):
        car = self.get_object(id)
        serializer = CarSerializer(car)
        return Response(serializer.data)


    def put(self,request,id):
        car = self.get_object(id)
        serializer = CarSerializer(car,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request , id ):
        car = self.get_object(id)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CarFilterList(generics.ListAPIView):

    serializer_class = CarSerializer

    def get(self, request):
        queryset = self.get_queryset(request)
        serializer = self.serializer_class(queryset, many=True)
        print(serializer.data)
        return JsonResponse(serializer.data, safe=False)

    def get_queryset(self, request):
        queryset = Car.objects.all()
        #carMake = request.query_params.get('carMake')
        #carModel = request.query_params.get('carModel')
        #carMileage = request.query_params.get('carMileage')
        #carColor = request.query_params.get('carColor')
        queries = []
        for _key in request.query_params:
            if _key == "carMake":
                qs = queryset.filter(carMake__icontains=request.query_params.get('carMake'))

            if _key == "carModel":
                qs = queryset.filter(carModel__icontains=request.query_params.get('carModel'))

            if _key == "carMileage":
                qs = queryset.filter(carMileage__icontains=request.query_params.get('carMileage'))

            if _key == "carColor":
                qs = queryset.filter(carColor__icontains=request.query_params.get('carColor'))
            if _key == "carPriceMin":
                qs = queryset.filter(carPrice__gte = request.query_params.get('carPriceMin'))
            if _key == "carPriceMax":
                qs = queryset.filter(carPrice__lte = request.query_params.get('carPriceMax'))
            if _key == "carYear":
                qs = queryset.filter(carYear = request.query_params.get('carYear'))    
            queries.append(qs)
        final_query = None

        if queries != []:
            final_query = queries[0]

        for i in range(1, len(queries)):
            final_query = final_query.intersection(queries[i])

        return final_query



