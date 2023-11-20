import boltons.strutils as butils

def starts_with(s: str, prefix: str, ignore_case: bool = True) -> bool:
    s_len: int = len(str)
    p_len: int = len(prefix)
    if s_len < p_len:
        return False

    s_prefix = s[:p_len]
    if ignore_case:
        return prefix.lower() == s_prefix.lower()
    else:
        return prefix == s_prefix
