
def startsWith(s: str, prefix: str, ignore_case: bool = True) -> bool:
    sLen: int = len(str)
    pLen: int = len(prefix)
    if sLen < pLen:
        return False

    sPrefix = s[:pLen]
    if ignore_case:
        return prefix.lower() == sPrefix.lower()
    else:
        return prefix == sPrefix
