import class_setup as setup


class TestImageComparison:

    @classmethod
    def setup_class(cls):
        print(setup.prepare_new_test_directory())
        print(setup.generate_resources())

    def test_foo(self):
        value = 1
        assert value == 1