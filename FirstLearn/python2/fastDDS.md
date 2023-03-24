# 获取fastDDS自定义参数地址

在python语言下，由于fastDDS的SubScribe通过take_next_sample获取大数据，**不论直接append到python的list中或者转换成np.array类型都需要花费1S左右的时间，而且传递的还不是原始数据，可能出现覆盖的情况**。所以考虑在接收是，使用np.frombuffer直接取出原始数据，快速进行处理。
在np.frombuffer直接取出原始数据的过程中则必须拿出该对象对应的内存地址。


# 方法

以Git上现有的测试代码，**RawData**数据的处理为例。

## 1.修改文件

打开 **DataTypes.cxx** 以及 **DataTypes.h** 进行编辑，找到RawData类后添加一个获取地址的函数。
[DataTypes.cxx]修改如下，**添加**以下内容：

uint64_t RawData::getRawDataAddr()
{
	 return uint64_t(&m_raw_data)
}

[DataTypes.h]修改如下，**添加**以下内容：

ePromisa_user_DllExport uint64_t getRawDataAddr();


## 2.编译

重新进行make指令，生成更新版本DataTypes.py，libDataTypes.so，_DataTypesWrapper.so

## 3.使用

data = DataTypes.RawData()
print('%#x'%data.getRawDataAddr)


