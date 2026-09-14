import os
import re

def extract_emails():
    input_file = "input_text.txt"
    output_file = "extracted_emails.txt"

    print("==========================================")
    print("   CodeAlpha Task Automation: Email Extractor")
    print("==========================================\n")

    # 1. Automatically create a sample input file if it doesn't exist
    if not os.path.exists(input_file):
        sample_text = (
            "Hello team,\n"
            "Please reach out to support@codealpha.tech for general inquiries.\n"
            "For technical issues, contact john.doe@techcorp.org or admin_123@domain.net.\n"
            "Thanks,\nHR Team (hr@company.co.uk)\n"
        )
        with open(input_file, "w") as file:
            file.write(sample_text)
        print(f"Sample file created: '{input_file}'\n")

    # 2. Read input file
    with open(input_file, "r") as file:
        content = file.read()

    # 3. Regular expression to find email patterns
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    found_emails = re.findall(email_pattern, content)

    # Remove duplicate emails while preserving order
    unique_emails = list(dict.fromkeys(found_emails))

    # 4. Save extracted emails to output file
    with open(output_file, "w") as file:
        for email in unique_emails:
            file.write(email + "\n")

    print(f"Extraction complete! Found {len(unique_emails)} email address(es):")
    for email in unique_emails:
        print(f" - {email}")

    print(f"\nExtracted list successfully saved to '{output_file}'.")

if __name__ == "__main__":
    extract_emails()