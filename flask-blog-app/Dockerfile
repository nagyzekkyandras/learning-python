FROM python

RUN mkdir /app

COPY ./ /app

WORKDIR /app

RUN pip3 install -r requirements.txt 

ENTRYPOINT [ "python3", "app.py" ]