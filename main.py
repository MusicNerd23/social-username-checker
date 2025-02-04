#OSINT USERNAME CHECKER v1.0
import requests 

#get username input
username = input("Enter a username to check: ").strip()

#list of social media sites 
websites = {
    # Social Media
    "Facebook": f"https://www.facebook.com/{username}",
    "Instagram": f"https://www.instagram.com/{username}/",
    "Twitter": f"https://twitter.com/{username}",
    "TikTok": f"https://www.tiktok.com/@{username}",
    "Snapchat": f"https://www.snapchat.com/add/{username}",
    "LinkedIn": f"https://www.linkedin.com/in/{username}",
    "Pinterest": f"https://www.pinterest.com/{username}",
    "Reddit": f"https://www.reddit.com/user/{username}",
    "Medium": f"https://medium.com/@{username}",
    "WordPress": f"https://{username}.wordpress.com",
    
    # Video & Streaming
    "YouTube": f"https://www.youtube.com/{username}",
    "Twitch": f"https://www.twitch.tv/{username}",
    "Vimeo": f"https://vimeo.com/{username}",
    "Dailymotion": f"https://www.dailymotion.com/{username}",
    
    # Gaming Platforms
    "Steam": f"https://steamcommunity.com/id/{username}",
    "Xbox Live": f"https://account.xbox.com/en-us/Profile?gamerTag={username}",
    "Roblox": f"https://www.roblox.com/user.aspx?username={username}",
    "Minecraft (NameMC)": f"https://namemc.com/profile/{username}",
    
    # Developer & Tech Sites
    "GitHub": f"https://github.com/{username}",
    "GitLab": f"https://gitlab.com/{username}",
    "Stack Overflow": f"https://stackoverflow.com/users/{username}",
    "Replit": f"https://replit.com/@{username}",
    "DeviantArt": f"https://www.deviantart.com/{username}",
    
    # Other Services
    "Ebay": f"https://www.ebay.com/usr/{username}",
    "Spotify": f"https://open.spotify.com/user/{username}",
    "Kickstarter": f"https://www.kickstarter.com/profile/{username}",
    "Flickr": f"https://www.flickr.com/people/{username}"
}

#check to see if the username exists on each site
print("\n🔎 Checking username availability...\n")


for site, url in websites.items():
    try:
        response = requests.get(url)

        if response.status_code == 200:
            print(f"✅ {site}: Username **exists** 👉 {url}")
        elif response.status_code == 404:
            print(f"❌ {site}: Username **not found**")
        else:
            print(f"⁉️ {site}: Unknown repsonse ({response.status_code})")
    except requests.exceptions.RequestException:
        print(f"‼️ {site}: Could not connect")