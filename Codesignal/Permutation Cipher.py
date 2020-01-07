def permutationCipher(password, key):
    table = str.maketrans("abcdefghijklmnopqrstuvwxyz",key)
    return password.translate(table)
© 2020 GitHub, Inc.
