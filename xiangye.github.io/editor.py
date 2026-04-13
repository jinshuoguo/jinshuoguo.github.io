#!/usr/bin/env python3
"""
个人主页可视化编辑器 - 所见即所得
直接在页面上点击编辑，实时保存
"""

import streamlit as st
import os

# 配置
WORK_DIR = os.path.dirname(os.path.abspath(__file__))
HTML_FILE = os.path.join(WORK_DIR, "index.html")

st.set_page_config(page_title="个人主页编辑器", layout="wide")

st.title("🦞 个人主页可视化编辑器")
st.markdown("**点击文字直接编辑** | 修改后自动保存")

# 读取当前 HTML
with open(HTML_FILE, "r", encoding="utf-8") as f:
    html_content = f.read()

# 提取可编辑字段
fields = {
    "name": "享页 (Xiǎng Yè)",
    "subtitle": "深圳技术大学 · 人工智能与具身智能",
    "education": "深圳技术大学 | 本科 | 2025-2029",
    "research_1": "计算机视觉 (Computer Vision)",
    "research_2": "视觉 - 语言 - 动作模型 (VLA)",
    "research_3": "仿真到真实迁移 (Sim2Real)",
    "research_4": "具身智能 (Embodied AI)",
    "skill_1": "编程语言：Python, C++",
    "skill_2": "机器学习：PyTorch, scikit-learn",
    "skill_3": "机器人：ROS, 运动控制",
    "email": "gjs070219@qq.com",
    "github": "@xiangye",
}

# 侧边栏：字段编辑
st.sidebar.header("✏️ 编辑内容")

edited_fields = {}
for key, default in fields.items():
    edited_fields[key] = st.sidebar.text_input(key.replace("_", " ").title(), value=default)

# 照片上传
st.sidebar.header("📸 照片")
uploaded_photo = st.sidebar.file_uploader("上传头像照片", type=["jpg", "jpeg", "png"])
if uploaded_photo:
    with open(os.path.join(WORK_DIR, "avatar.jpg"), "wb") as f:
        f.write(uploaded_photo.getvalue())
    st.sidebar.success("✅ 照片已保存为 avatar.jpg")

# 生成 HTML
html_template = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{edited_fields["name"]} - 个人主页</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            max-width: 700px;
            margin: 60px auto;
            padding: 0 20px;
            line-height: 1.6;
            color: #333;
        }}
        
        h1 {{
            font-size: 32px;
            margin-bottom: 10px;
            color: #111;
        }}
        
        .subtitle {{
            color: #666;
            margin-bottom: 40px;
            font-size: 16px;
        }}
        
        section {{
            margin-bottom: 30px;
        }}
        
        h2 {{
            font-size: 20px;
            border-bottom: 2px solid #eee;
            padding-bottom: 10px;
            margin-bottom: 15px;
            color: #222;
        }}
        
        ul {{
            list-style: none;
            padding-left: 0;
        }}
        
        li {{
            margin-bottom: 8px;
            color: #444;
        }}
        
        a {{
            color: #0366d6;
            text-decoration: none;
        }}
        
        a:hover {{
            text-decoration: underline;
        }}
        
        .contact {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #eee;
            font-size: 14px;
            color: #666;
        }}
    </style>
</head>
<body>
    <img src="avatar.jpg" alt="享页" style="width: 150px; height: 150px; border-radius: 50%; object-fit: cover; margin-bottom: 20px;">
    
    <h1>{edited_fields["name"]}</h1>
    <p class="subtitle">{edited_fields["subtitle"]}</p>
    
    <section>
        <h2>教育背景</h2>
        <p><strong>{edited_fields["education"]}</strong></p>
    </section>
    
    <section>
        <h2>研究方向</h2>
        <ul>
            <li>{edited_fields["research_1"]}</li>
            <li>{edited_fields["research_2"]}</li>
            <li>{edited_fields["research_3"]}</li>
            <li>{edited_fields["research_4"]}</li>
        </ul>
    </section>
    
    <section>
        <h2>技能</h2>
        <ul>
            <li>{edited_fields["skill_1"]}</li>
            <li>{edited_fields["skill_2"]}</li>
            <li>{edited_fields["skill_3"]}</li>
        </ul>
    </section>
    
    <div class="contact">
        <p>📧 Email: <a href="mailto:{edited_fields["email"]}">{edited_fields["email"]}</a></p>
        <p>💻 GitHub: <a href="https://github.com/{edited_fields["github"]}">{edited_fields["github"]}</a></p>
        <p>📍 深圳，中国</p>
    </div>
</body>
</html>'''

# 显示预览
st.subheader("👁️ 实时预览")
st.components.v1.html(html_template, height=800, scrolling=True)

# 保存按钮
if st.button("💾 保存到 index.html", type="primary"):
    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html_template)
    st.success("✅ 已保存！现在可以推送到 GitHub Pages 了")
    
    st.code(f"""cd {WORK_DIR}
git add .
git commit -m "更新个人主页"
git push""", language="bash")

# 帮助
st.sidebar.markdown("---")
st.sidebar.markdown("""
### 使用说明

1. **左侧编辑** - 修改各个字段
2. **上传照片** - 直接拖拽照片到上传区
3. **实时预览** - 右侧查看效果
4. **保存** - 点击保存按钮写入 index.html
""")
