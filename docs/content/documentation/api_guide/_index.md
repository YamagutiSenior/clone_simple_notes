---
bookCollapseSection: false
---

# API Guide

This is a guide letting you know the functions available via the API. You can perform Create, Delete, and View Operations on Notes using the API.

{{< hint info >}}
**Note:** If deploying from instructions, the `APPLICATION_PATH` is `notes-staging`.
{{< /hint >}}

## Creating a Note

```bash
$ curl -X POST http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/api -d '{"message": "ZAP"}'

{
  "Success": "Note added!"
}

$ curl -X POST http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/api -d '{"message": "YEET"}'

{
  "Success": "Note added!"
}
```

## View all Notes

```bash
$ curl -X GET http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/api

[(1, 'ZAP'), (2, 'YEET')]
```

## View select Note

```bash
$ curl -X GET http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/api\?id\=1

[(1, 'ZAP')]
```

## Delete select Note

```bash
$ curl -X DELETE http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/api\?id\=1

Note deleted successfully!

$ curl -X GET http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/api

[(2, 'YEET')]
```

# Admin API Guide

The admin functions are exactly the same as regular functions, except that
secrets created by an admin can only be seen or deleted by an admin.

{{< hint info >}}
**Note:** The admin path is `/api/admin` and requires Basic Authentication.
{{< /hint >}}

## Creating a Note

```bash
$ curl -u admin:yeet -X POST http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/api/admin -d '{"message": "ZAP"}'

{
  "Success": "Note added!"
}

$ curl -u admin:yeet -X POST http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/api/admin -d '{"message": "YEET"}'

{
  "Success": "Note added!"
}
```

## View all Notes

```bash
$ curl -u admin:yeet -X GET http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/api/admin

[(1, 'ZAP','<IP-Address>', '<HostName>', 1), (2, 'YEET','<IP-Address>', '<HostName>', 1)]
```

## View select Note

```bash
$ curl -u admin:yeet -X GET http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/api/admin\?id\=1

[(1, 'ZAP', '<IP-Address>', '<HostName>', 1)]
```

## Delete select Note

```bash
$ curl -u admin:yeet -X DELETE http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/api/admin\?id\=1

Note deleted successfully!

$ curl -u admin:yeet -X GET http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/api/admin

[(2, 'YEET', '<IP-Address>', '<HostName>', 1)]
```