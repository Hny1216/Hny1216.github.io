---
math: True
title: Life prediction model for lithium-ion battery via a 3D convolutional network enhanced by channel attention considering charging and discharging process
date: 2024-12-01
categories:
- 论文文献阅读
---

基于动态自编码网络的电池故障检测

<!-- more -->

# Life prediction model for lithium-ion battery via a 3D convolutional network enhanced by channel attention considering charging and discharging process

Article link: [Realistic fault detection of li-ion battery via dynamical deep learning (nature.com)]()

local link: [Realistic fault detection of li-ion battery via dynamical deep learning](/downloads/2024-12-01_Life prediction model for lithium-ion battery via a 3D convolutional network enhanced by channel attention considering charging and discharging process.pdf)

Date: 2024-12-01

## Gaps

+ 对于多路测量参数（温度、电压、电流等），已有研究大多将它们直接连接，忽视了其中的耦合关系，导致了在映射到潜在特征空间时出现解耦。这种数据交互不足阻碍了模型的性能。

+ 在模型层面：（1）许多方法仅关注充电或放电单一过程；（2）CNN在处理时序性数据时性能不佳，且缺乏不同充电策略下的泛化能力。

  

## Novelty/Originality

+ 从放电过程中的IC曲线和电压曲线中提取HI，与充电特征进行融合；

+ 通过RP技术将充电过程中的VIT数据转换为多维数据；

+ 提出了一种深度可分离的通道注意力3DCNN，用以解决权重数量多喝数据缺乏耦合计算的问题；

+ 提出了一种同时预测不同充电协议下的寿命预测方法。

  

## Input

### Datasets

数据集采用MIT的两套锂离子退化数据集，分别包含了124和45个电池样本，两套数据集的采用不同的充电策略。

+ （1）“C1(Q1)-C2”-(80%)-“1CC(3.6V)-1CV”
+ （2）“CC1-CC2-CC3-CC4”-“CC5-CV1”

### Charge process

RP技术：



### DisCharge process

+ IC曲线的峰值坐标（PIIC）
+ 







