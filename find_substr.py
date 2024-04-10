def find_substr(big_str: str, little_str: str) -> None | int:
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