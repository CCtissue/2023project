import pandas as pd

# 读取提交历史数据
commit_df = pd.read_csv('commit_history.csv')

# 使用包含 bug 关键字的行创建新的数据框
bug_df = commit_df[commit_df['message'].str.contains(r'\b(bug)\b', case=False, regex=True)]

# 将包含 bug 关键字的行存储到新文件
bug_df.to_csv('bug_commits.csv', index=False)