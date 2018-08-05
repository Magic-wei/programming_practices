## function/advanced_filter.py

```python
def _odd_iter(): # infinite odd sequence
    n = 1
    while True:
        n += 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0 # Q: 这种写法不太理解，x从哪儿输入？A: python可以返回函数

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
```
