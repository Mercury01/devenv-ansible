
## Ansible for my development environment
### Prerequisite

* ansible 2.5.x or above

### Usage

```
$ ansible-playbook -i hosts playbook.yml -u <user_name> --private-key=<path_to_private_key>
```

## Development and testing

This project use [molecule](https://github.com/metacloud/molecule) for unit test. 

### Prerequisite

python 2.7.13 or above.
The following is example to install python 2.7.13 by [pytenv](https://github.com/pyenv/pyenv) and [pyenv virtualenv](https://github.com/pyenv/pyenv-virtualenv).

```
$ pyenv version 2.7.13
$ pyenv virtualenv ansible-py2
$ pyenv activate ansible-py2
```

Required packages and versions are as follows.

package   | version
----------|---------
ansible   | 2.5.0
molecule  | 2.12.1
docker-py | 1.10.6

```
$ pip install ansible molecule docker-py
```

### How to test

Each `role directory` has a `molecule` project. `<role_directory>` are `anyenv`, `bash-it`, `docker`, etc.

```
$ cd ./roles/<role_directory>
$ molecule test
```

However, not all roles have a molecule. Applying molecule little by little...

* [x] anyenv
* [ ] bash-it
* [ ] docker
* [ ] docker-compose
* [ ] initialize
* [ ] routing
* [ ] vim

#### Note

1. If already exists a ansible role, add a molecule project to `role directory`.

    ```
    $ cd roles/<role_directory>
    $ molecule init scenario -r <role_name> -s default
    --> Initializing new scenario default...
    Initialized scenario in /path/to//role/molecule/default successfully.
    $ tree molecule
    molecule
    └── default
        ├── Dockerfile.j2
        ├── INSTALL.rst
        ├── create.yml
        ├── destroy.yml
        ├── molecule.yml
        ├── playbook.yml
        ├── prepare.yml
        └── tests
            ├── test_default.py
            └── test_default.pyc

    2 directories, 9 files
    ```

1. Write a target platform to `molecule/default/molecule.yml`.

    ```yaml
    dependency:
      name: galaxy
      enabled: false # does not use galaxy
    ...
    platforms:
    - name: instance
        image: ubuntu:16.04
    ...
    ```

1. Test code write to `molecule/default/tests/test_default.py`. 
[testinfra](https://github.com/philpep/testinfra) is used for unit test of molecule.

    ```py
    def test_anyenv_installed(host):
        anyenv = host.file('/root/.anyenv/bin/anyenv')

        assert anyenv.exists
    ```

1. Do a test.

    ```
    $ molecule test
    ```

    `molecule test` execute all test. If an test time is long, then you better use `converge` and` destroy` command.

    * converge - Use the provisioner to configure instances...
    * destroy - Use the provisioner to destroy the instances.

    molecule also has various other commands, so if you select the commands according to the situation, you will be able to test efficiently.

1. Debug

    ```
    $ molecule --debug test
    ```

    If you do not run `molecule destroy`, the docker container will not be destroyed so you can login to the container and investigate the cause.

    ```
    $ molecule list
    Instance Name    Driver Name    Provisioner Name    Scenario Name    Created    Converged
    ---------------  -------------  ------------------  ---------------  ---------  -----------
    instance         Docker         Ansible             default          True       False
    ```

    run a bash in docker.

    ```
    $ docker exec -it instance bash
    ```

