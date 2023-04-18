from flask import Blueprint, request
from ..models import Product 
from ..services import getProduct

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

@api.route('/db/<int:product_id>')
def indPost(product_id):
    product = Product.query.get(product_id)
    if product:
        p = product.to_dict() # Assuming to_dict() method returns a dictionary with product data
        return ({
            'status': 'ok',
            'data': p,
            'item_count': 1 # Since you are returning a single product
        })
    else:
        return ({
            'status': 'error',
            'message': 'Product not found'
        }), 404 # Return a 404 status code if product not found





