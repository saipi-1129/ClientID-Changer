import os

user_profile = os.getenv('USERPROFILE')

file_path = os.path.join(user_profile, r'AppData\Local\Packages\Microsoft.MinecraftUWP_8wekyb3d8bbwe\LocalState\games\com.mojang\minecraftpe\clientid.txt')

def modify_clientid_file(new_content):
    try:
        with open(file_path, 'r') as file:
            original_content = file.read()
            print("変更前:", original_content)
        
        with open(file_path, 'w') as file:
            file.write(new_content)
            print("新しい内容が変更されました:", new_content)
    except FileNotFoundError:
        print(f"ファイルが見つかりません: {file_path}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

new_client_id = ""
modify_clientid_file(new_client_id)
