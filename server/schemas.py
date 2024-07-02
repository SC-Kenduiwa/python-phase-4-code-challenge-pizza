from . import ma #marshmallow schema to serialize database
from .models import Restaurant, Pizza, RestaurantPizza

class RestaurantSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Restaurant
        include_relationships = True
        load_instance = True

class PizzaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Pizza
        include_relationships = True
        load_instance = True

class RestaurantPizzaSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = RestaurantPizza
        include_relationships = True
        load_instance = True
