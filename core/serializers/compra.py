from rest_framework.serializers import CharField, ModelSerializer

from core.models import Compra

class CompraSerializer(ModelSerializer):
    class Meta:
        model = Compra
        fields = "__all__"

class CompraSerializer(ModelSerializer):
    usuario = CharField(source="user.email", read_only=True) # inclua essa linha

class CompraSerializer(ModelSerializer):
    status = CharField(source="get_status_display", read_only=True) # inclua essa linha