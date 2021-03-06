# tests/runner.py
import unittest

# import your test modules
import tests.syntax as syntax
import tests.ast as test_ast

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(syntax))
suite.addTests(loader.loadTestsFromModule(test_ast))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
