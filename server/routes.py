from flask import Blueprint, request, jsonify
from .models import db, Restaurant, Pizza, RestaurantPizza

api_bp = Blueprint('api', __name__)

# Restaurant routes
@api_bp.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

@api_bp.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    return jsonify(restaurant.to_dict())

@api_bp.route('/restaurants', methods=['POST'])
def create_restaurant():
    data = request.get_json()
    new_restaurant = Restaurant(name=data['name'], address=data['address'])
    db.session.add(new_restaurant)
    db.session.commit()
    return jsonify(new_restaurant.to_dict()), 201

@api_bp.route('/restaurants/<int:id>', methods=['PUT'])
def update_restaurant(id):
    data = request.get_json()
    restaurant = Restaurant.query.get_or_404(id)
    restaurant.name = data['name']
    restaurant.address = data['address']
    db.session.commit()
    return jsonify(restaurant.to_dict())

@api_bp.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get_or_404(id)
    db.session.delete(restaurant)
    db.session.commit()
    return '', 204

# Pizza routes
@api_bp.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([pizza.to_dict() for pizza in pizzas])

@api_bp.route('/pizzas/<int:id>', methods=['GET'])
def get_pizza(id):
    pizza = Pizza.query.get_or_404(id)
    return jsonify(pizza.to_dict())

@api_bp.route('/pizzas', methods=['POST'])
def create_pizza():
    data = request.get_json()
    new_pizza = Pizza(name=data['name'], ingredients=data['ingredients'])
    db.session.add(new_pizza)
    db.session.commit()
    return jsonify(new_pizza.to_dict()), 201

@api_bp.route('/pizzas/<int:id>', methods=['PUT'])
def update_pizza(id):
    data = request.get_json()
    pizza = Pizza.query.get_or_404(id)
    pizza.name = data['name']
    pizza.ingredients = data['ingredients']
    db.session.commit()
    return jsonify(pizza.to_dict())

@api_bp.route('/pizzas/<int:id>', methods=['DELETE'])
def delete_pizza(id):
    pizza = Pizza.query.get_or_404(id)
    db.session.delete(pizza)
    db.session.commit()
    return '', 204

# RestaurantPizza routes
@api_bp.route('/restaurant_pizzas', methods=['GET'])
def get_restaurant_pizzas():
    restaurant_pizzas = RestaurantPizza.query.all()
    return jsonify([rp.to_dict() for rp in restaurant_pizzas])

@api_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    new_rp = RestaurantPizza(price=data['price'], pizza_id=data['pizza_id'], restaurant_id=data['restaurant_id'])
    db.session.add(new_rp)
    db.session.commit()
    return jsonify(new_rp.to_dict()), 201

@api_bp.route('/restaurant_pizzas/<int:id>', methods=['DELETE'])
def delete_restaurant_pizza(id):
    rp = RestaurantPizza.query.get_or_404(id)
    db.session.delete(rp)
    db.session.commit()
    return '', 204
