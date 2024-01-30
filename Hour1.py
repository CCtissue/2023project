import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
commit_df = pd.read_csv('commit_history.csv')

# 将日期时间数据转换为 pandas 的 datetime 类型
commit_df['date'] = pd.to_datetime(commit_df['date'], format='%Y-%m-%d %H:%M:%S%z', errors='coerce')

# 将时间划分为早、中、晚三个时间段
def get_time_period(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    else:
        return 'Evening'

commit_df['time_period'] = commit_df['date'].apply(lambda x: get_time_period(x.hour))

# 统计每个作者的提交次数
author_counts = commit_df['author'].value_counts()

# 选择提交次数大于2000的作者
top_developers = author_counts[author_counts > 2000].index

# 仅保留提交次数大于2000的作者的数据
commit_df = commit_df[commit_df['author'].isin(top_developers)]

# 统计每个时间段的出现次数
period_counts = commit_df['time_period'].value_counts()

# 绘制饼图
plt.figure(figsize=(8, 8))
plt.pie(period_counts, labels=period_counts.index, autopct='%1.1f%%')
plt.title('Commits by Time Period')
plt.show()