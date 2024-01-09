# Simple Wikipedia Web Application

Welcome to the Simple Wikipedia Web Application, a project created using HTML, CSS, and the Django framework. This web application allows users to browse a list of Wikipedia entries, view the content of each entry, create new entries, and edit existing ones. The entries are stored locally as Markdown (.md) files.

## Features

1. **Browse Entries**: The application provides a list of Wikipedia entries that users can browse through.

2. **View Entry Content**: Clicking on an entry displays the Wikipedia page content, which is stored locally as a Markdown file.

3. **Create New Entry**: Users can create new Wikipedia entries by providing a title and content.

4. **Edit Existing Entries**: Edit the content of existing entries to keep the information up-to-date.

## Technologies Used

- **HTML and CSS**: Used for the frontend development to create a clean and user-friendly interface.

- **Django Framework**: A high-level Python web framework used for backend development, providing a robust and scalable structure.

## Installation

1. **Clone the repository:**

   
   git clone https://github.com/your-username/simple-wikipedia-web-app.git
2. **Go to directory**
   cd simple-wikipedia-web-app
3. **Run migrations**
  python manage.py migrate
4. **Run server**
   python manage.py runserver
