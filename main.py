import pandas as pd

# 读取txt文件
data_first = pd.read_csv('first-candidates.txt', sep='\t', header=None,
                         names=['考生编号', '姓名', '政治理论成绩', '外国语成绩', '业务课一成绩', '业务课二成绩',
                                '初试总分'])
# 计算进入复试每门科目的平均分
first_avg_scores = data_first[['政治理论成绩', '外国语成绩', '业务课一成绩', '业务课二成绩', '初试总分']].mean()
print(first_avg_scores)

data_second = pd.read_csv('second-candidates.txt', sep='\t', header=None,
                          names=['考生编号', '姓名', '复试成绩百分制', '总成绩百分制'])

# 合并数据
merged_data = pd.merge(data_second, data_first, on='考生编号', how='left')
# 打印结果
# print(merged_data.to_string())

# 计算进入复试每门科目的平均分
second_avg_scores = merged_data[['政治理论成绩', '外国语成绩', '业务课一成绩', '业务课二成绩', '初试总分']].mean()
print(second_avg_scores)
second_min_scores = merged_data[['初试总分']].min()
print(second_min_scores)
