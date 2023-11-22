from django.urls import path
from main.views import *

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item,name="create_item"),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete_item/<int:item_id>/', delete_item, name='delete_item'),
    path('add_amount/<int:item_id>/', add_amount, name='add_amount'),
    path('reduce_amount/<int:item_id>/', reduce_amount, name='reduce_amount'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]