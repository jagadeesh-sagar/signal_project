# Django Signals Proofs

This project contains automated tests to verify the behavior of Django signals.

## Running the Tests

To execute all signal verification tests (Synchronous, Thread, and Transaction tests) at once, run:

```bash
python manage.py test core.tests.SignalTests
```

## Test Breakdown

- **test_question_1**: Verifies that signals execute synchronously.
- **test_question_2**: Verifies that signals share the caller's thread.
- **test_question_3**: Verifies that signals share the caller's database transaction.

## Running Custom Class Tests

To verify the Rectangle class iteration logic using the custom management command, run:

```bash
python manage.py rectangle_cls
```
