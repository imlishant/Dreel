# import viewsets
from rest_framework import viewsets
 
# import local data
from .serializers import GeeksSerializer
from .models import GeeksModel
 
# Create your views here.

# 1. description
## 2. video se caption
## 3. time cut silnce remover. stable timecutt.
# 4. video pe video merge 
# 5. photo frame by frame overlay



# create a viewset
 
class GeeksViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = GeeksModel.objects.all()
 
    # specify serializer to be used
    serializer_class = GeeksSerializer