FROM python:3.7

WORKDIR /app

EXPOSE 8504

COPY . /app

RUN pip install streamlit


RUN pip install -U scikit-learn

RUN touch "out.csv"

ENTRYPOINT ["streamlit", "run"]

RUN pwd

CMD ["App.py"]