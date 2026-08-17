import unittest
from optimus_core import OptimusCore

class TestOptimusCore(unittest.TestCase):
    def test_status(self):
        core = OptimusCore()
        status = core.ccloud_status()
        self.assertIsInstance(status, dict)

if __name__ == "__main__":
    unittest.main()
