import export

import git
import pandas as pd

# 指定Mozilla Firefox开源库的本地路径
repo_path = 'gecko-dev'

# 打开Git存储库
repo = git.Repo(repo_path)

# 获取提交历史信息
commits = list(repo.iter_commits('master'))  # 以master分支为例

# 将提交历史信息存入DataFrame
commit_data = []
# 打印提交历史信息示例
for commit in commits:
    commit_data.append({
        'commit_id': commit.hexsha,
        'author': commit.author.name,
        'date': commit.authored_datetime,
        'message': commit.message
    })
commit_df = pd.DataFrame(commit_data)
# 将DataFrame存入CSV表格
commit_df.to_csv('commit_history.csv')