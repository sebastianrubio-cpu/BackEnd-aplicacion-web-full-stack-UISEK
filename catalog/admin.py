from django.contrib import admin
from catalog.models.director import Director
from catalog.models.vendedor import Vendedor  
from catalog.models.pelicula import Pelicula


@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fecha_nacimiento', 'premios_ganados')
    search_fields = ('nombre',)

@admin.register(Vendedor)
class VendedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo')
    search_fields = ('nombre',)
    list_filter = ('tipo',)

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'duracion', 'fecha_lanzamiento', 'director')
    search_fields = ('nombre', 'director__nombre')
    list_filter = ('director', 'vendedores')
    filter_horizontal = ('vendedores',)  # Facilita la asignación de relación Many-to-Many en el panel