import pandas as pd
from flask import Blueprint, flash, render_template, request

from forms import NCForm
from regression import regression_mlr, regression_pls, regression_svr

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
                predict, r2, mae, mse, rmse = regression_pls(data)
                flash('PLS Regression')
                flash('NC = {:.2f}'.format(float(predict[0][0])))
            elif form.regression.data == 'mlr':
                predict, r2, mae, mse, rmse = regression_mlr(data)
                flash('MLR Regression')
                flash('NC = {:.2f}'.format(predict[0]))
            elif form.regression.data == 'svr':
                predict, r2, mae, mse, rmse = regression_svr(data)
                flash('SVR Regression')
                flash('NC = {:.2f}'.format(predict[0]))
        
        #flash('R² = {:.2f}'.format(float(r2)))
        #flash('MAE = {:.2f}'.format(float(mae)))
        #flash('MSE = {:.2f}'.format(float(mse)))
        #flash('RMSE = {:.2f}'.format(float(rmse)))

        return render_template('index.html', form=form)

    elif form.validate() == False and request.method == 'POST':
        flash('Error: Preencha todos os campos.')
        return render_template('index.html', form=form)

    else:
        return render_template('index.html', form=form)
