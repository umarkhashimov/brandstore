from django.contrib import admin

# Register your models here.


from .models import ProdutsModel, ColorsModel, SizesModel, TagsModel


admin.site.register(ProdutsModel)
admin.site.register(TagsModel)
admin.site.register(ColorsModel)
admin.site.register(SizesModel)