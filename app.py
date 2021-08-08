from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from db_connection import save_to_db
from write_to_txt import save_to_txt_file

username = "TrendsProject1"
password = "trends_project1"
file_name = "trends.db"

profile = webdriver.FirefoxProfile()
profile.set_preference('intl.accept_languages', 'en-US, en')
browser = webdriver.Firefox(firefox_profile=profile)
actions = ActionChains(browser)

def sign_in_twitter(username, password):
    browser.get("https://twitter.com/login")
    sleep(4)

    username_input = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
    password_input = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")

    username_input.send_keys(username)
    password_input.send_keys(password)

    submit_btn = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div")
    submit_btn.click()

    sleep(2)


def find_country_trends(country_name):

    explore_btn = browser.find_element_by_xpath("//a[@data-testid='AppTabBar_Explore_Link']")
    explore_btn.click()                               
    sleep(2)

    setting_btn = browser.find_element_by_xpath("//a[@aria-label='Settings']")
    setting_btn.click()

    sleep(2)


    location_btn = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/a/div")
    location_btn.click()    

    sleep(2)

    search_place = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[1]/div/label/div[2]/div/input")
    search_place.send_keys(country_name)          
    search_place.click()

    sleep(2)

    select_country = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]")
    select_country.click()
    sleep(2)

    close_btn = browser.find_element_by_xpath("/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[1]/div/div/div/div[1]/div/div")
    close_btn.click()
    sleep(2)



    try:
        trending_btn = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div")
        trending_btn.click()

        sleep(2)
    except:
        show_more_btn = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div/section/div/div/div[10]/div/a")
        show_more_btn.click()
        sleep(2)

def take_trends():
        list = browser.find_elements_by_xpath("//div[@data-testid='trend']/div[1]/div[2]")

        result = []
        count_trend = 1
        count_space = 0
        cond = True
        while cond:
            if count_space > 7:
                break
            trend_list = browser.find_elements_by_xpath("//div[@data-testid='trend']/div[1]/div[2]")
            for item in trend_list:
                if item.text not in result:
                    result.append(item.text.strip("#"))
                    count_trend += 1
                    if count_trend == 21:
                        cond = False
                        break
            actions.send_keys(Keys.SPACE).perform()
            sleep(2)
            count_space += 1
        return result


def main(username,password,country_list):
    sign_in_twitter(username,password)
    result_dict = {}
    for country in country_list:
        find_country_trends(country)
        result = take_trends()
        result_dict[country] = result

    save_to_db(result_dict)
    save_to_txt_file(result_dict)




my_list = ["United States","Turkey","United Kingdom"]

main(username,password,my_list)