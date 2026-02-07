# Guidelines

## Project structure

- This is a Streamlit application
- The entrypoint is `main.py`
- All source code is located in `src`
- All tests are located in `tests`
- This is a CMS like application, most of the content is stored in markdown files in `content` folder
- This is an `uv` project, use it to manage dependcies and run the application
- Use modern python syntax (>=3.13)

## Coding conventions

- Methods or functions or attributes should be either public or private (prefixed with `_`),
- Outside a class or a file, don't use other files or classes prvate objects
- declare an object public only if it's required
- Don't mix UI code and business logic code
- Business logic code should be located in `src/business` folder and use OOP and design patterns when relevant

## Tests

- Use `pytest`
- for mocks, use `pytest-mock` and fixtures
- Tests are contained in classes named `Test<NameOfTheClass>`
- Inside each class, each under-test methods are located in sub classes, e.g. `Test<NameOfTheMethod>`

Example:
```python
import pytest

class TestMyClass:
    @pytest.fixture
    def instance(self) -> MyClass:
        return MyClass()
    
    @pytest.fixture(autouse=True)
    def mock_something_class_level(self, mocker):
        mocker.patch("some_module.some_function")
    
    class TestMyMethod:
        @pytest.fixture(autouse=True)
        def mock_something_method_level(self, mocker):
            mocker.patch("some_module.some_other_function")
        
        def test_something(self, instance: MyClass):
            # Given
            ... # prepare data here
            
            # When
            res = instance.my_method()
            
            # Then
            assert res == "expected_result"
```

- inside the `tests` folder, the folder structure must be the same as in `src` folder
- Test only "public" methods,
- don't forget to add tests for edge and error cases