ARG PYTHON_VERSION=3.10.2-slim-bullseye

FROM python:${PYTHON_VERSION} as python

# BUILD STAGE
FROM python as pthyon-build-stage
ARG BUILD_ENVIORMENT=local

RUN apt-get update && apt-get install --no-install-recommends -y \
    build-essential \
    libpq-dev

COPY ./requirements . 

RUN pip wheel --wheel-dir /usr/src/app/wheels \
    -r ${BUILD_ENVIORMENT}.txt


# RUN STAGE
FROM python as python-run-stage

ARG BUILD_ENVIORMENT=local
ARG APP_HOME=/app

ENV PYTHONDONTWRITEBYTECODE 1

ENV UNBUFFERED 1

ENV BUILD_ENVIORMENT=${BUILD_ENVIORMENT}

WORKDIR ${APP_HOME}

RUN apt-get update && apt-get install --no-install-recommends -y \
    libpq-dev \
    gettext \
    && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
    && rm -rf /var/lib/apt/lists/*

# use wheels to make installation faster
COPY --from=python-build-stage /usr/src/app/wheels /wheels/

RUN pip install --no-cache-dir --no-index --find-links=/wheels/ /wheels/* \
    && rm -rf /wheels/
    
# Copy in entrypoint to test connection to database
COPY ./docker/local/django/entrypoint /entrypoint
RUN sed -i 's/\r$//g' /entrypoint
RUN chmod +x /entrypoint

# check if models are migrated
COPY ./docker/local/django/start /start
RUN sed -i 's/\r$//g' /start
RUN chmod +x /start

# COPY ./docker/local/django/celery/worker/start /start-celeryworker
# RUN sed -i 's/\r$//g' /start-celeryworker
# RUN chmod +x /start-celeryworker

# COPY ./docker/local/django/celery/flower/start /start-flower
# RUN sed -i 's/\r$//g' /start-flower
# RUN chmod +x /start-flower

COPY . ${APP_HOME}

ENTRYPOINT ["/entrypoint"]