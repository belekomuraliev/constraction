from django.contrib import admin
from .models import *





@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    actions_on_top = False
    actions_on_bottom = True
    list_display = ('block_number', 'amount_entry', 'amount_apartments_floor', 'ammount_floors',
                    'total_apartment', 'total_sum')
    list_display_links = ('block_number',)


    @admin.display(description='Общая колличеств квартир')
    def total_apartment(self, obj):
        return f'{obj.amount_apartments_floor  * obj.ammount_floors} квартир в блоке № {obj.block_number}'


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    date_hierarchy = 'sale_date'
    actions_on_top = False
    actions_on_bottom = True
    list_display = ( 'owner', 'sale_date', 'status', 'total_area', 'total_sum_aparment' )
    search_fields = ('owner',)
    ordering = ('sale_date',)
    list_editable = ('sale_date',)





