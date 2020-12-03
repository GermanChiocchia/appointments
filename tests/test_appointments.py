# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase

class test_appointments(TransactionCase):
    def test_appointment_generator_1(self):
        esperado = (4-1)*2      # esperado = (a-b)*n
        generator = self.env['appointments.generador.turno'].create({
            'date_start' : '2020-01-24',
            'date_end' : '2020-01-27',      #   a = date_end - date_start
            'state' : 'procesado'
        })
        self.env['appointments.dia.no.laboral'].create({
            'date_start' : '2020-01-24',
            'date_end' : '2020-01-24',      #   b = date_end - date_start   (no laboral)
        })
        generator.appointment_generator()   #   n = turnos simultaneos
        obtenido = len(generator.turnos_ids)
        self.assertEqual(esperado, obtenido)


    def test_appointment_generator_2(self):
        esperado = (5-1)*2      # esperado = (a-b)*n 
        generator = self.env['appointments.generador.turno'].create({
            'date_start' : '2020-01-24',
            'date_end' : '2020-01-28',      #   a = date_end - date_start
            'state' : 'procesado'    
        })
        self.env['appointments.dia.no.laboral'].create({
            'date_start' : '2020-01-24',
            'date_end' : '2020-01-24',      #   b = date_end - date_start   (no laboral)
        })
        generator.appointment_generator()   #   n = turnos simultaneos
        obtenido = len(generator.turnos_ids)
        self.assertEqual(esperado, obtenido)