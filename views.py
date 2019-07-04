import pandas as pd
from flask import Blueprint, flash, render_template, request

from forms import NCForm
from regression import (metrics_calc, regression_mlr, regression_pls,
                        regression_svr)

page = Blueprint('page', __name__, template_folder='templates')

@page.route('/', methods=['GET', 'POST'])
def index ():
    form = NCForm(request.form)

    if form.validate() and request.method == 'POST':
        data = [
            float(form.c8_0.data),
            float(form.c10_0.data),
            float(form.c12_0.data),
            float(form.c14_0.data),
            float(form.c16_0.data),
            float(form.c18_0.data),
            float(form.c18_1.data),
            float(form.c18_2.data),
            float(form.c18_3.data),
            float(form.c18_1_oh.data),
            float(form.c20_0.data),
            float(form.c20_1.data),
            float(form.c22_1.data),
            float(form.outros.data)
        ]
        if sum(data) > 100:
            flash('Error: Somatório dos valores maior que 100.')
        else:
            if form.regression.data == 'pls':
                Y_test, predict = regression_pls(data)
                r2, mae, mse, rmse = metrics_calc(Y_test, predict)
                flash('PLS Regression')
                flash('NC = {}'.format(predict[0][0]))
            elif form.regression.data == 'mlr':
                Y_test, predict = regression_mlr(data)
                r2, mae, mse, rmse = metrics_calc(Y_test, predict)
                flash('MLR Regression')
                flash('NC = {}'.format(predict[0]))
            elif form.regression.data == 'svr':
                Y_test, predict = regression_svr(data)
                r2, mae, mse, rmse = metrics_calc(Y_test, predict)
                flash('SVR Regression')
                flash('NC = {}'.format(predict[0]))

            flash('R² = {}'.format(r2))
            flash('MAE = {}'.format(mae))
            flash('MSE = {}'.format(mse))
            flash('RMSE = {}'.format(rmse))

        return render_template('index.html', form=form)

    elif form.validate() == False and request.method == 'POST':
        flash('Error: Preencha todos os campos.')
        return render_template('index.html', form=form)

    else:
        return render_template('index.html', form=form)
