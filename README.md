# devtoolsai_demo_selenium_python
Sample project showing how to use SmartDriver with Selenium python


# Setup

You need to first install the dependencies
```
python3 -m pip install -r requirements.txt
```

# Run the tests

There are two tests:
 - demo_find_by_ai.py that shows how to build a test case without locator by prompting the user for bounding boxes
 - demo_ingest.py that shows how an existing test case using xpaths or other locators can be ingested to become visual elements.

`

Find by AI test
```
export DEVTOOLSAI_INTERACTIVE=1 # enables interactive mode / prompting
python3 demo_find_by_ai.py
```

Ingest test
```
python3 demo_ingest.py
``
