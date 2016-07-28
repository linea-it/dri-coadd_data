#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simplejson
from tools.portaldb import PortalDB

class ClassContent():

    def __init__(self, database):

        self.db = database

    def get_django_data(self):
        database_data = self.get_all_records()
        return self.get_django_data_from_database_data(database_data)

    def get_all_records(self):

        sql = (
            "SELECT *,"
            " CASE category_name"
            " WHEN 'Astrometry' THEN 1"
            " WHEN 'Base' THEN 2"
            " WHEN 'Common' THEN 3"
            " WHEN 'Flux' THEN 4"
            " WHEN 'Magnitude' THEN 5"
            " WHEN 'Mask' THEN 6"
            " WHEN 'Model Fit' THEN 7"
            " WHEN 'Quality' THEN 8"
            " WHEN 'Shape' THEN 9"
            " ELSE NULL"
            " END AS category_id"
            " FROM catalog_class_property"
            " ORDER BY property_id;"
        )

        print(sql)
        return self.db.fetchall_dict(sql, assoc=True)

    def get_django_data_from_database_data(self, database_data):

        django_data = list()

        for record in database_data:
            django_record = {
                "model":"product_classifier.productclasscontent",
                "fields": {
                    "pcc_class": record.get('class_id'),
                    "pcc_category": record.get('category_id'),
                    "pcc_name": record.get('property_name'),
                    "pcc_display_name": record.get('column_name'),
                    "pcc_ucd": record.get('ucd'),
                    "pcc_unit": record.get('unit'),
                    "pcc_reference": record.get('reference'),
                    "pcc_mandatory": record.get('mandatory')
                }
            }
            django_data.append(django_record)

        return django_data


if __name__ == '__main__':

    db = PortalDB(
        config_key=None,
        # dburl="postgres://fnaldba:dbafnal@localhost/fnal", #[CMP] cannot be done due database changes
        dburl="postgres://develdba:dbadevel@dbmaster.linea.gov.br/devel",
        debug=False
    )

    export = ClassContent(db)
    file = open("class_content.json", "w")
    file.write(simplejson.dumps(export.get_django_data(), ensure_ascii=False))
    file.close()
