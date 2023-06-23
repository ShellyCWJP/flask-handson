FROM python:3.9.7-slim-buster

# Install tools
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        wget gnupg unzip curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update \
    && apt-get install -y google-chrome-stable \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install ChromeDriver
RUN wget -q https://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip \
    && chmod +x chromedriver \
    && mv chromedriver /usr/local/bin/ \
    && rm chromedriver_linux64.zip


WORKDIR /usr/src/app
ENV FLASK_APP=app

COPY /app/requirements.txt ./

RUN apt-get install google-chrome-stable
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

