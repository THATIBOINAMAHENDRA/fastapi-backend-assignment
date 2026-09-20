# Property Management API

A RESTful FastAPI backend for managing property and customer records.

## Setup Instructions
1. Clone the repository to your local machine.
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: 
   - Linux/Mac: `source venv/bin/activate`
   - Windows: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`

## Database Setup
The application uses SQLite for portability. The database file (`properties.db`) and all necessary tables are automatically created the first time the application starts.

## How to Run the API
Start the FastAPI server using Uvicorn by running this command in your terminal:
`uvicorn app.main:app --reload`

Once running, you can view the interactive Swagger/OpenAPI documentation by navigating to:
`http://127.0.0.1:8000/docs`

## How to Run Tests
The automated test suite is written using `pytest` and the FastAPI TestClient. To run the tests, execute:
`python -m pytest`

## API Examples
* **Create Record:** `POST /properties`
  * Body: `{"id": "AV1001", "customer_name": "Ravi Kumar", "customer_mobile": "9876543210", "property_name": "Serene Grand", "property_type": "APARTMENT", "status": "NEW"}`
* **Retrieve Record:** `GET /properties/AV1001`
* **List/Search Records:** `GET /properties?status=NEW`
* **Delete Record:** `DELETE /properties/AV1001`

## Assumptions & Technical Decisions
* **Database:** SQLite was chosen to ensure the application is easily runnable locally by another developer without requiring a separate SQL server installation.
* **Deletion:** A hard delete was implemented for the DELETE endpoint. 
* **Validation:** Phone numbers are validated purely on length (10-15 characters) using Pydantic's `constr`.

## Final Note
* **Implemented:** Full CRUD operations (Create, Read, Update, Delete) with SQLite, automated testing via pytest covering edge cases, and input validation using Pydantic.
* **Not Implemented:** Pagination for the list endpoint and authentication mechanisms, in order to keep the codebase focused strictly on the assignment's core requirements.
* **Future Improvements:** Given more time, I would implement a soft-delete mechanism (using an `is_deleted` boolean flag), migrate to PostgreSQL for production readiness, and add Docker support for containerized deployment.