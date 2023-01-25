import os
import json

try:
    import requests
except ImportError:
    os.system("pip install requests")
    print("\033[0;31m!! Please re-run the command again !!\033[0m")

# !!
print("\033[0;31m!! Please don't leak your access token to anyone !!\033[0m")
# !!

# Asking for access token... then clear the console
sAccessToken = input("Please enter your access token: ")
os.system("cls")

# Set API URL
profile_url = "https://app-api.salad.io/api/v1/profile"
selected_avatar_url = "https://app-api.salad.io/api/v2/avatars/selected"
xp_url = "https://app-api.salad.io/api/v1/profile/xp"
balance_url = "https://app-api.salad.io/api/v1/profile/balance"
referral_code_url = "https://app-api.salad.io/api/v1/profile/referral-code"

# Set the required parameter for webrequest
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36 Edg/92.0.902.84"
}

cookies = {
    # sIdRefreshToken is used to refresh the authentication token, it not needed for API requests unless you're trying to refresh the token.
    "sIdRefreshToken": "a",
    "sAccessToken": sAccessToken
}

# Get JSON response from API
profile = requests.get(url=profile_url, headers=headers, cookies=cookies)
selected_avatar = requests.get(url=selected_avatar_url, headers=headers, cookies=cookies)
xp = requests.get(url=xp_url, headers=headers, cookies=cookies)
balance = requests.get(url=balance_url, headers=headers, cookies=cookies)
referral_code = requests.get(url=referral_code_url, headers=headers, cookies=cookies)

# Output the response *nicely*
if profile.status_code != 200:
    print('It doesn\'t look like that was successful!')
else:
    # Convert from JSON to Python Dict
    profile_json = profile.json()
    selected_avatar_json = selected_avatar.json()
    xp_json = xp.json()
    balance_json = balance.json()
    referral_code_json = referral_code.json()
    
    print('It look like that was successful!')
    print(f"""
    Your username is {profile_json["username"]} and currently equipped '{selected_avatar_json["name"]}' as their avatar!

    Your lifetime balance is ${round(balance_json["lifetimeBalance"], 2)}
    Right now, your balance is ${round(balance_json["currentBalance"], 2)}!

    Your lifetime XP is {xp_json["lifetimeXp"]}
    That's means that you use Salad for {xp_json["lifetimeXp"]} minutes, that's about {round(xp_json["lifetimeXp"]/1440, 2)} days!
    
    Your referral code is {referral_code_json["code"]}
    """)

    # The output response was rounded up to 2 decimal points using 'round(value, 2)'