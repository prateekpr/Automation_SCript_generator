from helper.utils import generate_script
def scripts(test_cases):
  prompt = f"Generate Java Selenium test scripts for the following test cases:\n{test_cases}"
  return generate_script(prompt)