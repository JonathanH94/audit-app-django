# 📝 Audit Application Demo

This is a prototype/demo app to demonstrate to internal staff, a possible Sharepoint list replacement.

---

## 🔍 Overview

This app allows internal staff to:

- Select and complete audit forms
- Assign audits to teams
- View, edit, and delete past submissions
- Log in securely via Django’s authentication system

The homepage acts as a simple dashboard for navigation between actions.

---

## 💡 Purpose

This project served a dual purpose as a **demo** to showcase core features for internal auditing and an opportunity for me to gain a deeper understanding of the Django framework. It is not production-ready, but serves as a base for stakeholder feedback and future development.

---

## ⚙️ Tech Summary

- **Framework**: Django (Python)
- **Frontend**: HTML & Bootstrap
- **Database**: SQLite (for demo/testing)
- **Auth**: Django built-in login/logout

---

## 📎 Notes

- Forms are dynamically generated based on the selected audit
- Uses Django's built-in login/logout views
- Basic UI with Bootstrap, no JS frameworks or plugins

---
## ⬆️ Improvements/Next Steps

- Role-based access (i.e. admin, member, contributor, viewer)
- More dynamic form and model logic (allow multiple choice answers, an answer class/table etc.)
- Use staff directory or SSO for authentication
- Search & filter options on previous submissions (i.e. audit date, team, audit name)
- Dashboard analytics using **pandas** and **matplotlib**
- Improvements to the UX/UI
