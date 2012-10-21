from shop.models import Produto, PromocaoModelForm
from shop.models import Promocao
from django.contrib import admin

admin.site.register(Produto)


class PromocaoAdmin(admin.ModelAdmin):
    form = PromocaoModelForm
    class Media:
        js = ('/js/tinymce/jscripts/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Promocao, PromocaoAdmin)