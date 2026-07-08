def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    # Словари для проверки связей в обе стороны
    s_to_t = {}
    t_to_s = {}

    # Идем по буквам из двух слов одновременно, для удобства используем zip()
    for char_s, char_t in zip(s, t):
        if char_s in s_to_t:
            # Если буква из s уже была, проверяем, что она соответствует той же букве из t
            if s_to_t[char_s] != char_t:
                return False
        else:
            #создаем связь, если ее не было
            s_to_t[char_s] = char_t

        #проверяем в обратную сторону
        if char_t in t_to_s:
            # Если буква из t уже была, проверяем, что она соответствует той же букве из s
            if t_to_s[char_t] != char_s:
                return False
        else:
            #создаем связь, если ее не было
            t_to_s[char_t] = char_s
          
    return True

