# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase

class test_appointments(TransactionCase):
    def test_appointment_generator_unico_false(self):
        esperado = 4
        generator = self.env['appointments.generador.turno'].create({
            'date_start' : '2020-01-24',
            'date_end' : '2020-01-27',
            'state' : 'procesado'
        })
        generator.appointment_generator()
        obtenido = len(generator.turnos_ids)
        self.assertEqual(esperado, obtenido)

    def test_appointment_generator_unico_true(self):
        esperado = 5
        generator = self.env['appointments.generador.turno'].create({
            'date_start' : '2020-01-24',
            'date_end' : '2020-01-28',
            'state' : 'procesado'
        })
        generator.appointment_generator()
        obtenido = len(generator.turnos_ids)
        self.assertEqual(esperado, obtenido)