from flask import Blueprint, request, render_template, redirect, url_for, flash
import pandas as pd
from .forecast import forecast_demand
from .inventory import compute_inventory_parameters

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files.get('file')
        periods = int(request.form.get('periods', 1))
        if not file:
            flash('No file selected')
            return redirect(request.url)
        df = pd.read_csv(file)
        forecast = forecast_demand(df, periods)
        params = compute_inventory_parameters(forecast, df)
        return render_template('results.html', forecast=forecast.to_dict(), params=params)
    return render_template('upload.html')
