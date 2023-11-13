FROM python:3.8

WORKDIR /app/be/

RUN pip install fastapi uvicorn
RUN pip install sqlalchemy
RUN pip install pyyaml
RUN pip install psycopg2

COPY ./ ./

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]