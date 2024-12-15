---
title: Transformer
math: true
date: 2024-12-15
hidden: True
categories:
- [深度学习, Transformer]
---

Transformer——Transformer

<!-- more -->

## 构建神经网络的主要工具

构建网络层可以利用 `nn.Module`类或`nn.functional`函数。两者功能相同，性能相似。卷积层、全连接层、dropout层等含有可学习参数时一般选用`nn.Module`，而池化层、激活函数等不含可学习参数时使用`nn.functional`中的函数。

### `nn.Module`

现实情况下，常用通过继承`nn.Module`来生成自定义网络：`class Net(torch.nn.Module)`。`nn`中已经实现了全连接层、激活层等，均是`nn.Module`的子类，能够检测自己的参数，并将其作为学习参数，针对GPU运行进行cuDNN优化。可以直接利用`nn.Xxx`调用，如：`nn.Linear`、`nn.Conv2d`等。

### `nn.functional`

`nn.functional`中的函数具有同样的功能。可以利用`nn.functional.xxx`调用，如`nn.functional.linear`、`nn.functional.conv2d`等。

:::info no-icon

`nn.Xxx`和`nn.functional.xxx`功能和性能相差无几，主要区别在于：

1. `nn.Xxx`继承自`nn.Module`，需要先实例化并传入参数，然后以函数调用的方式调用实例化对象并传入输入数据。它能够很好地与`nn.Sequential`结合使用，而`nn.functional.xxx`无法与`nn.Sequential`结合使用。
2. `nn.Xxx`不需要自己定义和管理weight、bias参数，而`nn.functional.xxx`需要自定义，每次调用都需要手动输入，不利于代码复用。
3. dropout在训练和测试阶段有区别，使用`nn.Xxx`定义的dropout，在调用`model.eval()`后自动实现转换，而`nn.functional.xxx`不行。

:::

## 模型构建

PyTorch构建模型的方法主要有3种：（1）继承`nn.Module`基类构建模型；（2）使用`nn.Sequential`按层顺序构建模型；（3）继承`nn.Module`基类构建模型，再使用相关模型容器（`nn.Sequential`、`nn.ModuleList`、`nn.ModuleDict`）进行封装。

### 继承`nn.Module`基类构建模型

先定义一个类，继承`nn.Module`基类，层函数放在构造函数`__init__()`中，在`forward`方法中实现正向传播。

1. 导入模块

```python
import torch
from torch import nn
import torch.nn.functional as F
```

2. 构建模型

```python
class Model_1(nn.Module):
    def __init__(self,in_dim,n_hidden_1,n_hidden_2,out_dim):
        super(Model_1,self).__init__()
        self.flatten = nn.Flatten()
        self.linear1 = nn.Linear(in_dim,n_hidden_1)
        self.bn1 = nn.BatchNorm1d(n_hidden_1)
        self.linear2 = nn.Linear(n_hidden_1,n_hidden_2)
        self.bn2 = nn.BatchNorm1d(n_hidden_2)
        self.out = nn.Linear(n_hidden_2,out_dim)
    def forward(self,x):
        x = self.flatten(x)
        x = self.linear1(x)
        x = self.bn1(x)
        x = F.relu(x)
        x = self.linear2(x)
        x = self.bn2(x)
        x = F.relu(x)
        x = self.out(x)
        x = F.softmax(x,dim=1)
        return x
```

3. 模型实例化

```python
in_dim, n_hidden_1, n_hidden_2, out_dim = 28*28, 300, 100, 10
model1 = Model_1(in_dim,n_hidden_1,n_hidden_2,out_dim)
print(model1)
```

```bash 输出 command:("Output":1) 
Model_1(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (linear1): Linear(in_features=784, out_features=300, bias=True)
  (bn1): BatchNorm1d(300, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
  (linear2): Linear(in_features=300, out_features=100, bias=True)
  (bn2): BatchNorm1d(100, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
  (out): Linear(in_features=100, out_features=10, bias=True)
)
```



### 使用`nn.Sequential`按层顺序构建模型

由于`nn.Sequential`内部实现了forward函数，故不需要重写。

#### 可变参数传入

1. 导入模块

```python
import torch
from torch import nn
```



2. 构建模型

```python
Model_2 = nn.Sequential(
    nn.Flatten(),
    nn.Linear(in_dim,n_hidden_1),
    nn.BatchNorm1d(n_hidden_1),
    nn.ReLU(),
    nn.Linear(n_hidden_1,n_hidden_2),
    nn.BatchNorm1d(n_hidden_2),
    nn.ReLU(),
    nn.Linear(n_hidden_2,out_dim),
    nn.Softmax(dim=1)
)
```



3. 查看模型

```python
in_dim, n_hidden_1, n_hidden_2, out_dim = 28*28, 300, 100, 10
print(Model_2)
```

```bash 输出 command:("Output":1) 
Sequential(
  (0): Flatten(start_dim=1, end_dim=-1)
  (1): Linear(in_features=784, out_features=300, bias=True)
  (2): BatchNorm1d(300, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
  (3): ReLU()
  (4): Linear(in_features=300, out_features=100, bias=True)
  (5): BatchNorm1d(100, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
  (6): ReLU()
  (7): Linear(in_features=100, out_features=10, bias=True)
  (8): Softmax(dim=1)
)
```



