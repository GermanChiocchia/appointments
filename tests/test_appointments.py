# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase

class test_appointments(TransactionCase):
    def test_appointment_generator_unico_false(self):
        esperado = 3
        obte = self.env['appointments.generador.turno'].appointment_generator('2020-01-24','2020-01-27')
        obtenido = len(obte)
        self.assertEqual(esperado, obtenido)

    def test_appointment_generator_unico_true(self):
        esperado = 4
        obte = self.env['appointments.generador.turno'].appointment_generator('2020-01-24','2020-01-27')
        obtenido = len(self.env['appointments.generador.turno'])
        self.assertEqual(esperado, obtenido)