from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('postgresql://catalog:password@localhost/catalog')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(
    name="Robo Barista",
    email="tinnyTim@udacity.com",
    picture='https: //pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for UrbanBurger
restaurant1 = Restaurant(user_id=1, name="Urban Burger")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem(
    user_id=1,
    name="Veggie Burger",
    description="Juicy grilled veggie patty with tomato mayo and lettuce",
    price="$7.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(
    user_id=1,
    name="French Fries",
    description="with garlic and parmesan",
    price="$2.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    user_id=1,
    name="Chicken Burger",
    description="Juicy grilled chicken patty with tomato mayo and lettuce",
    price="$5.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(
    user_id=1,
    name="Chocolate Cake",
    description="fresh baked and served with ice cream",
    price="$3.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(
    user_id=1,
    name="Sirloin Burger",
    description="Made with grade A beef",
    price="$7.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(
    user_id=1,
    name="Root Beer",
    description="16oz of refreshing goodness",
    price="$1.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Iced Tea", description="with Lemon",
                     price="$.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(
    user_id=1,
    name="Grilled Cheese Sandwich",
    description="On texas toast with American Cheese",
    price="$3.49", course="Entree", restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(
    user_id=1,
    name="Veggie Burger",
    description="Made with freshest of ingredients and home grown spices",
    price="$5.99", course="Entree", restaurant=restaurant1)

session.add(menuItem8)
session.commit()


# Menu for Super Stir Fry
restaurant2 = Restaurant(user_id=1, name="Super Stir Fry")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(
    user_id=1,
    name="Chicken Stir Fry",
    description="With your choice of noodles vegetables and sauces",
    price="$7.99", course="Entree", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    user_id=1, name="Peking Duck",
    description= ''' A famous duck dish from Beijing[1]
    that has been prepared since the imperial era.
    The meat is prized for its thin, crisp skin,
    with authentic versions of the dish serving mostly
    the skin and little meat, sliced in front of the diners by the cook''',
    price="$25", course="Entree", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(
    user_id=1,
    name="Spicy Tuna Roll",
    description='''Seared rare ahi, avocado,
    edamame, cucumber with wasabi soy sauce ''',
    price="15", course="Entree", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(
    user_id=1,
    name="Nepali Momo ",
    description="Steamed dumplings made with vegetables, spices and meat. ",
    price="12", course="Entree", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(
    user_id=1,
    name="Beef Noodle Soup",
    description='''A Chinese noodle soup made of stewed or red braised beef,
    beef broth, vegetables and Chinese noodles.''',
    price="14", course="Entree", restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(
    user_id=1,
    name="Ramen",
    description='''a Japanese noodle soup dish.
    It consists of Chinese-style wheat noodles served
    in a meat - or (occasionally) fish-based broth,
    often flavored with soy sauce or miso,
    and uses toppings such as sliced pork, dried seaweed, kamaboko,
    and green onions.''',
    price="12", course="Entree", restaurant=restaurant2)

session.add(menuItem6)
session.commit()


# Menu for Panda Garden
restaurant1 = Restaurant(user_id=1, name="Panda Garden")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(
    user_id=1, name="Pho",
    description='''a Vietnamese noodle soup consisting of broth,
    linguine-shaped rice noodles called banh pho,
    a few herbs, and meat.''',
    price="$8.99", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    user_id=1,
    name="Chinese Dumplings",
    description='''a common Chinese dumpling which
    generally consists of minced meat and finely chopped
    vegetables wrapped into a piece of dough skin.
    The skin can be either thin and elastic or thicker.''',
    price="$6.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(
    user_id=1, name="Gyoza",
    description='''light seasoning of Japanese gyoza with salt and soy sauce,
    and in a thin gyoza wrapper''',
    price="$9.95", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(
    user_id=1,
    name="Stinky Tofu",
    description='''Taiwanese dish, deep fried
    fermented tofu served with pickled cabbage.''',
    price="$6.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(
    user_id=1, name="Veggie Burger",
    description="Juicy grilled veggie patty with tomato mayo and lettuce",
    price="$9.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Thyme for that
restaurant1 = Restaurant(user_id=1, name="Thyme for That Vegetarian Cuisine ")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(
    user_id=1, name="Tres Leches Cake",
    description='''Rich, luscious sponge cake soaked in
    sweet milk and topped with vanilla bean whipped cream and strawberries.''',
    price="$2.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(
    user_id=1,
    name="Mushroom risotto",
    description="Portabello mushrooms in a creamy risotto",
    price="$5.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

print( "added menu items!")
