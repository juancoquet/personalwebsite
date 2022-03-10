Note Type: #litnote
Source: [[📖 Django for Professionals]] ch1 p16

---
# What is a Docker image?
A Docker image is a snapshot in time of what a project contains. It is represented by a `Dockerfile` which consists of a list of instructions for the image. These instructions can be things like establishing environment variables in the destination container, copying files, and running other shell commands.

A container is a running instance of an image, it is the real thing. The image is like a blueprint, whereas the container is the fully-built building itself.