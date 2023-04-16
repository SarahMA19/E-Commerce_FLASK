from flask import Blueprint, request
from ..models import Product 

api = Blueprint('api', __name__, url_prefix='/api')

@api.route('/products')
def getProds():
    prods = Product.query.all()
    prodlist = [p.to_dict() for p in prods]
    return {
        'status' : 'ok',
        'data' : prodlist,
        'item_count' : len(prodlist)
    }

@api.route('/product/<int:prod_id>')
def getIndProd(prod_id):
    p = Product.query.get(prod_id)
    if p:
        prod = p.to_dict()
        return {
            'status': 'ok',
            'data': prod,
        }
    return {
        'status': 'Error',
        'message': 'No product with that ID exists',
    }





