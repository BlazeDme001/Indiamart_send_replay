from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-dev-shm-usage')

prefs = {
    'safebrowsing.enabled': True
}

def login():
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://seller.indiamart.com/')
    driver.get('https://seller.indiamart.com/bltxn/?pref=relevant')
    user_id = driver.find_element(By.XPATH, '//*[@id="user_sign_in"]')
    user_id.click()
    mobile = driver.find_element(By.XPATH, '//*[@id="mobile"]')
    mobile.click()
    mobile.clear()
    mobile.send_keys("9814214344")
    mob_submit = driver.find_element(By.XPATH, '//*[@id="logintoidentify"]')
    mob_submit.click()
    return driver

def main(key_words, qnty):
    driver = login()
    time.sleep(5)

    enter_pass = driver.find_element(By.XPATH, '//*[@id="passwordbtn1"]')
    enter_pass.click()
    enter_pass_txt = driver.find_element(By.XPATH, '//*[@id="usr_password"]')
    enter_pass_txt.click()
    enter_pass_txt.clear()
    enter_pass_txt.click()
    time.sleep(2)
    enter_pass_txt.send_keys('Indiamart@trio')

    submit_btn = driver.find_element(By.XPATH, '//*[@id="signWP"]')
    submit_btn.click()

    buy_leads = driver.find_element(By.XPATH, '//*[@id="lead_cen"]/a')
    buy_leads.click()
    time.sleep(10)

    try:
        allow_buy_leads = driver.find_element(By.XPATH, '//*[@id="optInText"]')
    except:
        allow_buy_leads = None

    if allow_buy_leads:
        allow_buy_leads.click()

    buy_leads = driver.find_element(By.XPATH, '//*[@id="lead_cen"]/a')
    buy_leads.click()

    states = ["andhra pradesh", "arunachal pradesh", "assam", "bihar", "chhattisgarh", "goa", "gujarat", "haryana", "himachal pradesh", "jharkhand", "karnataka", "kerala", "madhya pradesh", "maharashtra", "manipur", "meghalaya", "mizoram", "nagaland", "odisha", "punjab", "rajasthan", "sikkim", "tamil nadu", "telangana", "tripura", "uttar pradesh", "uttarakhand", "west bengal", "andaman and nicobar islands", "chandigarh", "dadra and nagar haveli and daman and diu", "delhi", "jammu and kashmir", "ladakh", "lakshadweep", "puducherry" ]

    try:
        search_key_words = driver.find_element(By.XPATH, '//*[@id="search_string"]')
        search_key_words.click()
        search_key_words.clear()
        search_key_words.send_keys(key_words)
        search_key_words_enter = driver.find_element(By.XPATH, '//*[@id="btnSearch"]')
        search_key_words_enter.click()

        time.sleep(10)
        try:
            suggest = driver.find_element(By.XPATH, "//span[@class='glob_sa_close']")
            suggest.click()
        except:
            pass

        driver.execute_script("window.scrollBy(0, 2000000000000000);")
        time.sleep(5)
        driver.execute_script("window.scrollTo(0,0);")
        time.sleep(2)
        leads = driver.find_elements(By.XPATH, '//*[@id="bl_listing"]')
        leads_list = []
        for l_txt in leads:
            leads_list.append(l_txt.text)
        count = leads_list[0].lower().count("contact buyer now")

        leads_xpaths = {}

        for j in range(1, count+1):
            lead_cur_xpath = f'//*[@id="list{j}"]/div[1]'
            lead_data = driver.find_element(By.XPATH, lead_cur_xpath).text
            leads_xpaths[lead_cur_xpath] = lead_data.split('\n')

        for xpath, lead in leads_xpaths.items():
            if any('Quantity' in item and int(''.join(filter(str.isdigit, item))) >= qnty for item in lead) and\
                    any(any(state.lower() in item.lower() for state in states) for item in lead):
                cont_xpath = xpath.replace('/div[1]', '')
                cont_buyer_xpath = f"{cont_xpath}//span[contains(text(),'Contact Buyer Now')]/ancestor::div[1]"
                contact_buyer = driver.find_element(By.XPATH, cont_buyer_xpath)
                actions = ActionChains(driver)
                actions.move_to_element(driver.find_element(By.XPATH, cont_buyer_xpath)).perform()
                driver.execute_script("window.scrollBy(0, 200);")
                contact_buyer.click()
                try:
                    send_reply = driver.find_element(By.XPATH, "//*[text()='Send Reply']")
                    send_reply.click()
                    try:
                        # outer_popup = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, '//*[@id="sourcediv11"]')))
                        element_or_outer_popup = driver.find_element(By.XPATH, '//*[@id="cls_btn"]')
                        element_or_outer_popup.click()
                        print('closed pop up')
                        pass
                    except:
                        pass
                except:
                    send_reply = None
                if send_reply:
                    time.sleep(10)
                    try:
                        popup = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "rr_outer")))
                        element_inside_popup = popup.find_element(By.XPATH, "//div[@id='rr_outer']/div[1]")
                        element_inside_popup.click()
                        popup_2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="innerPopup_suggested_BL"]/span')))
                        element_inside_popup_2 = popup_2.find_element(By.XPATH, '//*[@id="innerPopup_suggested_BL"]/span')
                        element_inside_popup_2.click()
                    except:
                        pass

    except Exception as err:
        print(str(err))

def run_bot(key_words, qnty):
    main(key_words, qnty)
