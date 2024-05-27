FROM openjdk:slim
COPY --from=python:3.6 / /

RUN sed -i '/jessie-updates/d' /etc/apt/sources.list  # Now archived

RUN apt-get update
RUN apt-get -y install locales
RUN sed -i -e \
  's/# ru_RU.UTF-8 UTF-8/ru_RU.UTF-8 UTF-8/' /etc/locale.gen \
   && locale-gen

COPY requirements.txt ./
RUN pip3 install -r requirements.txt
RUN pip3 install uvicorn[standard]

COPY ./app /api-student/app

WORKDIR /api-student

CMD ["uvicorn", "app.main:application", "--host", "0.0.0.0", "--port", "5050"]