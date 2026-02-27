def es_vip(respuesta):
    respuesta = respuesta.strip().lower()
    if respuesta in ["si", "s", "y", "yes"]:
        return True
    else:
        return False