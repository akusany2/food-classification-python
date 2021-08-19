FROM python:3.8

RUN pip install fastapi uvicorn wheel

EXPOSE 8000

COPY . /project

WORKDIR /project

RUN pip install -r requirements.txt

ENV PYTHONPATH /project

CMD ["uvicorn", "project.main:app", "--host", "0.0.0.0", "--port", "8000"]
