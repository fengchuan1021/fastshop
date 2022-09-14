FROM python:3.10
#FROM python:3.10-slim
ARG BRANCH_NAME='dev'
WORKDIR /app
ENV DEBIAN_FRONTEND noninteractive
ENV MODE ${BRANCH_NAME}
COPY requirements/requirements_${BRANCH_NAME}.txt /etc/requirements_${BRANCH_NAME}.txt
RUN /bin/cp /usr/share/zoneinfo/Europe/London /etc/localtime && echo 'Europe/London' >/etc/timezone
RUN pip3 install -r /etc/requirements_${BRANCH_NAME}.txt
COPY . /app
RUN python3 cli.py initall
EXPOSE 80
CMD sh ./dockerstart.sh