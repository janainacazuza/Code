# **Previsão do Fechamento Diário do Ibovespa:**

  ## *Sumário:*

  ### Capítulo 1 -  O Desafio no Mercado Financeiro

  ### Capítulo 2 -  A Coleta dos Dados – A Primeira Peça do Quebra-cabeça

  ### Capítulo 3 -  Escolha dos Modelos – Encontrando a Melhor Ferramenta

  ### Capítulo 4 -  Teste, Erro e Ajuste – A Busca pela Precisão

  ### Capítulo 5 -  A Escolha Final – Encontrando o Melhor Modelo

  ### Capítulo 6 -  Entrega e Impacto – Pronto para Fazer a Diferença

  ### Epílogo -  A Jornada Continua

<div style="page-break-after: always;"></div>

## Capítulo 1: O Desafio no Mercado Financeiro
Nós estamos no coração de um escritório de investimentos, onde cada decisão precisa ser rápida e precisa. A equipe quer antecipar os preços de fechamento do Ibovespa para mitigar riscos e buscar melhores oportunidades. Nesse cenário, nossa equipe foi convocada para desenvolver um modelo preditivo eficiente, capaz de fornecer previsões diárias do índice com alta acuracidade.

A missão : coletar dados históricos, modelar padrões e apresentar um sistema de previsão confiável que supere 70% de acuracidade. Essa jornada exigirá precisão e estratégia 

## Capítulo 2: A Coleta dos Dados – A Primeira Peça do Quebra-cabeça
O primeiro passo foi buscar os dados históricos do Ibovespa no site Investing.com. A escolha dessa fonte se deu por sua confiabilidade e abrangência. Selecionamos dados diários, que capturam as oscilações diárias do mercado, e definimos um período de análise adequado.

Com os dados em mãos, mergulhamos no processo de pré-processamento:

* Tratamos valores ausentes para evitar vieses.
* Convertemos tipos de dados (como datas e valores numéricos).
* Criamos novas features como retornos diários para enriquecer a análise.
* Os dados brutos foram transformados em um formato limpo e pronto para alimentar nossos modelos preditivos.

* ####  Análise exploratória: 
  **Gráfico: Decomposição da série temporal para mostrar tendencia, sazonalidade e resíduos dos dados.**
  ![Decomposição da Série Temporal](/storytelling/imagens/decomposicao.png)

<div style="page-break-after: always;"></div>


## Capítulo 3: Escolha dos Modelos – Encontrando a Melhor Ferramenta
Neste ponto, precisávamos de modelos robustos para lidar com a complexidade do mercado financeiro. Escolhemos três abordagens diferentes, cada uma com suas características e vantagens específicas:

* **SARIMAX:**
Um modelo estatístico capaz de capturar padrões sazonais e lidar com variáveis exógenas. Ele seria útil para identificar influências externas e ciclos sazonais no mercado.

* **Prophet:**
Desenvolvido pelo Facebook, este modelo é eficiente em séries temporais com tendência e sazonalidade. É intuitivo e fácil de interpretar, algo valioso para apresentar ao time de investimentos.

* **XGBoost:**
Um modelo de machine learning poderoso, capaz de capturar relações complexas e não lineares. O XGBoost oferece uma abordagem mais sofisticada e flexível para encontrar padrões nos dados.

#### Análise de Autocorrelação
Os gráficos ACF e PACF nos ajudaram a identificar os melhores parâmetros para o modelo SARIMAX.

![ACF do Ibovespa](/storytelling/imagens/acf.png)
![PACF do Ibovespa](/storytelling/imagens/pacf.png)

<div style="page-break-after: always;"></div>

## Capítulo 4: Teste, Erro e Ajuste – A Busca pela Precisão
Com os dados prontos e os modelos definidos, entramos na fase de treinamento e validação. Cada modelo foi treinado e avaliado com base nas seguintes métricas:

* RMSE (Root Mean Square Error): Para medir o desvio médio quadrático.
* MAE (Mean Absolute Error): Para medir a média dos erros absolutos.
* Acuracidade: Nosso objetivo era obter uma precisão superior a 70%.
  
Testamos diferentes configurações de hiperparâmetros e ajustamos os modelos para garantir que cada um entregasse o máximo de sua capacidade. A cada rodada de ajuste, o modelo se tornava mais refinado e alinhado às necessidades da equipe de investimentos.

 **Imagem: Comparando as métricas dos modelos**

  ![Metricas dos Modelos](/storytelling/imagens/comparandomodelos.png)

 

## Capítulo 5: A Escolha Final – Encontrando o Melhor Modelo
Depois de diversas iterações, finalmente encontramos o modelo ideal.  A escolha final considerou:

* Desempenho: O modelo escolhido apresentou métricas superiores de precisão e erro.
* Interpretação: Era importante que a equipe de investimentos entendesse como o modelo gerava suas previsões.

O modelo vencedor será utilizado para fornecer previsões diárias, ajudando o time a tomar decisões mais bem informadas e assertivas.

<div style="page-break-after: always;"></div>

## Capítulo 6: Entrega e Impacto – Pronto para Fazer a Diferença
Com o modelo escolhido e validado, o próximo passo foi a implementação prática. As previsões geradas pelo modelo serão disponibilizadas diariamente, fornecendo insights que ajudam a:

* Identificar tendências emergentes no mercado.
* Antecipar oscilações e mitigar riscos.
* Aproveitar oportunidades de investimento no curto prazo.
* Essa entrega marca apenas o início. O modelo poderá ser aprimorado continuamente, incluindo mais variáveis exógenas ou conectando-se a fontes e dados em tempo real.


![Previsões do Modelo Escolhido](/storytelling/imagens/Previsoes.png)

**Imagem: Previsões do Modelo Escolhido (SARIMAX) para os próximos 7 dias**

## Epílogo: A Jornada Continua
O desenvolvimento desse modelo preditivo foi um exercício de precisão técnica e pensamento estratégico. Cada decisão – desde a escolha dos dados até a seleção do modelo final – foi orientada pelo compromisso com a excelência e a necessidade de entregar valor real à equipe de investimentos.

A previsão do Ibovespa é apenas um dos muitos desafios que podem ser enfrentados com as ferramentas certas. E como todo bom projeto no mercado financeiro, sabemos que não há fim: as condições mudam, e o modelo deve evoluir junto com elas.