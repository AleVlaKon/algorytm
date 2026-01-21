def is_almost_palindrome(s: str) -> bool:
    left, right = 0, len(s) - 1
    removed = False

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            if removed:
                return False
            # пробуем «удалить» слева
            if s[left + 1] == s[right]:
                left += 1
                removed = True
            # или «удалить» справа
            elif s[left] == s[right - 1]:
                right -= 1
                removed = True
            else:
                return False

    return True


# print(is_almost_palindrome('ldlld'))