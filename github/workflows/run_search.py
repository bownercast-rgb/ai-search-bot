import os
import google.generativeai as genai

# 配置 API
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def perform_ai_search():
    # 使用具备搜索能力的模型
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        tools=[{'google_search': {}}]
    )
    
    prompt = "搜索并总结过去24小时内关于 AI Agent 和 自动化编程 的三大技术突破，包含原文链接。"
    
    response = model.generate_content(prompt)
    
    with open("latest_report.md", "w", encoding="utf-8") as f:
      f.write(response.text)

if __name__ == "__main__":
    perform_ai_search()
