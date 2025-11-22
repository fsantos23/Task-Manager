# Task Manager

> 🚧 **Status**: This project is currently under active development. The frontend is being built and features are being added regularly.

## 📖 About

A Notion-like task manager built for flexibility and self-hosting. This open-source solution provides companies, businesses, and individuals with a powerful, deployable task management system that you can run on your own infrastructure.

Built with modern web technologies including **Django** (backend), **React** (frontend), **JavaScript**, and containerized with **Docker** for easy deployment. The application uses **Nginx** as a reverse proxy to serve both the API and frontend efficiently.

Perfect for teams and organizations that want full control over their task management data without relying on third-party cloud services.

## ✨ Features

- RESTful API architecture
- Frotend (in development)
- Containerized deployment with Docker
- More features coming soon...

## 🛠️ Tech Stack

**Backend:**
- Django - Python web framework
- Django REST Framework - API development
- JWT (JSON Web Tokens) - Authentication
- PostgreSQL - Database

**Frontend:** (Under Development)
- React - JavaScript library for UI
- JavaScript - Programming language
- HTML & CSS - Markup and styling

**DevOps & Infrastructure:**
- Docker - Containerization
- Docker Compose - Multi-container orchestration
- Nginx - Web server and reverse proxy

**Development Tools:**
- Git - Version control
- npm/yarn - Package management

## 🚀 Getting Started

### Prerequisites

- Docker
- Docker Compose
- Git

### Local Deployment

1. Clone the repository
```bash
git clone https://github.com/fsantos23/Task-Manager
cd your-project
```

2. Set up environment variables
```bash
cp env-sample .env
# Edit .env with your configuration
```

3. Build and run with Docker Compose
```bash
docker-compose up --build
```

4. Access the application
```
Backend API: http://localhost:PORT
Frontend: http://localhost:PORT (when ready)
```

### Stopping the Application

```bash
# Stop containers
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

## 📦 Docker Configuration

The project uses Docker containers for seamless local deployment:

- **Django Backend** - REST API server running the Django application
- **React Frontend** - Development server for the React application (in development)
- **Nginx** - Reverse proxy server that routes requests to backend/frontend and serves static files
- **Database** - PostgreSQL container for data persistence

### Container Architecture

```
┌─────────────┐
│   Browser   │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│    Nginx    │ ← Reverse Proxy & Static Files
└──────┬──────┘
       │
       ├────────────┬─────────────┐
       ▼            ▼             ▼
┌──────────┐  ┌──────────┐  ┌──────────┐
│  Django  │  │  React   │  │ Database │
│  Backend │  │ Frontend │  │          │
└──────────┘  └──────────┘  └──────────┘
```

## 🔧 Configuration

Create a `.env` file in the root directory with the following environment variables:

### Database Configuration (PostgreSQL)

```env
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USERNAME=your_db_username
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DATABASE_NAME=taskmanager_db
```

**Explanation:**
- `POSTGRES_HOST` - The hostname of your PostgreSQL server. Use `db` if running with Docker Compose (matches the service name in docker-compose.yml)
- `POSTGRES_PORT` - PostgreSQL port number. Default is `5432`
- `POSTGRES_USERNAME` - Your PostgreSQL username. Example: `postgres` or `admin`
- `POSTGRES_PASSWORD` - A strong password for your database user. Example: `MySecurePassword123!`
- `POSTGRES_DATABASE_NAME` - The name of your database. Example: `taskmanager_db` or `notion_tasks`

### JWT Authentication Configuration

```env
REFRESH_TOKEN_LIFETIME_DAYS=7
ACCESS_TOKEN_LIFETIME_MINUTES=60
```

**Explanation:**
- `REFRESH_TOKEN_LIFETIME_DAYS` - How many days the refresh token remains valid. Recommended: `7` (one week) or `30` (one month)
- `ACCESS_TOKEN_LIFETIME_MINUTES` - How many minutes the access token remains valid. Recommended: `60` (1 hour) or `15` (15 minutes for higher security)

### Example .env File

```env
# Postgres
POSTGRES_HOST=db
POSTGRES_PORT=5432
POSTGRES_USERNAME=postgres
POSTGRES_PASSWORD=securepassword123
POSTGRES_DATABASE_NAME=taskmanager_db

