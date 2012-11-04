from django.contrib import admin
from ajibita.models import SeccoesModelForm, Seccoes

class SeccoesAdmin(admin.ModelAdmin):
    form = SeccoesModelForm
    class Media:
        js = ('/js/tinymce/jscripts/tiny_mce/tiny_mce.js', '/js/textareas.js')

admin.site.register(Seccoes, SeccoesAdmin)