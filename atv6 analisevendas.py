import pandas as pd
import smtplib
import os
from email.message import EmailMessage
import schedule
import time

def executar_analise_vendas():
    # Configurações do e-mail
    EMAIL_REMETENTE = "seuemail@gmail.com"
    EMAIL_SENHA = "sua_senha_de_app"  # Para Gmail, use uma senha de app
    EMAIL_DESTINATARIO = "destinatario@email.com"

    # 1. Verificar se o arquivo CSV existe
    arquivo_csv = "vendas.csv"
    if not os.path.exists(arquivo_csv):
        print(f"Erro: o arquivo {arquivo_csv} não foi encontrado.")
    else:
        # 2. Ler o arquivo CSV
        try:
            df = pd.read_csv(arquivo_csv)
            print(f"Arquivo {arquivo_csv} carregado com sucesso!")
        except Exception as e:
            print(f"Erro ao ler o arquivo CSV: {e}")

        # 3. Calcular total vendido por produto
        try:
            df["Total"] = df["Quantidade"] * df["Preço"]
            total_vendas = df.groupby("Produto", as_index=False)["Total"].sum()
        except KeyError as e:
            print(f"Erro: uma das colunas esperadas está faltando. Verifique se o arquivo contém 'Produto', 'Quantidade' e 'Preço'.")
            print(f"Erro: {e}")
            exit()

        # 4. Identificar o produto mais vendido
        produto_mais_vendido = total_vendas.loc[total_vendas["Total"].idxmax()]

        # 5. Criar o relatório em Excel
        arquivo_excel = "relatorio.xlsx"
        try:
            with pd.ExcelWriter(arquivo_excel, engine="openpyxl") as writer:
                df.to_excel(writer, sheet_name="Vendas", index=False)
                total_vendas.to_excel(writer, sheet_name="Resumo", index=False)

                resumo_df = pd.DataFrame({
                    "Produto mais vendido": [produto_mais_vendido["Produto"]],
                    "Total vendido (R$)": [produto_mais_vendido["Total"]],
                    "Total geral de vendas (R$)": [total_vendas["Total"].sum()]
                })
                resumo_df.to_excel(writer, sheet_name="Resumo", startrow=len(total_vendas) + 3, index=False)

            print("Relatório gerado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar o arquivo Excel: {e}")
            exit()

        # 6. Criar o e-mail
        msg = EmailMessage()
        msg["Subject"] = "Relatório de Vendas"
        msg["From"] = EMAIL_REMETENTE
        msg["To"] = EMAIL_DESTINATARIO
        msg.set_content(
            f"Olá,\n\nSegue em anexo o relatório de vendas.\n\n"
            f"Produto mais vendido: {produto_mais_vendido['Produto']} (R$ {produto_mais_vendido['Total']:.2f})\n"
            f"Total geral de vendas: R$ {total_vendas['Total'].sum():.2f}\n\n"
            "Atenciosamente,\nSistema de Relatórios"
        )

        # 7. Anexar o relatório
        try:
            with open(arquivo_excel, "rb") as f:
                msg.add_attachment(f.read(), maintype="application", subtype="xlsx", filename=arquivo_excel)
        except Exception as e:
            print(f"Erro ao anexar o arquivo: {e}")
            exit()

        # 8. Enviar o e-mail
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
                server.login(EMAIL_REMETENTE, EMAIL_SENHA)
                server.send_message(msg)
            print("E-mail enviado com sucesso!")
        except smtplib.SMTPAuthenticationError:
            print("Erro de autenticação: Verifique a senha de app do Gmail.")
        except Exception as e:
            print(f"Erro ao enviar e-mail: {e}")

# Agendar a execução para todos os dias às 9h
schedule.every().day.at("09:00").do(executar_analise_vendas)

# Manter o script rodando
while True:
    schedule.run_pending()
    time.sleep(60)  # Verificar a cada 60 segundos se é hora de executar