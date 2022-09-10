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

COPY --from=build-image /usr/local/bin/python /usr/local/bin/python
COPY --from=build-image /usr/local/lib/libpython3.10.so /usr/local/lib/libpython3.10.so
COPY --from=build-image /usr/local/lib/libpython3.10.so.1.0 /usr/local/lib/libpython3.10.so.1.0
COPY --from=build-image /usr/local/lib/libpython3.so /usr/local/lib/libpython3.so
COPY --from=build-image /usr/local/lib/python3.10 /usr/local/lib/python3.10
COPY --from=build-image /venv /venv
RUN echo "/usr/local/lib/" >> /etc/ld.so.conf
RUN ldconfig
ENV DEBIAN_FRONTEND noninteractive
ENV MODE ${BRANCH_NAME}

COPY . /app
RUN python3 cli.py initall
EXPOSE 8000
CMD sh ./dockerstart.sh