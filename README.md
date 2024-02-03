# Edutest

This projet is a test project for Eductive REIMS DevOps' lessons.

It consists in a simple API.

## Tests

To test, create an environment and load it, then:

```bash
pip install -r requirements.txt
pip install -e .
pytest # to run tests
pylint && flake8 # to lint
bandit -r src # to run security tests
```

## Maintainers

- Emmanuel PLUOT
