import google.generativeai as genai
import os
from datetime import datetime

# 1. API 키 설정
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_post():
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 2. 모델 설정 (models/ 를 생략하거나 포함하는 방식 중 가장 안정적인 형태)
    # 404 에러가 계속된다면 'gemini-1.5-flash-latest'로 적어보세요.
    model_name = 'gemini-1.5-flash' 
    
    try:
        model = genai.GenerativeModel(model_name)
        
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

        # 3. 콘텐츠 생성
        response = model.generate_content(prompt)
        
        if not response.text:
            print("❌ 생성된 내용이 없습니다.")
            return

        content = response.text

        # 4. 파일 저장
        os.makedirs("_posts", exist_ok=True)
        filename = f"_posts/{today}-gemini-post.md"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"✅ 성공: {filename} 생성 완료")

    except Exception as e:
        print(f"❌ 오류 상세: {e}")
        # 만약 404가 또 뜨면, 사용할 수 있는 모델 리스트를 출력해줍니다.
        print("사용 가능한 모델 목록을 확인해 보세요:")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)

if __name__ == "__main__":
    generate_post()