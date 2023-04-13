import requests
import json


def getProduct(jewelery):
    res = requests.get(f"https://fakestoreapi.com/products/category/jewelery")
    if res.ok:
        data = res.json()
       
        x = {}
        x["title"] = data["title"]
        x["price"] = data["price"]
        x["category"] = data["jewelery"]
        x["description"] = data["description"]
        x["image"] = data["image"]
        return x
     