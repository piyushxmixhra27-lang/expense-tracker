# 💸 Wisdom Expense Manager

> A premium, enterprise-grade School Expense Tracking & Financial Management System built for **Wisdom The Global School**.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

---

## ✨ Features

- 🔐 **Authentication** — Secure login with role-based access (Admin, Accountant, Viewer)
- 📊 **Dashboard** — KPI cards, monthly graphs, category pie charts & recent activity
- 💳 **Transactions** — Search, filter, paginated expense table with status badges
- 📈 **Analytics** — Spending trends, monthly comparisons, expense distribution
- 📋 **Reports** — Monthly/Yearly/Category-wise reports with PDF/Excel/CSV export
- 💰 **Budget Management** — Budget tracking and alerts
- 👥 **User Management** — Role management, add-user modal (Admin only)

---

## 🎨 Design

| Style | Description |
|-------|-------------|
| Theme | Premium Dark / Light Mode |
| Aesthetic | Glassmorphism, smooth shadows, elegant gradients |
| Palette | Deep Blue, Royal Blue, Emerald Green, Cyan accents |
| Components | Animated counters, loading shimmers, responsive tables |

---

## 🗂️ Project Structure

```
wisdom-expense-manager/
│
├── app.py                  # Flask application entry point
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Git ignore rules
│
├── templates/              # Jinja2 HTML templates
│   ├── login.html          # Login page (glassmorphism UI)
│   ├── dashboard.html      # Main dashboard with KPIs & charts
│   ├── transactions.html   # Expense management & table
│   ├── analatics.html      # Analytics & spending trends
│   ├── reports.html        # Reports & export
│   └── budget.html         # Budget management
│
└── static/                 # Static assets
    ├── css/                # Custom stylesheets
    ├── js/                 # Custom JavaScript
    └── img/                # Images & icons
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/wisdom-expense-manager.git
   cd wisdom-expense-manager
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   ```

3. **Activate virtual environment**
   ```bash
   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set environment variables** *(optional)*
   ```bash
   # Windows
   set SECRET_KEY=your-secret-key-here

   # macOS / Linux
   export SECRET_KEY=your-secret-key-here
   ```

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Open in browser**
   ```
   http://127.0.0.1:5000
   ```

---

## 👥 User Roles

| Role | Access |
|------|--------|
| **Admin** | Full access — user management, audit logs, all modules |
| **Accountant** | Expense entry, bill uploads, reports |
| **Viewer** | Read-only dashboard and reports |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Flask (Python) |
| Frontend | HTML5, CSS3, JavaScript |
| UI Framework | Bootstrap 5 |
| Charts | Chart.js |
| Icons | Bootstrap Icons / Font Awesome |

---

## 📄 License

This project is proprietary and built exclusively for **Wisdom The Global School**.

---

## 🤝 Contributing

This is a client project. For internal contributions, please follow the team's branching strategy:

- `main` → Production-ready code
- `develop` → Active development branch
- `feature/xyz` → Feature branches

---

> Built with ❤️ for Wisdom The Global School
