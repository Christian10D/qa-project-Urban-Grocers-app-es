import sender_stand_request
import data

# Función para modificar el cuerpo del kit
def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

# Función para pruebas positivas
def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Función para pruebas negativas
def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body)
    assert response.status_code == 400

# Pruebas basadas en la lista de comprobación

# 1. El número permitido de caracteres (1)
def test_kit_name_with_1_char():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

# 2. El número permitido de caracteres (511)
def test_kit_name_with_511_chars():
    name = "A" * 511
    kit_body = get_kit_body(name)
    positive_assert(kit_body)

# 3. El número de caracteres es menor que la cantidad permitida (0)
def test_kit_name_with_0_chars():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

# 4. El número de caracteres es mayor que la cantidad permitida (512)
def test_kit_name_with_512_chars():
    name = "A" * 512
    kit_body = get_kit_body(name)
    negative_assert_code_400(kit_body)

# 5. Se permiten caracteres especiales
def test_kit_name_with_special_chars():
    kit_body = get_kit_body("\"№%@\",")
    positive_assert(kit_body)

# 6. Se permiten espacios
def test_kit_name_with_spaces():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)

# 7. Se permiten números
def test_kit_name_with_numbers():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

# 8. El parámetro no se pasa en la solicitud
def test_kit_name_not_provided():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

# 9. Tipo de parámetro diferente (número)
def test_kit_name_as_number():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)
