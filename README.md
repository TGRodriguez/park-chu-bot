# park-chu-bot
Simple discord bot implemented using discordpy

## Installing the project

This project was build with [poetry](https://python-poetry.org/docs/) to manage dependencies.

Having poetry installed, run this command to install the dependencies:

```
poetry install
```

If you don't want the virtual environment to be created in the project root folder, you can modify the parameters of the `poetry.toml` file (Remember to don't push the changes!).


## Dev

To add new dependencies, you can run:

```
poetry add <dependency>
```

**NOTE**: Don't forget to commit all changes to `poetry.lock` and `pyproject.toml`! 

To activate the virtual environment run:

```
poetry shell
```

Then, you can run the app using:

```
python src/main.py
```

Finally, you can exit the virtual environment:

```
exit
```

## Running locally

In addition to running it directly within poetry's virtual environment you can run the project with [Docker](https://www.docker.com/get-started/) :

* Create a `.env` file with the same environment variables as in `.example-env`

* Run `docker build -t park-chu-bot .`

* Run `docker run --env-file=.env park-chu-bot`


## Links

- Fly.io deploy dashboard:

    - https://fly.io/apps/park-chu-bot