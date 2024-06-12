import sqlite3

def create_tables():
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()

    # Create Seasonal Flavors table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS seasonal_flavors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        flavor_name TEXT NOT NULL,
        description TEXT,
        availability TEXT
    )
    ''')

    # Create Ingredient Inventory table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ingredients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        ingredient_name TEXT NOT NULL,
        quantity INTEGER
    )
    ''')

    # Create Customer Suggestions table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer_suggestions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        customer_name TEXT,
        suggested_flavor TEXT,
        allergy_concern TEXT
    )
    ''')

    # Create Allergens table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS allergens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        allergen_name TEXT NOT NULL
    )
    ''')

    # Create Cart table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cart (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL
    )
    ''')

    conn.commit()
    conn.close()

create_tables()
