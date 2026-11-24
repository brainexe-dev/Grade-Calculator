FROM python:3.12
WORKDIR /app
COPY Grade_Calculator.py .
CMD ["python","Grade_Calculator.py"]
