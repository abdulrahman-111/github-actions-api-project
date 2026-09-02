FROM python:3.13-slim


# Install uv by copying it directly from the official image
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app


# Copy dependency files first for Docker layer caching
COPY pyproject.toml uv.lock ./

# Install only runtime dependencies  , not install project package 
RUN uv sync --locked --no-dev --no-install-project


# Copy the project into the image
COPY . .


# Install the project itself if your pyproject.toml defines it as a package
RUN uv sync --locked --no-dev

EXPOSE 8000

# Run the application.
CMD ["uv", "run", "uvicorn", "github_actions_api_project.main:app", "--host","0.0.0.0","--port","8000"]



