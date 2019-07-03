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
            float(request.form['c8_0']),
            float(request.form['c10_0']),
            float(request.form['c12_0']),
            float(request.form['c14_0']),
            float(request.form['c16_0']),
            float(request.form['c18_0']),
            float(request.form['c18_1']),
            float(request.form['c18_2']),
            float(request.form['c18_3']),
            float(request.form['c18_1_oh']),
            float(request.form['c20_0']),
            float(request.form['c20_1']),
            float(request.form['c22_1']),
            float(request.form['outros'])
        ]
        if sum(data) > 100:
            flash('Error: Somatório dos valores maior que 100%.')
        else:
            if form.regression.data == 'pls':
                Y_test, predict = regression_pls(data)
                r2, mae, mse, rmse = metrics_calc(Y_test, predict)
                flash('NC = {}'.format(predict[0][0]))
            elif form.regression.data == 'mlr':
                Y_test, predict = regression_mlr(data)
                r2, mae, mse, rmse = metrics_calc(Y_test, predict)
                flash('NC = {}'.format(predict[0]))
            elif form.regression.data == 'svr':
                Y_test, predict = regression_svr(data)
                r2, mae, mse, rmse = metrics_calc(Y_test, predict)
                flash('NC = {}'.format(predict[0]))

            flash('R² = {}'.format(r2))
            flash('MAE = {}'.format(mae))
            flash('MSE = {}'.format(mse))
            flash('RMSE = {}'.format(rmse))

        return render_template('index.html', form=form)

    return render_template('index.html', form=form)

@page.route('/NC')
def result ():
    return render_template('result.html')
