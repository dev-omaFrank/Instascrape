import csv
import selenium
import time
from selenium import webdriver
import selenium.common.exceptions
from selenium.common.exceptions import NoSuchElementException
import sys
from selenium.webdriver.common.action_chains import ActionChains
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

followers_data = []
follower_usernames = []
processed_count = 0



try:
    url = 'https://www.instagram.com/'
    username = 'enterinstagram username here'
    password = 'enter instagram account password'
    driverPath = chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    print(f'>> Opening {url} \n')
    driver.get(url)
    time.sleep(10.5)
except:
    error = sys.exc_info()[0]
    print(f'Error encountered: {error}')


try:
    username_input = driver.find_element(By.NAME, 'username')
    password_input = driver.find_element(By.NAME, 'password')

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_btn = driver.find_element(By.XPATH, '//button[@class="_acan _acap _acas _aj1-"]')
    login_btn.click()
    time.sleep(15)
    print(f'>> Enter OTP code')

    dont_save_login_info_btn = driver.find_element(By.XPATH, '//div[@class="_ac8f"]')
    dont_save_login_info_btn.click()
    time.sleep(7.5)
    print(f'>> Logging you in \n')

    dont_turn_on_notifications_btn = driver.find_element(By.XPATH, '//button[@class="_a9-- _a9_1"]')
    dont_turn_on_notifications_btn.click()
    time.sleep(7.5)
except:
    error = sys.exc_info()[0]
    print(f'Error encountered: {error}')


user_profile= driver.get(f'{url}{username}')
time.sleep(25)
total_followers = int(driver.find_element(By.CSS_SELECTOR, 'li.xl565be:nth-child(2) > a:nth-child(1) > span:nth-child(1) > span:nth-child(1)').text)
print(f'total followers: {total_followers}')
print(f'>> Opening followers page \n')

followers_page = driver.get(f'{url}{username}/followers/')
time.sleep(15.5)
followers_list = driver.find_element(By.XPATH, '//div[@class="_aano"]')
follower_list_div_width = followers_list.size['width']
follower_list_div_height = followers_list.size['height']
scroll_amount = follower_list_div_height
print(f'>> Getting followers... \n')


while True:
    try:
        driver.execute_script("arguments[0].scrollBy(0, arguments[1]);", followers_list, scroll_amount)
        time.sleep(2)

        follower_elements = followers_list.find_elements(By.XPATH, '//div[@class="x1i10hfl x1qjc9v5 xjbqb8w xjqpnuy xa49m3k xqeqjp1 x2hbi6w x13fuv20 xu3j5b3 x1q0q8m5 x26u7qi x972fbf xcfux6l x1qhh985 xm0m39n x9f619 x1ypdohk xdl72j9 x2lah0s xe8uvvx xdj266r x11i5rnm xat24cr x1mh8g0r x2lwn1j xeuugli xexx8yu x4uap5 x18d9i69 xkhd6sd x1n2onr6 x16tdsg8 x1hl2dhg xggy1nq x1ja2u2z x1t137rt x1q0g3np x87ps6o x1lku1pv x1a2a7pz xh8yej3 x193iq5w x1lliihq x1dm5mii x16mil14 xiojian x1yutycm"]')
        print('1')

        for element in follower_elements:
            processed_count += 1

            username_elements = element.find_elements(By.XPATH, './/div[@class="x9f619 xjbqb8w x1rg5ohu x168nmei x13lgxp2 x5pf9jr xo71vjh x1n2onr6 x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x6s0dn4 x1oa3qoh x1nhvcw1"]')
            name_elements = element.find_elements(By.XPATH, './/span[contains(@class, "x1lliihq") and contains(@class, "x193iq5w") and contains(@class, "x6ikm8r") and contains(@class, "x10wlt62") and contains(@class, "xlyipyv") and contains(@class, "xuxw1ft")]')

            for username_element, name_element in zip(username_elements, name_elements):
                follower_username = username_element.text
                follower_name = name_element.text
                print(follower_username + ','+ follower_name + '\n')

                if 'Follow' in name_element.text or 'Suggested' in name_element.text or 'Verified' in name_element.text:
                    follower_name = ''

                if follower_name != '':
                    start_index = 0
                    follower_usernames.append(follower_username)
                    print(follower_usernames)
                    if followers_data:
                        last_processed_element = followers_data[-1]
                        start_index = int(last_processed_element.split(',')[0].split(':')[1].strip()) + 1

                    for index, follower_username in enumerate(follower_usernames[start_index]):
                        url_for_bio_data = f'https://www.instagram.com/{follower_username}/'
                        print(f'>> Navigating to {follower_username} page \n')
                        driver.execute_script(f"window.open('{url_for_bio_data}', '_blank');")
                        window_handles = driver.window_handles
                        driver.switch_to.window(window_handles[-1])
                        time.sleep(15)

                        try:
                            name_element = driver.find_element(By.XPATH, '//span[@class="_aacl _aaco _aacw _aacx _aad7 _aade"]')
                            name_data = name_element.text
                            print(f'>> Getting {follower_username} name data')
                            print(name_data)
                        except NoSuchElementException:
                            print(f'>> Name data not found for {follower_username} \n')
                            name_data = f'No name data found for {follower_username}'
                            pass
                        except selenium.common.exceptions.StaleElementReferenceException:
                            print(f'>> Stale element reference for {follower_username}, skipping iteration.\n')
                            pass
                        except selenium.common.exceptions.JavascriptException:
                            error = sys.exc_info()[0]
                            print(f'Error encountered: {error}')

                        try:
                            bio_data_element = driver.find_element(By.XPATH, '//h1[@class="_aacl _aaco _aacu _aacx _aad6 _aade"]')
                            bio_data = bio_data_element.text
                            print(f'>> Getting {follower_username} bio data \n')
                            print(bio_data)
                        except NoSuchElementException:
                            print(f'>> Bio data not found for {follower_username} \n')
                            bio_data = f'No bio data found for {follower_username}'
                            pass

                        followers_data.append(f'Index: {index}, Username: {follower_username}, bio data: {bio_data}, name: {name_data} \n')
                        driver.close()
                        driver.switch_to.window(window_handles[0])

        if len(follower_usernames) == 3:
            break

    except AttributeError:
        bio_data = f'No bio data found for {follower_username}'
        pass

    except Exception as e:
        if "arguments[0].scrollBy is not a function" in str(e):
            # Handle the specific JavaScript exception when scrolling reaches the end
            print("Reached the end of the div.")
            break
        else:
            # Handle other exceptions
            print("An error occurred:", str(e))
            print(f'Successfully retrieved {len(followers_data)} followers data')
            break

    except:
        error = sys.exc_info()[0]
        print(f'Error encountered: {error}')

with open('instascrape.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    for data in followers_data:
        writer.writerow([data])
    writer.writerow([f'{len(followers_data)} followers data retrieved'])

driver.quit()

quit_command = input('>> Enter QUIT to close the browser...')
if quit_command.upper() == 'QUIT':
    print('>> Program execution complete')
    driver.quit()
