# Notes App 

A straightforward web-based notes application built with Flask and MySQL. It allows you to perform full CRUD (Create, Read, Update, Delete) operations, helping you keep your thoughts organized with a simple and clean interface.

## Features

- **Create Notes:** Quickly add new notes through a simple form.
- **Read Notes:** View all your saved notes on the main dashboard.
- **Update Notes:** Edit the content of any existing note.
- **Delete Notes:** Remove notes you no longer need.
- **User-Friendly Interface:** Clean and minimalistic HTML/CSS design for easy navigation.
- **Input Validation:** Prevents the submission of empty notes.

## Technologies Used

- **Backend:** Python with Flask web framework
- **Database:** MySQL
- **Frontend:** HTML, CSS
- **Database Connector:** `mysql-connector-python`

## Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.6+**
- **MySQL Server** (e.g., XAMPP, MAMP, or standalone MySQL)
- **pip** (Python package installer)

## Installation & Setup

Follow these steps to get the application up and running on your local machine.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/iamajaykr06/Notes-App.git
    cd Notes-App

2. **Set up a virtual environment (Recommended):**
   
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies:**
    As a requirements.txt file is not currently present in the repository, you will need to manually install the required packages.

    ```bash
    pip install flask mysql-connector-python

4. **Configure the Database:**

   * Open your MySQL client and create a new database:

    ```bash
    CREATE DATABASE notes_db;
    ```
    * Next, create the required `notes` table within this database:
    ```bash
    USE notes_db;
    CREATE TABLE notes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    content TEXT NOT NULL
    );
    ```

6.  **Update Database Credentials:**

     * Open the `app.py` file in a text editor.

     * Locate the `get_db_connection` function and update the connection parameters (host, user, password, database) to match your local MySQL setup:
     ```
      def get_db_connection():
        return mysql.connector.connect(
        host="localhost",
        user="your_mysql_username",
        password="your_mysql_password",
        database="notes_db"
        )
    ```

7.  **Run the Application:**
   `python app.py`
   The application will start on `http://127.0.0.1:5000/`. Open this address in your web browser.

## Usage
   Once the application is running, you can manage your notes as follows:

* **Add a Note:** Enter your text in the "Write Your Notes" textarea and click the "Post Note" button. It will immediately appear in the "All Posted Notes" section.

* **View All Notes:** All existing notes are displayed on the main page.

* **Edit a Note:** Next to each note, click the "Edit" button. This will take you to a new page where you can modify the content. Click "Update" to save your changes.

* **Delete a Note:** Click the "Delete" button next to the note you wish to remove.

## Project Structure

```bash
Notes-App/
│
├── app.py              # Main Flask application with all route logic
├── templates/          # Directory containing HTML templates
│   ├── index.html      # Main page for viewing and creating notes
│   └── edit.html       # Page for editing an existing note
└── README.md           # Project documentation (this file)
```
## Contributing

   Contributions, issues, and feature requests are welcome! Feel free to check the issues page if you'd like to contribute.

1. Fork the Project

2. Create your Feature Branch (git checkout -b feature/AmazingFeature)

3. Commit your Changes (git commit -m 'Add some AmazingFeature')

4. Push to the Branch (git push origin feature/AmazingFeature)

5. Open a Pull Request

## License

  This project is currently unlicensed. If you wish to add a license, the MIT license is a common choice for open-source projects.

## Contact

**Ajay Kumar** - @iamajaykr06

**Project Link:** https://github.com/iamajaykr06/Notes-App
