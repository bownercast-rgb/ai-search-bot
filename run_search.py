import os
import google.generativeai as genai
from datetime import datetime

# 1. 基础配置：从 GitHub Secrets 读取 API Key
api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("❌ 错误: 未找到 GEMINI_API_KEY，请检查 GitHub Secrets 配置")
    exit(1)

genai.configure(api_key=api_key)

def perform_upgraded_search():
    # 2. 初始化具备搜索能力的模型 (Gemini 1.5 Flash)
    model = genai.GenerativeModel(
        model_name='gemini-1.5-flash',
        tools=[{'google_search': {}}]
    )
    
    # 3. 定义多维度追踪主题：结合化工、期货与 AI 自动化
    # 这里的关键词基于你对水性树脂、锂电材料及量化模型的关注
    topics = {
        "AI 自动化": "AI Agent 社交媒体自动发布工具、n8n/Make 自动化流最新开源项目",
        "有色金属期货": "LME 铝、锂、铜今日价格走势及 SHFE 铝锭库存变化分析",
        "先进化工材料": "AI 大模型新技术新应用、电池、锂电池粘结剂 (PAA/SAR) 研发进展"
    }
    
    report_content = f"# 📊 定制化行业深度日报 ({datetime.now().strftime('%Y-%m-%d')})\n\n"
    report_content += "> **定位**：技术专家级洞察 | 自动化信息聚合\n\n"
    
    for category, query in topics.items():
        print(f"正在深度分析: {category}...")
        # 提示词强化：要求以 25 年经验的 GM/专家视角进行总结
        prompt = f"""
        作为一名拥有 25 年经验的化工与金融领域专家，请针对主题 '{query}' 进行深度搜索。
        要求：
        1. 总结过去 24 小时内最重要的 2 条动态。
        2. 必须附带原始新闻或技术文档的链接。
        3. 用专业、精准的语言解释其对行业或交易逻辑的影响。
        """
        
        try:
            response = model.generate_content(prompt)
            report_content += f"## 🔍 {category}\n\n{response.text}\n\n---\n"
        except Exception as e:
            report_content += f"## 🔍 {category}\n\n⚠️ 搜索执行异常: {str(e)}\n\n"

    # 4. 保存报告为 Markdown 文件
    with open("latest_report.md", "w", encoding="utf-8") as f:
        f.write(report_content)
    
    print("✅ 深度日报已生成：latest_report.md")

if __name__ == "__main__":
    perform_upgraded_search()
