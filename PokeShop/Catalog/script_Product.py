import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PokeShop.settings")
django.setup()

from Catalog.models import Product, Categoria

def load_csv():
    df = pd.read_csv('Catalog/Product.csv', usecols=['id', 'name', 'description', 'price', 'stock', 'category_name', 'rating'])
    
    for _, row in df.iterrows():
        categoria_obj, _ = Categoria.objects.get_or_create(nom=row['category_name'])

        Product.objects.create(
            nom=row['name'],
            descripcio=row['description'],
            preu=row['price'],
            stock=row['stock'],
            nom_categoria=categoria_obj,
            rating=row['rating']
        )
    
    print("Dades carregades amb èxit!")


if __name__ == "__main__":
    load_csv()
