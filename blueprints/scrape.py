from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.chrome.service import Service
import time
import base64

def scrape_img(url):
    chromedriver_path = r"D:\GenFolder\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    chrome_options = Options()
    headless = True
    # Function to set headless mode
    def set_headless(opt, value=True):
        if value:
            opt.add_argument('--headless')
        else:
            # Remove headless if present
            try:
                opt.arguments.remove('--headless')
            except ValueError:
                pass
    set_headless(chrome_options, True)
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--enable-unsafe-webgpu')
    chrome_options.add_argument('--enable-unsafe-swiftshader')
    
    
    # Set a common user-agent to mimic a real browser
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.7151.69 Safari/537.36')
    try:
        service = Service(executable_path=chromedriver_path)
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(url)
        time.sleep(3)
        
        # screenshot selected div elements
        try:
            # Close sfo_close element if present
            try:
                sfo_close = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'sfo_close'))
                )
                sfo_close.click()
                time.sleep(1)  # Give time for modal to close
            except Exception:
                pass
            # Close popup if present using provided XPath
            try:
                popup_close = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div/div[2]/div/span'))
                )
                popup_close.click()
                time.sleep(1)  # Give time for modal to close
            except Exception:
                pass
            
            try:
                popup_close = WebDriverWait(driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="module_age-restriction"]/div/div/div[3]/div[1]'))
                )
                popup_close.click()
                time.sleep(1)  # Give time for modal to close
            except Exception:
                pass
            
            # Find the product detail block
            product_detail = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.pdp-block.pdp-block__product-detail#block-NCWbFy4YCZ7'))
            )
            # Remove unwanted block if present
            try:
                unwanted1 = product_detail.find_element(By.CSS_SELECTOR, 'div.pdp-block.module#module_quantity-input')
                driver.execute_script('arguments[0].parentNode.removeChild(arguments[0]);', unwanted1)
            except Exception:
                pass
            try:
                unwanted2 = product_detail.find_element(By.CSS_SELECTOR, 'div.pdp-block.module#module_add_to_cart')
                driver.execute_script('arguments[0].parentNode.removeChild(arguments[0]);', unwanted2)
            except Exception:
                pass
            
            try:
                unwanted3 = product_detail.find_element(By.CSS_SELECTOR, 'div.pdp-mod-product-info-section.sku-prop-selection')
                driver.execute_script('arguments[0].parentNode.removeChild(arguments[0]);', unwanted3)
            except Exception:
                pass
            
            # Find the gallery block (updated selector)
            gallery = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div.pdp-block.module#module_item_gallery_1'))
            )
            # Take screenshots of both elements
            product_detail_b64 = base64.b64encode(product_detail.screenshot_as_png).decode('utf-8')
            gallery_b64 = base64.b64encode(gallery.screenshot_as_png).decode('utf-8')
            driver.quit()  # comment to keep browser open for debugging
            return {'product_detail_b64': product_detail_b64, 'gallery_b64': gallery_b64}

        except TimeoutException:
            driver.quit()  # comment to keep browser open for debugging
            return {'product_detail_b64': None, 'gallery_b64': None}
        
    except WebDriverException as e:
        return f"WebDriver error: {str(e)}"
    except Exception as e:
        return f"Error: An unexpected error occurred. Reason: {str(e)}"
    
def scrape_rev(url):
    # Placeholder for review scraping logic
    # This function should implement the logic to scrape reviews from the given URL
    # For now, it returns a dummy value
    
    reviews = []
    
    for i in range(1, 6):
        reviews.append(f'Review {i}')

    return reviews