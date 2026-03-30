from selenium import webdriver



def before_all(context):
    # This will run before all scenarios
    print("===Test Execution started===")
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    
    
def after_all(context):
    # This will run after all scenarios
    print("===Test Execution completed===", flush=True)
    context.driver.quit()
    
def before_scenario(context, scenario):
    print(f"---Starting scenario: {scenario.name}---")       
    context.driver.get("https://www.wikipedia.org/")
    
def after_scenario(context, scenario):
    print(f"---Finished scenario: {scenario.name}---")    
    if scenario.status == "failed":
        filename = scenario.name.replace(" ", "_") + ".png"
        context.driver.save_screenshot(filename)
        print(f"Screenshot saved for failed scenario: {filename}")