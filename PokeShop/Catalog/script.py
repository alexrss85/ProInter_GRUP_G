import os
import django
import pandas as pd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PokeShop.settings")
django.setup()

from Catalog.models import Product, Categoria

def load_csv():
    df = pd.read_csv('Catalog/Category.csv', usecols=['id', 'name'])
    
    for _, row in df.iterrows():
        Categoria.objects.create(
            nom=row['name']
        )
    
    print("Dades carregades amb èxit!")


if __name__ == "__main__":
    load_csv()
