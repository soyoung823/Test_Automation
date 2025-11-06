from abc import ABC, abtractmethod
import pytest

# --- Base Abstract Test Class ---
class BaseTest(ABC):
    def setup_method(self):
        print("Setting up test environment")

    def teardown_method(self):
        print("Tearing down test environment")

    @abstractmethod
    def run_test(self):
        pass

# --- Reusable page or Service object ---
class LoginPage:
    def __init__(self, driver):
        sefl.driver = driver

    def login(self, username, password):
        print(f"Logging in with {username}")
        return username == "admin" and password == "1234"

# --- Concrete Test Case using inheritance ---
class TestLogin(BaseTest):
    def __init__(self):
        self.page = LoginPage(driver=None)

    def run_test(self):
        assert self.page.login("admin", "1234"), "Login failed!"

# --- Test Suite Execution ---
@pytest.mark.usefixtures("TestLogin")
def test_login_suite():
    test = TestLogin()
    test.setup_method()
    test.run_test()
    test.teardown_method()

"""
BaseTest - abstract lifecycle hooks.
each test implements its own run_test() logic
common functionality (LoginPage) is encapsulated in reusable objects.

OOP techniques for Test suites
factory pattern: create test data or drivers dynamically for diff environments
Strategy pattern: plug in diff validation or execution strategies
Observer pattern: notify loggers, reporters when tests start end
Decorator pattern: add cross cutting converns like retry, timing, screenshots
"""
# Strategy pattern for validation
class ValidationStrategy(ABC):
    @abstractmethod
    def validate(self, result): pass

class JSONValidation(ValidationStrategy):
    def validate(self, result):
        assert "status" in result

class XMLValidation(ValidationStrategy):
    def validate(self, result):
         assert "<status>" in result

class APITest(BaseTest):
    def __init__(self, validator: ValidationStrategy):
        self.validator = validator

    def run_test(self):
        response = {"status": "OK"}
        self.validator.validate(response)

"""
Intgration and Automation
CI/CD: integrate with Jenkins, github
Reporting: Generate reports via Allure or HTMLTestRunner
Data-driven testing: excel, CSV, JSON
Mocking: use unittest.mock, pytest-mock
Parallel execution: integrate with pytest-sdist or threading
"""
"""
Use base classes for shared test set up
Keep tests independent, avoid shared state
use composition over inheritance when possible (inject helper objects)
make test data configurable (not hard coded)
apply solid principles to testing classes
separate test logic from framework code
automate test discovery and reporting
"""
