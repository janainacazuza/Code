# Previsão de Fechamento Diário do Ibovespa  
Este projeto tem como objetivo desenvolver um modelo preditivo para o preço de fechamento diário do Ibovespa, utilizando dados históricos extraídos do site Investing.com. O projeto segue uma abordagem de storytelling que abrange todas as etapas, desde a captura e manipulação dos dados até a escolha e avaliação do modelo mais adequado.

---

## 1. Contexto do Problema  
O mercado financeiro é dinâmico e altamente influenciado por variações diárias nos preços de ativos, impactando diretamente as decisões de investimento. O objetivo é fornecer previsões de curto prazo para o Ibovespa, auxiliando a equipe de investimentos na tomada de decisões e mitigação de riscos.

### Desafios
- Captura e manipulação dos dados financeiros históricos.
- Escolha do modelo mais apropriado para previsões de curto prazo.
- Justificação técnica das abordagens utilizadas.
- Obtenção de um modelo com acuracidade superior a 70%.

---

## 2. Coleta e Preparação dos Dados  
Os dados foram extraídos do site [Investing.com](https://br.investing.com/indices/bovespa-historical-data).  

### Etapas:
1. **Período**: Dados diários em um intervalo de tempo selecionado.
2. **Pré-processamento**:  
   - Tratamento de valores ausentes.
   - Conversão de datas e valores numéricos.
   - Criação de novas features (ex.: retornos diários).

---

## 3. Modelagem e Técnicas Utilizadas  
Três modelos foram comparados quanto à sua eficácia:  
- **SARIMAX**: Captura padrões sazonais e variáveis exógenas.  
- **Prophet**: Útil para séries temporais com tendências e sazonalidade.  
- **XGBoost**: Algoritmo de boosting adequado para padrões não lineares.

A escolha dos modelos foi baseada na robustez e relevância para previsões financeiras.

---

## 4. Validação e Avaliação dos Modelos  
Utilizamos as seguintes métricas de avaliação:  
- **RMSE** (Root Mean Square Error): Erro médio quadrático.  
- **MAE** (Mean Absolute Error): Erro médio absoluto.  
- **Acuracidade**: Meta de 70% para garantir previsões confiáveis.

Cada modelo foi treinado e avaliado com dados de validação, sendo escolhido o melhor com base no desempenho.

---

## 5. Resultados e Escolha do Modelo Final  
O modelo escolhido foi o que apresentou o melhor desempenho nas métricas de avaliação e equilíbrio entre precisão e interpretabilidade.

---

## 6. Conclusão e Próximos Passos  
Este projeto demonstrou como técnicas de aprendizado de máquina podem ser aplicadas para prever o Ibovespa. Futuramente, o modelo poderá ser aprimorado com mais variáveis exógenas ou dados em tempo real.

---

## 7. Como Reproduzir o Projeto  
### Pré-requisitos  
- Python 3.8+  
- Ambiente virtual (Conda ou virtualenv)  

### Instalação  
1. Clone o repositório:  
   ```bash
   git clone <URL do repositório>
   cd nome_do_projeto

2. Crie e ative o ambiente virtual:
   ```bash
   conda create -n ibov_model python=3.9
   conda activate ibov_model

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt

### Execução
1. Execute o notebook
   ```bash
   jupyter notebook tech_challenge2.ipynb

2. Verifique as células finais para visualizar as previsões.

## 8. Contato
* Janaína P. F. Martins Cazuza (janainamartinscazuza@gmail.com)