import importlib.util
import unittest
from pathlib import Path

MODULE_PATH = Path(__file__).parents[1] / "scripts" / "finance_math.py"
SPEC = importlib.util.spec_from_file_location("finance_math", MODULE_PATH)
finance_math = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(finance_math)


class FinanceMathTests(unittest.TestCase):
    def test_complete_estimated_baseline(self):
        fact = lambda value, status="known": {"value": value, "status": status, "confidence": "medium"}
        result = finance_math.calculate({
            "assets": {"status": "estimated", "items": [{"amount": fact(40000, "estimated")}, {"amount": fact(3000)}]},
            "liabilities": {"status": "known", "items": []},
            "monthly_income": fact(8000, "estimated"),
            "monthly_spending": fact(5000, "estimated"),
        })
        self.assertEqual(result["total_assets"]["value"], 43000.0)
        self.assertEqual(result["net_worth"]["status"], "estimated")
        self.assertEqual(result["monthly_surplus"]["value"], 3000.0)
        self.assertEqual(result["savings_rate"]["value"], 0.375)

    def test_unknown_spending_stays_unknown(self):
        result = finance_math.calculate({
            "assets": {"status": "known", "items": []},
            "liabilities": {"status": "known", "items": []},
            "monthly_income": {"value": 8000, "status": "known", "confidence": "high"},
            "monthly_spending": {"value": None, "status": "unknown"},
        })
        self.assertIsNone(result["monthly_surplus"]["value"])
        self.assertEqual(result["savings_rate"]["status"], "unknown")

    def test_unknown_collection_is_not_zero(self):
        result = finance_math.calculate({
            "assets": {"status": "unknown", "items": []},
            "liabilities": {"status": "known", "items": []},
            "monthly_income": {"value": None, "status": "unknown"},
            "monthly_spending": {"value": None, "status": "unknown"},
        })
        self.assertIsNone(result["total_assets"]["value"])
        self.assertIsNone(result["net_worth"]["value"])

    def test_rejects_value_on_unknown(self):
        with self.assertRaises(ValueError):
            finance_math.normalize({"value": 0, "status": "unknown"}, "amount")


if __name__ == "__main__":
    unittest.main()
