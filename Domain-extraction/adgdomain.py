import re

# 读取文件内容
file_path = "dns-us-first.txt"  # 替换为你的文件路径
with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
    content = f.readlines()

# 正则表达式匹配域名格式
domain_pattern = re.compile(r"\[/([^/\s]+)\/]")

# 提取域名
domains = set()
for line in content:
    matches = domain_pattern.findall(line)
    domains.update(matches)

# 生成格式化输出
formatted_output = f"[{'/'.join(sorted(domains))}/]"

# 输出结果
print(formatted_output)

# 可选：将结果保存到新文件
output_file = "extracted_domains.txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(formatted_output)

print(f"提取完成，结果已保存至 {output_file}")

