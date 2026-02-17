# SubTube

YouTube Subscription Manager — a full-stack web application for managing YouTube subscriptions.

## Tech Stack

- **Backend**: Python 3.12, Django 6, Django REST Framework, django-allauth, dj-rest-auth, SimpleJWT
- **Frontend**: Next.js 15, TypeScript, Tailwind CSS v4, React Query, shadcn/ui
- **Database**: PostgreSQL 16
- **Package Managers**: uv (backend), pnpm (frontend)

## Prerequisites

- [Python 3.12+](https://www.python.org/) (managed by uv)
- [uv](https://docs.astral.sh/uv/) — Python package manager
- [Node.js 20+](https://nodejs.org/)
- [pnpm](https://pnpm.io/) — Node.js package manager
- [Docker](https://www.docker.com/) — for running PostgreSQL locally

## Local Development Setup

### 1. Start the database

```bash
docker compose up -d
```

This starts a PostgreSQL 16 instance on port 5432 with database `subtube`.

### 2. Set up the backend

```bash
cd backend
cp .env.example .env          # Create local environment file
uv sync                       # Install dependencies
uv run python manage.py migrate  # Run database migrations
uv run python manage.py runserver  # Start dev server on http://localhost:8000
```

### 3. Set up the frontend

```bash
cd frontend
cp .env.local.example .env.local  # Create local environment file
pnpm install                      # Install dependencies
pnpm dev                          # Start dev server on http://localhost:3000
```

## Environment Variables

### Backend (`backend/.env`)

| Variable | Description | Default |
|----------|-------------|---------|
| `DJANGO_SETTINGS_MODULE` | Settings module to use | `subtube_api.settings.local` |
| `SECRET_KEY` | Django secret key | Insecure default (dev only) |
| `CORS_ALLOWED_ORIGINS` | Comma-separated allowed origins | `http://localhost:3000` |
| `DB_NAME` | PostgreSQL database name | `subtube` |
| `DB_USER` | PostgreSQL user | `subtube` |
| `DB_PASSWORD` | PostgreSQL password | `subtube` |
| `DB_HOST` | PostgreSQL host | `localhost` |
| `DB_PORT` | PostgreSQL port | `5432` |
| `GOOGLE_CLIENT_ID` | Google OAuth client ID | — |
| `GOOGLE_CLIENT_SECRET` | Google OAuth client secret | — |

### Frontend (`frontend/.env.local`)

| Variable | Description | Default |
|----------|-------------|---------|
| `NEXT_PUBLIC_API_URL` | Backend API base URL | `http://localhost:8000` |

## Running Tests

### Backend

```bash
cd backend
uv run ruff check .   # Linting
uv run pytest         # Tests
```

### Frontend

```bash
cd frontend
pnpm lint    # ESLint
pnpm build   # Type checking + build
```

## Project Structure

```
subtube/
├── backend/           # Django API
│   ├── subtube_api/   # Django project (settings, urls, wsgi)
│   ├── users/         # Users app (stub)
│   ├── subscriptions/ # Subscriptions app (stub)
│   ├── tests/         # pytest tests
│   ├── Dockerfile     # Production container
│   └── pyproject.toml # Python dependencies
├── frontend/          # Next.js app
│   ├── app/           # App Router pages
│   ├── lib/           # Shared utilities
│   ├── components/    # UI components
│   └── types/         # TypeScript types
├── .github/workflows/ # CI pipelines
├── docker-compose.yml # Local PostgreSQL
└── README.md
```
