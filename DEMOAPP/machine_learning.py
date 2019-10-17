from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler, LabelEncoder
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



class ModelTraining:
    model_lr = LinearRegression()
    model_trained = False
    model_name = 'DEMOAPP/CleanedData.csv'
    mse=0
    test_percent=0

    def train_model(model_name='DEMOAPP/CleanedData.csv'):
        apps = pd.read_csv(model_name)
        le = LabelEncoder()

        process_df = pd.DataFrame()
        process_df = process_df.assign(Category=le.fit_transform(apps['Category']))
        process_df=process_df.assign(Rating=apps['Rating'])
        process_df=process_df.assign(Reviews=apps['Reviews'])
        process_df = process_df.assign(Size=apps['Size'])

        mms = MinMaxScaler()
        scaled_installs = mms.fit_transform(apps['Installs'].values.reshape(-1, 1))
        scaled_installs = pd.Series(scaled_installs.reshape(len(apps.Installs)))
        scaled_installs = scaled_installs.mul(100)
        process_df = process_df.assign(Installs=scaled_installs)
        process_df.Size = process_df.Size.mul(10)
        process_df = process_df.assign(Price=apps.Price)
        process_df = process_df.drop(process_df.index[9117])
        apps = apps.drop(apps.index[9117])
        process_df = process_df.assign(Content=le.fit_transform(apps['Content Rating']))
        process_df = process_df.assign(Genres=le.fit_transform(apps['Genres']))
        process_df = process_df.assign(Version=apps['Android Version'])
        process_df.Version = process_df.Version.fillna(value=2.0)
        process_df.Size = process_df.Size.div(1000)
        train_data = ['Category', 'Reviews', 'Size', 'Installs', 'Price', 'Content', 'Genres', 'Version']
        test_data = ['Rating']
        ModelTraining.test_percent=0.2
        x_train, x_test, y_train, y_test = train_test_split(process_df[train_data], process_df[test_data], test_size=ModelTraining.test_percent,
                                                            random_state=3)
        ModelTraining.model_lr.fit(x_train, y_train)
        predictions = ModelTraining.model_lr.predict(x_test)
        ModelTraining.mse = mean_squared_error(predictions, y_test)

        predictions = pd.DataFrame(predictions)
        predictions.columns = ['Predicted Rating']

        y_test = pd.DataFrame(y_test)
        y_test.columns = ['Original Rating']

        ModelTraining.plotGraph(y_test,predictions)

        return ModelTraining.model_lr

    def plotGraph(y_test, predictions):
        plt.figure(figsize=(12, 12))
        g = sns.set_style(
            {'axes.spines.left': False, 'axes.spines.right': False, 'axes.spines.top': False,
             'axes.spines.bottom': False})
        g = sns.kdeplot(predictions['Predicted Rating'], color='#CCFF99', shade=True)
        g = sns.kdeplot(y_test['Original Rating'], color='#39EFFF', shade=True)
        plt.title('Predicted vs Expected Ratings',color='white',fontsize=30,pad=30)
        plt.tick_params(labelcolor='white', labelsize=25)
        plt.legend(fontsize='large')
        g.grid(False)

        plt.savefig('DEMOAPP/static/images/graphs/predictionGraph.png', transparent=True, pad_inches=0,
                    bbox_inches='tight')

    def rating_prediction(values_model):

        data = pd.Series(data=values_model, index=['Category', 'Reviews', 'Size', 'Installs', 'Price', 'Content', 'Genres', 'Version'])
        predicted_rating = ModelTraining.model_lr.predict(data.values.reshape(1, -1))

        return (predicted_rating/2)+1

    def get_stats():
        test=ModelTraining.test_percent*100
        train=100-test
        stats=[round(ModelTraining.mse,2), train, test]
        return stats
