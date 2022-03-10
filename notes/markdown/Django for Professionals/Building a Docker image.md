Note Type: #litnote
Source: [[📖 Django for Professionals]] ch1 p18

---
# Building a Docker image
To create a new Docker image, first create a new `Dockerfile`.
```bash
$ touch Dockerfile
```

Then open the `Dockerfile` and set up the instructions you wish to be ran upon instantiation of a new container using this image. Bear in mind that the `Dockerfile` will be read and executed top to bottom while writing your instructions.
```Dockerfile
# Pull base image
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

# Copy project files
COPY . /code/
```

The first command is always a `FROM` command — here we select a base image to use. A base image is like the fundamental layer of your container, the layer that everything else is built on top of. You might choose an Ubuntu base image, for example. Here we are selecting a Python base image. ==*presumably this is an image based on another OS image, but I'm not sure*==

We then establish two environment variables — the first will stop Python from trying to write `.pyc` files, and the second ensures that the console output is not buffered by Docker so that it looks familiar.

Next we establish a default work directory called `code` which is where we will store our code. This tells docker to assume we mean to run all commands from this directory so that we don't have to type a long path every time.

We use `COPY` and `RUN` to copy our `Pipfile` and `Pipfile.lock` files to our `code` directory, and then install dependencies contained within them. The `--system` flag is important, as Pipenv searches for a virtual environment to install dependencies to by default. Since we are creating a Docker container, it *is* our virtual environment, so we install to the system instead.

Finally we copy all remaining project files to the `code` directory.

To build an image using a `Dockerfile`, navigate to the directory where the image is contained and run `docker build .`.

---
### See also:
- [[What is a Docker image?]]