import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

class Modelo():
    def _init_(self):
        pass

    def CarregarDataset(self, path):
        """
        Carrega o conjunto de dados a partir de um arquivo CSV.

        Parâmetros:
        - path (str): Caminho para o arquivo CSV contendo o dataset.
        """
        names = ['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm', 'Species']
        self.df = pd.read_csv(path, names=names)

    def TratamentoDeDados(self):
        """
        Realiza o pré-processamento dos dados carregados.
        """
        # Verificar e tratar valores ausentes
        self.df = self.df.dropna()

        # Separar variáveis independentes (X) e dependente (y)
        self.X = self.df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
        self.y = self.df['Species']

        # Divisão em conjunto de treino e teste
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.3, random_state=42, stratify=self.y
        )

    def Treinamento(self):
        """
        Treina dois modelos de machine learning: SVM e Regressão Logística.
        """
        # Modelo 1: SVM
        self.svm_model = SVC(kernel='linear', random_state=42)
        self.svm_model.fit(self.X_train, self.y_train)

        # Modelo 2: Regressão Logística
        self.lr_model = LogisticRegression(max_iter=200, random_state=42)
        self.lr_model.fit(self.X_train, self.y_train)

    def Teste(self):
        """
        Avalia o desempenho dos modelos treinados.
        """
        # Teste para SVM
        y_pred_svm = self.svm_model.predict(self.X_test)
        accuracy_svm = accuracy_score(self.y_test, y_pred_svm)
        print(f"Acurácia do SVM: {accuracy_svm:.2f}")

        # Teste para Regressão Logística
        y_pred_lr = self.lr_model.predict(self.X_test)
        accuracy_lr = accuracy_score(self.y_test, y_pred_lr)
        print(f"Acurácia da Regressão Logística: {accuracy_lr:.2f}")

    def Train(self):
        """
        Fluxo principal para o treinamento e teste dos modelos.
        """
        self.CarregarDataset("iris.data")  # Carrega o dataset
        self.TratamentoDeDados()  # Pré-processa os dados
        self.Treinamento()  # Treina os modelos
        self.Teste()  # Testa os modelos

# Instancia a classe e executa o fluxo completo
modelo = Modelo()
modelo.Train()