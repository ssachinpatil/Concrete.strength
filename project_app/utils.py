import pickle
import json
import numpy as np
try:
    import config
except:
    pass

class concrete():
    def __init__(self,Cement,BlastFurnaceSlag,FlyAsh,Water,Superplasticizer,CoarseAggregate,FineAggregate,Age):
        self.Cement=Cement
        self.BlastFurnaceSlag=BlastFurnaceSlag
        self.FlyAsh=FlyAsh
        self.Water=Water
        self.Superplasticizer=Superplasticizer
        self.CoarseAggregate=CoarseAggregate
        self.FineAggregate=FineAggregate
        self.Age=Age

    def load_model(self):
        try:
            with open(config.MODEL_FILE_PATH,'rb') as f:
                self.model=pickle.load(f)
                
            with open(config.JSON_FILE_PATH,'r') as m:
                self.data=json.load(m)
        
        except:
            
            with open("concrete.pkl",'rb') as f:
                self.model=pickle.load(f)
        
            with open ("data.json",'r') as m:
                self.data=json.load(m)

    def get_pred(self):
        self.load_model()
        
        array=np.zeros(len(self.data['columns']))
            
        array[0]=self.Cement    
        array[1]=self.BlastFurnaceSlag
        array[2]=self.FlyAsh
        array[3]=self.Water   
        array[4]=self.Superplasticizer 
        array[5]=self.CoarseAggregate
        array[6]=self.FineAggregate
        array[7]=self.Age

        print(array)
        pred=self.model.predict([array])
        print(pred)
        return pred  

if __name__=="__main__":
    Cement=333
    BlastFurnaceSlag=2
    FlyAsh=3
    Water=400
    Superplasticizer=3
    CoarseAggregate=1400
    FineAggregate=900
    Age=365
    civil=concrete(Cement,BlastFurnaceSlag,FlyAsh,Water,Superplasticizer,CoarseAggregate,FineAggregate,Age)
    civil.get_pred()
