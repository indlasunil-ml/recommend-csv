
# This is basically the heart of my flask 

from flask import Flask, render_template, request

import pandas as pd
from time import sleep
import warnings
warnings.filterwarnings("ignore")
user_recommandation=pd.read_csv('dataset/user_final_rating_cos.csv')
user_recommandation.set_index('user',inplace=True)
data=pd.read_csv('dataset/train.csv')


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html',message="")



@app.route('/recommand', methods=['POST'])
def recommand():
    recommandation = pd.DataFrame(columns = ['product', 'positive','negative'])
    user=request.form['User'];
    if user in user_recommandation.index:
        sleep(5)
        result=user_recommandation.loc[user].sort_values(ascending=False)[0:20]
        prod=data[data['product'].isin(result.index)]
        final_recommandation=prod.sort_values('positive',ascending=False)[0:5]
        res = render_template('index.html', prediction_text='Product Recommendation for user : {}'.format(user),
                                    tables=[final_recommandation.to_html(classes='data')], titles=final_recommandation.columns.values)
        return res

    else:
        return render_template('index.html', message="Invalid Input")


    


if __name__ == '__main__':
    app.run(debug=True)








