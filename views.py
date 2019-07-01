from flask import Blueprint, render_template, flash, redirect, url_for
import pandas as pd
from forms import NCForm
from regression import *


page = Blueprint('page', __name__, template_folder='templates')

@page.route('/', methods=['GET', 'POST'])
def index ():
    form = NCForm()
    if form.validate_on_submit():
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

        if form.regression.data == 'pls':
            Y_test, predict = regression_pls(data)
            r2, mae, mse, rmse = metrics_calc(Y_test, predict)
        elif form.regression.data == 'mlr':
            Y_test, predict = regression_mlr(data)
            r2, mae, mse, rmse = metrics_calc(Y_test, predict)
        elif form.regression.data == 'svr':
            Y_test, predict = regression_svr(data)
            r2, mae, mse, rmse = metrics_calc(Y_test, predict)

        flash('NC = {}'.format(predict[0]))
        flash('R² = {}'.format(r2))
        flash('MAE = {}'.format(mae))
        flash('MSE = {}'.format(mse))
        flash('RMSE = {}'.format(rmse))

        return redirect(url_for('page.result'))
    return render_template('index.html', form=form)

@page.route('/NC')
def result ():
    return render_template('result.html')
