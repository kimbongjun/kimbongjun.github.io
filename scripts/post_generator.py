import google.generativeai as genai
import os
import re
from datetime import datetime

# 1. API 키 설정
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def generate_post():
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 2. 모델 설정 (models/ 를 생략하거나 포함하는 방식 중 가장 안정적인 형태)
    # 404 에러가 계속된다면 'gemini-1.5-flash-latest'로 적어보세요.
    model_name = 'models/gemini-2.5-flash' 
    
    try:
        model = genai.GenerativeModel(model_name)
                
        prompt = f"""
        당신은 실무 효율성을 중시하는 IT 블로거입니다. 
        아래 주제에 대해 '동료 개발자에게 핵심 노하우를 공유하는 톤'으로 포스팅을 작성하세요.

        [주제]: Figma, Jenkins 등 UX/DevOps 툴 최신 동향과 실무 효율화 팁
        
        [작성 스타일 가이드]:
        1. **불필요한 인사말(인사, 날씨 등) 생략**: 바로 본론으로 들어가거나 주제에 대한 문제 제기로 시작하세요.
        2. **말투 교정**: 
           - '~입니다', '~합니다' 대신 '~해요', '~하더라고요', '~인 것 같아요'를 70% 이상 사용하세요.
           - "~인 점이 인상 깊었습니다" 보다는 "이거 써보니까 진짜 편하더라고요" 식의 구어체를 지향하세요.
        3. **실무자 시점**: 
           - "이 기능은 유용합니다" 대신 "실무에서 이 설정 하나만 바꿔도 작업 속도가 확 올라가요" 처럼 본인의 노하우인 것처럼 서술하세요.
        4. **가독성**: 핵심은 **굵게** 표시하고, 리스트 형식을 적절히 활용하세요.

        ---
        layout: post
        title: "[클릭을 부르는 실무 밀착형 제목]"
        date: {today}
        categories: AI-Tech
        ---
        (이후 마크다운 형식으로 바로 본론 작성)
        """

        # 3. 콘텐츠 생성
        response = model.generate_content(prompt)
        
        if not response.text:
            print("❌ 생성된 내용이 없습니다.")
            return

        content = response.text
        
        # 3. 제목(title) 추출 및 파일명 정제
        # Front Matter 내의 title: "제목" 부분을 찾아냅니다.
        title_match = re.search(r'title:\s*["\']?(.*?)["\']?\n', content)
        
        if title_match:
            raw_title = title_match.group(1)
            # 파일명으로 부적절한 특수문자 제거 및 공백을 대시(-)로 변경
            clean_title = re.sub(r'[^\w\s-]', '', raw_title).strip()
            clean_title = re.sub(r'\s+', '-', clean_title)
            post_name = clean_title
        else:
            # 제목 추출 실패 시 기본값 설정
            post_name = "tech-post"

        # 4. 파일 저장 (날짜-제목.md 형식)
        os.makedirs("_posts", exist_ok=True)
        filename = f"{today}-{post_name}.md"
        file_path = os.path.join("_posts", filename)
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"✅ 성공: {file_path} 생성 완료")

    except Exception as e:
        print(f"❌ 오류 상세: {e}")
        print("사용 가능한 모델 목록을 확인해 보세요:")
        for m in genai.list_models():
            if 'generateContent' in m.supported_generation_methods:
                print(m.name)

if __name__ == "__main__":
    generate_post()