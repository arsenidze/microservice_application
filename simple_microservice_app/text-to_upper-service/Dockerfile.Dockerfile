FROM python:3.7
WORKDIR /app
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY app ./
ENV PORT 5002
CMD ["python", "api.py"]