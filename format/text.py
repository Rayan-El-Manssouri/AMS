import re

def format_const_name(name):
    # Supprimer les espaces et formater le nom de constante
    formatted_name = name.lower()
    formatted_name = re.sub(r'\W+', '_', formatted_name)  # Remplacer les caractères spéciaux par des underscores
    return formatted_name
