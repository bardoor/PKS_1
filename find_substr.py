def find_substr(big_str: str, little_str: str) -> None | int:
    if not(isinstance(big_str, str) and isinstance(little_str, str)):
        return None
    if not(little_str in big_str):
        return None
    for big_str_symbol_index in range(len(big_str)):
        if big_str[big_str_symbol_index] == little_str[0]:
            we_got_correct_index = True
            maybe_first_index_we_need = big_str_symbol_index   
            for little_str_symbol_index in range(len(little_str)):
                if little_str[little_str_symbol_index] == big_str[big_str_symbol_index]:
                    big_str_symbol_index += 1
                else:
                    we_got_correct_index = False
                    break
            if we_got_correct_index:
                return maybe_first_index_we_need
            

def test_not_str_in_params_in_find_substr() -> None:
    first_param = []
    second_param = 12
    must_return = None
    assert find_substr(first_param, second_param) == must_return, "В параметрах переданы не строки"

def test_not_second_str_in_first_str_in_find_substr() -> None:
    first_param = 'fav21'
    second_param = '0'
    must_return = None
    assert find_substr(first_param, second_param) == must_return, "В первой строке нету второй"