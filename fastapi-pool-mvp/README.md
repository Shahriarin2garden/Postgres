# fastapi-pool-mvp

A minimal, production-oriented FastAPI application showcasing **asyncpg connection pool** patterns for high-throughput PostgreSQL access.

## Quick Start

### Docker Compose (Recommended)

1. **Clone and setup**
   ```bash
   cd fastapi-pool-mvp
   cp .env.example .env
   ```

2. **Start services**
   ```bash
   docker-compose up --build
   ```

3. **Access the API**
   - Swagger UI: http://localhost:8000/docs
   - Health endpoint: http://localhost:8000/health

### Local Development

1. **Setup environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

2. **Configure database**
   Update `.env` with your PostgreSQL settings.

3. **Run application**
   ```bash
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```

## API Endpoints

- `GET /health` - Health check
- `GET /users/` - List all users
- `POST /users/` - Create user
- `GET /users/{user_id}` - Get user by ID

## Configuration

Environment variables (see `.env.example`):
- `DB_HOST`, `DB_PORT`, `DB_USER`, `DB_PASS`, `DB_NAME` - Database connection
- `POOL_MIN_SIZE`, `POOL_MAX_SIZE` - Connection pool settings
- `COMMAND_TIMEOUT` - Query timeout in seconds

## Testing

```bash
pytest tests/
```

## Architecture

- **Connection Pool**: Global asyncpg pool with configurable limits
- **Async Services**: All database operations use pool connections
- **Auto-initialization**: Tables created on startup
- **Error Handling**: Proper HTTP status codes and exception handling