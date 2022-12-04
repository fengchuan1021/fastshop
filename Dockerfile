FROM python:3.10-slim
#FROM python:3.10
ARG MODE='DEV'
ARG USE_TUNA
WORKDIR /app
ENV DEBIAN_FRONTEND noninteractive
ENV MODE ${MODE}
COPY requirements/requirements_${MODE}.txt /etc/requirements_${MODE}.txt
RUN rm /etc/localtime && /bin/cp /usr/share/zoneinfo/UTC /etc/localtime && echo 'UTC' >/etc/timezone
RUN if test -z "$USE_TUNA" ; then pip3 install -r /etc/requirements_${MODE}.txt ; else pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /etc/requirements_${MODE}.txt ; fi
COPY . /app
RUN python3 manage.py initall
EXPOSE 8000
CMD sh ./dockerstart.sh