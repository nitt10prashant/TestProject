from nose.plugins.base import Plugin

class TestPlugin(Plugin):

    """
    Custom pluging to run test cases using nose this will help you to
    use nose for test case collector and runner and provide you structure
    way to run the test cases
    ex:
    setup() ,teardown() , setupClass(), teardownClass() and asserts.
    """