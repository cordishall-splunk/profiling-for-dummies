#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
from flask import Flask
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import (
    BatchSpanProcessor,
    ConsoleSpanExporter,
)

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)

"""
Sample Python app to illustrate profiling.
"""

app=Flask(__name__)

@app.route('/high/<n>')
def fibonacci(n):
    return str(fibonacci_helper(int(n)))

@app.route('/low')
def low_cpu_function():
    # This function just returns a constant value
    # print("Low CPU function executed")
    return "Low CPU function executed"

@app.route('/medium')
def medium_cpu_function():
    # This function calculates the sum of squares of the first n natural numbers
    result = random.randint(random.randint(1,4),50)
    # print(result)
    return str(result)

# Define the first route
@app.route('/')
def hello():
    return "hi!"

def fibonacci_helper(n):
    if n <= 1:
        return n
    else:
        result=fibonacci(n-1) + fibonacci(n-2)
        return result

#Run Flask
if __name__ == "__main__":
    app.run(debug=True)





