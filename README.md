# Celery Example with Flask

This is a simple example of how to use Celery with Flask. The example is a
simple task that takes a string and returns it after a few seconds.

## Running the example

Run the application stack with docker-compose:

```bash
docker-compose up
```

The application will be available at `http://localhost:5000`.

After the application is running, you can test the task by calling the `run`
endpoint:

```bash
curl 0.0.0.0:5000/run
```
This will return the task id. For example:

```json
{
  "task_id": "e7a2b114-13e4-44fb-ae97-f014fe2bf720"
}
```

To check the status of the task, you can call the `get` endpoint with the task id.

```bash
curl 0.0.0.0:5000/get/e7a2b114-13e4-44fb-ae97-f014fe2bf720
```

This will return the status of the task. For example:

```json
{
  "task_id": "e7a2b114-13e4-44fb-ae97-f014fe2bf720"
  "status": "SUCCESS",
}
```
