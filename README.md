# profiling-for-dummies

This is a small example that illustrates how to idenitfy latency caused by high CPU usage in a simple python service called a by a client and how to pinpoint the source of latency at the specific line of code.

First clone the repo and install the Splunk Otel Collector via the GDI Wizard.

Ensure python is installed and install the requirements.

```
sudo apt install python
export PATH
pip install -r requirements.txt
```

Prepare the instrumentation by following the steps in the GDI wizard for Python. When setting the environmental variables, be sure to [enable profiling](https://docs.splunk.com/observability/en/gdi/get-data-in/application/python/instrumentation/instrument-python-application.html#activate-alwayson-profiling). For the `client.py`

```
pip install "splunk-opentelemetry[all]"
splunk-py-trace-bootstrap
export SPLUNK_PROFILER_ENABLED=true
export OTEL_SERVICE_NAME='client'
export OTEL_EXPORTER_OTLP_ENDPOINT='http://localhost:4317'
export OTEL_RESOURCE_ATTRIBUTES='deployment.environment=nova,service.version=1'
splunk-py-trace python3 client.py
```

For `app.py` ,

```
pip install "splunk-opentelemetry[all]"
splunk-py-trace-bootstrap
export SPLUNK_PROFILER_ENABLED=true
export OTEL_SERVICE_NAME='server'
export OTEL_EXPORTER_OTLP_ENDPOINT='http://localhost:4317'
export OTEL_RESOURCE_ATTRIBUTES='deployment.environment=nova,service.version=1'
export OTEL_PROPAGATORS=b3multi
splunk-py-trace python3 -m flask run
```

See [here](https://docs.splunk.com/observability/en/gdi/get-data-in/application/python/troubleshooting/common-python-troubleshooting.html#check-that-your-pip-install-directory-is-in-path) if you get `command not found` when running `splunk-py-trace-bootstrap`.


Run each application with 
