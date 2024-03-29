import grpc
from google.api_core.client_options import ClientOptions
from google.auth.credentials import AnonymousCredentials
from google.pubsub_v1.services.publisher.client import PublisherClient
from google.pubsub_v1.services.publisher.transports.grpc import PublisherGrpcTransport
from google.pubsub_v1.services.subscriber.client import SubscriberClient
from google.pubsub_v1.services.subscriber.transports import SubscriberGrpcTransport

PUBSUB_EMULATOR_ENDPOINT_DEFAULT = "localhost:8085"


def get_publisher_client(endpoint: str) -> PublisherClient:
    grpc_channel = grpc.insecure_channel(endpoint)
    transport = PublisherGrpcTransport(
        channel=grpc_channel, credentials=AnonymousCredentials()
    )
    client_options = ClientOptions(api_endpoint=endpoint)
    publisher = PublisherClient(transport=transport, client_options=client_options)

    return publisher


def get_subscriber_client(endpoint: str) -> SubscriberClient:
    grpc_channel = grpc.insecure_channel(endpoint)
    transport = SubscriberGrpcTransport(
        channel=grpc_channel, credentials=AnonymousCredentials()
    )
    client_options = ClientOptions(api_endpoint=endpoint)
    subscriber = SubscriberClient(transport=transport, client_options=client_options)

    return subscriber
