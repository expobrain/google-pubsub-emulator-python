import asyncio

import click

from common import (  # type: ignore
    PUBSUB_EMULATOR_ENDPOINT_DEFAULT,
    get_publisher_client,
)


async def create_topic(project: str, endpoint: str, topic: str) -> None:
    # Create PubSub clients
    publisher_client = get_publisher_client(endpoint)

    # Create topic
    topic_path = publisher_client.topic_path(project, topic)

    topic_obj = await publisher_client.create_topic(request={"name": topic_path})

    print(f"Created topic {topic_obj.name}")


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
def main(project: str, endpoint: str, topic: str) -> None:
    asyncio.run(create_topic(project, endpoint, topic))


if __name__ == "__main__":
    main()
