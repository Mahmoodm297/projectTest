#!/bin/bash
echo "FROM postgres
ENV POSTGRES_HOST=${POSTGRES_HOST}
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_DB=${POSTGRES_DB}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
EXPOSE 5432" > Dockerfile

