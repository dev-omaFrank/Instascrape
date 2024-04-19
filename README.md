
---

# InstaScrape

## Overview

InstaScrape is a Python-based bot designed to log into a user's Instagram account, retrieve a list of their followers, and save the data to a CSV file. This project utilizes Selenium for web automation and ChromeDriver as the WebDriver for controlling the Chrome browser. Additionally, other Python libraries are used to handle data processing and file I/O.

## Features

- **Automated Login**: InstaScrape automates the login process to access the user's Instagram account securely.
- **Follower Retrieval**: The bot fetches the list of followers for the specified user.
- **Data Export**: InstaScrape exports the follower data to a CSV file for further analysis or storage.
- **Customizable**: The bot can be easily extended or modified to suit specific requirements or additional functionalities.

## Technologies Used

- **Selenium**: Used for web automation to interact with the Instagram website.
- **ChromeDriver**: Provides the interface for controlling the Chrome browser during automation.
- **Python Libraries**: Various Python libraries are used for data processing, CSV handling, and other functionalities.

## Usage

1. **Clone the Repository**: Clone the InstaScrape repository to your local machine.
   ```bash
   git clone https://github.com/dev-omaFrank/Instascrape
   ```

2. **Install Dependencies**: Navigate to the project directory and install the required Python dependencies using pip.
   ```bash
   cd InstaScrape
   pip install -r requirements.txt
   ```

3. **Set Up ChromeDriver**: Download the appropriate ChromeDriver executable for your Chrome browser version and place it in the project directory.

4. **Configure Credentials**: Open the `config.py` file and provide your Instagram username and password.

5. **Run the Bot**: Execute the main Python script to run the InstaScrape bot.
   ```bash
   python instascrape.py
   ```

6. **Check Output**: Once the bot completes execution, check the generated CSV file in the project directory containing the follower data.

## Beneficial Use Cases

InstaScrape can be beneficial in various scenarios, including:

- **Social Media Analytics**: Analyzing follower demographics and engagement.
- **Influencer Marketing**: Identifying potential influencers based on follower count and engagement.
- **Audience Insight**: Understanding the interests and preferences of a user's followers.
- **Data Backup**: Creating backups of follower lists for account management or archival purposes.

## Disclaimer

It's important to use InstaScrape responsibly and in compliance with Instagram's terms of service. Automated interactions with social media platforms may be subject to restrictions or limitations, and misuse could result in account suspension or other consequences.

---
