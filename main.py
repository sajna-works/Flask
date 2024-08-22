from flask import Flask, jsonify, request
import json

main=Flask(__name__)

def load_myprod():
    with open('myproducts.json', 'r', encoding="utf-8")as file:
        return json.load(file)
    
def save_products(myprod):
    with open('myproducts.json','w', encoding="utf-8")as file:
        json.dump(myprod, file, indent=4)    

# Hello for URL
@main.route('/', methods=['GET'])
def hello():
    return "Hello"

# GET PRODUCTS FROM JSON FILE
@main.route('/products', methods=['GET'])
def get_myproducts():
    myprod=load_myprod()
    return jsonify(myprod)

# GET PRODUCTS BY ID
@main.route('/products/<int:pro_id>', methods=['GET'])
def get_product_byid(pro_id):
    myprod=load_myprod()
    prod=None
    for p in myprod:
        if p["id"]==pro_id:
            prod=p
            break
    return jsonify(prod) if prod else ("Not found", 400) 

# POST NEW PRODUCT   
@main.route('/products', methods=['POST'])
def create_products():
    new = request.json
    myprod=load_myprod()
    myprod.append(new)
    save_products(myprod)
    return new   

# UPDATE PRODUCTS-PUT

@main.route('/products/<int:pro_id>', methods = ['PUT'])
def update_prod(pro_id):
    myprod=load_myprod()
    prod=None
    for p in myprod:
        if p["id"]==pro_id:
            prod=p
            break
    updated_prod = request.json
    prod.update(updated_prod)
    save_products(myprod)
    return updated_prod    

# DELETE BY PRODUCT ID

@main.route('/products/<int:pro_id>', methods = ['DELETE'])
def delete_prod(pro_id):
    myprod = load_myprod()
    updated_list = list(filter(lambda p:p['id']!=pro_id, myprod))
    save_products(updated_list)
    return "Deleted", 204

   

main.run(debug=True)
