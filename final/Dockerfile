FROM python:3.8 

LABEL Author="Evgen Vlasov"
LABEL E-mail = "evgeny_vlasov@yahoo.com"
LABEL version ="1.0 unstable"




# Копируем Pipfile и Pipfile.lock в контейнер для переноса зависимостей
COPY Pipfile ./
COPY Pipfile.lock ./

# Теперь запускаем установку всех зависимостей
RUN pip install --upgrade pip
# Первое. Дозагружаем pipenv
RUN pip install pipenv 
RUN pipenv install --dev --system --deploy 

# Переносим всю код-базу
ADD . /

# Делаем доступным порт из контейнера
EXPOSE 8000

# Финальная команда - как запускать приложение в контейнере
CMD [ "python" , "./src/app.py" ]