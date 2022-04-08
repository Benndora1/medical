from odoo import models, fields

class MedicalForm(models.Model):
    _name = 'medical.form'

    name = fields.Char("Name of the patient:")
    d_o_b = fields.Date("Date of Birth:")
    blood_pressure = fields.Char("Blood Pressure:")
    tuberculosis = fields.Boolean("Tuberculosis")
    whopping = fields.Boolean("Whopping")
    tetanus = fields.Boolean("Tetanus")
    diabetes = fields.Boolean("Diabetes")
    polio = fields.Boolean("Poliomyelitis")
    diptheria = fields.Boolean("Diptheria")
    hepatitis = fields.Boolean("Hepatitis A/B & C")
    mouth_throat = fields.Boolean("Mouth & Throat")
    eyes_ears = fields.Boolean("Eyes & Ears")
    neck_head = fields.Boolean("Neck & Head")
    skin = fields.Boolean("Skin Condition")
    chest_lungs = fields.Boolean("Chest & Lungs")
    heart_blood_vessel = fields.Boolean("Heart & Blood Vessels")
    digestive_system = fields.Boolean("Digestive System")
    nervous = fields.Boolean("Nervous System")
    muscular_system = fields.Boolean("Skeletal Muscular System")
    reproductive_system = fields.Boolean("Urinary, Reproductive System")
    others = fields.Boolean("Others(Specify)")
    other_comments = fields.Text("Other Comments")