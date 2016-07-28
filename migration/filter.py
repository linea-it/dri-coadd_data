#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simplejson
from tools.portaldb import PortalDB


class FilterExport():

    def __init__(self, database):

        self.db = database

    def get_django_data(self):
        json_string = u'''[
    {
        "model":"coadd.filter",
        "pk":1,
        "fields":{
            "project":"DES",
            "filter":"u",
            "lambda_min":300.0,
            "lambda_max":409.0,
            "lambda_mean":354.5
        }
    },
    {
        "model":"coadd.filter",
        "pk":2,
        "fields":{
            "project":"DES",
            "filter":"g",
            "lambda_min":391.0,
            "lambda_max":557.0,
            "lambda_mean":474.0
        }
    },
    {
        "model":"coadd.filter",
        "pk":3,
        "fields":{
            "project":"DES",
            "filter":"r",
            "lambda_min":558.0,
            "lambda_max":733.0,
            "lambda_mean":645.5
        }
    },
    {
        "model":"coadd.filter",
        "pk":4,
        "fields":{
            "project":"DES",
            "filter":"i",
            "lambda_min":682.0,
            "lambda_max":885.0,
            "lambda_mean":783.5
        }
    },
    {
        "model":"coadd.filter",
        "pk":5,
        "fields":{
            "project":"DES",
            "filter":"z",
            "lambda_min":826.0,
            "lambda_max":1026.0,
            "lambda_mean":926.0
        }
    },
    {
        "model":"coadd.filter",
        "pk":6,
        "fields":{
            "project":"DES",
            "filter":"Y",
            "lambda_min":926.0,
            "lambda_max":1090.0,
            "lambda_mean":1008.0
        }
    },
    {
        "model":"coadd.filter",
        "pk":7,
        "fields":{
            "project":"DES",
            "filter":"irg",
            "lambda_min":null,
            "lambda_max":null,
            "lambda_mean":null
        }
    }
]'''

        return simplejson.loads(json_string)


if __name__ == '__main__':

    db = PortalDB(
        config_key=None,
        dburl="postgres://fnaldba:dbafnal@localhost/fnal",
        debug=False
    )

    export = FilterExport(db)
    file = open("json/filter.json", "w")
    file.write(simplejson.dumps(export.get_django_data(), ensure_ascii=False))
    file.close()
