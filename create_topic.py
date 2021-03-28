import click

from common import (  # type: ignore
    PUBSUB_EMULATOR_ENDPOINT_DEFAULT,
    get_publisher_client,
)


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
def main(project: str, endpoint: str, topic: str) -> None:
    # Create PubSub clients
    publisher_client = get_publisher_client(endpoint)

    # Create topic
    topic_path = publisher_client.topic_path(project, topic)

    topic_obj = publisher_client.create_topic(request={"name": topic_path})

    print(f"Created topic {topic_obj.name}")


if __name__ == "__main__":
    main()
