from tetianakh/todoapp-base:latest
MAINTAINER Tetiana Khotiaintseva

COPY target /wheelhouse

RUN . /appenv/bin/activate && \
    pip install --no-index -f /wheelhouse todoapp && \
    rm -rf /wheelhouse
