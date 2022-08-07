FROM python:3.8.13

WORKDIR /app/

COPY ./ /app/

# Environment
ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  BABEL_CACHE=0

# System deps:
RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    python -m pip install -U pip poetry

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false && \
  poetry install --no-interaction --no-root --no-dev && \
  rm -rf ~/.cache/pypoetry && \
  rm -rf ~/.config/pypoetry

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
