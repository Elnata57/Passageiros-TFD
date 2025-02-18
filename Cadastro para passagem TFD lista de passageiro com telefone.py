from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

passageiros = []

def gerar_lista_passageiros(passageiros):
    filename = "lista_passageiros.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    c.setPageSize((A4[1], A4[0]))  # Orientação em paisagem
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(A4[1] / 2, 550, "SMS de Ipixuna do Pará TFD")
    c.setFont("Helvetica", 10)
    c.drawString(30, 520, "Nome")
    c.drawString(180, 520, "Sexo")
    c.drawString(230, 520, "Idade")
    c.drawString(280, 520, "Destino")
    c.drawString(380, 520, "Estabelecimento")
    c.drawString(530, 520, "Data")
    c.drawString(600, 520, "Hora")
    c.drawString(670, 520, "Telefone")
    c.drawString(750, 520, "Poltrona")
    c.line(30, 515, 800, 515)

    y = 500
    if not passageiros:
        c.drawString(30, y, "Nenhum passageiro cadastrado.")
    else:
        for p in passageiros:
            c.drawString(30, y, p['nome'][:50])  # Nome com até 50 caracteres
            c.drawString(180, y, p['sexo'])
            c.drawString(230, y, str(p['idade']))
            c.drawString(280, y, p['destino'])
            c.drawString(380, y, p['estabelecimento'])
            c.drawString(530, y, p['data_consulta'])
            c.drawString(600, y, p['horario'])
            c.drawString(670, y, p['telefone'])
            c.drawString(750, y, p['poltrona'])
            y -= 20
            if y < 50:
                c.showPage()
                c.setFont("Helvetica", 10)
                y = 500

    c.save()
    print(f"Lista de passageiros salva como {filename}")
