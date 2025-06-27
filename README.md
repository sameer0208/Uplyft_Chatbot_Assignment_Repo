🛍️ E-commerce Chatbot – Uplyft Assignment

This repository contains the complete source code for an E-commerce Chatbot built as part of the Uplyft assignment. The project showcases a full-stack web application with a Flask backend and a React frontend, enabling users to log in and chat with a bot that recommends products dynamically.

📂 Project Structure
Uplyft_Assignment_E-commerce_Chatbot/
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── db_init.py
│   ├── chatbot_logic.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── components/
│   │   │   ├── Login.js
│   │   │   └── Chatbot.js
│   └── package.json
└── README.md

⚙️ Technologies Used
| Layer     | Stack                                |
| --------- | ------------------------------------ |
| Frontend  | React, React Router, React Bootstrap |
| Backend   | Flask, Flask-CORS, Flask-SQLAlchemy  |
| Database  | SQLite (local)                       |
| Mock Data | Faker                                |

🚀 Setup Instructions

1️⃣ Backend Setup:

1. Create a virtual environment
python -m venv venv

2. Activate it
Windows: venv\Scripts\activate
macOS/Linux: source venv/bin/activate

4. Install dependencies
pip install -r requirements.txt

6. Initialize the database with mock data
python db_init.py

7. Run the Flask server
python app.py
The backend will start at http://localhost:5000

2️⃣ Frontend Setup:

1. Install dependencies
2. Start the React app
npm start
The frontend will be available at http://localhost:3000

🖥️ How It Works
Users can log in with the credentials created in the database (testuser / 1234).
After login, users can chat with the bot by typing queries such as:
Show me laptops
Sort mobiles by price
I want a MacBook
The chatbot parses the message, queries matching products, and returns recommendations with images and prices.

🧠 Project Highlights
Full-stack integration: Seamless communication between React and Flask.

Dynamic recommendations: Products are fetched and filtered in real time.

Persistent chat history: Stored in localStorage.

Clean UI: Responsive and styled with React Bootstrap.

Mock Data: 120+ products generated using Faker.

📸 Screenshots

Login Page:

![image](https://github.com/user-attachments/assets/caa61ca2-ba7d-4e02-a620-c40e635df995)

Chatbot Chat Window:

![image](https://github.com/user-attachments/assets/ccf6d37e-d3ea-47f6-875a-3c9f81f4270b)

Product Cards:

![image](https://github.com/user-attachments/assets/0d65d79a-f803-41dc-a78a-c614793a19e5)

🧩 Architecture Diagram
![image](https://github.com/user-attachments/assets/7849469b-6d7b-4376-ad13-49d554c871d7)

📝 Potential Challenges & Solutions
CORS issues: Resolved using Flask-CORS.

Product filtering logic: Implemented keyword parsing with fallback responses.

UI responsiveness: Adjusted layouts with Bootstrap grid and media queries.

Data persistence: Used localStorage to save chat history.

📄 License
This project was developed as part of the Uplyft assignment.

👤 Author & Contact

SAYYED SAMEER BASIR

sayyedsameerbasir0208@gmail.com

https://www.linkedin.com/in/sayyed-sameer-basir-6b3195215/







