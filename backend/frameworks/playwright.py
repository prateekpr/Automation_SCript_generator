from helper.utils import generate_script
def scripts(test_cases):
    """Generate Playwright TypeScript test scripts."""
    prompt = f"Generate Playwright TypeScript test scripts for the following test cases:\n{test_cases}"
    return generate_script(prompt)