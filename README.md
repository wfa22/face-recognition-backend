# IdentityX

## Description
IdentityX is a comprehensive web application that offers functions for user registration, sending feedback, purchasing subscriptions and downloading the app. The app interacts with a camera to identify an individual, verifying that the person matches the uploaded photo. Users can upload a photo and the inbuilt model accurately recognises faces to confirm identity.
## Tech Stack
- Python
- Django
- Docker
- PostgreSQL

## Requirements
- Python 3.x
- Docker

## Installation

1. Clone the repository:
    ```bash
    https://github.com/wfa22/face-recognition-backend.git
    cd face-recognition-backend
    ```
    
2. Start Docker Engine

3. Build the Docker container:
    ```bash
    docker-compose build
    ```

## Running the Project

1. Apply database migrations:
    ```bash
    docker-compose run --rm app sh -c "python manage.py migrate"
    ```

2. Start the server:
    ```bash
    docker-compose up
    ```

The application should now be running and accessible.

## Running Tests
To run the tests, use the following command:
```bash
docker-compose run --rm app sh -c "python manage.py test"
```

### Documentation
This is our [API Documentation](./API-Documentation.md)

For more information on development, refer to the following documentation:

[Python Documentation](https://docs.python.org/3/)

[Django Documentation](https://docs.djangoproject.com/en/stable/)


## Related Repositories
Here you can visit repositories related to our project

[Frontend Repository](https://github.com/sadnesssssssss/face-recognition-fe)

[ML Repository](https://github.com/wh1t3tea/face-recognition)


### Contribution
This project is developed for educational purposes and can be further refined and expanded for specific needs.
When using this code in your projects, please provide references to the original research papers and datasets.


