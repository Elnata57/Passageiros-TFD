from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

passageiros = []

poltronas_disponiveis = [str(i) for i in range(1, 51)]  # Poltronas numeradas de 1 a 50

def calcular_idade(data_nascimento):
    while True:
        try:
            nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
            hoje = datetime.today()
            idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
            return idade
        except ValueError:
            print("Data inválida. Por favor, digite novamente no formato DD/MM/AAAA.")
            data_nascimento = input("Digite a data de nascimento (DD/MM/AAAA): ")

def escolher_poltrona():
    global poltronas_disponiveis
    print("Poltronas disponíveis:", ", ".join(poltronas_disponiveis))
    while True:
        poltrona = input("Escolha uma poltrona disponível: ")
        if poltrona in poltronas_disponiveis:
            poltronas_disponiveis.remove(poltrona)
            return poltrona
        else:
            print("Poltrona inválida ou já ocupada. Por favor, escolha outra.")

def gerar_passagem(nome, sexo, idade, destino, estabelecimento, horario, telefone, data_consulta, cpf, cns, poltrona):
    filename = f"passagem_{nome.replace(' ', '_')}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(A4[0] / 2, 820, "SMS de Ipixuna do Pará TFD")
    c.setFont("Helvetica", 10)
    c.drawString(50, 800, "=== Passagem ===")
    c.drawString(50, 780, f"Passageiro: {nome}")
    c.drawString(50, 760, f"Sexo: {sexo}, Idade: {idade} anos")
    c.drawString(50, 740, f"CPF: {cpf}, CNS: {cns}")
    c.drawString(50, 720, f"Destino: {destino}")
    c.drawString(50, 700, f"Estabelecimento: {estabelecimento}")
    c.drawString(50, 680, f"Data da Consulta: {data_consulta}")
    c.drawString(50, 660, f"Horário da Consulta: {horario}")
    c.drawString(50, 640, f"Telefone: {telefone}")
    c.drawString(50, 620, f"Poltrona: {poltrona}")
    c.save()
    print(f"Passagem salva como {filename}")

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

