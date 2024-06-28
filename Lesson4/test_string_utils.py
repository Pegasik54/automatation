import pytest
from string_utils import StringUtils

string_utils = StringUtils()

# capitalize
@pytest.mark.parametrize("input_string, expected_output",[
    ("example", "Example"),
    ("welcome home", "Welcome home"),
    ("123", "123"),
    ("", ""),
    (" ", " "),
    ("124qwert", "124qwert"),
])
def test_capitalize(input_string, expected_output):
    assert  string_utils.capitilize(input_string) == expected_output

# trim
def test_trim():
    # Позитивные тесты
    assert string_utils.trim("   example") == "example"
    assert string_utils.trim("welcome home ") == "welcome home "
    assert string_utils.trim("   example   ") == "example   "
    # Негативные тесты
    assert string_utils.trim("") == ""
    assert string_utils.trim("example") == "example"

# to_list
def test_to_list():
    # Позитивные тесты
    assert string_utils.to_list("q,w,e,r,t,y") == ["q", "w", "e", "r", "t", "y"]
    assert string_utils.to_list("1:2:3", ":") == ["1", "2", "3"]
    # Негативные тесты
    assert string_utils.to_list("") == []
    assert string_utils.to_list("q,w,e,r,t,y", ";") == ["q,w,e,r,t,y"]

# contains
def test_contains():
    # Позитивные тесты
    assert string_utils.contains("Hello World", "H") == True
    assert string_utils.contains("Hello World", "l") == True
    # Негативные тесты
    assert string_utils.contains("Hello World", "Z") == False
    assert string_utils.contains("Hello World", "") == True  # Проверка на пустую строку

# delete_symbol
def test_delete_symbol():
    # Позитивные тесты
    assert string_utils.delete_symbol("Hello World", "l") == "Heo Word"
    assert string_utils.delete_symbol("HelloWorld", "World") == "Hello"
    # Негативные тесты
    assert string_utils.delete_symbol("Hello World", "Z") == "Hello World"
    assert string_utils.delete_symbol("Hello World", "") == "Hello World"

# starts_with
def test_starts_with():
    # Позитивные тесты
    assert string_utils.starts_with("Hello World", "H") == True
    assert string_utils.starts_with("Hello World", "Hello") == True
    # Негативные тесты
    assert string_utils.starts_with("Hello World", "W") == False
    assert string_utils.starts_with("Hello World", "hello") == False

# end_with
def test_end_with():
    # Позитивные тесты
    assert string_utils.end_with("Hello World", "d") == True
    assert string_utils.end_with("Hello World", "World") == True
    # Негативные тесты
    assert string_utils.end_with("Hello World", "H") == False
    assert string_utils.end_with("Hello World", "world") == False

# is_empty
def test_is_empty():
    # Позитивные тесты
    assert string_utils.is_empty("") == True
    assert string_utils.is_empty("   ") == True
    # Негативные тесты
    assert string_utils.is_empty("Hello World") == False
    assert string_utils.is_empty(" H ") == False

# list_to_string
def test_list_to_string():
    # Позитивные тесты
    # Позитивные тесты
    assert string_utils.list_to_string([1, 2, 3, 4]) == "1, 2, 3, 4"
    assert string_utils.list_to_string(["Welcom", "Home"]) == "Welcom, Home"
    assert string_utils.list_to_string(["Welcom", "Home"], "-") == "Welcom-Home"
    # Негативные тесты
    assert string_utils.list_to_string([]) == ""
    assert string_utils.list_to_string([None, "Home"]) == "None, Home"

if __name__ == "__main__":
    pytest.main()