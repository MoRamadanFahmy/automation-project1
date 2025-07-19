import pyautogui
import subprocess
import time
import requests
import os


desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
save_dir = os.path.join(desktop, 'tjm-project')


if not os.path.exists(save_dir):
    os.makedirs(save_dir)

print("🗂️ Current folder:", os.getcwd())
print("📄 Files:", os.listdir())


for post_id in range(1, 11):

    response = requests.get(f'https://jsonplaceholder.typicode.com/posts/{post_id}')

    if response.status_code == 200:
        post = response.json()
        title = post['title']
        body = post['body']

        full_text = f"Title: {title}\n\n{body}"

        subprocess.Popen('notepad.exe')
        time.sleep(2)

        pyautogui.write(full_text, interval=0.05)
        time.sleep(1)

        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)

        file_path = os.path.join(save_dir, f'post {post_id}.txt')

        pyautogui.write(file_path)
        time.sleep(0.5)

        pyautogui.press('enter')  
        time.sleep(1)

        
        pyautogui.press('left')   
        time.sleep(0.2)
        pyautogui.press('enter')  
        time.sleep(1)

        print(f"✅ Saved Post {post_id}")

        pyautogui.hotkey('alt', 'f4')
        time.sleep(1)

    else:
        print(f"❌ Failed to fetch post {post_id}")

print("\n✅ All posts processed.")
