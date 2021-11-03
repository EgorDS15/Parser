import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


def yt_parser(link="https://www.youtube.com/watch?v=kuhhT_cBtFU&t=2s", drvrpath=r'files/chromedriver.exe', n_iter=10):
    data = []
    # So here is how it works:
    with Chrome(executable_path=drvrpath) as driver:
        wait = WebDriverWait(driver, 15)
        # Access the URL you want with the driver.get function.
        driver.get(link)

        # Scroll down and wait until everything is visible with wait.until and EC.visibility_of_element_located.
        for item in range(n_iter):
            wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body"))).send_keys(Keys.END)
            time.sleep(15)

        # Scrape the comments by finding all the #content-text elements (which is what we want, as you can see below)
        # in the current viewed page.
        for comment in wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#content"))):
            # Append the comments to the data list.
            data.append(comment.text)

        df = pd.DataFrame(data, columns=['comment'])
        return df


if __name__ == '__main__':
    print(yt_parser(link='https://www.youtube.com/watch?v=4LLcaaK_iA4'))