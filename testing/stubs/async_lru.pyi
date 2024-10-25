from typing import Callable, TypeVar

T = TypeVar('T')    # Here T is generic type variable

# alru_cache is function which takes argument
# of type either int or None
# written callable entity, which in turns takes generic type T
# returns T
def alru_cache(maxsize: int | None) -> Callable[[T], T]: ...
