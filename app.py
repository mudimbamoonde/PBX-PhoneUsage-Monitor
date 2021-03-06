#!/usr/bin/python3 
from flask import Flask, render_template, url_for, request, jsonify,redirect
from random import sample
from dbConnection import Master
import json
import pymssql
from datetime import date

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


@app.route("/novatek/allCalls/")
def allCalls():
    view = Master()
    data = view.GetData()
    return render_template("allCalls.html", list=data)


@app.route("/novatek/cost/<accountCode>")
def accountView(accountCode):
      view = Master()
      data = view.AccontCode(accountCode)
      other = view.GroupOfMany(accountCode)
    #   print(data)
      return render_template("account.html",list = data,other=other )

@app.route("/novatek/cost/")
def cost():
    view = Master()
    data = view.CalculateCost()
    return render_template("Cost.html", list=data)


@app.route("/novatek//CostTaken/")
def costTaken():
    view = Master()
    data = view.ChartDisplay()
    return jsonify({"results": data})
    # return jsonify({"results": sample(range(100, 500), 5)})


# Account Codes
@app.route("/novatek/addAccount")
def addAccounts():
    return render_template("addAccount.html")

@app.route("/novatek/saveAccount",methods=['GET','POST'])
def saveAccounts():
    if request.method == "POST":
        accountCode = request.form["accountCode"]
        fname = request.form["fname"]
        lname = request.form["lname"]
        location = request.form["location"]
        dpt = request.form["dpt"]
        try:
            insert = Master()
            insert.InsertCode(accountCode,fname,lname,location,dpt,date.today())
            return redirect("/novatek/")
        except Exception as e:
            raise "Failed to Submit: "+ str(e)

@app.route("/novatek/viewAccountCode")
def viewAccountCode():
    query = Master()
    codes = query.QueryCodes()
    return render_template("viewAccount.html", code = codes)


@app.route("/novatek/deleteUser/<id>")
def deleteStaff(id):
    try:
        delete = Master()
        delete.DeleteUser(id)
        return redirect("/viewAccountCode")
    except Exception as e:
        raise "Failed to Delete: "+ str(e)
   
        

    

if __name__ == "__main__":
    app.run(debug=False,host='192.168.0.247',port='5050')
    # app.run(debug=True)
