---
bookCollapseSection: false
---

# API Guide

This is a guide letting you know the functions available via the API. You can perform Create, Delete, and View Operations on Notes using the API.

## Create a Note

```bash
$ curl -X POST http://{API_PATH} -d '{"message": "ZAP"}'

{
  "Success": "Note added!"
}

$ curl -X POST http://{API_PATH} -d '{"message": "YEET"}'

{
  "Success": "Note added!"
}
```

## View all Notes

```bash
$ curl -X GET http://{API_PATH}

[(1, 'ZAP'), (2, 'YEET')]
```

## View select Note

```bash
$ curl -X GET http://{API_PATH}\?id\=1

[(1, 'ZAP')]
```

## Delete select Note

```bash
$ curl -X DELETE http://{API_PATH}\?id\=1

Note deleted successfully!
```
