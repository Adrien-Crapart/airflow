# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:02:14 2022
@author: adrien.crapart
"""
from processing.script import ScriptUtils
from processing.core.Processing import Processing
from processing.modeler.ModelerUtils import ModelerUtils
import processing
import sys
import os.path
import json
import time
import datetime
import psycopg2
from qgis.core import QgsApplication, QgsProcessingFeedback, QgsProcessingModelAlgorithm, Qgis
from qgis.analysis import QgsNativeAlgorithms

# Initialize QGIS Application
QgsApplication.setPrefixPath("C:\\OSGeo4W\\apps\\qgis", True)
app = QgsApplication([], False)
app.initQgis()

# Add the path to Processing framework
sys.path.append('C:\\OSGeo4W\\apps\\qgis\\python\\plugins')

# Import and initialize Processing framework
Processing.initialize()
QgsApplication.processingRegistry().providerById('model').refreshAlgorithms()

# Setting model parameters
f = open(r'parameters/models_parameters.json', encoding=('utf-8'))
models_parameters = json.load(f)
f.close()


def connection_of_padu_parameters(var_field):
    connection = psycopg2.connect(
        host='klabs-data-postgresql.kinaxia.lan',
        port=5432,
        database='DATA_GPU',
        user='data_team',
        password='EKpPEniJuUkpH4QJ'
    )
    # Connect to postgres to get cities with parameters writing
    cursor = connection.cursor()
    cursor.execute("""SELECT city_id, city_name FROM "Etude du GPU"."_PADU_parameters" WHERE {}_buffer_1 != '' AND {}_buffer_2 != '' ORDER BY city_id ASC;""".format(
        var_field, var_field))
    city_list = cursor.fetchall()
    connection.close()
    return (city_list)


def all_cities_reset(model_name):
    mailing_text = []
    for model in models_parameters:
        if model['model_name'] == model_name:
            model_field = model['model_field']
            input_parameters = model['input_parameters']
            break

    cities_name = connection_of_padu_parameters(model_field)

    for city in cities_name:
        # Count begining time
        start_time = time.time()
        check = ''
        print('Début du traitement : {}'.format(city[0]))
        input_parameters['territoire'] = city[0]
        processing.run(model_name, input_parameters)
        check = """<img class="checklist" src="cid:circle-xmark-regular"/>"""
        '''
        try:
            input_parameters['territoire'] = city[0]
            processing.run(model_name, input_parameters)
            check = """<img class="checklist" src="cid:circle-check-solid"/>"""
        except:
            check = """<img class="checklist" src="cid:circle-xmark-regular"/>"""
        '''
        mailing_text.append("""
            <tr>
              <th colspan="1" align="left" valign="top">{}</th>
              <th colspan="1" align="left" valign="top">{}</th>
              <th colspan="1" align="middle" valign="top">{}</th>
              <th colspan="1" align="left" valign="top">{}</th>
            </tr>
            """.format(str(city[0]), str(city[1]), check, str(datetime.timedelta(seconds=(time.time() - start_time)))))

        print('Fin du traitement : {}'.format(city[0]))

    return(mailing_text)


recipients = ['adrien.crapart@preventimmo.fr']
sending_mail_for_updating_cadastre(all_cities_reset(
    'model:ZONAGE - intersection à la parcelle'), 'ZONAGE', 'banner_padu_zonage', recipients)

# Finally, exitQgis() is called to remove the provider and layer registries from memory
app.exitQgis()
