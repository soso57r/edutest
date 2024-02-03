# Edutest

This projet is a test project for Eductive REIMS DevOps' lessons.

It consists in a simple API.

## Endpoints

### Root endpoint

GET - `/`

Simply returns `ok`.

### Increase endpoint

POST - `/inc`

Increase the internal counter of the application by one. It returns a JSON response formatted as followed:

```json
{
    "msg": "<any information>",
    "prev": <an integer of the previous value of the counter>,
    "new": <an integer with the new value of the counter>
}
```

### Info endpoint

GET - `/info`

Return a JSON response with the current status of the app:

```json
{
    "counter": <an integer of the current value of the counter>,
}
```

## Tests

To test, create an environment and load it, then:

```bash
pip install -r requirements.txt
pip install -e .
pytest # to run tests
pylint src && flake8 # to lint
bandit -r src # to run security tests
```

## Maintainers

- Emmanuel PLUOT
