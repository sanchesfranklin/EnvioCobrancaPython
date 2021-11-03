# Envio automatizado de Cobranças com Python
Envios de cobranças via Whatsapp para clientes com faturas a vencer, e também envios de mensagens para clientes já com a status Vencido!
No envio a vencer, teremos também o envio com PDF/IMAGE com o boleto para pagamento, assim como as informações de PIX.

O projeto usará as bibliotecas: Selenium, Pandas, Webdriver.

Iremos ter uma planilha no Excel que ficará hospedada no Google Drive, o Bot vai ler a planilha com as informações principais dos clientes, como: Nome, Telefone, Data de Envio, ID do painel Gdoor. Iremos iterar sobre cada linha na planilha para o bot verificar o dia de envio da cobrança de acordo com a data de vencimento de cada cliente. Quando estiver no dia de envio, o bot irá enviar via Whatsapp a mensagem de cobrança para aquele cliente.

Abaixo segue um fluxograma simples sobre o funcionamento do bot

![image](https://user-images.githubusercontent.com/55898372/139970512-30dcc5f5-4e0e-4fe8-b7d7-f2c7ee69226c.png)



