---
bookCollapseSection: false
---

# API Guide

This is a guide letting you know the functions available via the API. You can perform Create, Delete, and View Operations on Notes using the API.

{{< hint info >}}
**Note:** If deploying from instructions, the `APPLICATION_PATH` is `notes`.
{{< /hint >}}

## Create a Note

```bash
$ curl -X POST http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/add -d '{"message": "ZAP"}'

{
  "Success": "Note added!"
}

$ curl -X POST http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/add -d '{"message": "YEET"}'

{
  "Success": "Note added!"
}
```

## View all Notes

```bash
$ curl -X GET http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/get

[(1, 'ZAP'), (2, 'YEET')]
```

## View select Note

```bash
$ curl -X GET http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/get\?id\=1

[(1, 'ZAP')]
```

## Delete select Note

```bash
$ curl -X DELETE http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/delete\?id\=1

Note deleted successfully!

$ curl -X GET http://{LOAD_BALANCER_IP}/{APPLICATION_PATH}/get

[(2, 'YEET')]
```
