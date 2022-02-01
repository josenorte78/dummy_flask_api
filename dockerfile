FROM python

RUN yes | pip install flask

ENV STATIC_URL /static
ENV STATIC_PATH /var/www/app/static

COPY main.py /home/main.py

# EXPOSE 5000:5000

CMD [ "python", "./home/main.py" ]