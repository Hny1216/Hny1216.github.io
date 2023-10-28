---
title: Realistic fault detection of li-ion battery via dynamical deep learning
date: 2023-10-21
categories:
- 论文文献阅读
---

# Realistic fault detection of li-ion battery via dynamical deep learning

Article link: [Realistic fault detection of li-ion battery via dynamical deep learning (nature.com)](https://www.nature.com/articles/s41467-023-41226-5.pdf)

local link: [Realistic fault detection of li-ion battery via dynamical deep learning](/downloads/2023-10-09 Realistic fault detection of li-ion battery via dynamical deep learning.pdf)

Date: 2023-10-09

## 1.论文主旨

​	文章针对当前电池动力电池数据的隐私以及成本问题，提出了一种现实可应用的深度学习框架模型（动态自编码异常检测，`Dynamical autoencoder for Anomaly Detection`, `DyAD` ），并且公布了347个电动汽车的690000个[锂电池充电片段数据](https://figshare.com/articles/dataset/Realistic_fault_detection_of_Li-ion_battery_via_dynamical_deep_learning_approach/23659323)。

​	此前研究面临的问题主要有：（1）传统的数据使用方法（温度、电压的方差等）难以辨认异常与正常汽车，数据关联性表现较弱，ROC在0.5左右；（2）数据直接上传容易泄露，用户隐私难以保护；为此，文章提出了一种可大规模使用的定制深度学习框架。

### 1.1.模型建模

​	不直接上传用户的各项直接数据，而是将用户数据分为系统输入（电流，SOC）和系统响应（电压，温度）两部分，而后在充电站部署编码器，编码器学习系统输入到系统响应的映射关系，编码后的数据上传到云端经过解码后对电动汽车的异常是否做出检测。通过编码-解码架构避免了用户的隐私和厂商的模型细节泄露。

### 1.2.建模细节

​	问题1：传统的深度学习方法通过研究数据分布来检测异常，对不常见的数据表现出较差的检测效果（如恒流充电数据，可能会被误判为正常电池）。

​	解决方法：在自编码-解码器中，编码器保持不变，编码器学习系统输入和系统响应的映射关系后得到潜在变量；而解码器不再仅仅利用潜在变量进行解码，而是通过潜在变量以及系统输入进行解码。具体理解如下：编码器学习到系统输入与系统响应的映射关系，那么可以用`y=f(x)`来表示这一过程，其中`y`是系统响应，`x`是系统输入，而编码器正是通过`x`和`y`学习到映射函数`f`。传统方法便是将`f`得到的潜在变量直接做出检测。然而本文构造了一个解码器`f1`来模型物理系统，通过系统输入`x`重构了系统响应`y1=f1(x)`,对比真实响应`y`和重构响应`y1`得到重构误差损失。其次通过里程进行弱监督从而引入辅助损失，引入KL正则化防止过拟合。三个损失函数共同影响模型的训练过程以及样本的异常情况。

​	模型包含了三组参数，分别是编码器参数$ \theta$，解码器参数$\zeta$和多感知机头部参数$\xi$，前两组参数均通过图卷积神经网络参数化得到。三个损失函数分别定义为：$l_{recon.}$，$l_{reg.}$，$l_{mileage}$。







## 2.复现

### 2.1.数据集

























