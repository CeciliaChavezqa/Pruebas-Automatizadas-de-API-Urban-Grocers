import sender_stand_request
import data

#Para recibir el nombre del kit
def get_kit_body(kit_name):
    current_kit_body = data.kit_body.copy()
    current_kit_body['name'] = kit_name
    return current_kit_body
# Para recibir authtoken
def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]
# Definición de Pruebas
def possitive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token())
    assert response.status_code == 201

def negative_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body,get_new_user_token())
    assert response.status_code == 400

# Pruebas

def test_1_nombre_del_kit_con_1_caracter():
    current_body = get_kit_body("a")
    possitive_assert(current_body)

def test_2_nombre_del_kit_con_511_caracteres():
    current_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    possitive_assert(current_body)

def test_3_nombre_del_kit_sin_caracteres():
    current_body = get_kit_body("")
    negative_assert(current_body)

def test_4_nombre_del_kit_con_512_caracteres():
    current_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(current_body)

def test_5_nombre_del_kit_con_caracteres_especiales():
    current_body = get_kit_body("№%@")
    possitive_assert(current_body)

def test_6_nombre_del_kit_con_espacios():
    current_body = get_kit_body(" A Aaa ")
    possitive_assert(current_body)

def test_7_nombre_del_kit_con_numeros():
    current_body = get_kit_body("123")
    possitive_assert(current_body)

def test_8_nombre_del_kit_sin_parametro_en_la_solicitud():
    current_body = get_kit_body()
    negative_assert(current_body)

def test_9_nombre_del_kit_con_parametro_en_la_solicitud_tipo_int():
    current_body = get_kit_body(123)
    negative_assert(current_body)