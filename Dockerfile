FROM --platform=linux/amd64 python:3.11.3-slim

# Set the working directory and copy the application code
WORKDIR /app

# Install dependencies
RUN apt-get update
RUN apt-get install -y git g++ gcc pkg-config make cmake m4 libgmp-dev libsodium-dev libsecp256k1-dev

# # Create a new user
# RUN useradd -m -s /bin/bash smartchain
# RUN chown -R smartchain:smartchain /app

# # Switch to the new user
# USER smartchain

# Set the working directory for the application code
WORKDIR /app/aleph-vortex-app

# Install Poetry
RUN pip install --upgrade pip==23.1.2
RUN pip install poetry==1.5.1
COPY pyproject.toml poetry.lock ./
RUN poetry env info
RUN poetry install
COPY . .

# Run the application
CMD ["poetry", "run", "python", "src/main.py"]