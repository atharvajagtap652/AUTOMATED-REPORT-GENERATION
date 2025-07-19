import csv
from fpdf import FPDF

# Step 1: Read data and calculate averages
def read_data(file_name):
    students = []
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # Calculate average marks
            total = int(row["Maths"]) + int(row["Science"]) + int(row["English"])
            average = round(total / 3, 2)
            row["Average"] = average
            students.append(row)
    return students

# Step 2: Generate PDF report
def generate_pdf(data, output_file):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, "Student Performance Report", ln=True, align='C')
    pdf.ln(10)  # Add space after title

    pdf.set_font("Arial", size=12)
    for student in data:
        line = f'{student["Name"]} | Maths: {student["Maths"]} | Science: {student["Science"]} | English: {student["English"]} | Average: {student["Average"]}'
        pdf.cell(200, 10, line, ln=True)

    pdf.output(output_file)
    print("PDF Report Generated Successfully!")

# Step 3: Main Program Execution
data = read_data("student_data.csv")
generate_pdf(data, "student_report.pdf")
