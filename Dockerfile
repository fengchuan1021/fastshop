FROM python:3.10
WORKDIR /app
RUN  apt-get clean
RUN apt-get update
ENV DEBIAN_FRONTEND noninteractive
ARG BRANCH_NAME='dev'
ENV MODE ${BRANCH_NAME}
RUN /bin/cp /usr/share/zoneinfo/Europe/London /etc/localtime && echo 'Europe/London' >/etc/timezone
COPY environment/requirements_${BRANCH_NAME}.txt /etc/requirements_${BRANCH_NAME}.txt
RUN pip3 install -r /etc/requirements_${BRANCH_NAME}.txt
COPY . /app
RUN python cli.py initall
EXPOSE 8000
CMD sh ./dockerstart.sh