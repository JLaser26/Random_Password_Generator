import secrets

def GenNewPassword(NUC: int, NLC: int, NI: int, NS: int, TotalLength: int):
    """********Details about these parameters********\n
        NUC :- mininum number of upper case characters\n
        NLC :- mininum number of lower case characters\n
        NI :- mininum number of Numbers\n
        NS :- mininum number of symbol\n
        TotalLength :- total length of your password
        """
    NUMS = "1234567890"
    ALPHA_U = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ALPHA_L = ALPHA_U.lower()
    SYMBOLS = "!@#$%^&*|/?.~:;'+=-_"
    ALL = NUMS + ALPHA_U + ALPHA_L + SYMBOLS

    result = []

    # minimum requirements
    result += [secrets.choice(NUMS) for _ in range(NI)]
    result += [secrets.choice(ALPHA_U) for _ in range(NUC)]
    result += [secrets.choice(ALPHA_L) for _ in range(NLC)]
    result += [secrets.choice(SYMBOLS) for _ in range(NS)]

    # fill remaining
    remaining = TotalLength - len(result)
    result += [secrets.choice(ALL) for _ in range(remaining)]

    # shuffle securely
    secrets.SystemRandom().shuffle(result)

    return ''.join(result)
