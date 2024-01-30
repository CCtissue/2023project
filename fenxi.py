import libcst as cst
import ast

# 静态分析示例
filename = 'Git.py'
with open(filename, 'r', encoding='utf-8') as file:
    code = file.read()


def static_analysis(code):
    # 使用libcst解析代码
    tree = cst.parse_module(code)
    print(tree)

    # 使用ast解析代码
    tree_ast = ast.parse(code)
    print(ast.dump(tree_ast))


if __name__ == "__main__":
    # 调用静态分析函数
    static_analysis(code)
