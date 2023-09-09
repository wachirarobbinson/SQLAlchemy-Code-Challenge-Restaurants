from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///restaurant.db')
Base = declarative_base()

# Define the association table for the many-to-many relationship
restaurant_customer_association = Table(
    'restaurant_customer_association',
    Base.metadata,
    Column('restaurant_id', Integer, ForeignKey('restaurant.id')),
    Column('customer_id', Integer, ForeignKey('customer.id'))
)

# Define the Restaurant class
class Restaurant(Base):
    __tablename__ = "restaurant"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)

    # Define the many-to-many relationship
    customers = relationship("Customer", secondary=restaurant_customer_association, back_populates="restaurants")
    reviews = relationship("Review", back_populates="restaurant")

    def __repr__(self):
        return f"Restaurant(name='{self.name}', price={self.price})"

# Define the Customer class
class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    # Define the many-to-many relationship
    restaurants = relationship("Restaurant", secondary=restaurant_customer_association, back_populates="customers")
    reviews = relationship("Review", back_populates="customer")

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        highest_rating = -1
        favorite = None
        for review in self.reviews:
            if review.star_rating > highest_rating:
                highest_rating = review.star_rating
                favorite = review.restaurant
        return favorite

    def add_review(self, restaurant, rating):
        new_review = Review(star_rating=rating, restaurant=restaurant, customer=self)
        self.reviews.append(new_review)

    def delete_reviews(self, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            self.reviews.remove(review)

    def __repr__(self):
        return f"Customer(first_name='{self.first_name}', last_name='{self.last_name}')"

# Define the Review class
class Review(Base):
    __tablename__ = 'review'
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))

    # Define the many-to-one relationships
    restaurant = relationship("Restaurant", back_populates="reviews")
    customer = relationship("Customer", back_populates="reviews")

    def full_review(self):
        return f"Review for {self.restaurant.name} by {self.customer.full_name()}: {self.star_rating} stars"

    def __repr__(self):
        return f"Review(star_rating={self.star_rating})"
