# data.py
# Este archivo contiene los datos necesarios para las solicitudes POST.

from copy import deepcopy

# Cuerpos de solicitud para las pruebas
KIT_BODY_VALID = {"name": "Kit válido"}
KIT_BODY_MIN_LENGTH = {"name": "a"}
KIT_BODY_MAX_LENGTH = {"name": "a" * 511}
KIT_BODY_OVER_MAX_LENGTH = {"name": "a" * 512}
KIT_BODY_EMPTY = {"name": ""}
KIT_BODY_SPECIAL_CHARS = {"name": "!@#$%^&*()"}
KIT_BODY_NUMBERS = {"name": "12345"}
KIT_BODY_SPACES = {"name": "   Nombre con espacios   "}
KIT_BODY_NO_NAME = {}

def get_kit_body(name):
    """Retorna un cuerpo de kit con un nombre específico."""
    kit_body = deepcopy(KIT_BODY_VALID)
    kit_body["name"] = name
    return kit_body
