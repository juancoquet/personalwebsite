Note Type: #litnote
Source: [[📖 Django for Professionals]] ch2 p33

---
# Always install new packages within Docker, not locally
Installing new software packages within docker and rebuilding the image will prevent `Pipfile.lock` conflicts.

The automatic generation of the `Pipfile.lock` file depends heavily on the OS being used. The entire OS that an app runs on can be specified within Docker, so it makes sense to install new packages there where the `lock` file will be created in compliance with the Docker OS, where the app will always run.

If you install packages to your local computer, which has a different OS to your Docker host, the resulting `Pipfile.lock` will also be different. This can cause problems when the `volumes` mount automatically syncs local changes to your Docker filesystem and overwrites the Docker version with the newer local version — the Docker container will be trying to run an incorrect `Pipfile.lock` file.

After installing a new package, you'll always need to rebuild the image to force 
Docker to start a new build with the updated  `Pipfile` and `Pipfile.lock`.

---
### See also:
- [[Rebuild image after installing a package on Docker]]