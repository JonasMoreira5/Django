# Importamos a função index() definida no arquivo views.py
from . import views

app_name = 'website'

# urlpatterns contém a lista de roteamentos de URLs
urlpatterns = [
    # GET/
    __path__('',views.index, name='index'),
]