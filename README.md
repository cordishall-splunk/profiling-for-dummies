# profiling-for-dummies

This is a small example that illustrates how to idenitfy latency caused by high CPU usage in a simple python service called a by a client and how to pinpoint the source of latency at the specific line of code.

First clone the repo and install the Splunk Otel Collector via the GDI Wizard.

Ensure python is installed and install the requirements.

```
sudo apt install python
export PATH
pip install -r requirements.txt
```

Prepare the instrumentation by following the steps in the GDI wizard for Python. When setting the environmental variables, be sure to [enable profiling](https://docs.splunk.com/observability/en/gdi/get-data-in/application/python/instrumentation/instrument-python-application.html#activate-alwayson-profiling) with,

```
export SPLUNK_PROFILER_ENABLED=true
```

Run each application with 
