#!/bin/bash

if `test ! -d "$1"`
then
    echo "Usage: $0 <source> <dest>"
    echo "Example: $0 /archive/staging/DES/Y1A1_COADD/Y1A1_COADD_COSMOS_D04/pngs $HOME/thumbs/releases/Y1_SUPPLEMENTAL_D04/images/aladin/thumb"
    echo "Example: $0 /archive/staging/DES/Y1A1_COADD/Y1A1_COADD_SN_D04/pngs $HOME/thumbs/releases/Y1_SUPPLEMENTAL_D04/images/aladin/thumb"
    echo "Example: $0 /archive/staging/DES/Y1A1_COADD/Y1A1_COADD_VVDS14_D04/pngs $HOME/thumbs/releases/Y1_SUPPLEMENTAL_D04/images/aladin/thumb"
    exit 1
fi

BANDS=griYz
SRC_DIR=$1
DEST_DIR=$2

CURRENT_DIR=`pwd`

echo -n "${BANDS}" | while read -n 1
do
    BAND="${REPLY}"
    DIR="${BAND}"
    mkdir -p "${DEST_DIR}/${DIR}"

    echo "==== ${BAND} ===="
    cd "${SRC_DIR}"

    for THUMB in *"_${BAND}_thumb.png"
    do
        if `test -f "${THUMB}"`
        then
            THUMB_DEST=`echo "${THUMB}" | cut -d '_' -f 1`
            echo "${THUMB}" '-->' "${DEST_DIR}/${DIR}/${THUMB_DEST}.png"
            cp "${THUMB}" "${DEST_DIR}/${DIR}/${THUMB_DEST}.png"
            if test "$?" -ne 0
            then
                echo >&2 "ERROR, exit."
                exit 1
            fi
        fi
    done
done



BAND="RGB"
DIR="irg"
mkdir -p "${DEST_DIR}/${DIR}"

echo "==== ${BAND} ===="
cd "${SRC_DIR}"

for THUMB in *"_${BAND}_thumb.png"
do
    if `test -f "${THUMB}"`
    then
        THUMB_DEST=`echo "${THUMB}" | cut -d '_' -f 1`
        echo "${THUMB}" '-->' "${DEST_DIR}/${DIR}/${THUMB_DEST}.png"
        cp "${THUMB}" "${DEST_DIR}/${DIR}/${THUMB_DEST}.png"
        if test "$?" -ne 0
        then
            echo >&2 "ERROR, exit."
            exit 1
        fi
    fi
done

cd $CURRENT_DIR



# End

