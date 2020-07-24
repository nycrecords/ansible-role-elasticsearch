# Ansible Role: Elasticsearch

[![Build Status](https://travis-ci.org/nycrecords/ansible-role-elasticsearch.svg?branch=master)](https://travis-ci.org/nycrecords/ansible-role-elasticsearch)

An Ansible Role that installs Elasticsearch on RedHat/CentOS or Debian/Ubuntu.

## Requirements

Requires at least Java 8. See [`nycrecords.java`](https://github.com/nycrecords/ansible-role-java#example-playbook-install-openjdk-8) role instructions for installing OpenJDK 8.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    elasticsearch_version: '7.x'

The major version to use when installing Elasticsearch.

    elasticsearch_package_state: present

The `elasticsearch` package state; set to `latest` to upgrade or change versions.

    elasticsearch_service_state: started
    elasticsearch_service_enabled: true

Controls the Elasticsearch service options.

    elasticsearch_network_host: localhost

Network host to listen for incoming connections on. By default we only listen on the localhost interface. Change this to the IP address to listen on a specific interface, or `0.0.0.0` to listen on all interfaces.

    elasticsearch_http_port: 9200

The port to listen for HTTP connections on.

    elasticsearch_heap_size_min: 1g

The minimum jvm heap size.

    elasticsearch_heap_size_max: 2g

The maximum jvm heap size.

    elasticsearch_extra_options: ''

A placeholder for arbitrary configuration options not exposed by the role. This will be appended as-is to the end of the `elasticsearch.yml` file, as long as your variable preserves formatting with a `|`. For example:

```yaml
elasticsearch_extra_options: |  # Dont forget the pipe!
  some.option: true
  another.option: false
```

## Setting up SSL

If you want to setup SSL you will need to generate your certificates using your own CA ahead of time. This role includes a dummy CA that should not be used in Production.

If you would like to bootstrap some additional test instances using Vagrant and Molecule you can use the CA key and Certificate to generate additional server certs. 

To generate server certificates:

```shell
openssl req -new -newkey rsa:2048 -nodes -out <INSTANCE_NAME>.csr -keyout molecule/resources/<INSTANCE_NAME>/<INSTANCE_NAME>.key -subj "/CN=<INSTANCE_NAME>"
openssl x509 -req -in <INSTANCE_NAME>.csr -CA molecule/resources/ca/ca.crt -CAkey molecule/resources/ca/ca.key -CAcreateserial -out molecule/resources/<INSTANCE_NAME>/<INSTANCE_NAME>.crt -days 365 -sha256
```

To add hosts to Molecule:

1) Edit the `vagrant-cluster` scenario in the molecule folder to add additional Vagrant hosts. You can copy the configuration for `instance-1`.
2) In Provisioner -> Inventory -> Host Vars add a new entry for the vagrant host(s) you added to the Platform configuration and make sure to update the certificate and key filename to match the instance name.

## Dependencies

  - nycrecords.java

## Example Playbook

    - hosts: search
      roles:
        - nycrecords.java
        - nycrecords.elasticsearch

## License

MIT / BSD

## Author Information

This role was created in 2014 by [Jeff Geerling](https://www.jeffgeerling.com/), author of [Ansible for DevOps](https://www.ansiblefordevops.com/).
