from names import make_full_name, extract_family_name, extract_given_name
import pytest

def test_extract_family_name():
    assert(extract_family_name("Brown; Sally")) == "Brown"

def test_extract_given_name():
    assert(extract_given_name("Brown; Sally")) == "Sally"

def test_make_full_name():
    assert(make_full_name("Sally", "Brown")) == "Brown; Sally"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])