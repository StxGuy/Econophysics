from arch import arch_model
model = arch_model(log_returns,vol=‘GARCH’,p=1,q=1,dist=‘Normal’)
model_fit = model.fit()
estimation = model_fit.forecast()
print(model_fit.summary())
