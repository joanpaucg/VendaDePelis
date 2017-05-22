from django.contrib import admin
import models
# Register your models here.
admin.site.register(models.Actor)
admin.site.register(models.Film)
admin.site.register(models.Review)
admin.site.register(models.FavouriteList)
admin.site.register(models.UserProfile)