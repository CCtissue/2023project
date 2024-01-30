import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
commit_df = pd.read_csv('commit_history.csv')

# 将日期时间数据转换为 pandas 的 datetime 类型
commit_df['date'] = pd.to_datetime(commit_df['date'], format='%Y-%m-%d %H:%M:%S%z', errors='coerce')

# 提取年份信息
commit_df['year'] = commit_df['date'].apply(lambda x: x.year)

# 统计每个年份的出现次数
yearly_counts = commit_df['year'].value_counts()

# 过滤掉1997年之前的数据
yearly_counts = yearly_counts[yearly_counts.index >= 1998]

# 绘制柱状图
plt.figure(figsize=(10, 6))
plt.bar(yearly_counts.index, yearly_counts.values)
plt.xlabel('Year')
plt.ylabel('Number of Commits')
plt.title('Commits by Year')
plt.show()