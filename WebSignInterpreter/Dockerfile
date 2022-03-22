FROM python:3.9.7

ADD ./ /api

WORKDIR /api

RUN pip install -r requirements.txt

#EXPOSE 3478
#CMD ["sh","-c","streamlit run main.py"]

CMD ["sh","-c","streamlit run --server.port $PORT main.py"]
