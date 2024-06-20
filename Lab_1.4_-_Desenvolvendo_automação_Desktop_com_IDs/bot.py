from botcity.core import DesktopBot, Backend

def main():
    bot = DesktopBot()

    app_path = r"C:\Program Files (x86)\Programas RFB\Sicalc Auto Atendimento\SicalcAA.exe"

    bot.execute(app_path)

    bot.connect_to_app(backend=Backend.WIN_32, path=app_path)

    # Pop-up inicial
    janela_esclarecimento = bot.find_app_window(title="Esclarecimento ao Contribuinte")
    btn_continuar = bot.find_app_element(from_parent_window=janela_esclarecimento, title="&Continuar", class_name="ThunderRT6CommandButton")
    btn_continuar.click()

    # Menu
    janela_principal = bot.find_app_window(title="Sicalc Auto Atendimento", class_name="ThunderRT6MDIForm")
    janela_principal.menu_select("Funções -> Preenchimento de DARF")

    # Preenchendo DARF
    darf = bot.find_app_element(from_parent_window=janela_principal, title="Preenchimento de DARF", class_name="ThunderRT6FormDC")

    # Codigo da receita
    darf.Edit3.type_keys("5629")
    darf.type_keys("{TAB}")

    # Continuando preenchimento
    janela_principal = bot.find_app_window(title_re="Sicalc Auto Atendimento", class_name="ThunderRT6MDIForm")
    form_darf = bot.find_app_element(from_parent_window=janela_principal, title="Receita", class_name="ThunderRT6Frame")
    form_darf.type_keys("{TAB}")

    # Periodo apuração
    form_darf.Edit4.type_keys("310120")
    bot.wait(2000)
    form_darf.type_keys("{TAB}")

    # Valor em reais
    bot.wait(2000)
    form_darf.Edit5.type_keys("10000")

    # Calcula
    form_darf.type_keys("{ENTER}")

    # Atalho para o botão DARF
    form_darf.type_keys("%{f}")

    # Preenchendo ultimo formulario
    form_darf = bot.find_app_window(title="Preenchimento DARF Auto Atendimento", class_name="ThunderRT6FormDC")

    # Nome
    form_darf.Edit5.type_keys("Petrobras")

    # Telefone
    form_darf.Edit6.type_keys("1199991234")

    # CNPJ
    form_darf.Edit11.type_keys("33000167000101")

    # Referencia
    form_darf.Edit10.type_keys("0")

    # Imprimir
    btn_imprimir = bot.find_app_element(from_parent_window=form_darf, title="&Imprimir", class_name="ThunderRT6CommandButton")
    btn_imprimir.click()

    # Salvando arquivo PDF
    save = bot.find_app_window(title="Salvar Saída de Impressão como")
    save.type_keys(r"C:\Users\menez\Documents\DARF2.pdf")
    save.type_keys("{ENTER}")

    # Fechando janela formulário
    form_darf.type_keys("%{F4}")
    form_darf.type_keys("%{F4}")


def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()