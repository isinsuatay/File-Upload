# Django File Upload Application

This Django project is a simple web application where users can upload files.

## Requirements

- Python (3.x)
- Django (3.x)

## Usage

- On the homepage, use the "Choose File" button to select a file.
- After selecting the file, click the "Upload File" button to upload the file to the server.
- Upon successful upload, you will receive a confirmation message.
## Installation

1. Clone this repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd django-file-upload
    ```

3. Create a virtual environment (optional):

    ```bash
    python -m venv myenv
    ```

4. Activate the virtual environment (Windows):

    ```bash
    myenv\Scripts\activate
    ```

   Activate the virtual environment (Unix or MacOS):

    ```bash
    source myenv/bin/activate
    ```

5. Install required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

6. Update the database:

    ```bash
    python manage.py migrate
    ```

7. Start the server:

    ```bash
    python manage.py runserver
    ```

8. Go to `http://127.0.0.1:8000/` in your browser and observe the application.


