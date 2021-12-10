from app import take_screenshot

def run_script(driver, event):
    try:
        # Navigate to bot.silverlining.cloud
        driver.get("https://bot.silverlining.cloud")

        # Scroll down to browser size frame
        element = driver.find_element_by_xpath("//div[@id='size']")
        driver.execute_script("arguments[0].scrollIntoView(true);", element)

        # Take first screenshot
        screenshot_url1 = take_screenshot(driver)

        # Click on 'Visit SilverLining.cloud'
        driver.find_element_by_xpath("//a[@id='visit']").click()

        # Take second screenshot
        screenshot_url2 = take_screenshot(driver)
        
        # Return Screenshot URLs
        return_dict = {
            "screenshot_url1": screenshot_url1,
            "screenshot_url2": screenshot_url2
        }

        return return_dict

    except Exception as e:
        return_dict = {
            "error": str(e)
        }
        return return_dict
