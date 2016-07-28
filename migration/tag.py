#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simplejson
from tools.portaldb import PortalDB


class TagExport():

    def __init__(self, database):

        self.db = database

    def get_django_data(self):
        database_data = self.get_all_records()
        return self.get_django_data_from_database_data(database_data)

    def get_all_records(self):

        sql = (
            "SELECT DISTINCT"
            " coadd.fields.field_id,"
            " LOWER(coadd.fields.field_name) AS field_name,"
            " coadd.fields.display_name,"
            " coadd.fields.install_date,"
            " coadd.fields.release_date,"
            " coadd.fields.status,"
            " coadd.fields.start_date,"
            " coadd.fields.discovery_date,"
            " CASE coadd.fields.field_name"
            " WHEN 'Y1A1_COADD_STRIPE82' THEN 1"
            " WHEN 'Y1A1_COADD_SPT' THEN 1"
            " WHEN 'Y1A1_COADD_COSMOS_D04' THEN 2"
            " WHEN 'Y1A1_COADD_VVDS14_D04' THEN 2"
            " WHEN 'Y1A1_COADD_SN_D04' THEN 2"
            " WHEN 'Y1A1_COADD_COSMOS_D10' THEN 3"
            " WHEN 'Y1A1_COADD_VVDS14_D10' THEN 3"
            " WHEN 'Y1A1_COADD_SN_D10' THEN 3"
            " WHEN 'Y1A1_COADD_COSMOS_DFULL' THEN 4"
            " WHEN 'Y1A1_COADD_VVDS14_DFULL' THEN 4"
            " WHEN 'Y1A1_COADD_SN_DFULL' THEN 4"
            " ELSE coadd.release_tag.tag_id"
            " END AS release_tag_id"
            " FROM coadd.fields"
            " INNER JOIN coadd.tiletags ON coadd.tiletags.field_id = coadd.fields.field_id"
            " INNER JOIN coadd.release_tag ON coadd.release_tag.tag_id = coadd.tiletags.tag_id"
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
            " ORDER BY coadd.fields.field_id ASC;"
        )

        return self.db.fetchall_dict(sql, assoc=True)

    def get_django_data_from_database_data(self, database_data):

        django_data = list()

        for record in database_data:
            django_record = {}
            django_record["model"] = "coadd.tag"
            django_record["pk"] = record["field_id"]
            django_record["fields"] = {}

            django_record["fields"]["tag_release"] = record["release_tag_id"]
            django_record["fields"]["tag_name"] = record["field_name"]
            django_record["fields"]["tag_display_name"] = (
                record["display_name"])
            django_record["fields"]["tag_install_date"] = (
                str(record["install_date"]) if (
                    record["install_date"] is not None) else None)
            django_record["fields"]["tag_release_date"] = (
                str(record["release_date"]) if (
                    record["release_date"] is not None) else None)
            django_record["fields"]["tag_status"] = record["status"]
            django_record["fields"]["tag_start_date"] = (
                str(record["start_date"]) if (
                    record["start_date"] is not None) else None)
            django_record["fields"]["tag_discovery_date"] = (
                str(record["discovery_date"]) if (
                    record["discovery_date"] is not None) else None)

            django_data.append(django_record)

        return django_data


if __name__ == '__main__':

    db = PortalDB(
        config_key=None,
        dburl="postgres://fnaldba:dbafnal@localhost/fnal", #[CMP] cannot be done due database changes
        #dburl="postgres://develdba:dbadevel@localhost/devel",
        debug=False
    )

    export = TagExport(db)
    file = open("json/tag.json", "w")
    file.write(simplejson.dumps(export.get_django_data(), ensure_ascii=False))
    file.close()
