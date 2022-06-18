from flask import Flask
from housing.logger import logging
from housing.exception import Housing_Exception
import sys

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    ## testing exception
    '''try:
        raise Exception("Testing custome exception")
    except Exception as e:
        housing = Housing_Exception(e,sys)
        logging.info(housing.error_message)'''
    logging.info("Calling index fns")
    return "<h1>Simple machine Learning Project</h1>"

if __name__=='__main__':
    app.run(debug=True)