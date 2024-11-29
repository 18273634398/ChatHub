# ChatHub
 ## 一款简单上手的大模型调用Python框架
 
---

 ## 使用说明
 ### 填写与修改配置信息
 本框架将运行过程中用到的数据已经全部放于 **control.settings** 中，在这里可以进行修改配置API_Key,Base_url以及用户昵称user_name等全局或核心数据。
![Settings](https://github.com/18273634398/picture/blob/main/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20241128153733.png?raw=true)

### 常见问题
> 1.该框架支持多轮对话，但需要在settings中设置longConversation字段的值，当其为True时为长对话模式，在这种模式下，模型将聚焦于同一个问题，即使你后来提出的内容于最开始提出的问题毫不相干，但是模型仍将沉浸于第一个问题的解答中。

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
2. **重启设备**：关闭并重新打开耳机和连接的设备。
3. **重新配对**：删除旧的配对信息，重新进行配对。
4. **软件更新**：确保耳机和连接设备的软件都是最新的。
5. **清洁耳机**：有时灰尘或污垢可能导致连接问题，清洁耳机和充电接口。
6. **联系制造商**：如果以上方法都无效，可以联系耳机的制造商或查看是否有保修服务。
如果耳机有物理损坏，可能需要专业的电子维修服务，而不是去医院。医院通常不处理这类问题。


Input: 左手一只鸭，右手一只鸡。交换两次双手物品后，左右手中各是啥？
Output:如果您的蓝牙耳机出现了物理损坏，比如外壳破裂、内部零件损坏等，您可能需要寻求专业的电子维修服务。以下是一些可能的解决方案：
1. **联系制造商或品牌客服**：许多品牌提供售后服务，包括维修或更换损坏的设备。您可以查看耳机的保修条款，看看是否在保修期内。
2. **寻找当地的电子维修店**：有些电子产品维修店可以处理小型电子设备的维修，包括蓝牙耳机。您可以在当地的电子市场或通过网络搜索找到这样的维修店。
3. **在线维修服务**：有些公司提供在线维修服务，您可以将耳机寄给他们进行维修。
4. **购买新的耳机**：如果维修成本过高或耳机已经过时，您可能需要考虑购买新的耳机。
总之，蓝牙耳机的维修通常不需要去医院，而是需要联系专业的电子产品维修服务。
```