#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simplejson
from tools.portaldb import PortalDB


class TileExport():

    def __init__(self, database):

        self.db = database

    def get_django_data(self):
        database_data = self.get_all_records()
        return self.get_django_data_from_database_data(database_data)

    def get_all_records(self):

        sql = (
            "SELECT"
            " tile_id,"
            " tilename,"
            " project,"
            " ra,"
            " dec,"
            " equinox,"
            " pixelsize,"
            " npix_ra,"
            " npix_dec,"
            " rall,"
            " decll,"
            " raul,"
            " decul,"
            " raur,"
            " decur,"
            " ralr,"
            " declr,"
            " urall,"
            " udecll,"
            " uraur,"
            " udecur"
            " FROM coadd.tiles"
            # [CMP] follow code remove duplicated tiles.
            # maybe better to select only DES tiles (project = 'DES')
            " WHERE tilename NOT IN"
            " (SELECT tilename"
            " FROM coadd.tiles"
            " GROUP BY tilename"
            " HAVING count(*) > 1)"
            " ORDER BY tile_id ASC;"
        )

        return self.db.fetchall_dict(sql, assoc=True)

    def get_django_data_from_database_data(self, database_data):

        django_data = list()

        for record in database_data:
            django_record = {}
            django_record["model"] = "coadd.tile"
            django_record["pk"] = record["tile_id"]
            django_record["fields"] = {}

            django_record["fields"]["tli_tilename"] = record["tilename"]
            django_record["fields"]["tli_project"] = record["project"]
            django_record["fields"]["tli_ra"] = record["ra"]
            django_record["fields"]["tli_dec"] = record["dec"]
            django_record["fields"]["tli_equinox"] = record["equinox"]
            django_record["fields"]["tli_pixelsize"] = record["pixelsize"]
            django_record["fields"]["tli_npix_ra"] = record["npix_ra"]
            django_record["fields"]["tli_npix_dec"] = record["npix_dec"]
            django_record["fields"]["tli_rall"] = record["rall"]
            django_record["fields"]["tli_decll"] = record["decll"]
            django_record["fields"]["tli_raul"] = record["raul"]
            django_record["fields"]["tli_decul"] = record["decul"]
            django_record["fields"]["tli_raur"] = record["raur"]
            django_record["fields"]["tli_decur"] = record["decur"]
            django_record["fields"]["tli_ralr"] = record["ralr"]
            django_record["fields"]["tli_declr"] = record["declr"]
            django_record["fields"]["tli_urall"] = record["urall"]
            django_record["fields"]["tli_udecll"] = record["udecll"]
            django_record["fields"]["tli_uraur"] = record["uraur"]
            django_record["fields"]["tli_udecur"] = record["udecur"]

            django_data.append(django_record)

        return django_data


if __name__ == '__main__':

    db = PortalDB(
        config_key=None,
        dburl="postgres://fnaldba:dbafnal@localhost/fnal",
        debug=False
    )

    export = TileExport(db)
    file = open("json/tile.json", "w")
    file.write(simplejson.dumps(export.get_django_data(), ensure_ascii=False))
    file.close()
