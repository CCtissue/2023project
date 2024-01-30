import pandas as pd
from collections import Counter
import re
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')

# 读取csv文件
df = pd.read_csv('bug_commits.csv')

# 获取停用词列表
stop_words = set(stopwords.words('english'))

# 合并所有message
all_messages = ' '.join(df['message'].tolist())

# 使用正则表达式分割单词
words = re.findall(r'\b\w+\b', all_messages.lower())

# 过滤掉停用词和常见介词
filtered_words = [word for word in words if word not in stop_words]

# 使用Counter统计单词出现的次数
word_counts = Counter(filtered_words)

# 找出出现次数最多的单词
most_common_words = word_counts.most_common(20)  # 取出现次数最多的前10个单词

# 打印出现次数最多的单词
print(most_common_words)