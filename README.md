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
- Python 3.13.1
- poetry (Python package manager)

---

## Installation

1. **Clone the repository**  
  ```sh
  git clone https://github.com/derekgygax/zoo-breeding-service.git
  cd zoo-breeding-service
  ```

2. **Install dependencies**  
  Ensure you have **Poetry** installed, then run:  
  ```sh
  poetry install
  ```

3. **Set up environment variables**  
  - Create a `.env` file in the root directory and add the required configuration:  
    ```ini
    DATABASE_URL=postgresql://user:password@localhost:5432/zoo_breeding
    AUTH_SECRET=your_secret_key
    AUTH_ALGORITHM=your_algorithm
    ```

---

## VS Code Recognize the Poetry Installs  

By default, VS Code may not detect the virtual environment created by Poetry. Follow these steps to ensure VS Code properly recognizes and uses the Poetry environment:  

1. **Locate the Poetry Virtual Environment Path**  
  Run the following command to get the path to the Poetry virtual environment:  
  ```sh
  poetry env info --path
  ```

2. **Select the Virtual Environment in VS Code**  
  - Open the **Command Palette** (`Cmd + Shift + P` on macOS, `Ctrl + Shift + P` on Windows/Linux).  
  - Search for **"Python: Select Interpreter"** and select it.  
  - Click **"Enter interpreter path"** → **"Find..."**  
  - Paste the path from the command in the first step and press Enter.  

3. **Set Up the Workspace for Auto-Detection (If Needed)**  
  If VS Code still doesn’t detect the Poetry environment automatically, manually specify it in `.vscode/settings.json`:  

  ```json
  {
    "python.defaultInterpreterPath": "<PASTE_THE_PATH_HERE>",
    "python.venvPath": "~/.cache/pypoetry/virtualenvs"
  }
  ```

  Replace `<PASTE_THE_PATH_HERE>` with the exact path from `poetry env info --path`.  

4. **Restart VS Code (If Needed)**  
  Close and reopen VS Code, then check that it is using the correct environment by running:  
  ```sh
  poetry run python --version
  ```  
  This should match the Python version used by your Poetry environment.  

---

## Running the API

1. Start the development server:
  ```bash
  poetry run uvicorn app.main:app --reload --port 8103
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
poetry run pytest
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