import libcst as cst
import pandas as pd

# 读取之前保存的提交历史信息
commit_df = pd.read_csv('commit_history.csv')

# 提取提交者、提交时间、文件修改等信息
for index, row in commit_df.iterrows():
    commit_message = row['message']
    # 使用libcst解析提交消息
    try:
        tree = cst.parse_module(commit_message)
        # 在这里你可以进行更多的处理，比如提取文件修改信息等
        print(f"Message: {row['message']}")
    except cst._exceptions.ParserSyntaxError:
        # 无法解析的提交消息
        continue