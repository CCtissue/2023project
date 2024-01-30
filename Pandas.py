import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')

# 读取提交历史文件
commit_df = pd.read_csv('commit_history.csv')

# 使用value_counts()方法统计不同作者出现的次数
author_counts = commit_df['author'].value_counts()

threshold = 5000
top_authors = author_counts[author_counts >= threshold]
other_authors = author_counts[author_counts < threshold]


# 绘制饼图
plt.figure(figsize=(8, 8))
plt.pie(top_authors, labels=top_authors.index, autopct='%1.1f%%')
plt.title('Commit Author Distribution')
plt.show()
