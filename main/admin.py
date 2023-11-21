from django.contrib import admin

# Register your models here.


class ForumAdmin(admin.ModelAdmin):
    list_display = ('user', 'BookName', 'forumsDescription', 'dateOfPosting')

