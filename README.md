# Cloudlit

## Requirements

- Install python dependencies:
  ```bash
  $ pip install -r requirements.txt
  ```

  Run django project with:

  ```bash
  $ python manage.py runserver
  ```

  Send to [http://127.0.0.1:8000/cloudlit/python](http://127.0.0.1:8000/cloudlit/python) your code as a POST request. Your body must contain:
  ```
  {
      code: <Your Code>,
      filename: <Any Name>,
      extension: <For now .py> #Maybe we add more languages like c++ or java
  }
  ```