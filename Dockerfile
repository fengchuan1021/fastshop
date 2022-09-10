FROM python:3.10 as build-image
ARG BRANCH_NAME='dev'
RUN python -m venv /venv
ENV VIRTUAL_ENV=/venv
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"
WORKDIR /app
COPY environment/requirements_${BRANCH_NAME}.txt /etc/requirements_${BRANCH_NAME}.txt
RUN /bin/cp /usr/share/zoneinfo/Europe/London /etc/localtime && echo 'Europe/London' >/etc/timezone
RUN pip3 install -r /etc/requirements_${BRANCH_NAME}.txt

FROM ubuntu:20.04 as final-image
ARG BRANCH_NAME='dev'
ENV VIRTUAL_ENV=/venv
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"
WORKDIR /app
COPY --from=build-image /venv /venv
ENV DEBIAN_FRONTEND noninteractive
ENV MODE ${BRANCH_NAME}

COPY . /app
RUN python cli.py initall
EXPOSE 8000
CMD sh ./dockerstart.sh