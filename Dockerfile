FROM google/cloud-sdk:332.0.0

RUN apt-get update \
    && apt-get install -y google-cloud-sdk-pubsub-emulator
