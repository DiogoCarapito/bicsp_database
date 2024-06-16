from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import sqlite3
import time
import logging


def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )

    # Correct initialization using Chrome as an example
    service = Service(ChromeDriverManager().install())
    logging.info("Service created")
    driver = webdriver.Chrome(service=service)
    logging.info("Driver created")

    try:
        # Navigate to the Power BI report URL
        driver.get(
            "https://bicsp.min-saude.pt/pt/contratualizacao/ide/Paginas/default.aspx"
        )
        logging.info("Navigated to the URL")

        # Updated element locator using data-automation-id
        where_to_click = "//li[@data-automation-id='carousel_section']"

        # Use explicit wait to wait for the element to be clickable
        # element_to_click = WebDriverWait(driver, 20).until(
        #     EC.element_to_be_clickable((By.XPATH, where_to_click))
        # )
        # logging.info("Element to click found")
        time.sleep(12)

        # Click the element
        driver.execute_script(
            "arguments[0].click();", driver.find_element(By.XPATH, where_to_click)
        )
        logging.info("Clicked on the element successfully")

        # Keep the window open for debugging
        time.sleep(20)
        logging.info("waited for 20 seconds")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
    finally:
        # Optionally, keep the browser open for inspection or close it
        driver.quit()
        logging.info("Browser closed")

    # # Wait for elements to load (example)
    # time.sleep(10)  # It's better to use explicit waits

    # #clck in a lower tab on the power bi report
    # driver.find_element(By.XPATH, '/html/body/div[3]/report-embed/div/div/div[1]/div/div/div/exploration-container/div/div/docking-container/div/div/div/div/exploration-host/div/div/exploration-footer-modern/div/ul/carousel/div/div[2]/li[2]/exploration-navigation-tab/div').click()

    # time.sleep(20)  # It's better to use explicit waits

    # Interact with elements
    # driver.find_element(By.ID, 'input-text-id').send_keys('Some text')
    # driver.find_element(By.ID, 'dropdown-id').click()
    # driver.find_element(By.XPATH, '//option[text()="Option Text"]').click()

    # # Extract data (example)
    # extracted_data = driver.find_element(By.ID, 'data-element-id').text

    # print(extracted_data)

    # Process and store data in SQLite (simplified example)
    # conn = sqlite3.connect('example.db')
    # c = conn.cursor()
    # c.execute('''CREATE TABLE IF NOT EXISTS data (extracted_text TEXT)''')
    # c.execute('''INSERT INTO data (extracted_text) VALUES (?)''', (extracted_data,))
    # conn.commit()
    # conn.close()

    return None


if __name__ == "__main__":
    main()
