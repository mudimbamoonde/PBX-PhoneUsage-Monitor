from flask import Flask, render_template, url_for, request, jsonify,redirect
from random import sample
from dbConnection import Master
import json
import pymssql
import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("dashboard.html")

@app.route("/novatek/")
def novatek():
    view = Master()
    data = view.GetData()
    # data = {}
    # while True:
    #     data = view.GetData()
    # return render_template("index.html")
    # print(data)
    return render_template("index.html", list=data)


@app.route("/cost/<accountCode>")
def accountView(accountCode):
      view = Master()
      data = view.AccontCode(accountCode)
      other = view.GroupOfMany(accountCode)
    #   print(data)
      return render_template("account.html",list = data,other=other )

@app.route("/cost/")
def cost():
    view = Master()
    data = view.CalculateCost()
    return render_template("Cost.html", list=data)


@app.route("/CostTaken/")
def costTaken():
    view = Master()
    data = view.ChartDisplay()
    return jsonify({"results": data})
    # return jsonify({"results": sample(range(100, 500), 5)})


# Account Codes
@app.route("/addAccount")
def addAccounts():
    return render_template("addAccount.html")

@app.route("/saveAccount",methods=['GET','POST'])
def saveAccounts():
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
