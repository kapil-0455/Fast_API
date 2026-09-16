import psycopg

connection = psycopg.connect(
    "dbname=Customer_management "
    "user=postgres "
    "password=your_password "
    "host=localhost "
    "port=5432"
)

print("Database connected successfully")