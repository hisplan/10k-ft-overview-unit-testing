# 10,000-ft Overview of Unit Testing

## Setup

```
conda create -n unittest python pip
conda activate unittest
```

## Topics

- Philosophy
  - TDD
  - "I unit test my unit tests"
- unittest, nose, pytest
- assertion
- setUp and tearDown
- skip
- CI/CD
  - GitHub Actions
  - CircleCI

## Running Tests

Run all:

```
pytest -q
```

Run a specific file, specific class, specific test:

```
pytest -q test_multiple.py::TestMultiple::test_should_increment_by_1
```
