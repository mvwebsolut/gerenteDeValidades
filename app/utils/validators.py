def validate_product(product):

    if product['name'] == "" or product['name'] == None:
        raise Exception("nome do produto inválido")

    if product['lote_number'] == "" or product["lote_number"] == None:
        raise Exception("lote do produto inválido")

    if product['validity_date'] == "" or product['validity_date'] == None:
        raise Exception("validade do produto inválido")

    return