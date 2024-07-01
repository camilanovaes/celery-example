from flask import Flask

from celery_app import celery_init_app
from celery.result import AsyncResult
from tasks import hello_world


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        CELERY=dict(
            broker_url="amqp://rabbitmq",
            result_backend="rpc://",
        ),
    )
    celery_init_app(app)
    app.add_url_rule(
        "/",
        "default_endpoint",
        lambda: "Hello World, new version 1",
        methods=["GET"],
    )
    app.add_url_rule(
        "/run",
        "run_task",
        run_task,
        methods=["GET"],
    )
    app.add_url_rule(
        "/get/<id>",
        "get_task_status",
        get_task_status,
        methods=["GET"],
    )
    return app


def run_task():
    task = hello_world.delay("hello")
    return {"task_id": task.id}


def get_task_status(id: str):
    task = AsyncResult(id)
    return {
        "task_id": task.id,
        "task_status": task.status,
        "task_result": task.result,
    }


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
