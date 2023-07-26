# ALEPH VORTEX APP :

Python-based application designed to index and expose data from the Vortex DEX on Aleph.im protocol.

This application stores the indexed data in a Postgres database, and exposes it via a GraphQL server.

## Indexed contracts :

```md
# Contracts :
VORTEX DEX @ "KT1LzyPS8rN375tC31WPAVHaQ4HyBvTSLwBu"

# Tokens :
SMAK TOKEN @ "KT1TwzD6zV3WeJ39ukuqxcfK2fJCnhvrdN1X"
ANTI TOKEN @ "KT1MsktCnwfS1nGZmf8QbaTpZ8euVijWdmkC"

# Token Factories :
FACTORY FA12 @ "KT1PwnTa2f1Uac958RFTk6i6EecPNgJrtHKv"
FACTORY FA2 @ "KT1JW8AeCbvshGkyrsyu1cWa5Vt7GSpNKrUz"
FACTORY DOGA @ "KT1Ck9M83JrQuTkxFw6RLZz15BGDhQQhMbXd"

# Staking :
SMAK STAKING @ "KT1TR4qabnDU6aAUym6nauSGaRwJpoKU3efP"

# Farming :
Farms V1 @ "KT1QF1kK7WD8gMVrcE3P2FVFFQnKV2a4JwgU"
Farms V2 @ "KT1GDqyEpUk7zE227M66eLPR4evVa1vjjvQY"
``````

## Running the app via Docker-Compose :

If you wish to test the app locally via Docker, make sure your `.env` file is correctly setup.

Make sure the `PG_HOST` is set to the name of the correpsonding service in the `Docker-compose.yaml`` :

```bash
## POSTGRES
PG_HOST="postgres"
```

Then you can run the following command :

```bash
docker-compose up -d
```

## Running the app locally :

If you wish to test the app locally, make sure your `.env` file is correctly setup.

Then you can run the following commands :

```bash
sudo apt-get update
sudo apt-get install -y git g++ gcc pkg-config make cmake m4 libgmp-dev libsodium-dev libsecp256k1-dev
pip install --upgrade pip==23.1.2
pip install poetry==1.5.1
poetry install
poetry poetry run uvicorn main:app
```

___

## Aleph Deployment Requirements :

If you wish to deploy this app to Aleph.im, you will need the `aleph` command from [aleph-client](https://github.com/aleph-im/aleph-client)

## Aleph Virtual Machines

Programs on Aleph run within virtual machines: emulated computer systems with dedicated resources that run isolated from each other.

Aleph Virtual Machines (VMs) are based on Linux and use [Firecracker](https://firecracker-microvm.github.io/) under the hood.

Each program runs on its own dedicated Linux system, with the host providing additional functionalities related to Aleph.

## Aleph Runtime

The base of each VM is a Linux [root filesystem](https://en.wikipedia.org/wiki/Root_directory) named __runtime__ and configured to run programs on the Aleph platform.

The runtime currently supported by Aleph is [aleph-debian-11-python](https://github.com/aleph-im/aleph-vm/blob/main/runtimes/aleph-debian-11-python).

* Python programs must support the [ASGI interface](https://asgi.readthedocs.io/en/latest/), described in the example below.
* Binaries must listen for HTTP requests on port 8080

## Aleph Volumes

VMs can be extended by specifying additional volumes that will be mounted in the system :

- **Read-only volumes** are useful to separate Python virtual environments, Javascript `node_modules` or static data from the program itself. These volumes can be updated independently from the program and the runtime, and maintained by a third party.

- **Ephemeral volumes** provide temporary disk storage to a VM during its execution without requiring more memory.

- **Host persistent volumes** are persisted on the VM execution node, but may be garbage collected by the node without warning.

- **Store persistent volumes** (not available yet) are persisted on the Aleph network. New VMs will try to use the latest version of this volume, with no guarantee against conflicts.

## Uploading to Aleph 

After installing [aleph-client](https://github.com/aleph-im/aleph-client), you should have access to the `aleph` command:

```shell
aleph --help
```

Upload your program:

```shell
aleph program ./src main:app
```

Press `Enter` to skip adding extra volumes to your program:
```shell
Add volume ? [y/N]
```

You should then get a response similar to the following:
```
Your program has been uploaded on Aleph.

Available on:
- https://aleph.sh/vm/1d3842fc4257c0fd4f9c7d5c55bba16264de8d44f47265a14f8f6eb4d542dda2
- https://du4ef7cck7ap2t44pvoflo5bmjsn5dke6rzglikpr5xljvkc3wra.aleph.sh

Visualise on:
- https://explorer.aleph.im/address/ETH/0x101d8D16372dBf5f1614adaE95Ee5CCE61998Fc9/message/PROGRAM/1d3842fc4257c0fd4f9c7d5c55bba16264de8d44f47265a14f8f6eb4d542dda2
```

> ℹ️ You may get the warning `Message failed to publish on IPFS and/or P2P`. This is common and usually not an issue.

> ℹ️ The second URL uses a hostname dedicated to your VM. Aleph identifiers are too long to work for URL subdomains, so a base32 encoded version of the identifier is used instead.

> ℹ️ You can make your own domain point to the VM. See the [ADVANCED](https://github.com/aleph-im/aleph-vm/blob/main/tutorials/ADVANCED.md) section.

## Running on Aleph

You can now run your program by opening one of the URLs above. Each URL is unique for one program :

`https://aleph.sh/vm/1d3842fc4257c0fd4f9c7d5c55bba16264de8d44f47265a14f8f6eb4d542dda2`

## Uploading updates to Aleph
You could upload the new version as a new program, but this would break the URL above and you would have to give the updated URL to all your friends.

While Aleph messages cannot be edited, there is a solution to this issue: you can publish _amend_ messages that reference the original message to add some changes to it.

The `aleph update` command is similar to `aleph program`, except it requires the hash of the program to update.

```shell
aleph update $HASH ./src
```

> ℹ️ Note that _amend_ messages must be sent from the same Aleph address as the original program to work, else they will be ignored.

> ℹ️ Backup your private key, else you may lose the ability to update a program.