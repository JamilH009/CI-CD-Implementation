# Pre-Lecture Task: Build Your Own Task Management API

## Software Requirements

Before starting, ensure you have the following installed:

1. **Python 3.11**
   ```bash
   # For macOS (using Homebrew)
   brew install python@3.11
   
   # For Windows
   # Download from https://www.python.org/downloads/
   ```

2. **Docker**
   ```bash
   # For macOS (using Homebrew)
   brew install --cask docker
   
   # For Windows
   # Download from https://www.docker.com/products/docker-desktop/
   ```

3. **Required Python Packages**
   ```bash
   pip install fastapi==0.104.1 uvicorn==0.24.0 pydantic==2.4.2 pytest==7.4.3 httpx==0.25.1 python-dotenv==1.0.0
   ```

4. **Git** (for version control)
   ```bash
   # For macOS (using Homebrew)
   brew install git
   
   # For Windows
   # Download from https://git-scm.com/downloads
   ```

## Project Setup

1. Create a new project directory:
   ```bash
   mkdir task-management-api
   cd task-management-api
   ```

2. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Create the following project structure:
   ```
   task-management-api/
   ├── app/
   │   ├── api/
   │   │   └── tasks.py
   │   ├── models/
   │   │   └── task.py
   │   └── main.py
   ├── tests/
   │   └── test_tasks.py
   ├── requirements.txt
   └── README.md
   ```

## Task Requirements

### 1. Task Model
Create a Task model with the following fields:
- `id`: UUID (auto-generated)
- `title`: String (required, max 100 characters)
- `description`: String (optional)
- `category`: String (required, e.g., "Work", "Personal", "Shopping")
- `priority`: Enum (required, values: "High", "Medium", "Low")
- `status`: Enum (required, values: "Pending", "In Progress", "Completed")
- `due_date`: DateTime (optional)
- `created_at`: DateTime (auto-generated)
- `updated_at`: DateTime (auto-generated)

### 2. API Endpoints
Implement the following endpoints:

1. **Create Task**
   - Endpoint: `POST /api/v1/tasks/`
   - Request Body: Task details
   - Response: Created task with ID

2. **List Tasks**
   - Endpoint: `GET /api/v1/tasks/`
   - Query Parameters:
     - `category`: Filter by category
     - `priority`: Filter by priority
     - `status`: Filter by status
     - `sort_by`: Sort by field (due_date, priority, created_at)
   - Response: List of tasks

3. **Get Task**
   - Endpoint: `GET /api/v1/tasks/{task_id}`
   - Response: Task details

4. **Update Task**
   - Endpoint: `PUT /api/v1/tasks/{task_id}`
   - Request Body: Updated task details
   - Response: Updated task

5. **Delete Task**
   - Endpoint: `DELETE /api/v1/tasks/{task_id}`
   - Response: Success message

6. **Get Tasks by Category**
   - Endpoint: `GET /api/v1/tasks/categories/{category}`
   - Response: List of tasks in category

7. **Get Tasks by Priority**
   - Endpoint: `GET /api/v1/tasks/priority/{priority}`
   - Response: List of tasks with priority

8. **Update Task Status**
   - Endpoint: `PUT /api/v1/tasks/{task_id}/status`
   - Request Body: New status
   - Response: Updated task

### 3. Testing Requirements

1. **Unit Tests**
   - Test all API endpoints
   - Test input validation
   - Test error handling
   - Test filtering and sorting
   - Test status updates

2. **Test Cases**
   - Create task with valid data
   - Create task with invalid data
   - Update task
   - Delete task
   - Filter tasks
   - Sort tasks
   - Update task status

### 4. Docker Setup

1. Create a Dockerfile:
   ```dockerfile
   FROM python:3.11-slim
   WORKDIR /app
   COPY requirements.txt .
   RUN pip install --no-cache-dir -r requirements.txt
   COPY . .
   CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
   ```

2. Build and run the container:
   ```bash
   docker build -t task-api .
   docker run -p 8000:8000 task-api
   ```

## Implementation Tips

1. **Start with the Basics**
   - Set up the project structure
   - Create the Task model
   - Implement basic CRUD operations

2. **Add Features Incrementally**
   - Add one feature at a time
   - Test each feature before moving on
   - Keep the code organized

3. **Testing Strategy**
   - Write tests as you develop
   - Test both success and error cases
   - Use pytest fixtures for common setup

4. **Documentation**
   - Use FastAPI's automatic docs
   - Add clear comments
   - Document your API

## What to Bring to Next Lecture

1. Your working Task Management API
2. Questions about any challenges you faced
3. Ideas for improvements
4. Any specific topics you'd like to discuss

## Resources

1. [FastAPI Documentation](https://fastapi.tiangolo.com/)
2. [Pydantic Documentation](https://docs.pydantic.dev/)
3. [Python Testing with pytest](https://docs.pytest.org/)
4. [Docker Documentation](https://docs.docker.com/)

## Note

This is a learning exercise - focus on understanding the concepts rather than creating a perfect application. We'll review and improve the code together in the next lecture. 