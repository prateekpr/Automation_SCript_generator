from backend.frameworks import selenium,appium,playwright

def generate_test_script(framework,test_cases):
    if framework=="Java Selenium":
        return selenium.scripts(test_cases)
    if framework=="Java Appium":
        return appium.scripts(test_cases)
    if framework=="Playwright typescript":
        return playwright.scripts(test_cases)
    else:
        return "Unsupported framework."