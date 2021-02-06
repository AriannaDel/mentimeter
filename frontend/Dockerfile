FROM python:3
ADD front.py /
RUN pip install flask
RUN pip install requests
RUN pip install numpy scipy pandas matplotlib
EXPOSE 5000
CMD [ "python", "./front.py" ]

