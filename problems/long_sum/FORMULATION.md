# Long sum

Необходимо реализовать сложение двух чисел, выражемых, как массивы цифр, где элемент, идущий раньше, выражает меньшую 
разрядность (т. е., например, число 10 представляется последовательностью [0, 1])


Сигнатуры целевых функций ожидаются следующими:
## Python

```python
from typing import List


def long_sum(
    first_number: List[int],
    second_number: List[int],
    base: int
) -> List[int]:
    pass
```