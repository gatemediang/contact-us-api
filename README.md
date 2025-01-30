# Contact Us API

This is a simple Flask application that provides a public API to return information in JSON format. The API returns the registered email address, the current datetime as an ISO 8601 formatted timestamp, and the GitHub URL of the project's codebase.

## Prerequisites

- Python 3.x
- Flask

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/gatemediang/Contac-us-api.git
    cd Contac-us-api
    ```

2. Create a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Create a `data.json` file with the following content:

    ```json
    {
        "email": "example@gmail.com",
        "github_url": "https://github.com/example/Contac-us-api"
    }
    ```

2. Run the Flask application:

    ```bash
    python main.py
    ```

3. Access the API at `http://127.0.0.1:5000/api/info`.

## API Endpoint

- **GET /api/info**

    Returns a JSON object with the following information:
    - `email`: The registered email address.
    - `current_datetime`: The current datetime as an ISO 8601 formatted timestamp.
    - `github_url`: The GitHub URL of the project's codebase.

## License

This project is licensed under the MIT License.