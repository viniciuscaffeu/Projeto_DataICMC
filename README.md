# **Classificação de Espécies de Flores - Dataset Iris**

## **Descrição do Projeto**
Este projeto utiliza o dataset Iris para resolver um problema clássico de classificação de espécies de flores. Foram implementados dois modelos de aprendizado de máquina para analisar o desempenho em prever as espécies com base em características morfológicas.

## **Modelos Utilizados**
1. **SVM (Support Vector Machine)**:
   - Kernel: Linear
   - Objetivo: Maximizar a margem entre as classes.
2. **Regressão Logística**:
   - Um modelo estatístico para classificação baseado em probabilidades.

## **Resultados**
| Modelo                | Acurácia |
|-----------------------|----------|
| SVM                  | 100%     |
| Regressão Logística  | 93,33%   |

## **Análise das Diferenças**

1. **Desempenho Geral**:
   - **SVM** obteve acurácia perfeita, separando corretamente todas as classes. Este modelo se mostrou altamente eficaz para o dataset Iris devido às fronteiras bem definidas entre as espécies.
   - **Regressão Logística** apresentou uma acurácia competitiva, mas com pequenos erros de classificação em algumas amostras.

2. **Método de Classificação**:
   - **SVM**: Utiliza hiperplanos que maximizam a separação entre as classes, sendo ideal para problemas com fronteiras bem definidas.
   - **Regressão Logística**: Baseia-se em combinações lineares das características, sendo menos eficiente em problemas com classes próximas.

3. **Complexidade e Aplicação**:
   - **SVM** pode ser mais custoso computacionalmente para grandes datasets, mas foi ideal para o Iris devido ao seu tamanho reduzido.
   - **Regressão Logística** é mais simples e eficiente, tornando-se uma boa opção para aplicações que demandam simplicidade e interpretabilidade.

## **Conclusões**
- O **SVM** foi o modelo mais eficaz, atingindo 100% de acurácia no conjunto de teste.
- A **Regressão Logística**, embora menos precisa, demonstrou ser uma alternativa eficiente e de fácil implementação.
- A escolha do modelo deve considerar o contexto:
  - **SVM**: Quando a precisão máxima é prioridade.
  - **Regressão Logística**: Quando há necessidade de simplicidade e maior eficiência computacional.

## **Como Executar**
1. Certifique-se de que os arquivos `main.py` e `iris.data` estejam no mesmo diretório.
2. Execute o script `main.py`:
   ```bash
   python main.py
   ```
3. O resultado será exibido no console, mostrando as acurácias dos dois modelos.

## **Tecnologias Utilizadas**
- Python
- Bibliotecas: `pandas`, `scikit-learn`

## **Autor**
Este projeto foi desenvolvido como parte de um exercício prático para o aprendizado de machine learning.
