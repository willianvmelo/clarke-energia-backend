from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Supplier
from .serializers import SupplierSerializer

class SupplierFilterView(APIView):
    def post(self, request):

        consumption = request.data.get('consumption')
        
        if consumption is not None:
            
            suppliers = Supplier.objects.filter(min_kwh_limit__lt=consumption)
            serializer = SupplierSerializer(suppliers, many=True)

            if not serializer.data:
                return Response({"error": "Nenhum fornecedor corresponde ao filtro"}, status=status.HTTP_404_NOT_FOUND)
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response({"error": "Consumo não informado."}, status=status.HTTP_400_BAD_REQUEST)