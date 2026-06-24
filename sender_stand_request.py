import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

# Para  revisar que todo en el post new user name esta ok = 201
response = post_new_user(data.user_body)

#print(response.status_code)
# Para obtener authToken
#print(response.json())
# Para concatenar authToken a la palabra Bearer
# ("Bearer " + response.json()["authToken"])

# Para crear el kit
def post_new_client_kit(kit_body, auth_token):
    current_headers = data.headers.copy()
    current_headers['Authorization'] = 'Bearer ' + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=current_headers)