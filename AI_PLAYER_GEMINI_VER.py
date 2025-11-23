import os
import json
from google import genai

os.environ['GEMINI_API_KEY']='AIzaSyCWDtNiFqtW6f0mJ3YjYYpWLmai4BvKL6U'

client=genai.Client()

##상황정보 딕셔너리 
current_game_data={
    "turn_info":{"turn_count":0},
    "bank":{"diamond": 5, "sapphire": 5, "emerald": 5, "ruby": 5, "onyx": 5},
    "players":{
        "ai":{"score":0,"tokens":{"diamond": 0, "sapphire": 0, "emerald": 0, "ruby": 0, "onyx": 0},
              "bounuses":{"diamond": 0, "sapphire": 0, "emerald": 0, "ruby": 0, "onyx": 0}
              },
        "opponent":{"score":0,"tokens":{"diamond": 0, "sapphire": 0, "emerald": 0, "ruby": 0, "onyx": 0},
              "bounuses":{"diamond": 0, "sapphire": 0, "emerald": 0, "ruby": 0, "onyx": 0}
              }
    }

}


##프롬프트
SPLENDOR_PROMPT = """
[역할] 당신은 스플렌더 AI 플레이어입니다. 
당신의 **유일한 임무**는 [출력 형식] 중 하나를 골라, 그 형식에 **정확히** 맞춰 한 문장을 출력하는 것입니다. 
다른 말은 절대 하지 마십시오. 
[출력 형식] (규칙 포함)당신의 답변은 **반드시** 아래 3가지 형식 중 하나여야 합니다.

1. (규칙) 서로 다른 보석 3개를 가져오는 행동을 할 경우:* **출력:** "[보석A] 1개, [보석B] 1개, [보석C] 1개를 가져오겠습니다."* (예시: "다이아몬드 1개, 사파이어 1개, 루비 1개를 가져오겠습니다.")

2. (규칙) 같은 색 보석 2개를 가져오는 행동을 할 경우 (해당 보석 재고 4개 이상 시):* **출력:** "[보석A] 2개를 가져오겠습니다."* (예시: "오닉스 2개를 가져오겠습니다.")

3. (규칙) 카드를 구매하는 행동을 할 경우 (현재 보석 0개로 불가능):* **출력:** "[카드 단계] [카드 할인보석]([비용]) 카드를 구매하겠습니다."* (예시: "1단계 오닉스(1다이아,1사파이어,1에메랄드,1루비) 카드를 구매하겠습니다.")

[금지 사항]당신의 최종 답변에는 "각기 다른 색 보석", "같은 색 보석", "개발카드 한 장" 같은 **규칙 설명**이 절대 포함되어서는 안 됩니다.

[명령][게임 상황]을 보고, [출력 형식] 1번 또는 2번 중에서 **규칙에 맞는** 행동을 선택하여, **[출력:]** 뒤에 있는 **형식 그대로** 즉시 출력하십시오.

"""

## 제미나이 불러오기
chat = client.chats.create( 
    model='gemini-2.5-flash',
    config=genai.types.GenerateContentConfig(
            system_instruction=SPLENDOR_PROMPT
        ),
    history=[]
)








## 메인 

while True:
    user_message = input("사용자:")
    if user_message == 'exit':
        break

    last_message=f"""
    [현재 게임 상황 데이터]
    {current_game_data}

    [필드카드목록]
    {user_message}
    """

    result=chat.send_message(last_message)
    print(f"\n행동:{result.text.strip()}\n")
    

 