"""
Integration Tests - CLI + Calculator Working Together
"""

from click.testing import CliRunner
import pytest


class TestCLIIntegration:
    """Test CLI application integrating with calculator module (in-process)"""

    def run_cli(self, *args):
        """Invoke Click CLI in-process so coverage is measured."""
        from src.cli import calculate
        runner = CliRunner()
        return runner.invoke(calculate, list(args))

    # --- Positive tests for all operations ---
    @pytest.mark.parametrize("operation, num1, num2, expected", [
        ("add", "5", "3", "8"),
        ("subtract", "10", "4", "6"),
        ("multiply", "4", "7", "28"),
        ("divide", "15", "3", "5"),
        ("power", "2", "3", "8"),
    ])
    def test_cli_operations_integration(self, operation, num1, num2, expected):
        res = self.run_cli(operation, num1, num2)
        assert res.exit_code == 0
        assert res.output.strip() == expected

    def test_cli_sqrt_integration(self):
        res = self.run_cli("sqrt", "16")
        assert res.exit_code == 0
        assert res.output.strip() == "4"

    # --- Error handling tests ---
    def test_cli_divide_by_zero(self):
        res = self.run_cli("divide", "10", "0")
        assert res.exit_code == 1
        assert "Cannot divide by zero" in res.output

    def test_cli_missing_num2(self):
        """Operations that require num2 should fail if missing"""
        res = self.run_cli("add", "5")
        assert res.exit_code != 0
        assert "Error" in res.output

    def test_cli_invalid_operation(self):
        res = self.run_cli("invalid", "1", "2")
        assert res.exit_code == 1
        assert "Unknown operation" in res.output


class TestCalculatorModuleIntegration:
    """Test calculator module functions work together"""

    def test_chained_operations(self):
        """Test using results from one operation in another"""
        from src.calculator import add, multiply, divide
        step1 = add(5, 3)        # 8
        step2 = multiply(step1, 2)  # 16
        step3 = divide(step2, 4)    # 4
        assert step3 == 4.0

    def test_complex_calculation_integration(self):
        """Test complex calculation using multiple functions"""
        from src.calculator import power, square_root, add
        a_squared = power(3, 2)        # 9
        b_squared = power(4, 2)        # 16
        sum_squares = add(a_squared, b_squared)  # 25
        hypotenuse = square_root(sum_squares)    # 5
        assert hypotenuse == 5.0
