from sklearn.linear_model import LogisticRegression


class LogisticRegressionModel:
    def __init__(self, **kwargs):
        self.model = LogisticRegression(**kwargs)

    def fit(self, X, y):
        self.model.fit(X, y)

    def predict(self, X):
        self.predicts = self.model.predict(X)
        return self.predicts

    def predict_proba(self, X):
        return self.model.predict_proba(X)
    
    def evaluate(self, X, y):
        return self.model.score(X, y)

    def plot_confusion_matrix(self, X, y, labels=None, cmap='Blues'):
        from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
        import matplotlib.pyplot as plt
        y_pred = self.predicts
        cm = confusion_matrix(y, y_pred, labels=labels)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
        disp.plot(cmap=cmap)
        plt.title('Confusion Matrix')
        plt.show()

    def f1_score(self, X, y, average='binary'):
        from sklearn.metrics import f1_score
        y_pred = self.predicts
        return f1_score(y, y_pred, average=average)