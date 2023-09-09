from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, Review, Base

# Create the database engine
engine = create_engine('sqlite:///restaurant.db')
Session = sessionmaker(bind=engine)
session = Session()

# Create tables in the database
Base.metadata.create_all(engine)

# Sample data creation
restaurant1 = Restaurant (name="Cafe Deli", price=2500)
restaurant2 = Restaurant (name="Cj`s", price=3900)

customer1 = Customer (first_name="Robbinson", last_name="Ngirigacha")
customer2 = Customer (first_name="Lyndiwe", last_name="Lydia")

review1 = Review (star_rating=3, restaurant = restaurant1, customer = customer1)
review2 = Review (star_rating=5, restaurant = restaurant2, customer = customer2)

session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])
session.commit()


# Test methods and relationships
restaurant = session.query(Restaurant).first()
customer = session.query(Customer).first()

print(f"Restaurant Name: {restaurant.name}")
print(f"Customer Full Name: {customer.full_name()}")

restaurant_reviews = restaurant.reviews
customer_reviews = customer.reviews

print(f"Restaurant Reviews: {[review.full_review() for review in restaurant_reviews]}")
print(f"Customer Reviews: {[review.full_review() for review in customer_reviews]}")

favorite = customer.favorite_restaurant()
print(f"Customer's Favorite Restaurant: {favorite.name if favorite else 'None'}")

restaurant_to_review = session.query(Restaurant).filter_by(name="Cafe Deli").first()
customer.add_review(restaurant_to_review, 5)
print("Added a review.")


# Close the session
session.close()