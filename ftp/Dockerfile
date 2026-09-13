FROM python:3.12-alpine

RUN pip install --no-cache-dir pyftpdlib

COPY entrypoint.py /entrypoint.py

EXPOSE 21 30000-30009

CMD ["python", "/entrypoint.py"]
