FROM python:3.9-slim
WORKDIR /usr/src/app

COPY . .
RUN pip install --no-cache-dir -r requirements.pip
RUN pip install -e .

# RUN :)
ENTRYPOINT ["rfquack"]
CMD [ "--help" ]
