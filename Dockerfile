FROM python
COPY . /app
WORKDIR /app
EXPOSE 8080
RUN pip install -r requirements.txt
ENTRYPOINT ["python", "app.py"]
