# Function definition

def get_domain(email):
    split = email.split("@")
    if len(split) != 2:
        raise ValueError("Endereço de e-mail inválido. Deve conter exatamente um '@'.")
    return split[1]
