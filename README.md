## CI/CD with Jenkins

## TASK 1: 1. Jenkins CI CD pipeline for flask application

This project is configured with a Jenkins CI/CD pipeline for the Flask application.

### Prerequisites

- Jenkins server (e.g., Ubuntu VM)
- Java 17+
- Python 3 and pip
- Git
- (Optional) MongoDB instance for the application
- Access to GitHub

### Pipeline Overview

The pipeline is defined in the `Jenkinsfile` at the root of the repository.

Stages:

1. **Checkout**
   - Jenkins checks out the latest code from the `main` branch of this repository.

2. **Build**
   - Creates a Python virtual environment inside the Jenkins workspace.
   - Installs all dependencies from `requirements.txt` using `pip`.

3. **Test**
   - Runs unit tests using `pytest`.
   - The tests are located in the `tests/` directory.
   - If any test fails, the pipeline stops and deployment does not happen.

4. **Deploy**
   - If tests pass, the Flask application is started as a "staging" server on the Jenkins machine.
   - Environment variables such as `MONGO_URI` and `SECRET_KEY` are set before starting the app.
   - The app is started with `nohup` so it continues running in the background.

### Triggers

- The Jenkins job is configured with a **GitHub webhook**.
- Whenever a commit is pushed to the `main` branch, GitHub sends a webhook to Jenkins, which triggers a new build.

### Notifications

- Jenkins is configured with SMTP (e.g., Gmail).
- The pipeline uses the `mail` step in the `post` section:
  - Sends an email when the build **succeeds**.
  - Sends an email when the build **fails**.
- Emails include the job name, build number, and a link to the Jenkins build logs.

### How to Run the Pipeline

1. Ensure Jenkins is running and configured with the correct Git repository and credentials.
2. Push any change to the `main` branch.
3. Jenkins will:
   - Checkout the code
   - Build and install dependencies
   - Run tests
   - Deploy the application (if tests pass)
4. Check the Jenkins console output and your email for the build status.# Student Registration System




A simple **Flask** web application to manage student records with **MongoDB** as the backend database. Users can **add, view, update, and delete** student details.

---

## Features

* List all students on the home page
* Add a new student
* Update existing student details
* Delete a student with confirmation
* Simple and responsive UI using Bootstrap

---

## Tech Stack

* **Backend:** Python, Flask
* **Database:** MongoDB (via Flask-PyMongo)
* **Frontend:** HTML, Jinja2 templates, Bootstrap 5
* **Environment Variables:** Managed via `.env` file

---

## Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Activate venv
# Windows:
venv\Scripts\activate
# Linux / Mac:
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt` example:**

```
Flask
Flask-PyMongo
python-dotenv
bson
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```
MONGO_URI=<your-mongodb-connection-string>
SECRET_KEY=<your-secret-key>
```

### 5. Run the application

```bash
python app.py
```

Open your browser at: [http://localhost:8000](http://localhost:8000)

---

## Project Structure

```
project/
│
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_student.html
│   ├── update_student.html
│
├── app.py
├── requirements.txt
└── .env
```

---

## Screenshots

**Home Page**
Lists all students with Edit/Delete buttons.
- <img width="1902" height="607" alt="image" src="https://github.com/user-attachments/assets/a58a6a6d-4978-4769-8074-232e4d31e69d" />


**Add Student**
Form to add a new student.
- <img width="1897" height="801" alt="image" src="https://github.com/user-attachments/assets/d65d25c3-ebb5-410a-adb1-e130ad7c5878" />


**Update Student**
Form pre-filled with student details.
- <img width="1905" height="897" alt="image" src="https://github.com/user-attachments/assets/04febf01-879f-431f-ab07-abcfb993acf1" />



---

## Notes

* Make sure MongoDB is running and accessible via the URI in `.env`
* Delete action includes a confirmation page to prevent accidental deletion
* Uses `ObjectId` from `bson` to work with MongoDB document IDs

---

## License

MIT License

---



