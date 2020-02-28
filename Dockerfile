FROM python:3.8.1-alpine
WORKDIR /usr/src/app

# First solve requirements
COPY requirements.pip Pipfile Pipfile.lock ./
RUN pip install --no-cache-dir -r requirements.pip

# Then copy the rest and install RFQ-CLI
COPY . .
RUN python setup.py install

# RUN :)
ENTRYPOINT ["rfquack"]
CMD [ "--help" ]
