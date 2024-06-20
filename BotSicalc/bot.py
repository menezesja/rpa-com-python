from botcity.core import DesktopBot

def main():
    
    bot = DesktopBot()
    bot.execute(r"C:\Program Files (x86)\Programas RFB\Sicalc Auto Atendimento\SicalcAA.exe")

    if not bot.find( "popup-esclarecimento", matching=0.97, waiting_time=10000):
        not_found("popup-esclarecimento")
    bot.click_relative(250, 264)
    
    if not bot.find( "funcoes", matching=0.97, waiting_time=10000):
        not_found("funcoes")
    bot.click()
    
    if not bot.find( "preenchimento-darf", matching=0.97, waiting_time=10000):
        not_found("preenchimento-darf")
    bot.click()
    
    if not bot.find( "cod-receita", matching=0.97, waiting_time=10000):
        not_found("cod-receita")
    bot.click_relative(215, 18)
    
    # Inserindo no campo um código fictício
    bot.paste("5629")
    
    # Tecla "tab" avança para o próximo formulário
    bot.tab()
    
    # Espera para os campos carregarem
    bot.wait(1000)
    
    if not bot.find( "periodo-apuracao", matching=0.97, waiting_time=10000):
        not_found("periodo-apuracao")
    bot.click_relative(25, 30)
    
    # Inserindo PA
    bot.paste("310120")
    
    if not bot.find( "valor", matching=0.97, waiting_time=10000):
        not_found("valor")
    bot.click_relative(60, 33)
    
    # Inserindo valor
    bot.paste("10000")
    
    if not bot.find( "calcular", matching=0.97, waiting_time=10000):
        not_found("calcular")
    bot.click()
    
    if not bot.find( "botao-darf", matching=0.97, waiting_time=10000):
        not_found("botao-darf")
    bot.click()
    
    if not bot.find( "nome", matching=0.97, waiting_time=10000):
        not_found("nome")
    bot.click_relative(129, 36)
    
    # Inserindo nome
    bot.paste("Petrobras")
    
    if not bot.find( "telefone", matching=0.97, waiting_time=10000):
        not_found("telefone")
    bot.click_relative(54, 40)
    
    # Inserindo telefone
    bot.paste("1199991234")
    
    if not bot.find( "cnpj", matching=0.97, waiting_time=10000):
        not_found("cnpj")
    bot.click_relative(204, 18)
    
    # Inserindo CNPJ
    bot.paste("33000167000101")
    
    if not bot.find( "referencia", matching=0.97, waiting_time=10000):
        not_found("referencia")
    bot.click_relative(189, 12)
    
    # Inserindo referência
    bot.paste("0")
    
    if not bot.find( "click-imprimir", matching=0.97, waiting_time=10000):
        not_found("click-imprimir")
    bot.click()
    
    if not bot.find( "janela-salvar", matching=0.97, waiting_time=10000):
        not_found("janela-salvar")
    bot.click()
    
    # Inserindo path do arquivo
    bot.paste(r"C:\Users\menez\Documents\DARF.pdf")
    bot.enter()
    
    bot.wait(2000)

    # Fechando janela do formulário
    bot.alt_f4()

    # Fechando app do SiCalc
    bot.alt_f4()
      
def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()

