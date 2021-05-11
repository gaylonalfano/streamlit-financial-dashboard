import psycopg2
import psycopg2.extras
import config


# Connect to the database
connection = psycopg2.connect(
    host=config.DB_HOST,
    database=config.DB_NAME,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
)
# Create a cursor object so we can run SQL
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
