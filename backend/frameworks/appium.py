from helper.utils import generate_script
def scripts(test_cases):
    """Generate Java Appium test scripts."""
    prompt = f"Generate Java Appium test scripts for the following test cases:\n{test_cases}"
    return generate_script(prompt)