def main():
    print("Cadastro de informações de saúde")

    while True:
        nome = input("Digite seu nome completo: ")
        sexo = input("Digite seu sexo (M/F): ").strip().upper()
        while sexo not in ["M", "F"]:
            print("Opção inválida. Por favor, digite M para masculino ou F para feminino.")
            sexo = input("Digite seu sexo (M/F): ").strip().upper()

        data_nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")
        idade = calcular_idade(data_nascimento)
        print(f"Sua idade: {idade} anos")

        cpf = input("Digite seu CPF: ")
        cns = input("Digite seu CNS: ")

        telefone = input("Digite seu número de telefone: ")

        print("Selecione o destino:")
        print("1. Castanhal - PA")
        print("2. Belém - PA")
        destino_opcao = input("Digite o número correspondente ao destino: ")

        while destino_opcao not in ["1", "2"]:
            print("Opção inválida. Por favor, escolha 1 ou 2.")
            destino_opcao = input("Digite o número correspondente ao destino: ")

        destino = "Castanhal - PA" if destino_opcao == "1" else "Belém - PA"

        if destino == "Belém - PA":
            print("Selecione o estabelecimento de saúde:")
            estabelecimentos_belem = [
                "Hospital Abelardo Santos",
                "Hospital Cynthia Charone",
                "Santa Casa de Misericórdia do Pará",
                "Hospital e Maternidade Dom Luiz I",
                "Hospital U. Bettina Ferro de Souza",
                "Hospital Ophir Loyola",
                "Fundação H. de C. Gaspar Vianna",
                "Gaspar Vianna Antigo S. Clara",
                "URE Marcello Cândia",
                "URE Doca",
                "Unidade de R. E. Demétrio Medrado",
                "Ure Dipe",
                "Unidades de R. E. Materno Infantil",
                "Centro de S. E. do Marco - UEPA",
                "Hospital Jean Bitar",
                "Hospital Divina Providência",
                "Cardiologia Ures Presidente Vargas",
                "ENDOCLIN",
                "Policlinica E. do Pará - U. Marco",
                "Hospital Maradei",
                "Hospital Metropolitano",
                "Hospital U. João de Barros Barreto",
                "Hospital O. I. Octávio Lobo",
                "CIIR",
                "Hospital P. E. Galileu",
                "Outros"
            ]
            for i, est in enumerate(estabelecimentos_belem, start=1):
                print(f"{i}. {est}")
            estabelecimento_opcao = input("Digite o número correspondente ao estabelecimento: ")

            while not estabelecimento_opcao.isdigit() or not (1 <= int(estabelecimento_opcao) <= 26):
                print("Opção inválida. Por favor, escolha uma opção válida.")
                estabelecimento_opcao = input("Digite o número correspondente ao estabelecimento: ")

            if estabelecimento_opcao == "26":
                estabelecimento = input("Digite o nome do estabelecimento: ")
            else:
                estabelecimento = estabelecimentos_belem[int(estabelecimento_opcao) - 1]

        else:
            print("Selecione o estabelecimento de saúde:")
            estabelecimentos_castanhal = [
                "Hospital Francisco Magalhães",
                "CADIST",
                "HRPC - Hospital R. P. de Castanhal",
                "Clínica Pró-Cardíaco",
                "Hospital M. de Castanhal",
                "Outros"
            ]
            for i, est in enumerate(estabelecimentos_castanhal, start=1):
                print(f"{i}. {est}")
            estabelecimento_opcao = input("Digite o número correspondente ao estabelecimento: ")

            while not estabelecimento_opcao.isdigit() or not (1 <= int(estabelecimento_opcao) <= 6):
                print("Opção inválida. Por favor, escolha uma opção válida.")
                estabelecimento_opcao = input("Digite o número correspondente ao estabelecimento: ")

            if estabelecimento_opcao == "6":
                estabelecimento = input("Digite o nome do estabelecimento: ")
            else:
                estabelecimento = estabelecimentos_castanhal[int(estabelecimento_opcao) - 1]

        data_consulta = input("Digite a data da consulta (DD/MM/AAAA): ")
        while True:
            try:
                datetime.strptime(data_consulta, "%d/%m/%Y")
                break
            except ValueError:
                print("Data inválida. Por favor, insira no formato DD/MM/AAAA.")
                data_consulta = input("Digite a data da consulta (DD/MM/AAAA): ")

        hora_consulta = input("Digite o horário da consulta (HH:MM): ")
        while True:
            try:
                datetime.strptime(hora_consulta, "%H:%M")
                break
            except ValueError:
                print("Horário inválido. Por favor, insira no formato HH:MM.")
                hora_consulta = input("Digite o horário da consulta (HH:MM): ")

        poltrona = escolher_poltrona()

        acompanhante = input("Você precisa de um acompanhante? (s/n): ").strip().lower()
        if acompanhante == "s":
            print("\nCadastro do acompanhante:")
            nome_acompanhante = input("Digite o nome completo do acompanhante: ")
            sexo_acompanhante = input("Digite o sexo do acompanhante (M/F): ").strip().upper()
            while sexo_acompanhante not in ["M", "F"]:
                print("Opção inválida. Por favor, digite M para masculino ou F para feminino.")
                sexo_acompanhante = input("Digite o sexo do acompanhante (M/F): ").strip().upper()

            data_nascimento_acompanhante = input("Digite a data de nascimento do acompanhante (DD/MM/AAAA): ")
            idade_acompanhante = calcular_idade(data_nascimento_acompanhante)
            print(f"Idade do acompanhante: {idade_acompanhante} anos")

            cpf_acompanhante = input("Digite o CPF do acompanhante: ")
            cns_acompanhante = input("Digite o CNS do acompanhante: ")

            telefone_acompanhante = input("Digite o número de telefone do acompanhante: ")

            poltrona_acompanhante = escolher_poltrona()

            passageiros.append({
                "nome": nome_acompanhante, "sexo": sexo_acompanhante, "idade": idade_acompanhante,
                "destino": destino,
                "estabelecimento": estabelecimento,
                "horario": hora_consulta,
                "data_consulta": data_consulta,
                "telefone": telefone_acompanhante,
                "poltrona": poltrona_acompanhante
            })

            gerar_passagem(nome_acompanhante, sexo_acompanhante, idade_acompanhante, destino, estabelecimento, hora_consulta, telefone_acompanhante, data_consulta, cpf_acompanhante, cns_acompanhante, poltrona_acompanhante)

        passageiros.append({
            "nome": nome, "sexo": sexo, "idade": idade,
            "destino": destino,
            "estabelecimento": estabelecimento,
            "horario": hora_consulta,
            "data_consulta": data_consulta,
            "telefone": telefone,
            "poltrona": poltrona
        })

        gerar_passagem(nome, sexo, idade, destino, estabelecimento, hora_consulta, telefone, data_consulta, cpf, cns, poltrona)

        continuar = input("Deseja cadastrar outro passageiro? (s/n): ").strip().lower()
        if continuar != "s":
            break

    gerar_lista_passageiros(passageiros)

if __name__ == "__main__":
    main()
