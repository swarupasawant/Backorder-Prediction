from flask import Flask
from Backorder.logger import logging
from Backorder.exception import BackorderException
import sys 

app=Flask(__name__)

@app.route("/",methods =['GET','POST'])
def index():
    try:
        raise Exception("testing")
    except Exception as e :
        Backorder = BackorderException(e,sys)
        logging.info (Backorder.error_message)
        logging.info('AAAAAAAAAAAAAAAAAAAAAA')
    return "Hello Swarupa"

if __name__ == "__main__":
    app.run(debug= True)
