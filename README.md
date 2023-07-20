# Coleta de Dados no site Status Invest 
site: https://statusinvest.com.br/ 
Coleta de Dados do site Status Invest "B3 - Bolsa Valores Brasil"
- retirado do fundo do baú o projeto rsrsrs 

### Projeto de 2019 em Python - WebScraping
Link Bases: https://1drv.ms/u/s!Aq7afOrVCVo-gY5Qgw0G8MYYv7ckUw?e=j6uyVP
- desde 2021, foram coletadas e armazenadas para análises comparativas.

### Informações Coletadas no site:
- FIIs  - fundos de investimento imobiliário
- Ações - ações negociadas na bolsa de valores brasileira (B3)

### Indicadores Coletados Ações :
  - DY (Dividend Yield): Indica o rendimento anual dos dividendos pagos pela empresa em relação ao preço atual da ação. Quanto maior o DY, melhor, pois representa um maior retorno para o acionista.
  - P/L (Preço/Lucro): É a relação entre o preço de mercado da ação e o lucro gerado pela empresa de forma anualizada (lucro por ação). Quanto menor o P/L, mais barata está a empresa em relação ao seu lucro.
  - P/VP (Preço/Valor Patrimonial): É o valor de mercado da empresa dividido pelo valor patrimonial (patrimônio líquido) por ação. Indica o quanto a ação está sendo negociada em relação ao valor contábil. Quanto menor o P/VP, mais barata está a empresa.
  - P/ATIVOS (Preço/Ativos): É o preço da ação dividido pelos ativos totais por ação. Indica quanto do preço está representado nos ativos da empresa. Quanto menor o P/ATIVOS, mais barata está a empresa em relação aos seus ativos.
  - Margem Bruta: É a divisão do Lucro Bruto pela Receita Líquida. Indica a porcentagem de lucro após deduzidos os custos do produto ou serviço. Quanto maior a margem bruta, melhor.
  - Margem EBIT: É o EBIT (Lucro Operacional) dividido pela Receita Líquida. Indica a porcentagem de cada R$1,00 de venda que sobrou após pagamento dos custos e despesas operacionais. Quanto maior a margem EBIT, melhor.
  - Margem Líquida: É a divisão do Lucro Líquido pela Receita Líquida. Indica a porcentagem de lucro que a empresa gera após todos os custos. Quanto maior a margem líquida, melhor.
  - P/EBIT (Preço/EBITDA): É o preço da ação dividido pelo EBITDA por ação. O EBITDA é uma medida do lucro operacional da empresa. Quanto menor o P/EBIT, mais barata está a empresa.
  - EV/EBIT (Valor da Empresa/EBIT): É o custo total para se comprar a empresa (valor de mercado + dívidas) dividido pelo EBIT. Quanto menor o EV/EBIT, mais barata está a empresa em relação ao seu lucro operacional.

### Indicadores Coletados FIIs :
  - DY (Dividend Yield): Indica o rendimento anual dos dividendos pagos pelo FII em relação ao preço atual da cota. Quanto maior o DY, melhor, pois representa um maior retorno para o investidor em termos de renda gerada pelo FII.
  - P/VP (Preço/Valor Patrimonial): É o preço da cota dividido pelo valor patrimonial (patrimônio líquido) do FII. Indica o quanto a cota está sendo negociada em relação ao valor contábil do fundo. Quanto menor o P/VP, mais barato está o FII.
  - Liquidez Média Diária: Representa o volume médio de negociação diária das cotas do FII. Quanto maior a liquidez média diária, mais fácil é a negociação das cotas.
  - Percentual em Caixa: Refere-se ao poder de caixa disponível para o FII comprar novas cotas. Um percentual mais alto indica uma maior capacidade de expansão do fundo.
  - CAGR Dividendos 3 Anos: É a taxa de crescimento anual composta dos dividendos distribuídos pelo FII nos últimos 3 anos.
  - CAGR Valor Cota 3 Anos: Representa a taxa de crescimento anual composta do valor da cota do FII nos últimos 3 anos.
  - Patrimônio: Indica o valor total dos ativos do FII em determinado período.
  - N Cotistas: Refere-se ao número de cotistas (investidores) que possuem participação no FII.
  - Gestão: Indica o tipo de gestão do FII, que pode ser ativa, passiva ou híbrida.
  - _Dt_arquivo_Prim: Data do arquivo com informações sobre o FII no primeiro momento.
  - _PRECO_Prim_Cotação: Preço da cota do FII no primeiro momento.
  - _Dt_arquivo_MesAnt: Data do arquivo com informações sobre o FII no mês anterior.
  - _PRECO_MesANT_Cotação: Preço da cota do FII no mês anterior.

Entre outros indicadores e outros criados. 
Iniciei o projeto com foco em Fundos de Investimento Imobiliário (FIIs) e Ações. 
Embora tenha realizado algumas análises, ainda não evoluí o projeto para uma abordagem preditiva. 
No entanto, tenho planos de retomar o projeto em breve, com o objetivo de incorporar análises estatísticas, como regressão, análise de séries temporais.

Compartilhei o Excel, com as análises básicas, utilizando a funcionalidade do PowerQuery para tratar os dados e obter insights iniciais.

=)
