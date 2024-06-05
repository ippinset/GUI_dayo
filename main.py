from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class JankenRequest(BaseModel):
    user_choice: str

@app.post("/janken")
def play_janken(request: JankenRequest):
    choices = ['グー', 'チョキ', 'パー']
    if request.user_choice not in choices:
        return {"message": "無効な選択です。グー、チョキ、パーのいずれかを選んでください。"}
    
    computer_choice = random.choice(choices)
    if request.user_choice == computer_choice:
        result = "引き分けです。"
    elif (request.user_choice == 'グー' and computer_choice == 'チョキ') or \
         (request.user_choice == 'チョキ' and computer_choice == 'パー') or \
         (request.user_choice == 'パー' and computer_choice == 'グー'):
        result = "あなたの勝ちです！"
    else:
        result = "あなたの負けです。"
    
    return {
        "user_choice": request.user_choice,
        "computer_choice": computer_choice,
        "result": result
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
