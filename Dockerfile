FROM python:3.8-slim
WORKDIR /dalle2-in-python
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "src/main.py"]
