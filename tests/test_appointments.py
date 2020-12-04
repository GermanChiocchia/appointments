# -*- coding: utf-8 -*-
from odoo.tests import TransactionCase

class test_appointments(TransactionCase):
    def test_appointment_generator_1(self):
        esperado = 2*(4-1)*9%1      # esperado = n*(a-b)*h%r
        generator = self.env['appointments.generador.turno'].create({
            'date_start' : '2020-01-24',
            'date_end' : '2020-01-27',      #   a = date_end - date_start
            'state' : 'procesado'
        })
        self.env['appointments.dia.no.laboral'].create({
            'date_start' : '2020-01-24',
            'date_end' : '2020-01-24',      #   b = date_end - date_start   (no laboral)
        })
        self.env.user.company_id.create({
            'name' : 'test',
            'appointment_qty' : '2',        #   n = turnos simultaneos
            'appointment_duration' : '1',   #   r = duracion del turno
            'start_time' : '08.00',
            'end_time' : '17.00'            #   h = end_time - start_time
        })
        generator.appointment_generator()
        obtenido = len(generator.turnos_ids)
        self.assertEqual(esperado, obtenido)


    def test_appointment_generator_2(self):
        esperado = 2*(5-1)*9%1      # esperado = n*(a-b)*h%r 
        generator = self.env['appointments.generador.turno'].create({
            'date_start' : '2020-01-24',
            'date_end' : '2020-01-28',      #   a = date_end - date_start   
        })
        self.env['appointments.dia.no.laboral'].create({
            'date_start' : '2020-01-24',
            'date_end' : '2020-01-24',      #   b = date_end - date_start   (no laboral)
        })
        self.env['res.company'].create({
            'name' : 'name',
            'appointment_qty' : '2',        #   n = turnos simultaneos
            'appointment_duration' : '1',   #   r = duracion del turno
            'start_time' : '08.00',
            'end_time' : '17.00'            #   h = end_time - start_time
        })
        generator.appointment_generator()
        obtenido = len(generator.turnos_ids)
        self.assertEqual(esperado, obtenido)