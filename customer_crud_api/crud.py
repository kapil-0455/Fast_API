from database import connection


def create_customer(name, email, phone, city, age):
    cursor = connection.cursor()
    query = """
        insert into customers (name, email, phone, city, age)
        values (%s, %s, %s, %s, %s)
        returning customer_id;
    """

    cursor.execute(query, (name, email, phone, city, age))
    customer_id = cursor.fetchone()[0]
    connection.commit()
    cursor.close()

    return customer_id


def get_customers():
    cursor = connection.cursor()

    query = """
        select * from customers;
    """

    cursor.execute(query)
    customers = cursor.fetchall()
    cursor.close()
    return customers


def get_customer_by_id(customer_id):
    cursor = connection.cursor()
    query = """
        select *
        from customers
        where customer_id = %s;
    """
    cursor.execute(query, (customer_id,))
    customer = cursor.fetchone()
    cursor.close()

    return customer


def update_customer(customer_id, name, email, phone, city, age):
    cursor = connection.cursor()

    query = """
        update customers
        set name = %s,
            email = %s,
            phone = %s,
            city = %s,
            age = %s
        where customer_id = %s;
    """

    cursor.execute(query,(name, email, phone, city, age, customer_id))
    connection.commit()
    updated = cursor.rowcount
    cursor.close()

    return updated


def delete_customer(customer_id):
    cursor = connection.cursor()

    query = """
        delete from customers
        where customer_id = %s
        returning customer_id, name, email, phone, city, age;
    """

    cursor.execute(query, (customer_id,))
    deleted = cursor.fetchone()
    connection.commit()
    cursor.close()

    return deleted

