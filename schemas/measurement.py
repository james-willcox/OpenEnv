from ma import ma
from models.measurement import MeasurementModel

class MeasurementSchema(ma.ModelSchema):
    class Meta:
        model = MeasurementModel