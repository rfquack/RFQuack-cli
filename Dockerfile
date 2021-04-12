FROM python:3.9-slim
WORKDIR /usr/src/app

COPY . .
RUN pip install -e .

# RUN :)
ENTRYPOINT ["rfquack"]
CMD [ "--help" ]
