from rest_framework.viewsets import ModelViewSet
from .models import Project, Measurement
from .serializers import ProjectModelSerializer, MeasurementModelSerializer


class ProjectApiView(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializer


class MeasurementApiView(ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementModelSerializer


