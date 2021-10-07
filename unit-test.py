"""

Prisma Inc. 2021

unit-test.py

Status: Checked

Note: For unit testing purposes.

Made by Alexis W.

"""
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sneakers.api.utils as skutils
from sneakers.api.composer import Composer
from sneakers.api.airtable_complite import Aircomposer
import sneakers.api.core as skcore
import sneakers.api.ticker as skticker
import sneakers.api.datautils as skdata
#from sneakers.vision import training as skvtraining
#from sneakers.vision import dataset as skvdataset
#from sneakers.vision import model as skvmodel
#from sneakers.vision import computation as skvcomps
#from sneakers.vision import modelutils as skvutils
from sneakers.api.low import database as lowd


titl = skutils.composer_title('composer', 'HelloWorld')

url = "https://goat.com/sneakers/lebron-18-ep-goat-cq9284-008"

if __name__ == '__main__':
    conf = skcore.load_config()
    training_name = 'adidas2'
    training_path = 'sneakers/datasets/adidas2'
    test_name = 'adidas2test'
    test_path = 'sneakers/datasets/adidas2test'
    # data = skvdataset.build_dataset(20, 'adidas')
    # skvdataset.build_tf_training(data, training_name)
    # lab = skvdataset.get_labels(training_path)
    # vmodel = skvmodel.load_model(len(lab))
    # vmodel.summary()
    # train = skvtraining.training_constructor(training_path)
    # test = skvtraining.training_constructor(test_path)
    # x = train.class_indices
    # print(x)
    # skvmodel.compile_model(vmodel, train, 'skvision')
    #results = skvcomps.do_magic('skvision', test)

    # skvutils.prediction_labeling(x,results)

    # x = skdata.get_link_by_sku('CZ4178-005')
    # print(x)
    lowd.load_database()

























    
    