FROM python:3.8.1

COPY . .
WORKDIR .

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]

EXPOSE 5000