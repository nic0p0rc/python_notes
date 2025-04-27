from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, mean_squared_error

# Esempio di classificazione
y_true = [0, 1, 1, 0, 1, 0, 1, 1, 0, 1]
y_pred = [0, 1, 0, 0, 1, 0, 1, 0, 0, 1]

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1 = f1_score(y_true, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-score: {f1:.2f}")

# Esempio di regressione
y_true_reg = [3.0, -0.5, 2.0, 7.0]
y_pred_reg = [2.5, 0.0, 2.1, 7.8]

mse = mean_squared_error(y_true_reg, y_pred_reg)
rmse = mean_squared_error(y_true_reg, y_pred_reg, squared=False)

print(f"MSE: {mse:.2f}")
print(f"RMSE: {rmse:.2f}")
