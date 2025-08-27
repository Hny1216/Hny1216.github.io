---
title: Leetcode刷题记录-title
math: true
fancybox: true
date: 2025-08-15
categories:
- 技能工具

---

Leetcode刷题记录

<!-- more -->

# Leetcode刷题



## 数组/字符串

### [1071. 字符串的最大公因子](https://leetcode.cn/problems/greatest-common-divisor-of-strings/)

对于字符串 `s` 和 `t`，只有在 `s = t + t + t + ... + t + t`（`t` 自身连接 1 次或多次）时，我们才认定 “`t` 能除尽 `s`”。

给定两个字符串 `str1` 和 `str2` 。返回 *最长字符串 `x`，要求满足 `x` 能除尽 `str1` 且 `x` 能除尽 `str2`* 。

:::info no-icon

若两个字符串是由同一个字符串 X重复拼接而成，那么无论先拼哪个，结果应该相同。
如果 str1 + str2 != str2 +str1，说明不存在公共的重复因子，直接返回空串 ""。
如果两个字符串都是由同一个字符串 X 组成，那么 X 的长度必然是str1.size()和 str2.size() 的最大公约数。

```python
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 + str2 == str2 + str1:
            return ""
        return str1[0:self.gcd(len(str1), len(str2))]
    
    def gcd(self, a,b):
        if b == 0: return a
        else: return gcd(b, a%b)
    
```

作者：Random
链接：https://leetcode.cn/problems/greatest-common-divisor-of-strings/solutions/3749891/shu-xue-zui-da-gong-yue-shu-by-coder-ran-a88u/

:::

