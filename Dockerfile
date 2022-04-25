FROM ubuntu:latest

RUN apt update && apt-get install -y --no-install-recommends \
        clang-format python3 \
        git \
        && rm -rf /var/lib/apt/lists/*

ADD clang-format-wrapper.py /usr/bin

RUN chmod 777 -R /usr/bin/clang-format-wrapper.py
