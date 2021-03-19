import click

from common import (  # type: ignore
    PUBSUB_EMULATOR_ENDPOINT_DEFAULT,
    get_publisher_client,
    get_subscriber_client,
)


@click.command()
@click.option(
    "--project",
    default="bulb-smart-energy-local",
    help="Project where PubSub is running",
)
@click.option(
    "--endpoint",
    default=PUBSUB_EMULATOR_ENDPOINT_DEFAULT,
    help="Host and port of the running Google PubSub Emulator",
)
@click.argument("topic")
@click.argument("subscription")
def main(project: str, endpoint: str, topic: str, subscription: str):
    # Create PubSub clients
    publisher_client = get_publisher_client(endpoint)
    subscriber_client = get_subscriber_client(endpoint)

    # Create subscriptions
    topic_path = publisher_client.topic_path(project, topic)
    subscription_path = subscriber_client.subscription_path(project, subscription)

    subscription_obj = subscriber_client.create_subscription(
        request={"name": subscription_path, "topic": topic_path}
    )

    print(f"Created subscription {subscription_obj.name}")


if __name__ == "__main__":
    main()
