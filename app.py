from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # تأكد من تعيين المفتاح السري لاستخدام رسائل الفلاش

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678",
    database="nikeshop"
)

# Create a cursor to interact with the database
cursor = db.cursor()

# Create table if not exists
cursor.execute("CREATE TABLE IF NOT EXISTS My_Product (product_id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20), amount INT, phone CHAR(10))")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/product_list')
def product_list():
    # Fetch all products from the database
    cursor.execute("SELECT * FROM My_Product")
    products = cursor.fetchall()
    return render_template('product_list.html', products=products)

@app.route('/add_product', methods=['POST'])
def add_product():
    # Get product data from the form
    name = request.form['name']
    amount = request.form['amount']
    phone = request.form['phone']

    # Validate amount
    if int(amount) <= 0:
        flash("Amount must be greater than zero.")
        return redirect(url_for('product_list'))

    # Validate phone number
    if len(phone) != 10 or not phone.isdigit():
        flash("Phone number must be exactly 10 digits.")
        return redirect(url_for('product_list'))

    # Insert the product into the database
    query = "INSERT INTO My_Product (name, amount, phone) VALUES (%s, %s, %s)"
    values = (name, amount, phone)
    cursor.execute(query, values)
    db.commit()

    return redirect(url_for('product_list'))

@app.route('/edit_product/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    if request.method == 'POST':
        # Get updated product data from the form
        name = request.form['name']
        amount = request.form['amount']
        phone = request.form['phone']

        # Validate amount
        if int(amount) <= 0:
            flash("Amount must be greater than zero.")
            return redirect(url_for('edit_product', product_id=product_id))

        # Validate phone number
        if len(phone) != 10 or not phone.isdigit():
            flash("Phone number must be exactly 10 digits.")
            return redirect(url_for('edit_product', product_id=product_id))

        # Update the product in the database
        query = "UPDATE My_Product SET name = %s, amount = %s, phone = %s WHERE product_id = %s"
        values = (name, amount, phone, product_id)
        cursor.execute(query, values)
        db.commit()

        return redirect(url_for('product_list'))

    else:
        # Fetch the product from the database
        select_query = "SELECT * FROM My_Product WHERE product_id = %s"
        select_values = (product_id,)
        cursor.execute(select_query, select_values)
        product = cursor.fetchone()

        if product is None:
            flash("Product not found.")
            return redirect(url_for('product_list'))

        return render_template('edit_product.html', product=product)

@app.route('/delete_product/<int:product_id>', methods=['GET', 'POST'])
def delete_product(product_id):
    # Delete the product from the database
    query = "DELETE FROM My_Product WHERE product_id = %s"
    values = (product_id,)
    cursor.execute(query, values)
    db.commit()

    # Update primary key values after deletion
    cursor.execute("SET @count = 0;")
    cursor.execute("UPDATE My_Product SET product_id = @count:= @count + 1;")
    cursor.execute("ALTER TABLE My_Product AUTO_INCREMENT = 1;")

    return redirect(url_for('product_list'))

if __name__ == "__main__":
    app.run(debug=True)