# from crypt import methods
from project_app.utils import concrete
import config

from flask import Flask,jsonify,request

app=Flask(__name__)
@app.route('/')
def sms():
    return 'hello'
@app.route('/output')
def strength():
    dt=request.form
    print(dt)
    Cement=eval(dt['Cement'])
    BlastFurnaceSlag=eval(dt['BlastFurnaceSlag'])
    FlyAsh=eval(dt['FlyAsh'])
    Water=eval(dt['Water'])
    Superplasticizer=eval(dt['Superplasticizer'])
    CoarseAggregate=eval(dt['CoarseAggregate'])
    FineAggregate=eval(dt['FineAggregate'])
    Age=eval(dt['Age'])
    civil=concrete(Cement,BlastFurnaceSlag,FlyAsh,Water,Superplasticizer,CoarseAggregate,FineAggregate,Age)
    charges=civil.get_pred()
    return jsonify({"result":f"the strength o cement is{charges}"})

if __name__=="__main__":
    app.run(host='0.0.0.0',port=config.PORT_NUMBER,debug=False)