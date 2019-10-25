参考  https://blog.csdn.net/robinhjwy/article/details/79174914 



##### RANSAC （Random sample consensus）是随机抽样一致算法。

通过迭代方式估计数学模型。其基本假设有：

1）数据由“局内点”组成，这些“局内点”可以形成一些模型；

2）“局外点”是被舍弃的数据，不形成模型；

3）除“局内点”和“局外点”之外的数据属于噪声；

##### 概述

从数据集中选取一部分数据作为初始局内点，根据初始局内点拟合模型

利用此模型判断局外点是否满足该模型。如果局外点的一些数据与模型的误差在一定范围内，那么局外点被认为是新的局内点并重新更新模型。（可能出现模型变差的情况；模型更好的结果。对此分别考虑）

根据可能出现的情况，通过估计局内点与模型的错误率评估模型

##### 伪代码：

*data —— 一组观测数据*
*model —— 适应于数据的模型*
*n —— 适用于模型的最少数据个数*
*k —— 算法的迭代次数*
*t —— 用于决定数据是否适应于模型的阀值*
*d —— 判定模型是否适用于数据集的数据数目*
*输出：*
*best_model —— 跟数据最匹配的模型参数（如果没有找到好的模型，返回null）*
*best_consensus_set —— 估计出模型的数据点*
*best_error —— 跟数据相关的估计出的模型错误*
*————————————————*
*版权声明：本文为CSDN博主「robinhjwy」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。*
*原文链接：https://blog.csdn.net/robinhjwy/article/details/79174914*

```
//以下伪代码，参考博主进行添加备注等
iterations = 0	
best_model = null
best_consensus_set = null
best_error = 无穷大	//越小表示模型越好
while ( iterations < k )
	maybe_inliers = 从数据集中随机选择n个点   		//初始化选择局内点
	maybe_model = 适合于maybe_inliers的模型参数	  //需要拟合的模型（参数提前设置，模型会更新）	
	consensus_set = maybe_inliers			   //把更新后的局内点放在变量 consensus_set 中

	for ( 每个数据集中不属于maybe_inliers的点 ） 		//针对局外点进行操作迭代模型
		/*把在阈值范围内的“局外点”的数据，放在consensus_set。*/
		if ( 如果点适合于maybe_model，且错误小于t ）
			将点添加到consensus_set	
		if （ consensus_set中的元素数目大于d ）
			//已经找好了更新后的数据集，根据数据集拟合模型
			better_model = 计算适合于consensus_set中所有点的模型
			this_error = better_model的误差分析  	//根据计算的最优模型，对其计算误差
			
			//对这些误差进行比较。如果寻找最小化误差模型
			if ( this_error < best_error )
				我们发现了比以前好的模型，保存该模型直到更好的模型出现
				best_model =  better_model
				best_consensus_set = consensus_set
				best_error =  this_error
		//迭代次数控制，迭代的情况。当迭代次数满足设定值或者best_error满足指定要求，则停止迭代
		增加迭代次数
最终返回 best_model, best_consensus_set, best_error
```

