FROM python:3.10-slim
#FROM python:3.10
ARG MODE='DEV'
ARG USE_TUNA
WORKDIR /app
RUN echo $MODE
ENV DEBIAN_FRONTEND noninteractive
ENV MODE ${MODE}
COPY requirements/requirements_${MODE}.txt /etc/requirements_${MODE}.txt
RUN /bin/cp /usr/share/zoneinfo/Europe/London /etc/localtime && echo 'Europe/London' >/etc/timezone
RUN pip3 install -r /etc/requirements_${MODE}.txt
RUN if test -z "$USE_TUNA" ; then pip3 install -r /etc/requirements_${MODE}.txt ; else pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /etc/requirements_${MODE}.txt ; fi
COPY . /app
RUN python3 manage.py initall
EXPOSE 8000
CMD sh ./dockerstart.sh