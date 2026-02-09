import google.generativeai as genai
import os
from datetime import datetime

# API 키 설정
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_post():
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 💡 모델명을 'models/gemini-1.5-flash'로 명시해 보세요.
    # 만약 계속 에러가 난다면 'gemini-pro'로 테스트해 볼 수 있습니다.
    model = genai.GenerativeModel('models/gemini-1.5-flash') 

    prompt = f"""
    주제: 최신 기술 및 AI 뉴스 요약
    형식: GitHub Jekyll 블로그 마크다운 포스트
    요구사항:
    - 아래 Front Matter를 포함할 것:
    ---
    layout: post
    title: "Gemini AI Daily: {today}"
    date: {today}
    categories: AI-Tech
    ---
    - 한국어로 작성하고 가독성 좋게 마크다운 문법을 활용해줘.
    """

    try:
        # 콘텐츠 생성
        response = model.generate_content(prompt)
        
        # 💡 응답이 비어있는지 확인하는 안전장치
        if not response.text:
            print("❌ 생성된 내용이 없습니다.")
            return

        content = response.text

        os.makedirs("_posts", exist_ok=True)
        filename = f"_posts/{today}-gemini-post.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"✅ 성공: {filename} 생성 완료")

    except Exception as e:
        print(f"❌ 오류 상세: {e}")

if __name__ == "__main__":
    generate_post()