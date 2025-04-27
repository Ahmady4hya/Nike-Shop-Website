🏬 Nike Shop - Product Management System
A Python Flask web application for managing Nike product orders, with a MySQL database backend and a simple HTML/CSS frontend.

📖 Overview
This project is designed to allow users to add, edit, view, and delete Nike products through a web interface.
It demonstrates skills in backend development, database integration, and basic frontend design.

🛠️ Technologies Used
Python Flask (Backend framework)

MySQL (Database management)

HTML/CSS (Frontend interface)

🧩 Project Structure

File	Description
app.py	Main Flask application (backend routes)
templates/index.html	Landing page (home)
templates/product_list.html	List and manage products
templates/edit_product.html	Edit existing products
static/	(Optional) CSS or images folder
📂 Database Configuration
Host: localhost

User: root

Password: 12345678

Database: nikeshop

Table: My_Product

Column	Type	Description
product_id	INT (Auto Increment)	Product ID
name	VARCHAR	Product Name
amount	INT	Quantity Available
phone	VARCHAR	Customer Phone Number
🚀 Key Features
Add Product (with validation: amount > 0, 10-digit phone number)

Edit Product (with flash messages for errors)

Delete Product (with confirmation and re-indexing IDs)

View Product List (dynamic display from MySQL database)

🖥️ Demo
Add a new product.

Edit existing products.

Delete products after confirmation.

(Screenshots or a short video link here would make it even better!)

⚙️ Installation and Running
bash
Copy
Edit
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/Nike_Shop.git
cd Nike_Shop

# 2. Install dependencies
pip install flask mysql-connector-python

# 3. Run the application
python app.py
Then open your browser and go to:
http://localhost:5000
