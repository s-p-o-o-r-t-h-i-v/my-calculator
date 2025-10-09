"""
Integration Tests - CLI + Calculator Working Together
"""

from click.testing import CliRunner
import pytest


class TestCLIIntegration:
    """Test CLI application integrating with calculator module"""

    def run_cli(self, *args):
        """Invoke Click CLI in-process"""
        from src.cli import calculate
        runner = CliRunner()
        return runner.invoke(calculate, list(args))

    # --- Positive tests for all operations ---
    @pytest.mark.parametrize("operation,num1,num2,expected", [
        ("add", "5", "3", "8"),
        ("subtract", "10", "4", "6"),
        ("multiply", "4", "7", "28"),
        ("divide", "15", "3", "5"),
        ("power", "2", "3", "8"),
    ])
    def test_cli_operations(self, operation, num1, num2, expected):
        res = self.run_cli(operation, num1, num2)
        assert res.exit_code == 0
        assert res.output.strip() == expected

    # sqrt only needs num1
    @pytest.mark.parametrize("operation,num1,expected", [
        ("sqrt", "16", "4"),
        ("square_root", "25", "5")
    ])
    def test_cli_sqrt(self, operation, num1, expected):
        res = self.run_cli(operation, num1)
        assert res.exit_code == 0
        assert res.output.strip() == expected

    # --- Error handling tests ---
    def test_cli_divide_by_zero(self):
        res = self.run_cli("divide", "10", "0")
        assert res.exit_code == 1
        assert "Cannot divide by zero" in res.output

    def test_cli_missing_num2(self):
        """Operations that require num2 should fail if missing"""
        for op in ["add", "subtract", "multiply", "divide", "power"]:
            res = self.run_cli(op, "5")
            assert res.exit_code != 0
            assert "Error" in res.output
            assert f"Operation '{op}' requires a second number." in res.output

    def test_cli_invalid_operation(self):
        res = self.run_cli("invalid", "1", "2")
        assert res.exit_code == 1
        assert "Unknown operation" in res.output


class TestCalculatorModuleIntegration:
    """Test calculator module functions work together"""

    def test_chained_operations(self):
        from src.calculator import add, multiply, divide
        # (5 + 3) * 2 / 4 = 4
        step1 = add(5, 3)
        step2 = multiply(step1, 2)
        step3 = divide(step2, 4)
        assert step3 == 4.0

    def test_complex_calculation(self):
        from src.calculator import add, power, square_root
        # sqrt(3^2 + 4^2) = 5
        hypotenuse = square_root(add(power(3, 2), power(4, 2)))
        assert hypotenuse == 5.0
