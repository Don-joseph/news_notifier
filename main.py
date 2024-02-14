import time
import pyttsx3
from plyer import notification
import json
import requests
engine=pyttsx3.init('sapi5')
def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.SpVoice")
    speak.Speak(str)
if __name__=="__main__":
    r = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=0be9f875cc694f6db95758e138d506aa")
    data = json.loads(r.content)
    i=0
    while True:
        News = data['articles'][i]['title']
        notification.notify(
            title="Top news update!",
            message=News,
            app_icon="C:\\Users\\donjo\\OneDrive\\Desktop\\news.ico",
            timeout=10
        )
        speak("Top news update!")
        speak(News)
        i+=1
        if i==5:
            i=0
        time.sleep(60*3)
