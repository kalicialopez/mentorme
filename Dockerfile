FROM --platform=$BUILDPLATFORM ghcr.io/astral-sh/uv:python3.12-bookworm

EXPOSE 8000

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install binutils libproj-dev gdal-bin

# Install the project into `/app`
WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Copy from the cache instead of linking since it's a mounted volume
ENV UV_LINK_MODE=copy

ENV UV_PYTHON_PREFERENCE="only-system"

COPY .python-version /app
COPY uv.lock /app
COPY pyproject.toml /app

# Install the project's dependencies using the lockfile and settings
# RUN --mount=type=cache,target=/root/.cache/uv \
#    --mount=type=bind,source=uv.lock,target=uv.lock \
#    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
#    uv sync --frozen --no-install-project
#    uv sync --frozen --no-install-project --no-dev

RUN uv sync --frozen

# Then, add the rest of the project source code
ADD app /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Reset the entrypoint, don't invoke `uv`
ENTRYPOINT []

# Run the application by default
CMD ["/app/run.sh"]
