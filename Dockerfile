FROM ubuntu:19.04

RUN apt update && apt-get install -y --no-install-recommends \
        clang-format python3 \
        && rm -rf /var/lib/apt/lists/*

ADD clang-format-wrapper.py /usr/bin

ENTRYPOINT ["clang-format-wrapper.py"]
