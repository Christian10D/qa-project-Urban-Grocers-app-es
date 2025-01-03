import pytest
from sender_stand_request import post_new_client_kit
from data import get_kit_body

def get_new_user_token():
  #implementar logica para obtener un token de autenticacion
  pass

def positive_asssert(kit_body):
  auth_token = get_new_user_token()
  response = post_new_client_kit(kit_body, auth_token)
  assert response.status_code == 201
  assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
  auth_token = get_new_user_token()
  response = post_new_client_kit(kit_body, auth_token)
  assert response.status_code == 400

#pruebas
def test_valid_name():
  positive_assert(get_kit_body("Valid Kit"))

def test_name_too_short():
  negative_assert_code_400(get_kit_body(""))

def test_name_too_long():
  negative_assert_code_400(get_kit_body("A" * 512))

def test_special_character_in_name():
  positive_assert(get_kit_body("!@#$%^&*()"))

def test_space_in_name():
  positive_assert(get_kit_body("Name with space"))
  
