# github-actions-api-project

sources used for ci.yaml 
https://docs.astral.sh/uv/guides/integration/github/#setting-up-python

https://github.com/marketplace/actions/astral-sh-setup-uv


# Commands to RUn 

uv run pytest 
uv run ruff check .

uv run uvicorn github_actions_api_project.main:app --reload