# -*- coding: utf-8 -*-

from chalice import Chalice
from test_with_localstack-project.lbd import hello

app = Chalice(app_name="test_with_localstack-project")


@app.lambda_function(name="hello")
def handler_hello(event, context):
    return hello.high_level_api(event, context)
