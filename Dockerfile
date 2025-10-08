FROM python:3.12-slim

# Install git, which is required to clone the repository
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Set the application directory
WORKDIR /app

# Clone the specified repository
# The '.' at the end clones it into the current WORKDIR
RUN git clone https://github.com/limcheekin/parlant-qna.git .

# Install the package and its dependencies from the cloned source
RUN pip install .
RUN pip install --no-cache-dir litellm datasets transformers
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu
