import os
import uuid
from fpdf import FPDF


def get_file_patch(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('cardapio', filename)


class GerarPdf(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Relatório de Pedidos Concluídos', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def create_table(self, dataframe, title, total):
        self.chapter_title(title)
        self.set_font('Arial', 'B', 12)
        col_width = self.epw / len(dataframe.columns)
        for column in dataframe.columns:
            self.cell(col_width, 10, column, border=1)
        self.ln()

        self.set_font('Arial', '', 12)
        for row in dataframe.itertuples():
            for value in row[1:]:
                self.cell(col_width, 10, str(value), border=1)
            self.ln()
        self.ln(5)
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, f"Total do Pedido: R${total:.2f}", 0, 1, 'R')
        self.ln(10)
