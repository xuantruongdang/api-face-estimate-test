from flask import Flask, Blueprint, request, redirect, jsonify, render_template
from src.distance.base import processing
import os 

distance = Blueprint('distance', __name__)

@distance.route('/', methods=['GET', 'POST'])
def home():
    return render_template("estimate.html")

@distance.route('/distance/estimate', methods=['GET', 'POST'])
def estimate_distance():
    # if request.method == 'POST':
    tmp = "Done!"
    os.system('python src/distance/base.py')
    
    return render_template("estimate.html")