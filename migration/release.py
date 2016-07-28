#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simplejson
from tools.portaldb import PortalDB


class ReleaseExport():

    def __init__(self, database):

        self.db = database

    def get_django_data(self):
        json_string = u'''[
    {
        "model":"coadd.release",
        "pk":1,
        "fields":{
            "rls_name":"y1_wide_survey",
            "rls_display_name":"Y1 Wide Survey",
            "rls_version":"v1.6",
            "rls_date":"2014-10-10",
            "rls_description":"A subset of Y1A1_COADD coadds in the Stripe82 and SPT regions.",
            "rls_doc_url":"https://deswiki.cosmology.illinois.edu/confluence/x/BgAi",
            "rls_default":true
        }
    },
    {
        "model":"coadd.release",
        "pk":2,
        "fields":{
            "rls_name":"y1_supplemental_d04",
            "rls_display_name":"Y1 Supplemental D04",
            "rls_version":"1.0",
            "rls_date":"2016-04-08",
            "rls_description":"A subset of Y1A1_COADD coadds in the COSMOS, VVDS and SN regions.",
            "rls_doc_url":"https://deswiki.cosmology.illinois.edu/confluence/x/BgAi",
            "rls_default":false
        }
    },
    {
        "model":"coadd.release",
        "pk":3,
        "fields":{
            "rls_name":"y1_supplemental_d10",
            "rls_display_name":"Y1 Supplemental D10",
            "rls_version":"1.0",
            "rls_date":"2016-04-08",
            "rls_description":"A subset of Y1A1_COADD coadds in the COSMOS, VVDS and SN regions.",
            "rls_doc_url":"https://deswiki.cosmology.illinois.edu/confluence/x/BgAi",
            "rls_default":false
        }
    },
    {
        "model":"coadd.release",
        "pk":4,
        "fields":{
            "rls_name":"y1_supplemental_dfull",
            "rls_display_name":"Y1 Supplemental DFULL",
            "rls_version":"1.0",
            "rls_date":"2016-04-08",
            "rls_description":"A subset of Y1A1_COADD coadds in the COSMOS, VVDS and SN regions.",
            "rls_doc_url":"https://deswiki.cosmology.illinois.edu/confluence/x/BgAi",
            "rls_default":false
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

    export = ReleaseExport(db)
    file = open("json/release.json", "w")
    file.write(simplejson.dumps(export.get_django_data(), ensure_ascii=False))
    file.close()
