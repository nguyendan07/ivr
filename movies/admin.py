from django.contrib import admin

from .models import Movie, Show, Theater


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'digits')
    list_filter = ('title',)


@admin.register(Show)
class ShowAdmin(admin.ModelAdmin):
    list_display = ('movie', 'theater', 'starts_at')
    list_filter = ('movie', 'theater', 'starts_at',)


@admin.register(Theater)
class TheaterAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'digits')
    list_filter = ('name', 'address',)


# admin.site.register(Movie)
# admin.site.register(Show)
# admin.site.register(Theater)
