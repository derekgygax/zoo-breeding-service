# Zoo Breeding Service

This is the **Breeding API** for managing breeding-related data in the zoo management system. Built with **FastAPI**, it handles operations such as breeding records and litter data. It is part of a larger microservices-based architecture for zoo management.

---

## Features

- CRUD operations for breeding.
- Management of breeding events.
- Integration with a relational database (e.g., PostgreSQL).
- Role-based access control (RBAC) with JWT authentication.
- API documentation via Swagger UI and ReDoc.

---

## Requirements

Make sure you have the following installed:
- Python 3.12.5
- pip (Python package manager)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/derekgygax/zoo-breeding-service.git
   cd zoo-breeding-service
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory with the necessary configuration.
     Example:
     ```
     DATABASE_URL=postgresql://user:password@localhost:5432/zoo_breeding
     AUTH_SECRET=your_secret_key
     AUTH_ALGORITHM=your_algorithm
     ```

---

## Running the API

1. Start the development server:
   ```bash
   uvicorn main:app --reload
   ```


2. Access the API documentation:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Project Structure

```
zoo-breeding-service/
├── app/
│   ├── models/        # Database models
│   ├── routers/        # API routes
│   ├── schemas/       # Pydantic schemas
│   ├── services/      # Business logic
│   ├── __init__.py    # Package initialization
├── main.py            # Entry point of the application
├── requirements.txt   # Dependency file
├── .env               # Environment variables
├── README.md          # Project documentation
```

---

## Testing

Run tests using your preferred testing framework (e.g., `pytest`):
```bash
pytest
```

---

## Contributing

Contributions are welcome! Please fork the repository, create a new branch, and submit a pull request for review.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Repository

The repository for this project is hosted at: [https://github.com/derekgygax/zoo-breeding-service.git](https://github.com/derekgygax/zoo-breeding-service.git)
```