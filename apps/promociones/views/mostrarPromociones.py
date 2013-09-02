#encoding:utf-8
""" 
	Datos necesarios para la api de Google Places,
	se debe tratar de eliminar el places_api_key 
	de este archivo y colocarlo en un solo archivo
	como lo hace saul en la configurariones.
"""
from googleplaces import GooglePlaces, types, lang
PLACES_API_KEY = 'AIzaSyCy1NFjXXz9R2VV9vaZ0VQVKolvKyazR8k' ### Mi clave de de consola Google
google_places = GooglePlaces(PLACES_API_KEY)


""" Importando el modelo del Usuario """
from django.contrib.auth.models import User

""" 
	importando la funcion que me retorna las
	categorias y tags que más ha consumido el Usuario
"""
from apps.promociones.views.promosSinFiltrar import devolverCategorias
"""
def solicitudApiMisGustos(latlon=""):
	ids_t = None
	types_g = None
	ids_t,types_g = devolverCategorias(us)
	if ids_t and types_g:
		query_result = google_places.nearby_search(
						lat_lng=latlon, 
						radius=5000, 
						types=types_g
						)

"""