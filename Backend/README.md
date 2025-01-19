This is the backend directory of the HealthAid repository

1. Navigate to the Backend directory and create a virtual environment:
    ```bash
    cd Backend
    python -m venv venv
    ```

2. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```
    On Windows use
    ```bash 
    venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the MySQL database:
    ```bash
    mysql -u root -p
    CREATE DATABASE health_aid;
    ```

5. Configure the database URI in your environment variables:
    ```bash
    export DATABASE_URL='mysql://username:password@localhost/health_aid'

    ```

6. Create a `.env` file to hold all variables in `config.py`:
    ```bash
    touch .env
    ```

7. Run the Flask application:
    ```bash
    flask run
    ```

8. Access the application in your browser at `http://127.0.0.1:5000`

9. SymptomChecker API setup:
    - Create an account with APIMEDIC.
    - Add the API key to your `.env` file:
      ```bash
      APIMEDIC_API_KEY=your_api_key
      SYMPTOM_CHECKER_SECRET_KEY=your_secret_key
      ```
