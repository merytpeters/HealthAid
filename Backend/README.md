This is the backend directory of the HealthAid repository
cd Backend
1. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Set up the MySQL database:
    ```bash
    mysql -u root -p
    CREATE DATABASE health_aid;
    ```

3. Configure the database URI in your environment variables:
    ```bash
    export DATABASE_URL='mysql+pymysql://username:password@localhost/health_aid'

    ```

4. Create a `.env` file to hold all variables in `config.py`:
    ```bash
    touch .env
    ```

5. Run the Flask application:
    ```bash
    flask run
    ```
    ```bash
    flask run
    ```

6. Access the application in your browser at `http://127.0.0.1:5000`
