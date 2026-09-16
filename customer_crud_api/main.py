from crud import (
    create_customer,
    delete_customer,
    get_customer_by_id,
    get_customers,
    update_customer,
)
from fastapi import FastAPI
from schema import CustomerCreate

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API is running"}



@app.post("/customer")
def create_customer_api(customer: CustomerCreate):

    customer_id = create_customer(
        customer.name,
        customer.email,
        customer.phone,
        customer.city,
        customer.age
    )

    return {
        "message": "Customer created successfully",
        "customer_id": customer_id
    }

@app.get("/customers")
def get_all_customers():

    customers = get_customers()

    return customers

@app.get("/customers/{customer_id}")
def get_customer(customer_id: int):

    customer = get_customer_by_id(customer_id)

    return customer

@app.put("/customers/{customer_id}")
def update_customer_api(customer_id: int, customer: CustomerCreate):

    update_customer(
        customer_id,
        customer.name,
        customer.email,
        customer.phone,
        customer.city,
        customer.age
    )

    return {
        "message": "Customer updated successfully"
    }


@app.delete("/customers/{customer_id}")
def delete_customer_api(customer_id: int):

    deleted = delete_customer(customer_id)

    return {
        "message": "Customer deleted successfully",
        "customer": deleted
    }