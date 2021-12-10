from app import take_screenshot
import time

def run_script(driver, event):
    try:
        # Homepage loading time
        start_time = time.time()
        driver.get("https://silverlining.cloud")
        end_time = time.time()
        load_time_homepage = end_time - start_time

        # Product page loading time
        start_time = time.time()
        driver.get("https://silverlining.cloud/products")
        end_time = time.time()
        load_time_product = end_time - start_time
        
        # Return loading times
        return_dict = {
            "load_time_homepage": load_time_homepage,
            "load_time_product": load_time_product
        }

        return return_dict

    except Exception as e:
        return_dict = {
            "error": str(e)
        }
        return return_dict
