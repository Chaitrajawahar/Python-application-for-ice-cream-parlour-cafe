import sqlite3

def add_seasonal_flavor(flavor_name, description, availability):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO seasonal_flavors (flavor_name, description, availability)
    VALUES (?, ?, ?)
    ''', (flavor_name, description, availability))
    conn.commit()
    conn.close()

def add_ingredient(ingredient_name, quantity):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO ingredients (ingredient_name, quantity)
    VALUES (?, ?)
    ''', (ingredient_name, quantity))
    conn.commit()
    conn.close()

def add_customer_suggestion(customer_name, suggested_flavor, allergy_concern):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO customer_suggestions (customer_name, suggested_flavor, allergy_concern)
    VALUES (?, ?, ?)
    ''', (customer_name, suggested_flavor, allergy_concern))
    conn.commit()
    conn.close()

def add_allergen(allergen_name):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO allergens (allergen_name)
    VALUES (?)
    ''', (allergen_name,))
    conn.commit()
    conn.close()

def add_to_cart(product_name):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO cart (product_name)
    VALUES (?)
    ''', (product_name,))
    conn.commit()
    conn.close()

def get_seasonal_flavors():
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM seasonal_flavors')
    flavors = cursor.fetchall()
    conn.close()
    return flavors

def search_seasonal_flavors(keyword):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT * FROM seasonal_flavors
    WHERE flavor_name LIKE ? OR description LIKE ?
    ''', ('%' + keyword + '%', '%' + keyword + '%'))
    flavors = cursor.fetchall()
    conn.close()
    return flavors

def get_cart():
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM cart')
    cart_items = cursor.fetchall()
    conn.close()
    return cart_items
