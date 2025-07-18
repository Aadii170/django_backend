# 🛒 Django E-commerce Backend API

Welcome to the **Django E-commerce Backend**, a powerful RESTful API for managing users, products, payments, reviews, and more — built using Django and Django REST Framework.

---

## 🚀 Features

- 🔐 **Authentication System**  
  Token-based authentication for secure login/logout and user management.

- 🛍️ **Store Module**  
  Handles products, categories, stock, and pricing.

- 📦 **Checkout & Orders**  
  Manage shopping cart, order placement, and payment status.

- 🎨 **Customize Module**  
  Allows user personalization and additional feature settings.

- 💳 **Payment Gateways**  
  Supports Stripe, Razorpay, and CCAvenue integrations.

- ✉️ **Email Notifications**  
  Sends confirmation and status updates via SMTP.

- ⭐ **Reviews System**  
  Users can post product reviews and ratings.

- 🔄 **Google OAuth Login** *(Optional)*  
  Simplified sign-in with Google account.

---

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework  
- **Database:** PostgreSQL / SQLite  
- **Auth:** DRF Token Auth, Google OAuth  
- **Payments:** Stripe, Razorpay, CCAvenue  
- **Dev Tools:** Baton Admin Panel, .env support with `python-dotenv`

---

## 📁 Project Structure

```
backend/
├── authentication/
├── store/
├── checkout/
├── payments/
├── reviews/
├── customize/
├── feedback/
├── staticfiles/
└── manage.py
```

---

## 📦 Setup Instructions

1. **Clone the repo:**
   ```bash
   git clone https://github.com/your-username/django_backend.git
   cd django_backend
   ```

2. **Create virtual environment & install dependencies:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Set up `.env` file:**
   ```
   SECRET_KEY=your_secret_key
   DEBUG=True
   DB_URL=sqlite:///db.sqlite3
   EMAIL_HOST_USER=your_email
   EMAIL_HOST_PASSWORD=your_password
   STRIPE_SECRET_KEY=your_stripe_key
   ```

4. **Run migrations & start server:**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

## ✅ Endpoints Preview

| Feature      | Endpoint Prefix        |
|--------------|------------------------|
| Auth         | `/api/auth/`           |
| Store        | `/api/store/`          |
| Checkout     | `/api/checkout/`       |
| Customize    | `/api/customize/`      |
| Reviews      | `/api/reviews/`        |
| Payments     | `/payments/`           |
| Admin Panel  | `/admin/` or `/baton/` |

---

## 🧪 Run Tests

```bash
python manage.py test
```

---

## 👨‍💻 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.

---

## 📫 Contact

Made with ❤️ by [Aditya Kumar](https://github.com/Aadii170)  
📧 Feel free to reach out for collaboration or suggestions!

---

## ⭐ Show Your Support

If you found this helpful, give it a ⭐ on [GitHub](https://github.com/Aadii170/django_backend)!

