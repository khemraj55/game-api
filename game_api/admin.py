from django.contrib import admin
from .models import Game,User

class UserAdmin(admin.ModelAdmin):
    list_display=("username","email")
class GameAdmin(admin.ModelAdmin):
  list_display = ('game_id', 'is_palindrome', 'user')
  
  def is_palindrome(self, obj):
    return obj.string == obj.string[::-1]

admin.site.register(Game, GameAdmin)
admin.site.register(User,UserAdmin)
