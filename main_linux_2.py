import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re

logging.basicConfig(filename='indiamart_bot_v6_2.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logger = logging.getLogger('indiamart_bot_v6_2')
service = Service('/usr/local/bin/chromedriver')
# service = Service(r"C:\Chrome Driver\chromedriver-win64\chromedriver.exe")
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--incognito')
chrome_options.add_argument('--start-maximized')
chrome_options.add_argument('--disable-dev-shm-usage')

prefs = {
    'safebrowsing.enabled': True
}

def extract_max_integer(item):
    digits = re.findall(r'\d+', item)
    if digits:
        return max(map(int, digits))
    else:
        return 0

def login():
    logger.info('Opening safebrowsing')
    driver = webdriver.Chrome(service=service,options=chrome_options)
    # driver.get('https://seller.indiamart.com/')
    driver.get('https://seller.indiamart.com/bltxn/?pref=relevant')
    user_id = driver.find_element(By.XPATH, '//*[@id="user_sign_in"]')
    user_id.click()
    mobile = driver.find_element(By.XPATH, '//*[@id="mobile"]')
    mobile.click()
    mobile.clear()
    mobile.send_keys("9814214344")
    mob_submit = driver.find_element(By.XPATH, '//*[@id="logintoidentify"]')
    mob_submit.click()

# Changes of new code: Start: ======================================
    try:
        time.sleep(5)
        sec_mob = driver.find_element(By.XPATH, '//*[@id="mobNo"]')
        sec_mob.click()
        time.sleep(2)
        sec_mob.clear()
        sec_mob.send_keys("9814214344")
        login_btn_mob = driver.find_element(By.XPATH, '//button[@class="login_btn"]')
        login_btn_mob.click()
    except Exception as err:
        print(f'Error is : {str(err)}')
        pass
# Changes of new code: End: ======================================

    time.sleep(5)
    try:
        enter_pass = driver.find_element(By.XPATH, '//*[@id="passwordbtn1"]')
        enter_pass.click()
        time.sleep(2)
        enter_pass_txt = driver.find_element(By.XPATH, '//*[@id="usr_password"]')
        enter_pass_txt.click()
        time.sleep(2)
        enter_pass_txt.clear()
        enter_pass_txt.click()
        time.sleep(2)
        enter_pass_txt.send_keys('Indiamart@trio')

        submit_btn = driver.find_element(By.XPATH, '//*[@id="signWP"]')
        submit_btn.click()
    except Exception as err:
        print(f'Error2 is : {str(err)}')
        pass
    return driver

def main(driver, key_words, qnty):
    buy_leads = driver.find_element(By.XPATH, '//*[@id="lead_cen"]/a')
    buy_leads.click()
    time.sleep(10)

# Changes of new code: Start: ======================================
    try:
        recent_leads = driver.find_element(By.XPATH, "//*[text()='Recent Leads']")
        recent_leads.click()
    except:
        pass
# Changes of new code: End: ======================================
    try:
        allow_buy_leads = driver.find_element(By.XPATH, '//*[@id="optInText"]')
        logger.info('Allow detected')
    except:
        allow_buy_leads = None
        logger.info('Allow not detected')

    if allow_buy_leads:
        allow_buy_leads.click()
        logger.info('Allow clicked')

    buy_leads = driver.find_element(By.XPATH, '//*[@id="lead_cen"]/a')
    buy_leads.click()

    # Changes of new code: Start: ======================================
    try:
        recent_leads = driver.find_element(By.XPATH, "//*[text()='Recent Leads']")
        recent_leads.click()
    except:
        pass
    # Changes of new code: End: ======================================

    states = ["andhra pradesh", "arunachal pradesh", "assam", "bihar", "chhattisgarh", "goa", "gujarat", "haryana", "himachal pradesh", "jharkhand", "karnataka", "kerala", "madhya pradesh", "maharashtra", "manipur", "meghalaya", "mizoram", "nagaland", "odisha", "punjab", "rajasthan", "sikkim", "tamil nadu", "telangana", "tripura", "uttar pradesh", "uttarakhand", "west bengal", "andaman and nicobar islands", "chandigarh", "dadra and nagar haveli and daman and diu", "delhi", "jammu and kashmir", "ladakh", "lakshadweep", "puducherry" ]

    try:
        search_key_words = driver.find_element(By.XPATH, '//*[@id="search_string"]')
        search_key_words.click()
        search_key_words.clear()
        search_key_words.send_keys(key_words)
        search_key_words_enter = driver.find_element(By.XPATH, '//*[@id="btnSearch"]')
        search_key_words_enter.click()
        logger.info(f"Search for the '{key_words}'")
        time.sleep(10)
        try:
            suggest = driver.find_element(By.XPATH, "//span[@class='glob_sa_close']")
            suggest.click()
        except:
            pass

        driver.execute_script("window.scrollBy(0, 2000000000000000);")
        logger.info("scroll to the end (2000000000000000 times) ")
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
        c = 0
        for xpath, lead in leads_xpaths.items():
            print(xpath)

            new_key_dict = {
                'fire resistant doors': ['Fire Doors','Fire Resistant Metal Door','Fire Emergency Door','Hours Fire Resistant Doors',
                                         'GI Fire Proof Resistant Door','Color Coated','Fire Resistant Safety Door','Fire Shaft Door',
                                         'Emergency Exit Door','Fire Protection Door'],
                'lead lined doors':['Lead Lined Door','Hospital Operation Theater Door','Hospital MS Door','Xray room Door',
                                    'Hospital OT Doors'],
                'ot doors':['Lead Lined Door','Hospital Operation Theater Door','Hospital MS Door','X-ray room Door',
                            'Hospital OT Doors'],
                'aluminium coving':['aluminium coving'],
                'modular cleanroom doors':['MS Powder Coated Fire Proof Door','Powder Coated Clean Room Service',
                                           'Clean Room Partition','Modular Cleanroom Door','Cleanroom Penal',
                                           'Gi Modular Clean Room Door'],
                'pvc coving':['pvc coving'],
                'emergency exit doors':['emergency exit doors'],
                'drop seal':['drop seal']
            }

            if any('Quantity' in item and extract_max_integer(item) >= qnty for item in lead) and\
                    any(any(state.lower() in item.lower() for state in states) for item in lead[:4]) \
                    and any(any(word.lower() in key.lower() for word in new_key_dict[key_words]) for key in lead):
                logger.info(f'Lead data:\n{lead}')
                logger.info(f'Quantity in the leads is more than {qnty-1}')
                c+=1
                try:
                    cont_xpath = xpath.replace('/div[1]', '')
                    cont_buyer_xpath = f'{cont_xpath}/div[3]/div[2]/div/span'
                    contact_buyer = driver.find_element(By.XPATH, cont_buyer_xpath)
                    actions = ActionChains(driver)
                    actions.move_to_element(driver.find_element(By.XPATH, cont_buyer_xpath)).perform()
                    driver.execute_script("window.scrollBy(0, 200);")
                    contact_buyer.click()
                    logger.info(f"Lead XPATH: {xpath} and contact XPATH: {cont_buyer_xpath}")
                except:
                    cont_xpath = xpath.replace('/div[1]', '')
                    cont_buyer_xpath = f"{cont_xpath}//span[contains(text(),'Contact Buyer Now')]/ancestor::div[1]"
                    contact_buyer = driver.find_element(By.XPATH, cont_buyer_xpath)
                    actions = ActionChains(driver)
                    actions.move_to_element(driver.find_element(By.XPATH, cont_buyer_xpath)).perform()
                    driver.execute_script("window.scrollBy(0, 200);")
                    contact_buyer.click()
                    logger.info(f"Lead XPATH: {xpath} and contact XPATH: {cont_buyer_xpath}")

                try:
                    send_reply = driver.find_element(By.XPATH, "//*[text()='Send Reply']")
                    send_reply.click()
                    logger.info('Clicked on send reply')
                    try:
                        element_or_outer_popup = driver.find_element(By.XPATH, '//*[@id="cls_btn"]')
                        element_or_outer_popup.click()
                        logger.info('Closeing the popup')
                        pass
                    except:
                        logger.info('Unable to close the popup')
                        pass
                except:
                    send_reply = None
                    logger.info('Unable to click on send reply')
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
        logger.info(f'Error at main function, Error: {str(err)}')


def run_bot():
    keywords_list = ['ot doors', 'pvc coving', 'panic bar', 'emergency exit doors', 'drop seal']
    quantities_list = [2, 500, 10, 5, 20]
    driver = login()
    logger.info('Log in to indiamart portal')
    time.sleep(5)
    for i in range(1,151):
        logger.info(f"Main cycle no: '{i}'")
        print(f"Main cycle no: '{i}'")
        for keywords, quantities in zip(keywords_list, quantities_list):
            print(keywords)
            time.sleep(10)
            main(driver=driver, key_words=keywords, qnty=quantities)
        time.sleep(60)
    try:
        try:
            driver.close()
        except:
            driver.quit()
    except:
        pass


while True:
    try:
        run_bot()
    except Exception as er:
        logger.info(str(er))
        print('Please check logger')
