---
title: My Article
date: 2023-10-21
categories:
- 现代控制理论
---

这是摘要部分。

<!-- more -->

# 这是全文内容。

## 中山大学

在那边



```python
import numpy
```



```
```java 行高亮 https://shoka.lostyu.me 参考链接 mark:1,6-7 
import java.util.Scanner; 
... 
Scanner in = new Scanner (System.in); // 输入 Scan 之后，按下键盘 Alt + “/” 键，Eclipse 下自动补全。 
System.out.println (in.nextLine ()); System.out.println ("Hello" + "world."); ```
```

```java 行高亮 https://shoka.lostyu.me 参考链接 mark:1,6-7 import java.util.Scanner; ... Scanner in = new Scanner (System.in); // 输入 Scan 之后，按下键盘 Alt + “/” 键，Eclipse 下自动补全。 System.out.println (in.nextLine ()); System.out.println ("Hello" + "world."); ```

```java 行高亮 https://shoka.lostyu.me 参考链接 mark:1,6-7
import java.util.Scanner; 
... 
Scanner in = new Scanner (System.in); // 输入 Scan 之后，按下键盘 Alt + “/” 键，Eclipse 下自动补全。 
System.out.println (in.nextLine ()); 
System.out.println ("Hello" + "world."); ```
```



```java 行高亮 https://laoevil.gitee.io 参考链接 mark:1,6-7 import java.util.Scanner; ... Scanner in = new Scanner (System.in); // 输入 Scan 之后，按下键盘 Alt + “/” 键，Eclipse 下自动补全。 System.out.println (in.nextLine ()); System.out.println ("Hello" + "world."); ```



```markdown
|             |          Grouping           || 
First Header  | Second Header | Third Header | 
------------ | :-----------: | -----------: | 
Content       |          *Long Cell*        || 
Content       |   **Cell**    |         Cell |     

New section   |     More      |         Data | 
And more      | With an escaped '\\|'       || 
[Prototype table]
```

1. 编译时多态主要指运算符重载与函数重载，而运行时多态主要指虚函数。 {.quiz .true}

2. 有基类 `SHAPE`，派生类 `CIRCLE`，声明如下变量：  {.quiz .multi}
    ```cpp
    SHAPE shape1,*p1;
    CIRCLE circle1,*q1;
    ```
    下列哪些项是 “派生类对象替换基类对象”。
    - `p1=&circle1;` {.correct}
    - `q1=&shape1;`
    - `shape1=circle1;` {.correct}
    - `circle1=shape1;`
    {.options}
    > - :heavy_check_mark: 令基类对象的指针指向派生类对象
    > - :x: 派生类指针指向基类的引用
    > - :heavy_check_mark: 派生类对象给基类对象赋值
    > - :x: 基类对象给派生类对象赋值
    > {.options}

3. 下列叙述正确的是 []{.gap} 。 {.quiz}
    - 虚函数只能定义成无参函数
    - 虚函数不能有返回值
    - 能定义虚构造函数
    - A、B、C 都不对 {.correct}
    {.options}

10. 如果定义 `int e=8; double f=6.4, g=8.9;`，则表达式 `f+int (e/3*int (f+g)/2)%4` 的值为 [9.4]{.gap}。 {.quiz .fill}
    > 注意运算顺序和数据类型
    > [8.4]{.mistake}
