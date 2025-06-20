# multitenant
# 🏢 Multitenant Authentication System

This project implements a **multitenant authentication system** using **Flask**, **MongoDB**, and **JWT**. Each tenant (e.g., `client1.localhost`, `client2.localhost`) has its own isolated user base. The architecture supports scalable, secure authentication flows suitable for SaaS platforms.

---

## 🚀 Features

- Subdomain-based multitenancy (e.g., `client1.localhost`, `client2.localhost`)
- User registration and login per tenant
- JWT-based authentication
- Tenant-aware routing
- MongoDB backend
- Easily extensible for role-based access, tenant dashboards, and more

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Database**: MongoDB
- **Auth**: JSON Web Tokens (JWT) via [`python-jose`](https://github.com/mpdavis/python-jose)
- **Subdomain handling**: Flask blueprints with custom middleware

---

## 📁 Project Structure
multitenant-auth/
├── app.py
├── controllers/
│ └── auth_controller.py
├── routes/
│ └── auth_routes.py
├── utils/
│ └── token_utils.py
├── models/
│ └── user_model.py
├── templates/
│ └── login.html
├── middleware/
│ └── tenant_middleware.py
└── requirements.txt


```bash
git clone https://github.com/your-org/multitenant-auth.git
cd multitenant-aut

2. Create a virtual environment
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate
3. Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
4. Add local subdomains
Edit your hosts file:

Windows: C:\Windows\System32\drivers\etc\hosts

Add:

Copy
Edit
127.0.0.1 client1.localhost
127.0.0.1 client2.localhost


5. Run the app
bash
Copy
Edit
python app.py
Visit:

http://client1.localhost:5000

http://client2.localhost:5000

Dependencies
nginx
Copy
Edit
Flask
Flask-PyMongo
python-jose
Make sure these are listed in your requirements.txt.

 Security Notes
JWT tokens should be stored securely on the client (e.g., in HttpOnly cookies)

Token expiration and refresh flows should be added for production

Rate limiting and email verification are recommended for user registration

📌 TODO
Add role-based access

Add tenant admin dashboard

Implement token refresh mechanism

Add support for invitation-based user onboarding


Author
MIR AQIB MUSHTAQ
