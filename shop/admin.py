from shop.models import Produto, DestaqueModelForm, Imagem
from shop.models import Destaque
from django.contrib import admin

admin.site.register(Produto)
admin.site.register(Imagem)



class DestaqueAdmin(admin.ModelAdmin):
    form = DestaqueModelForm

    class Media:
        js = ('/js/tinymce/jscripts/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Destaque, DestaqueAdmin)