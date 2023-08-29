FROM python:3.10

WORKDIR /Users/nnm2/Documents/
COPY . .
RUN python3 -m venv virtenv
RUN pip3 install feedparser

CMD ["python","parsing_ria.py"]