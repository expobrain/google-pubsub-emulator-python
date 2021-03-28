import grpc
from google.auth.credentials import AnonymousCredentials
from google.pubsub_v1.services.publisher.async_client import PublisherAsyncClient
from google.pubsub_v1.services.publisher.transports.grpc import PublisherGrpcTransport
from google.pubsub_v1.services.subscriber.async_client import SubscriberAsyncClient
from google.pubsub_v1.services.subscriber.transports import SubscriberGrpcTransport

PUBSUB_EMULATOR_ENDPOINT_DEFAULT = "localhost:8085"


def get_publisher_client(endpoint: str) -> PublisherAsyncClient:
    grpc_channel = grpc.insecure_channel(endpoint)
    transport = PublisherGrpcTransport(
        channel=grpc_channel, credentials=AnonymousCredentials()
    )
    publisher = PublisherAsyncClient(
        transport=transport,
        client_options={"api_endpoint": endpoint},
    )

    return publisher


def get_subscriber_client(endpoint: str) -> SubscriberAsyncClient:
    grpc_channel = grpc.insecure_channel(endpoint)
    transport = SubscriberGrpcTransport(
        channel=grpc_channel, credentials=AnonymousCredentials()
    )
    subscriber = SubscriberAsyncClient(
        transport=transport,
        client_options={"api_endpoint": endpoint},
    )

    return subscriber
