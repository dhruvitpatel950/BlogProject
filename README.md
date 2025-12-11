# WriteHub - Multi-User Blogging Platform ✍️

WriteHub is a robust, full-featured blogging application built with **Django 5**. It allows users to register, publish articles with images, manage their content, and interact with other authors via comments. 

This project demonstrates proficiency in **MVT architecture**, **Relational Database Design**, and **Django's Authentication System**.

---

## 🚀 Features

### 🔐 Authentication & Authorization
* **User Registration & Login:** Secure user account creation and session management using Django's built-in Auth system.
* **Role-Based Access Control:** * Only logged-in users can create posts or comments.
    * **Author Permissions:** Users can only edit or delete *their own* posts.

### 📝 Content Management (CRUD)
* **Create/Edit/Delete:** Full control over blog posts.
* **Rich Content:** Support for titles, text content, and **image uploads**.
* **Draft System:** Posts can be saved as "Drafts" or "Published" instantly.

### 🔍 Discovery & Interaction
* **Search Functionality:** Filter posts by title or content keywords.
* **Pagination:** Optimized browsing experience for large datasets.
* **Comments System:** Threaded conversations on individual blog posts.

---

## 🛠️ Tech Stack

* **Backend:** Python 3.x, Django 5
* **Database:** SQLite (Dev), configurable for PostgreSQL
* **Frontend:** Django Templates (DTL), CSS3, HTML5
* **Media Handling:** Pillow (Image processing)

---

## 🏗️ Project Structure

```text
BlogProject/
├── core/                   # Project configuration settings
├── blogs/                  # Main application (Posts, Comments, Auth)
│   ├── models.py           # Database Schema (Post, Comment)
│   ├── views.py            # Business logic & Request handling
│   └── templates/          # Frontend templates
├── home/                   # Static pages (About, Contact)
├── media/                  # User-uploaded images
└── manage.py               # Django command-line utility
