from rest_framework import serializers

from apps.products.models import Product
# from apps.products.api.serializers.general_serializers import (
#     MeasureUnitSerializer, CategoryProductSerializer
# )

class ProductSerializer(serializers.ModelSerializer):
    # hay 3 formars de representar valores con FK
    # measure_unit = MeasureUnitSerializer() #lo toma del serializer como otro dict
    # category_product = serializers.StringRelatedField() #lo toma del str del modelo 
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'name': instance.name,            
            'description': instance.description,
            'image': instance.image.url if instance.image != '' else '',
            'measure_unit': instance.measure_unit.description if instance.measure_unit is not None else '',
            'category_product': instance.category_product.description if instance.category_product is not None else ''
        }
    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','deleted_date')