#### `add_module`方法

1. 导入模块

```python
import torch
from torch import nn
```



2. 构建模型

```python
Model_3 = nn.Sequential()
Model_3.add_module("flatten",nn.Flatten())
Model_3.add_module("linear1",nn.Linear(in_dim,n_hidden_1))
Model_3.add_module("bn1",nn.BatchNorm1d(n_hidden_1))
Model_3.add_module("relu1",nn.ReLU())
Model_3.add_module("linear2",nn.Linear(n_hidden_1,n_hidden_2))
Model_3.add_module("bn2",nn.BatchNorm1d(n_hidden_2))
Model_3.add_module("relu2",nn.ReLU())
Model_3.add_module("out",nn.Linear(n_hidden_2,out_dim))
Model_3.add_module("softmax",nn.Softmax(dim=1))
```



3. 查看模型

```python
in_dim, n_hidden_1, n_hidden_2, out_dim = 28*28, 300, 100, 10
print(Model_3)
```

```bash 输出 command:("Output":1) 
Sequential(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (linear1): Linear(in_features=784, out_features=300, bias=True)
  (bn1): BatchNorm1d(300, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
  (relu1): ReLU()
  (linear2): Linear(in_features=300, out_features=100, bias=True)
  (bn2): BatchNorm1d(100, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
  (relu2): ReLU()
  (out): Linear(in_features=100, out_features=10, bias=True)
  (softmax): Softmax(dim=1)
)
```



#### `OrderedDict`方法

1. 导入模块

```python
import torch
from torch import nn
from collections import OrderedDict
```



2. 构建模型

```python
Model_4 = nn.Sequential(OrderedDict([
    ("flatten",nn.Flatten()),
    ("linear1",nn.Linear(in_dim,n_hidden_1)),
    ("bn1",nn.BatchNorm1d(n_hidden_1)),
    ("relu1",nn.ReLU()),
    ("linear2",nn.Linear(n_hidden_1,n_hidden_2)),
    ("bn2",nn.BatchNorm1d(n_hidden_2)),
    ("relu2",nn.ReLU()),
    ("out",nn.Linear(n_hidden_2,out_dim)),
    ("softmax",nn.Softmax(dim=1))
]))
```



3. 查看模型

```python
in_dim, n_hidden_1, n_hidden_2, out_dim = 28*28, 300, 100, 10
print(Model_4)
```

```bash 输出 command:("Output":1) 
Sequential(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (linear1): Linear(in_features=784, out_features=300, bias=True)
  (bn1): BatchNorm1d(300, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
  (relu1): ReLU()
  (linear2): Linear(in_features=300, out_features=100, bias=True)
  (bn2): BatchNorm1d(100, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
  (relu2): ReLU()
  (out): Linear(in_features=100, out_features=10, bias=True)
  (softmax): Softmax(dim=1)
)
```



### 继承`nn.Module`基类构建模型，再使用相关模型容器进行封装

模型结构较为复杂时，可以通过相关容器（`nn.Sequential`、`nn.ModuleList`、`nn.ModuleDict`）对部分结构进行封装。

#### 使用`nn.Sequrntial`模型容器

```python
# 导入模块
import torch
from torch import nn
import torch.nn.functional as F

# 构建模型
class Model_5(nn.Module):
    def __init__(self,in_dim,n_hidden_1,n_hidden_2,out_dim):
        super(Model_5,self).__init__()
        self.flatten = nn.Flatten()
        self.layer1 = nn.Sequential(nn.Linear(in_dim,n_hidden_1),nn.BatchNorm1d(n_hidden_1))
        self.layer2 = nn.Sequential(nn.Linear(n_hidden_1,n_hidden_2),nn.BatchNorm1d(n_hidden_2))
        self.out = nn.Sequential(nn.Linear(n_hidden_2,out_dim))
    def forward(self,x):
        x = self.flatten(x)
        x = F.relu(self.layer1(x))
        x = F.relu(self.layer2(x))
        x = F.softmax(self.out(x),dim=1)
        return x

# 查看模型
in_dim, n_hidden_1, n_hidden_2, out_dim = 28*28, 300, 100, 10
model5 = Model_5(in_dim,n_hidden_1,n_hidden_2,out_dim)
print(model5)
```

```bash 输出 command:("Output":1) 
Model_5(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (layer1): Sequential(
    (0): Linear(in_features=784, out_features=300, bias=True)
    (1): BatchNorm1d(300, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
  )
  (layer2): Sequential(
    (0): Linear(in_features=300, out_features=100, bias=True)
    (1): BatchNorm1d(100, eps=1e-05, momentum=0.1, affine=True, track_running_stats=True)
  )
  (out): Sequential(
    (0): Linear(in_features=100, out_features=10, bias=True)
  )
)
```



#### 使用`nn.ModuleList`模型容器



#### 使用`nn.ModuleDict`模型容器





## 模型训练

模型训练主要包括加载数据，损失计算，优化算法，反向传播和参数更新。

损失计算可以通过自定义方法也可以通过内置的损失函数。

优化算法都封装在`torch.optim`中。

## 实例

### 参数定义及数据准备







