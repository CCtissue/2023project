import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
commit_df = pd.read_csv('commit_history.csv')

# 将日期时间数据转换为 pandas 的 datetime 类型
commit_df['date'] = pd.to_datetime(commit_df['date'], format='%Y-%m-%d %H:%M:%S%z', errors='coerce')


def get_time_period(hour):
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 18:
        return 'Afternoon'
    else:
        return 'Evening'


commit_df['time_period'] = commit_df['date'].apply(lambda x: get_time_period(x.hour))

author_counts = commit_df['author'].value_counts()

threshold = 3000
top_authors = author_counts[author_counts >= threshold].index

developer_commit_counts = commit_df[commit_df['author'].isin(top_authors)].groupby(['author', 'time_period']).size().unstack(fill_value=0)

# 绘制堆叠条形图
developer_commit_counts.plot(kind='bar', stacked=True, figsize=(12, 8))
plt.title('Developer Commits by Time Period')
plt.xlabel('Author')
plt.ylabel('Commit Count')
plt.show()