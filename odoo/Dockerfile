# syntax = docker/dockerfile:1.2
FROM camptocamp/odoo-project:16.0-latest

COPY --chown=1000:1000 ./src /odoo/src
COPY --chown=1000:1000 ./VERSION /odoo/
COPY --chown=1000:1000 ./setup.py /odoo/
COPY --chown=1000:1000 ./requirements.txt /odoo/

RUN pip3 install -e /odoo
RUN pip3 install -e /odoo/src

# Project's specifics packages

RUN cd /odoo && pip3 install -r requirements.txt

ENV ADDONS_PATH=/odoo/external-src/enterprise,/odoo/external-src/custom,/odoo/src/addons
