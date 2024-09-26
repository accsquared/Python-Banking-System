import os
import re
import pandas as pd
import pdfplumber

# Function to extract data from a PDF file
def extract_data(pdf_path):
    extracted_data = []  # List to hold all extracted data

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                # Create a dictionary to hold the extracted sections
                parameters = {
                    "Abstract": extract_section(text, "Abstract", "Introduction"),
                    "Introduction": extract_section(text, "Introduction", "Materials and Methods"),
                    "Materials and Methods": extract_section(text, "Materials and Methods", "Results and Discussion"),
                    "Results and Discussion": extract_section(text, "Results and Discussion", "Conclusion"),
                    "Conclusion": extract_section(text, "Conclusion", ""),
                }

                # Extract experiment data from the entire text
                parameters.update(extract_experiment_data(text))
                
                # Append the parameters for this page to the extracted data
                extracted_data.append(parameters)

    return extracted_data  # Return the list of dictionaries

# Function to extract a specific section of text based on headings
def extract_section(text, start_heading, end_heading):
    # Create a regex pattern to find the section
    pattern = rf"{re.escape(start_heading)}(.*?)(?={re.escape(end_heading)})"
    match = re.search(pattern, text, re.DOTALL | re.IGNORECASE)
    return match.group(1).strip() if match else ""

# Function to extract experiment data defined by key-value pairs
def extract_experiment_data(text):
    parameters = {}
    keys = [
        "Experiment ID", "Bacteria Type", "Bacteria Concentration (cells/mL)",
        "Encapsulation Method", "Nutrient Type", "Cement Type",
        "Water-Cement Ratio", "Sand/Cement Ratio", "Coarse Aggregate (kg)",
        "HRWR/Superplasticizer (kg)", "Fiber Content (kg)", "Curing Type",
        "Curing Duration (days)", "Initial Crack Width (mm)", "Final Crack Width (mm)",
        "Healing Time (days)", "Healing Conditions", "Healing Efficiency (%)",
        "Area Repair Rate (%)", "Anti-Seepage Repair Rate (%)", "Cracking Age (days)",
        "Water Permeability (L/m²/s)", "Microbial Survival Duration (days)"
    ]

    # Search each line for key-value pairs
    lines = text.split('\n')
    for line in lines:
        for key in keys:
            # Create a regex pattern to find "Key: Value"
            pattern = re.compile(rf'{re.escape(key)}:\s*(.+)', re.IGNORECASE)
            match = pattern.search(line)
            if match:
                parameters[key] = match.group(1).strip()  # Capture and strip whitespace

    return parameters

# Main function to execute the data extraction
def main():
    pdf_file = "/Users/achuilchoch/Downloads/2-data.pdf"  # Path to your PDF file
    data = extract_data(pdf_file)  # Extract data from the PDF
    
    # Create a DataFrame and save to an Excel file
    df = pd.DataFrame(data)
    df.to_excel("/Users/achuilchoch/Documents/output.xlsx", index=False)  # Adjust file path as needed

if __name__ == "__main__":
    main()