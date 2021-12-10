from app import take_screenshot

def run_script(driver, event):
    # Pass body parameter 'url' in API call
    driver.get(event["url"])
    
    # Return page title and a screenshot
    return_dict = {
        "title": driver.title,
        "screenshot": take_screenshot(driver)
    }

    return return_dict