import os
import django
import pandas as pd

# Setup Django before using models
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PokeShop.settings")  # Change "PokeShop" to your project name
django.setup()

from Catalog.models import Product  # Import after django.setup()


def load_csv():
    df = pd.read_csv('PokeShop/Catalog/Product.csv', usecols=['id', 'name', 'description', 'price', 'category_name'])
    
    for _, row in df.iterrows():
        Product.objects.create(
            id=row['id'],
            name=row['name'],
            description=row['description'],
            price=row['price'],
            category_name=row['category_name']
        )
    
    print("Dades carregades amb èxit!")


if __name__ == "__main__":
    load_csv()
