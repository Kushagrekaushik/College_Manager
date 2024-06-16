import os
from fpdf import FPDF
company="Thapar University"
address="Patiala"


class my_cust_PDF(FPDF):
    def header(self):
        self.set_text_color(121, 46, 166)
        self.set_font('Helvetica', 'B', 20)
        w = self.get_string_width(company) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 10, company)
        self.ln(15)

        self.set_font('Helvetica', 'B', 12)
        w = self.get_string_width(address) + 6
        self.set_x((210 - w) / 2)
        self.cell(w, 10, address)
        self.ln(10)



        self.ln(20)

    def footer(self):

        self.set_y(-15)

        self.set_font('Arial', 'I', 8)

        self.set_text_color(128)

        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

    def chapter_content(self,data,headings,total_cols):
        self.set_fill_color(200, 220, 255)
        self.ln()
        self.ln()


        self.set_font('Arial', 'B', 11)
        spacing=1
        col_width = self.w /(total_cols+1)
        row_height = self.font_size+2



        for i in headings:
            self.cell(col_width, row_height * spacing, txt=i, border=1)
        self.ln(row_height * spacing)


        self.set_font('Arial', '', 11)
        for row in data:
            for item in row:
                self.cell(col_width, row_height * spacing, txt=str(item), border=1)
            self.ln(row_height * spacing)


        self.ln()



        self.ln()
        self.ln()
        self.ln()
        self.set_font('', 'I')
        text1 = '(---------------------  end of page  -----------------------)'
        w = self.get_string_width(text1) + 6
        self.set_x((210 - w) / 2)
        self.cell(0, 6, text1)

    def print_chapter(self,data,headings,total):
        self.add_page()
        self.chapter_content(data,headings,total)

if __name__ == '__main__':
    pdf = my_cust_PDF()
    data=[['Rollno','Name','Gender','Phone No','Address','Department','Course','DOB'],
          ['Rollno','Name','Gender','Phone No','Address','Department','Course','DOB'],
          ['Rollno','Name','Gender','Phone No','Address','Department','Course','DOB']]

    headings = ['Rollno', 'Name', 'Gender', 'Phone No', 'Address', 'Department', 'Course', 'DOB']
    pdf.print_chapter(data,headings,8)
    pdf.output('pdf_file1.pdf')
    os.system('explorer.exe "pdf_file1.pdf"')