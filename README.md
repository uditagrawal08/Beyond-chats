# Flask API Data Viewer

This Flask application fetches data from an API endpoint and displays it on a web page. The data consists of responses along with their associated sources and citations. Users can navigate through the data using pagination.

## Installation and Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/uditagrawal08/Beyond-chats.git
    ```

2. Navigate to the project directory:

    ```bash
    cd your_repository
    ```

3. Install the required dependencies:
    
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Access the application in your web browser at `http://localhost:5000`.

## Requirements

- Python 3.x

## Usage

- Upon accessing the application, you'll be presented with a paginated view of the fetched data.
- Each response is displayed along with its associated sources and citations.
- Use the next buttons to move to next pages.

## Dependencies

- Flask: A lightweight WSGI web application framework.
- Requests: HTTP library for making requests to web servers.
- Jinja2: Templating engine used for rendering HTML templates.


