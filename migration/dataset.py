#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simplejson
from tools.portaldb import PortalDB


class DatasetExport():

    def __init__(self, database):

        self.db = database

    def get_django_data(self):
        database_data = self.get_all_records()
        return self.get_django_data_from_database_data(database_data)

    def get_all_records(self):

        sql = (
            "SELECT"
            " coadd.tiletags.tiletag_id,"
            " coadd.tiletags.tag_id,"
            " coadd.tiletags.tile_id,"
            " coadd.tiletags.field_id,"
            " coadd.tiletags.image_id,"
            " coadd.tiletags.run,"
            " coadd.tiletags.flag_reject,"
            " coadd.tiletags.flag_analized,"
            " coadd.tiletags.defect_category"
            " FROM coadd.tiletags"
            " INNER JOIN coadd.fields ON coadd.fields.field_id = coadd.tiletags.field_id"
            " INNER JOIN coadd.tiles"
            " ON coadd.tiletags.tile_id = coadd.tiles.tile_id"
            " WHERE coadd.fields.field_name IN ("
            " 'Y1A1_COADD_STRIPE82',"
            " 'Y1A1_COADD_SPT',"
            " 'Y1A1_COADD_COSMOS_D04',"
            " 'Y1A1_COADD_COSMOS_D10',"
            " 'Y1A1_COADD_COSMOS_DFULL',"
            " 'Y1A1_COADD_VVDS14_D04',"
            " 'Y1A1_COADD_VVDS14_D10',"
            " 'Y1A1_COADD_VVDS14_DFULL',"
            " 'Y1A1_COADD_SN_D04',"
            " 'Y1A1_COADD_SN_D10',"
            " 'Y1A1_COADD_SN_DFULL'"
            " )"
            # [CMP] follow code remove duplicated tiles.
            # maybe better to select only DES tiles (project = 'DES')
            " AND coadd.tiles.tilename NOT IN"
            " (SELECT tilename"
            " FROM coadd.tiles"
            " GROUP BY tilename"
            " HAVING count(*) > 1)"
            " ORDER BY coadd.tiletags.tiletag_id ASC;"
        )

        return self.db.fetchall_dict(sql, assoc=True)

    def get_django_data_from_database_data(self, database_data):

        django_data = list()

        for record in database_data:
            django_record = {}
            django_record["model"] = "coadd.dataset"
            django_record["pk"] = record["tiletag_id"]
            django_record["fields"] = {}

            django_record["fields"]["tag"] = record["field_id"]
            django_record["fields"]["tile"] = record["tile_id"]
            django_record["fields"]["run"] = record["run"]

            django_data.append(django_record)

        return django_data


if __name__ == '__main__':

    db = PortalDB(
        config_key=None,
        dburl="postgres://fnaldba:dbafnal@localhost/fnal",
        debug=False
    )

    export = DatasetExport(db)
    file = open("json/dataset.json", "w")
    file.write(simplejson.dumps(export.get_django_data(), ensure_ascii=False))
    file.close()
