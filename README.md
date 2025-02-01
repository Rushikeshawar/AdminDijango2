
# Digando - Admin Panel

**Tech Stack:**
- **Frontend:** HTML, CSS, Bootstrap
- **Backend:** Django
- **Database:** SQLite3
- **Authentication:** JWT (JSON Web Token)

# Admin Login Details
- Admin credentials (rushi / 1234). 

## Project Overview
Digando is an admin panel that allows admins to manage products in an e-commerce platform. The application provides features like adding, viewing, updating, and deleting products. Admin access is secured via JWT authentication. The backend is built using Django with SQLite as the database.

---

## Features & Functionality

1. **Authentication (Login & Registration)**
   - Admin can log in using JWT authentication.
   - Once logged in, the Navbar is visible with options to manage products.

2. **Navbar (Visible only to Admin)**
   - Admin has the following options available in the Navbar:
     - ✅ Add Product
     - ✅ Show Products

3. **Add Product (Form Validation & Database Integration)**
   - Only accessible to Admin.
   - Admin can enter product details such as Name, Price, Description, and Image.
   - Input fields are validated before saving the product to the SQLite database.

4. **Show Products (Fetch & Display Data from Database)**
   - Displays all stored products in the database.
   - Includes action buttons to update or delete each product.

5. **Update & Delete Product (CRUD Operations)**
   - Admin can update product details or delete products from the database.

---

## Development Roadmap

### 1. Backend (Django + SQLite)
   - ✅ Setup Django project
   - ✅ Create API routes: /Admin, /login, /add-product, /update-product, /delete-product, /get-products
   - ✅ Implement JWT Authentication
   - ✅ Configure SQLite3 database

### 2. Frontend (HTML, CSS, Bootstrap)
   - ✅ Create Login & Registration Page
   - ✅ Implement Protected Routes (only Admin can access dashboard)
   - ✅ Build Product Form (Add & Update)
   - ✅ Fetch and display products
   - ✅ Add Update & Delete functionality
