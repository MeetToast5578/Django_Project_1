FROM python:3.12
ARG DIR=/code

WORKDIR $DIR

# Install the system dependencies needed to compile uWSGI and other C-extensions
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN python3 -m pip install --upgrade pip

# Now pip will have the tools to compile uWSGI
RUN python3 -m pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8050

CMD [ "uwsgi", "--ini", "uwsgi.ini"]