Note Type: #litnote
Source: [[📖 Django for Professionals]] ch1 p7

---
# What is Docker?
Docker is a service that allows you to implement Linux containers. So what are containers?

Containers are a way of compartmentalising a single machine into multiple *virtual machines*, from the operating system layer up. When you use a cloud computing service such as AWS, the provider doesn't typically allot a separate, dedicated piece of hardware (a computer) to each user. Instead, you share a single physical server with other clients, each given access to a virtual machine running on that server. For example, you might have one physical server running 5 VMs, each containing their own installation of Linux, for 5 separate clients. This makes it appear to the client as if they have their own physical server.

The problem with the above method of creating VMs is speed and size. An operating system takes up a lot of disk space, which needs to be multiplied by the number of installations (number of VMs running on the server, one for each client) required. Also, each VM needs its own CPU and memory resources to be able to run. It becomes very cumbersome.

This is the problem that Docker addresses. Docker creates *containers* which run on a shared Linux kernel — that is, it creates independent user spaces which share a common base operating system. It virtualises from the operating system layer up. The idea is that most servers rely on the same Linux operating system, so why install multiple instances of the same OS on one server? Instead we can install one OS on each server and add isolation mechanisms to create independent containers for separate clients, as well as add resource-management features (CPU and memory management) to limit the impact of one container's activities on other containers hosted on the same kernel.

---
### See also:
- [OS-level virtualization, Wikipedia](https://en.wikipedia.org/wiki/OS-level_virtualization)