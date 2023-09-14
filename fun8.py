def allparams(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args", args)
    print("kwargs", kwargs)


allparams(1, 2)  # a, b 1 2
allparams(1, 2, 3)  # c, d 3 256
allparams(1, 2, 3, d=34)  # c, d 3 34
# allparams(a=56, b=89, c=89, d=87)  # TypeError: allparams() missing 2 required positional arguments: 'a' and 'b'
# / - argumenty po lewej stronie / muszą byc podane jako pozycyjne
allparams(1, 2, c=4)  # c, d 4 256
allparams(1, 2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14, d=30)
# args (1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14)
allparams(1, 2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14, a=9, d=30)  # kwargs {'a': 9}

# d - obowiazkowo po nazwie
allparams(1, 2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 14, a=7, e=9, d=30, root='/')  # kwargs {'a': 9}
