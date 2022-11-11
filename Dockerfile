FROM python:3.10-slim
#FROM python:3.10
ARG BRANCH_NAME='DEV'
RUN if test "$BRANCH_NAME" = "DEV" ; then BRANCH_NAME="STAGE" ; else BRANCH_NAME="MAIN" ; fi
RUN echo $BRANCH_NAME
ARG USE_TUNA
WORKDIR /app
ENV DEBIAN_FRONTEND noninteractive
ENV MODE ${BRANCH_NAME}
COPY requirements/requirements_${BRANCH_NAME}.txt /etc/requirements_${BRANCH_NAME}.txt
RUN /bin/cp /usr/share/zoneinfo/Europe/London /etc/localtime && echo 'Europe/London' >/etc/timezone
RUN pip3 install -r /etc/requirements_${BRANCH_NAME}.txt
RUN if [[ -z "$USE_TUNA" ]] ; then pip3 install -r /etc/requirements_${BRANCH_NAME}.txt ; else pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple -r /etc/requirements_${BRANCH_NAME}.txt ; fi
COPY . /app
RUN python3 manage.py initall
EXPOSE 8000
CMD sh ./dockerstart.sh