 <p align="center"><img src="https://github.com/18273634398/ChatHub/blob/master/logo.png?raw=true"    width="300" /></p>
 
# ChatHub
 ## 一款简单上手的大模型调用Python框架
 
---

 ## 使用说明
 ### 快速上手

本框架将运行过程中用到的数据部分写于
 control.settings中，在这里可以进行修改配置Base_url以及用户昵称user_name等全局或核心数据<br>
 <p align="left"><img src="https://github.com/18273634398/picture/blob/main/global.png?raw=true"    width="800" /></p>
 
  ![important](https://img.shields.io/badge/-important-important)
  但基于安全考虑，API_key等个人隐私信息，需要用户在config.txt中按照图示方法进行填写
  
<p align="left"><img src="https://github.com/18273634398/picture/blob/main/api.png?raw=true"    width="800" /></p>

---
当你填写api_key等配置信息后即可使用

### 常见问题
> 1.该框架支持多轮对话，但需要在settings中设置longConversation字段的值，当其为True时为长对话模式，在这种模式下，模型将聚焦于同一个问题，即使你后来提出的内容于最开始提出的问题毫不相干，但是模型仍将沉浸于第一个问题的解答中。<br>
**此问题已于0.2.0测试版本解决**

```
【单论对话(longConversation=False)】
Welcome to chatHub!now type your question
Input: 蓝牙耳机坏了需要看医院的哪个科室
Output:如果您指的是蓝牙耳机出现了技术问题，那么这通常不属于医疗问题，不需要去医院就诊。您应该联系耳机的生产厂家或者去销售该产品的商店寻求技术支持或者维修服务。
但如果您的问题是关于使用蓝牙耳机导致的耳朵不适或听力问题，那么您应该去看医院的耳鼻喉科。耳鼻喉科可以处理与耳朵相关的各种问题，包括因为使用耳机导致的听力下降、耳痛等问题。
在前往医院之前，建议您先停止使用蓝牙耳机，观察症状是否有所缓解。同时，也请注意保护听力，合理安排使用耳机的时间，避免音量过大对耳朵造成伤害。

Input: 左手一只鸭，右手一只鸡。交换两次双手物品后，左右手中各是啥？
Output:这是一个常见的逻辑谜题。初始状态下，左手是鸭，右手是鸡。如果进行两次交换：
```

```
【多轮对话(longConvsersation=True)】
Welcome to chatHub!now type your question
Input: 蓝牙耳机坏了需要看医院的哪个科室
Output:蓝牙耳机坏了通常不需要去医院。您可以尝试以下几种方法来解决问题：
1. **检查电池**：确保耳机电池有电，尝试充电。
......
如果耳机有物理损坏，可能需要专业的电子维修服务，而不是去医院。医院通常不处理这类问题。


Input: 左手一只鸭，右手一只鸡。交换两次双手物品后，左右手中各是啥？
Output:如果您的蓝牙耳机出现了物理损坏，比如外壳破裂、内部零件损坏等，您可能需要寻求专业的电子维修服务。以下是一些可能的解决方案：
1. **联系制造商或品牌客服**：许多品牌提供售后服务，包括维修或更换损坏的设备。您可以查看耳机的保修条款，看看是否在保修期内。
......
总之，蓝牙耳机的维修通常不需要去医院，而是需要联系专业的电子产品维修服务。
```

## 版本更新
>V0.4.2 [Test | NEW]<br>
Date: 2024/11/29<br>
1.常规更新 新增chatGPT[代理]模型调用<br>
<p></p><br><br>

>V0.4.0 [Test | NEW]<br>
Date: 2024/11/29<br>
1.优化体验
<p></p><br><br>

> V0.4.0 [Test]<br>
Date: 2024/11/29<br>
1.基于安全问题，现在已经移除了软件内部的API相关数据，关于如何填写自己的API信息，清参考之前的使用说明<br>
2.优化大语言模型的提示词工程，尤其是对于BigModel(智谱清言模型)，通过设置提示词，可以让通过API调用的大语言模型坚定一个新的身份<br>
3.优化代码结构<br>
<p></p><br><br>

> V0.3.0 [Test]<br>
Date: 2024/11/29<br>
1.新增百川AI模型调用 (百川模型具有极强的实时信息处理能力)<br>
<p></p><br><br>

> V0.3.0 [Test]<br>
Date: 2024/11/29<br>
1.修复了之前版本中，对大模型输入指令"update"后出现的修改api_key后无法继续对话的bug，本版本通过重启函数让api_key更新后系统自动重启<br>
2.新增了Restart函数用于系统重启<br>
<p></p><br><br>

> V0.2.0 [Test]<br>
Date: 2024/11/28<br>
版本更新内容<br>
<p></p><br><br>

> V0.1.1 [Test]<br>
Date: 2024/11/27<br>
版本更新内容<br>
<p></p><br><br>

> V0.1.0 [Test]<br>
Date: 2024/11/27<br>
<p></p><br><br>
