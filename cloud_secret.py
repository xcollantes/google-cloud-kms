"""Using Google Cloud Secret Manager."""

from absl import flags
from absl import app
from google.cloud import secretmanager

FLAGS = flags.FLAGS

flags.DEFINE_string("project_id", None, "Google Cloud Project ID.")
flags.DEFINE_string("secret_id", None, "Google Secrets Manager ID.")

def main(argv) -> None:
    client = secretmanager.SecretManagerServiceClient()

def addSecretVersion(client: secretmanager.SecretManagerServiceClient,
                     secretId: str) -> None:
    version = client.add_secret_version(
        request={
            "parent": secretId,
            "payload": {
                "data": b"This is some random data."
            }
        }
    )
    print(version)

def accessSecret(client: secretmanager.SecretManagerServiceClient,
                 version: str) -> None:
    response = client.access_secret_version(
        request={ "name": version })

    print("Secret: ", response)

def createSecret(client: secretmanager.SecretManagerServiceClient) -> None:
    parent = f"projects/{FLAGS.project_id}"
    secret = client.create_secret(
        request={
            "parent": parent,
            "secret_id": FLAGS.secret_id,
            "secret": {
                "replication": { "automatic": {} }
            }
        }
    )
    print(secret)


if __name__ == "__main__":
    app.run(main)
