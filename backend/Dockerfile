FROM python:3
ADD myapp.py /
RUN pip install flask
RUN pip install requests
EXPOSE 5000
CMD [ "python", "./myapp.py" ]

