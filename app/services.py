import requests
import json
from .models import Product


def getProduct():
    res = requests.get(f"https://fakestoreapi.com/products")
    if res.ok:
        data = res.json()
        print(data)
        for d in data:
            pid = d["id"]
            prod = Product.query.get(pid)
            if prod:
                continue
            else:
                id = d["id"]
                title = d["title"]
                price = d["price"]
                category = d["category"]
                description = d["description"]
                image = d["image"]
        
                new_product = Product(id, title, price, category, description, image)
                new_product.saveProduct()
                
     