# JWT
REFRESH_TOKEN_LIFETIME_DAYS=7
ACCESS_TOKEN_LIFETIME_MINUTES=60
```

## 📚 API Documentation

The API is built with Django REST Framework and uses JWT authentication. All task endpoints require authentication.

### Authentication Endpoints

**Base URL:** `/authentication/`

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| POST | `/authentication/user` | Register a new user | No |
| GET | `/authentication/user` | Get current user information | Yes |
| PATCH | `/authentication/user` | Update current user information | Yes |
| POST | `/authentication/login` | Login and obtain JWT tokens | No |
| POST | `/authentication/logout` | Logout user (blacklist refresh token) | Yes |
| POST | `/authentication/token/refresh` | Refresh access token | Yes |
| POST | `/authentication/token/verify` | Verify token validity | Yes |

**Example - User Registration:**
```json
POST /authentication/user
{
  "username": "newuser",
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Example - Get Current User:**
```json
GET /authentication/user
Headers: Authorization: Bearer <access_token>

Response:
{
  "id": 1,
  "username": "newuser",
  "email": "user@example.com"
}
```

**Example - Update User:**
```json
PATCH /authentication/user
Headers: Authorization: Bearer <access_token>
{
  "email": "newemail@example.com"
}
```

**Example - Login:**
```json
POST /authentication/login
{
  "username": "newuser",
  "password": "securepassword123"
}

Response:
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

**Example - Logout:**
```json
POST /authentication/logout
Headers: Authorization: Bearer <access_token>
{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}

Response:
"Successfully logged out"
```

### Task Management Endpoints

**Base URL:** `/api/`

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| GET | `/api/tasks` | Get all tasks (paginated, max 50 per page) | Yes |
| POST | `/api/tasks` | Create a new task | Yes |
| GET | `/api/tasks/<task_id>` | Get a specific task by ID | Yes |
| PATCH | `/api/tasks/<task_id>` | Update a specific task | Yes |
| DELETE | `/api/tasks/<task_id>` | Delete a specific task | Yes |

**Features:**
- ✅ Pagination (50 tasks per page)
- ✅ Filtering support via query parameters
- ✅ JWT authentication required for all task endpoints
- ✅ Partial updates supported (PATCH)

**Example - Create Task:**
```json
POST /api/tasks
Headers: Authorization: Bearer <access_token>
{
  "title": "Complete project documentation",
  "description": "Update README and API docs",
  "status": "pending",
  "priority": "high"
}
```

**Example - Update Task:**
```json
PATCH /api/tasks/1
Headers: Authorization: Bearer <access_token>
{
  "status": "completed"
}
```

**Example - Get Tasks with Filtering:**
```
GET /api/tasks?status=pending&priority=high
Headers: Authorization: Bearer <access_token>
```

### Authentication Flow

1. **Register** a new user at `POST /authentication/user`
2. **Login** at `POST /authentication/login` to receive access and refresh tokens
3. **Use access token** in the Authorization header: `Authorization: Bearer <access_token>`
4. **Access user info** at `GET /authentication/user` or update with `PATCH /authentication/user`
5. **Refresh token** when access token expires using `POST /authentication/token/refresh`
6. **Logout** at `POST /authentication/logout` with refresh token to blacklist it


### [Ongoing]
- 🚧 Frontend development in progress

### Upcoming Features
- Complete frontend interface
- User dashboard
- Additional API endpoints
- Performance optimizations
- Documentation improvements

---

⭐ **Note**: This project is actively being developed. Star the repo to stay updated with new features!


