import asyncio

import click

from common import (
    PUBSUB_EMULATOR_ENDPOINT_DEFAULT,
    get_publisher_client,
    get_subscriber_client,
)


async def create_subscription(
    project: str, endpoint: str, topic: str, subscription: str
) -> None:
    # Create PubSub clients
    publisher_client = get_publisher_client(endpoint)
    subscriber_client = get_subscriber_client(endpoint)

    # Create subscriptions
    topic_path = publisher_client.topic_path(project, topic)
    subscription_path = subscriber_client.subscription_path(project, subscription)

    subscription_obj = await subscriber_client.create_subscription(
        request={"name": subscription_path, "topic": topic_path}
    )

    print(f"Created subscription {subscription_obj.name}")


@click.command()
@click.option(
    "--project", default="my-test-project", help="Project where PubSub is running"
)
@click.option(
    "--endpoint",
    default=PUBSUB_EMULATOR_ENDPOINT_DEFAULT,
    help="Host and port of the running Google PubSub Emulator",
)
@click.argument("topic")
@click.argument("subscription")
def main(project: str, endpoint: str, topic: str, subscription: str) -> None:
    asyncio.run(create_subscription(project, endpoint, topic, subscription))


if __name__ == "__main__":
    main()
