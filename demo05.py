from collections.abc import Iterable, Iterator


print(isinstance({}, Iterable))
print(isinstance({}, Iterator))
print(isinstance([], Iterable))
print(isinstance([], Iterator))
print(isinstance('aaaa', Iterable))
print(isinstance(iter("aaaa"), Iterator))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance((x for x in range(10)), Iterator))
