# url_shortener_app
Shortens provided url and redirect to original url when shortened url is used
## Getting Started

### Prerequisites

- Python 3.x installed
- [Pipenv](https://pipenv.pypa.io/en/latest/install/) installed

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/url-shortener.git
   ```
2. Navigate to the project directory:
   ```bash
   cd url_shortener_app
   cd url_shortener_proj
   ```
3. Install dependencies using Pipenv:
   ```bash
   pipenv install
   ```
4. Run migrations:
   ```bash
   python manage.py migrate
   ```
5. Run the dev server:
   ```bash
   python manage.py runserver
   ```
6. Open your web browser and input http://127.0.0.1:8000/ to access the URL shortener web app.
   
### Usage
Access the shortener by visiting the home page.
Enter a URL in the field and submit it to get a shortened URL.
Click on the shortened url to redirect to the original long URL or copy and paste it into a new browser tab.

### Contributing
If you'd like to contribute to this project, please follow these guidelines:

1. Fork the repository.
2. Create a new branch: git checkout -b feature/new-feature.
3. Make your changes and commit them: git commit -m 'Add new feature'.
4. Push to the branch: git push origin feature/new-feature.
5. Submit a pull request.

