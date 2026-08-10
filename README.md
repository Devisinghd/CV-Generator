# CV Generator

A modern Django-based web application that helps users create, manage, and download professional CV/resume profiles as polished PDF documents. The project combines a clean user experience with backend PDF generation so candidates can present their experience in a professional format with minimal effort.

## Why this project stands out

- Built with Django for a robust and scalable web architecture
- Supports profile creation, resume preview, and PDF download
- Uses HTML-to-PDF rendering for polished document output
- Designed with a simple workflow that is easy for users to understand and extend

## Key Features

- Create a professional profile with personal, academic, and work experience details
- Preview the generated CV in the browser
- Download the final resume as a PDF file
- Maintain a dashboard of saved profiles for quick access

## Tech Stack

- Python
- Django
- XHTML2PDF
- ReportLab
- HTML5Lib
- Pillow

## Project Structure

- myapp/ — main application logic, views, templates, and models
- mysite/ — Django project configuration and URL routing
- templates/ — HTML templates for the user interface
- migrations/ — database schema changes

## Getting Started

### Prerequisites

- Python 3.9+
- pip
- Virtual environment (recommended)

### Local Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply database migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```

6. Open the app in your browser at http://127.0.0.1:8000/

7. Available Live at - https://cv-generator-3d1d.onrender.com/

## Docker Deployment

Build and run the app with Docker:

```bash
docker build -t cvgenweb .
docker run -p 8000:8000 cvgenweb
```

The container will start the Django development server and expose the application on port 8000.


## Architecture Diagram

```text
User -> Django Web App -> Profile Storage (SQLiteDB)
        |                     |
        |                     +--> Resume Template Engine
        |                                     |
        +-------------------------------------> PDF Generator
```

This simple flow highlights how user input is captured, stored, rendered into a resume layout, and exported as a PDF.

## Future Enhancements

- Add authentication and user-specific profile management
- Improve the resume templates with modern themes
- Add export options for DOCX and plain text
- Integrate cloud storage or database-backed deployment

## Contact

For questions or collaboration opportunities, feel free to reach out through the project repository or contact the maintainer directly.

