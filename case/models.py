from django.db import models
from account.models import User
from location.models import Region, City, Neighborhood

# Create your models here.

class Case(models.Model):
    # case_number = models.AutoField(primary_key=True, default=10000, null=True)
    realEstate  = models.OneToOneField('RealEstate', on_delete=models.CASCADE)
    status      = models.ManyToManyField('Status', through='CaseStatus')
    user        = models.ManyToManyField(User, through='UserCase')
    # inspector   = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at  = models.DateTimeField(verbose_name='Created at', auto_now_add=True)

    def __str__(self):
        return "{}".format(self.pk)
    
    def get_the_inspector(self):
        # user = 
        inspector = self.user.filter(groups__name = 'المعاينين')
        if inspector.exists():
            return "{0}\n{1}".format(inspector.first().get_full_name(), inspector.first().phone)
        return "لم يتم تسجيل أي معاين للمعاملة"



class UserCase(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    case_id = models.ForeignKey(Case, on_delete=models.CASCADE)
    create_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1}".format(self.user_id, self.case_id)



class Status(models.Model):
    status_for = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status_for+' - '+self.status


class CaseStatus(models.Model):
    case    = models.ForeignKey(Case, on_delete=models.CASCADE)
    status  = models.ForeignKey(Status, on_delete=models.CASCADE)
    isActive= models.BooleanField(default=True)
    dataEntryUpdate = models.DateTimeField(blank=True, null=True)
    InspectorUpdate = models.DateTimeField(blank=True, null=True)
    create_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} - {1}".format(self.case, self.status)



class ArchitecturalDesign(models.Model):
    architectural_design = models.CharField(max_length=15)

    def __str__(self):
        return self.architectural_design


class PublicLocation(models.Model):
    public_location_name = models.CharField(max_length=15)

    def __str__(self):
        return self.public_location_name


class Slope(models.Model):
    slope = models.CharField(max_length=15)

    def __str__(self):
        return self.slope


class StreetCondition(models.Model):
    street_condition = models.CharField(max_length=15)

    def __str__(self):
        return self.street_condition


class SkeletonStructure(models.Model):
    skeleton_structure = models.CharField(max_length=20)

    def __str__(self):
        return self.skeleton_structure


class CeillingType(models.Model):
    ceilling_type = models.CharField(max_length=20)

    def __str__(self):
        return self.ceilling_type


class Facade(models.Model):
    facade = models.CharField(max_length=20)

    def __str__(self):
        return self.facade

class Utility(models.Model):
    utility = models.CharField(max_length=20)

    def __str__(self):
        return self.utility


class WallCondition(models.Model):
    wall_condition = models.CharField(max_length=20)

    def __str__(self):
        return self.wall_condition


class Ground_SidewalkCondition(models.Model):
    ground_sidewalk = models.CharField(max_length=20)

    def __str__(self):
        return self.ground_sidewalk


############## Function to Customize uploading file ################
from datetime import datetime
import random
def Outside_Fences_7oashCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}'.format(instance.Case.id, "Outside_Fences_7oash", filename)
############################ End Function###########################

class Outside_Fences_7oash(models.Model):
    ground_condition = models.ForeignKey(Ground_SidewalkCondition, related_name="OutsideFencesGround", on_delete=models.CASCADE)
    sidewalk_condition = models.ForeignKey(Ground_SidewalkCondition, related_name="OutsideFencesSidewalk", on_delete=models.CASCADE)
    wall_condition = models.ForeignKey(WallCondition, on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to=Outside_Fences_7oashCustomization)
    picture2 = models.ImageField(upload_to=Outside_Fences_7oashCustomization)
    picture3 = models.ImageField(upload_to=Outside_Fences_7oashCustomization)
    picture4 = models.ImageField(upload_to=Outside_Fences_7oashCustomization)
    picture5 = models.ImageField(upload_to=Outside_Fences_7oashCustomization)
    



class InsulationType(models.Model):
    insulationType = models.CharField(max_length=20)

    def __str__(self):
        return self.insulationType



class FencesCondition(models.Model):
    fences_condition = models.CharField(max_length=20)

    def __str__(self):
        return self.fences_condition


class TankInsulatorCondition(models.Model):
    tank_insulator_condition = models.CharField(max_length=20)

    def __str__(self):
        return self.tank_insulator_condition


############## Function to Customize uploading file ################
def RoofCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}'.format(instance.Case.id, 'Roof', filename)
############################ End Function###########################

class Roof(models.Model):
    fences_condition    = models.ForeignKey(FencesCondition, on_delete=models.CASCADE)
    ground_condition    = models.ForeignKey(Ground_SidewalkCondition, on_delete=models.CASCADE)
    tank_insulator_condition = models.ForeignKey(TankInsulatorCondition, on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to=RoofCustomization)
    picture2 = models.ImageField(upload_to=RoofCustomization)
    picture3 = models.ImageField(upload_to=RoofCustomization)
    picture4 = models.ImageField(upload_to=RoofCustomization)
    picture5 = models.ImageField(upload_to=RoofCustomization)


class WindowDoorCondition(models.Model):
    window_door_condition = models.CharField(max_length=20)

    def __str__(self):
        return self.window_door_condition


############## Function to Customize uploading file ################
def TopGarageCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}'.format(instance.Case.id, 'TopGarage', filename)
############################ End Function###########################

class TopGarage(models.Model):
    wall_ceiling_condition  = models.ForeignKey(WallCondition, on_delete=models.CASCADE)
    window_door_condition   = models.ForeignKey(WindowDoorCondition, on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to=TopGarageCustomization)
    picture2 = models.ImageField(upload_to=TopGarageCustomization)
    picture3 = models.ImageField(upload_to=TopGarageCustomization)
    picture4 = models.ImageField(upload_to=TopGarageCustomization)
    picture5 = models.ImageField(upload_to=TopGarageCustomization)

class FilterCondition(models.Model):
    filter_condition = models.CharField(max_length=20)

    def __str__(self):
        return self.filter_condition


############## Function to Customize uploading file ################
def FilterCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}'.format(instance.Case.id, 'Filter', filename)
############################ End Function###########################

class SwimPool(models.Model):
    ground_condition= models.ForeignKey(Ground_SidewalkCondition, on_delete=models.CASCADE)
    filter_condition= models.ForeignKey(FilterCondition, on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to=FilterCustomization)
    picture2 = models.ImageField(upload_to=FilterCustomization)
    picture3 = models.ImageField(upload_to=FilterCustomization)
    picture4 = models.ImageField(upload_to=FilterCustomization)
    picture5 = models.ImageField(upload_to=FilterCustomization)



############## Function to Customize uploading file ################
def HallwaysCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}'.format(instance.Case.id, 'Hallways', filename)
############################ End Function###########################

class Hallways(models.Model):
    illumination_condition    = models.ForeignKey(FilterCondition, on_delete=models.CASCADE)
    ground_condition    = models.ForeignKey(Ground_SidewalkCondition, on_delete=models.CASCADE)
    wall_roof_condition = models.ForeignKey(WallCondition, on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to=HallwaysCustomization)
    picture2 = models.ImageField(upload_to=HallwaysCustomization)
    picture3 = models.ImageField(upload_to=HallwaysCustomization)
    picture4 = models.ImageField(upload_to=HallwaysCustomization)
    picture5 = models.ImageField(upload_to=HallwaysCustomization)


############## Function to Customize uploading file ################
def GardenCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}'.format(instance.Case.id, 'Garden', filename)
############################ End Function###########################

class Garden(models.Model):
    illumination_condition= models.ForeignKey(FilterCondition, related_name="garden_illumination_condition", on_delete=models.CASCADE)
    ground_condition      = models.ForeignKey(Ground_SidewalkCondition, on_delete=models.CASCADE)
    system_condition      = models.ForeignKey(FilterCondition, related_name="garden_system_condition", on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to=GardenCustomization)
    picture2 = models.ImageField(upload_to=GardenCustomization)
    picture3 = models.ImageField(upload_to=GardenCustomization)
    picture4 = models.ImageField(upload_to=GardenCustomization)
    picture5 = models.ImageField(upload_to=GardenCustomization)



############## Function to Customize uploading file ################
def OutsideGarageCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}'.format(instance.Case.id, 'OutsideGarage', filename)
############################ End Function###########################

class OutsideGarage(models.Model):
    wall_ceiling_condition    = models.ForeignKey(WallCondition, related_name="outsideDarage_wall_ceiling_condition", on_delete=models.CASCADE)
    windows_doors_condition    = models.ForeignKey(WindowDoorCondition, on_delete=models.CASCADE)
    accessories_condition = models.ForeignKey(WallCondition, related_name="outsideDarage_accessories_condition", on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to=OutsideGarageCustomization)
    picture2 = models.ImageField(upload_to=OutsideGarageCustomization)
    picture3 = models.ImageField(upload_to=OutsideGarageCustomization)
    picture4 = models.ImageField(upload_to=OutsideGarageCustomization)
    picture5 = models.ImageField(upload_to=OutsideGarageCustomization)


class Ground(models.Model):
    ground = models.CharField(max_length=20)

    def __str__(self):
        return self.ground


############## Function to Customize uploading file ################
def HoashGroundCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}'.format(instance.Case.id, 'HoashGround', filename)
############################ End Function###########################

class HoashGround(models.Model):
    ground      = models.ForeignKey(Ground, on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to=HoashGroundCustomization)
    picture2 = models.ImageField(upload_to=HoashGroundCustomization)
    picture3 = models.ImageField(upload_to=HoashGroundCustomization)
    picture4 = models.ImageField(upload_to=HoashGroundCustomization)
    picture5 = models.ImageField(upload_to=HoashGroundCustomization)
    other_ground= models.CharField(max_length=50, blank=True, null=True, default="")


############## Function to Customize uploading file ################
def BasementCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}'.format(instance.Case.id, "Basement", filename)
############################ End Function###########################

class Basement(models.Model):
    ground_condition = models.ForeignKey(Ground_SidewalkCondition, on_delete=models.CASCADE)
    wall_ceiling_condition = models.ForeignKey(WallCondition, on_delete=models.CASCADE)
    ventilation_condition = models.ForeignKey(FilterCondition, on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to=BasementCustomization)
    picture2 = models.ImageField(upload_to=BasementCustomization)
    picture3 = models.ImageField(upload_to=BasementCustomization)
    picture4 = models.ImageField(upload_to=BasementCustomization)
    picture5 = models.ImageField(upload_to=BasementCustomization)
    


############## Function to Customize uploading file ################
def ElevatorCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}'.format(instance.Case.id, "Elevator", filename)
############################ End Function###########################

class Elevator(models.Model):
    elevator_condition      = models.ForeignKey(FilterCondition, on_delete=models.CASCADE)
    illumination_condition  = models.ForeignKey(FilterCondition, related_name="elevator_illumination_condition", on_delete=models.CASCADE)
    ventilation_condition   = models.ForeignKey(FilterCondition, related_name="elevator_ventilation_condition", on_delete=models.CASCADE)
    picture1 = models.ImageField(upload_to=ElevatorCustomization)
    picture2 = models.ImageField(upload_to=ElevatorCustomization)
    picture3 = models.ImageField(upload_to=ElevatorCustomization)
    picture4 = models.ImageField(upload_to=ElevatorCustomization)
    picture5 = models.ImageField(upload_to=ElevatorCustomization)
    



# class Coordinations(models.Model):
#     # real_estate            = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
#     north_direction_value  = models.DecimalField(verbose_name="شمال", max_digits=10, decimal_places=3)   
#     north_length           = models.DecimalField(verbose_name="بطول", max_digits=10, decimal_places=3)
#     west_direction_value   = models.DecimalField(verbose_name="غرب", max_digits=10, decimal_places=3)   
#     west_length            = models.DecimalField(verbose_name="بطول", max_digits=10, decimal_places=3)
#     south_direction_value  = models.DecimalField(verbose_name="جنوب", max_digits=10, decimal_places=3)   
#     south_length           = models.DecimalField(verbose_name="بطول", max_digits=10, decimal_places=3)
#     east_direction_value   = models.DecimalField(verbose_name="شرق", max_digits=10, decimal_places=3)   
#     east_length            = models.DecimalField(verbose_name="بطول", max_digits=10, decimal_places=3)






############## Function to Customize uploading file ################
def StreetConditionCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % ('street_condtion', ext)
    return 'case_{0}/{1}/{2}'.format(instance.Case.id, 'Street', filename)
############################ End Function###########################

############## Function to Customize uploading file ################
def FacadeImgCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % ('facade',str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}'.format(instance.Case.id, 'Facade', filename)
############################ End Function###########################


class RealEstate(models.Model):
    # fulfilled by coordinator
    contact_name    = models.CharField(verbose_name= "اسم رقم التواصل", max_length=50)
    contact_number  = models.BigIntegerField(verbose_name= "رقم التواصل")
    agent_name      = models.CharField(max_length=15,default='وزارة الإسكان', editable=False)
    region_id       = models.ForeignKey(Region, verbose_name= "المنطقة", on_delete=models.CASCADE)
    city_id         = models.ForeignKey(City, verbose_name= "المدينة", on_delete=models.CASCADE)
    neighborhood_id = models.ForeignKey(Neighborhood, verbose_name= "الحي", on_delete=models.CASCADE)
    location        = models.URLField(verbose_name="الموقع", blank=True, null= True)
    coordinator_note= models.TextField(verbose_name="الملاحظات ( إذا وجدت )", blank=True, null=True, default='لا توجد')

    # fulfilled by dataEntry
    # coordinations   = name = models.OneToOneField(Coordinations, verbose_name="الحدود", on_delete=models.CASCADE, blank=True, null=True)
    north_direction_value  = models.CharField(verbose_name="شمال", max_length=100, blank=True, null=True)   
    north_length           = models.CharField(verbose_name="بطول", max_length=50, blank=True, null=True)
    west_direction_value   = models.CharField(verbose_name="غرب", max_length=100, blank=True, null=True)   
    west_length            = models.CharField(verbose_name="بطول", max_length=50, blank=True, null=True)
    south_direction_value  = models.CharField(verbose_name="جنوب", max_length=100, blank=True, null=True)   
    south_length           = models.CharField(verbose_name="بطول", max_length=50, blank=True, null=True)
    east_direction_value   = models.CharField(verbose_name="شرق", max_length=100, blank=True, null=True)   
    east_length            = models.CharField(verbose_name="بطول", max_length=50, blank=True, null=True)
    owner_name      = models.CharField(verbose_name="اسم المالك", max_length=50, blank=True, null=True)
    deed_number     = models.CharField(verbose_name="رقم الصك", max_length=15, blank=True, null=True)
    deed_date       = models.DateField(verbose_name="تاريخ الصك", blank=True, null=True)
    notary          = models.CharField(verbose_name="كتابة عدل", max_length=50, blank=True, null=True)
    outline_number  = models.CharField(verbose_name="رقم المخطط", max_length=15, blank=True, null=True)
    outline_name    = models.CharField(verbose_name="اسم المخطط", max_length=50, blank=True, null=True)
    piece_number    = models.CharField(verbose_name="رقم القطعة", max_length=15, blank=True, null=True)
    area            = models.DecimalField(verbose_name="المساحة", max_digits=10, decimal_places=2, blank=True, null=True)
    license_number  = models.CharField(verbose_name="رقم الرخصة", max_length=15, blank=True, null=True)
    license_date    = models.DateField(verbose_name="تاريخ الرخصة", blank=True, null=True)
    dataEntry_note  = models.TextField(verbose_name="الملاحظات ( إذا وجدت )", blank=True, null=True)
    
    # fulfilled by Inspector
    public_location         = models.ForeignKey(PublicLocation, verbose_name="الموقع العام", on_delete=models.CASCADE, blank=True, null=True)
    architectural_design    = models.ForeignKey(ArchitecturalDesign, verbose_name="التصميم المعماري", on_delete=models.CASCADE, blank=True, null=True)
    slope                   = models.ForeignKey(Slope, verbose_name="المنسوب", on_delete=models.CASCADE, blank=True, null=True)
    street_condition        = models.ForeignKey(StreetCondition, verbose_name="الشوارع", on_delete=models.CASCADE, blank=True, null=True)
    street_condition_pic    = models.ImageField(verbose_name="صورة الشارع", upload_to=StreetConditionCustomization, blank=True, null=True)
    nearest_street_name     = models.CharField(verbose_name="اسم أقرب شارع", max_length=50, blank=True, null=True)
    distance_nearest_street = models.DecimalField(verbose_name="على بعد", max_digits=10, decimal_places=3, blank=True, null=True)
    skeleton_structure      = models.ForeignKey(SkeletonStructure, verbose_name="الهيكل الأنشائي", on_delete=models.CASCADE, blank=True, null=True)
    ceiling_type            = models.ForeignKey(CeillingType, verbose_name="نوع الأسقف", on_delete=models.CASCADE, blank=True, null=True)
    facade                  = models.ManyToManyField(Facade, verbose_name="الواجهات", through="FacadeRealEstate")
    utility                 = models.ManyToManyField(Utility, verbose_name="الخدمات")
    outside_fences          = models.OneToOneField(Outside_Fences_7oash, verbose_name="الأسوار الخارجية والأحواش", on_delete=models.CASCADE, blank=True, null=True)
    insulation_type         = models.ForeignKey(InsulationType, verbose_name="أنواع العزل", on_delete=models.CASCADE, blank=True, null=True)
    roof                    = models.ForeignKey(Roof, verbose_name="السطح", on_delete=models.CASCADE, blank=True, null=True)
    top_garage              = models.ForeignKey(TopGarage, verbose_name="الملحق العلوي", on_delete=models.CASCADE, blank=True, null=True)
    swim_pool               = models.ForeignKey(SwimPool, verbose_name="المسبح", on_delete=models.CASCADE, blank=True, null=True)
    hoash_ground            = models.ForeignKey(HoashGround, verbose_name="أرضية الحوش", on_delete=models.CASCADE, blank=True, null=True)
    garden                  = models.ForeignKey(Garden, verbose_name="الحديقة", on_delete=models.CASCADE, blank=True, null=True)
    basement                = models.ForeignKey(Basement, verbose_name="القبو", on_delete=models.CASCADE, blank=True, null=True)
    elevator                = models.ForeignKey(Elevator, verbose_name="المصعد", on_delete=models.CASCADE, blank=True, null=True)
    before_entring_building_note    = models.TextField(verbose_name="ملاحظات قبل دخول العقار", blank=True, null=True)
    after_entring_building_note     = models.TextField(verbose_name="ملاحظات بعد دخول العقار", blank=True, null=True)
    roof_note               = models.TextField(verbose_name="ملاحظات السطح و الملحق العلوي", blank=True, null=True)

    # fulfilled by Evaluator
    real_estate_age         = models.DecimalField(verbose_name="عمر العقار", max_digits=5, decimal_places=2, blank=True, null=True)



    def __str__(self):
        return "{}".format(self.deed_number)






class FacadeRealEstate(models.Model):
    facade      = models.ForeignKey(Facade, on_delete=models.CASCADE)
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    picture     = models.ImageField(upload_to="FacadeImgCustomization")
    other_facade= models.CharField(max_length=20)

    def __str__(self):
        return self.real_estate



############## Function to Customize uploading file ################
def RealEstateDocumentCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (instance.document_type, ext)
    return 'case_{0}/{1}/{2}'.format(instance.realEstate.case.id, 'documents', filename)
############################ End Function###########################

class RealEstateDocument(models.Model):
    realEstate = models.ForeignKey(RealEstate,on_delete=models.CASCADE)
    document_type = models.CharField(max_length=50)
    document = models.FileField(upload_to=RealEstateDocumentCustomization)
    
    def __str__(self):
        return self.document_type

    def delete(self, *args, **kwargs):
        self.document.delete()
        super().delete(*args,**kwargs)



class Floor(models.Model):
    real_estate = models.ForeignKey(RealEstate, on_delete=models.CASCADE)
    floor       = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.floor


class UnitType(models.Model):
    unit_type = models.CharField(max_length=15)

    def __str__(self):
        return self.unit_type


class UnitCondition(models.Model):
    unit_condition = models.CharField(max_length=15)

    def __str__(self):
        return self.unit_condition


class Door(models.Model):
    door_type = models.CharField(max_length=20)

    def __str__(self):
        return self.door_type



############## Function to Customize uploading file ################
def ReceptionistGroundCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}/{3}'.format(instance.Case.id, instance.unit.unit_number, 'ReceptionistGround', filename)
############################ End Function###########################

class ReceptionistGround(models.Model):
    ground      = models.ForeignKey(Ground, on_delete=models.CASCADE)
    picture1    = models.ImageField(upload_to=ReceptionistGroundCustomization)
    picture2    = models.ImageField(upload_to=ReceptionistGroundCustomization)
    picture3    = models.ImageField(upload_to=ReceptionistGroundCustomization)
    picture4    = models.ImageField(upload_to=ReceptionistGroundCustomization, blank=True, null=True)
    picture5    = models.ImageField(upload_to=ReceptionistGroundCustomization, blank=True, null=True)
    other_receptionist_ground = models.CharField(max_length=50, blank=True, null=True)



############## Function to Customize uploading file ################
def RoomsGroundCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}/{3}'.format(instance.Case.id, instance.unit.unit_number, 'RoomsGround', filename)
############################ End Function###########################

class RoomsGround(models.Model):
    ground      = models.ForeignKey(Ground, on_delete=models.CASCADE)
    picture1    = models.ImageField(upload_to=RoomsGroundCustomization)
    picture2    = models.ImageField(upload_to=RoomsGroundCustomization)
    picture3    = models.ImageField(upload_to=RoomsGroundCustomization)
    picture4    = models.ImageField(upload_to=RoomsGroundCustomization, blank=True, null=True)
    picture5    = models.ImageField(upload_to=RoomsGroundCustomization, blank=True, null=True)
    other_rooms_ground = models.CharField(max_length=50, blank=True, null=True)
    

############## Function to Customize uploading file ################
def EntranceGroundCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}/{3}'.format(instance.Case.id, instance.unit.unit_number, 'EntranceGround', filename)
############################ End Function###########################

class EntranceGround(models.Model):
    ground      = models.ForeignKey(Ground, on_delete=models.CASCADE)
    picture1    = models.ImageField(upload_to=EntranceGroundCustomization)
    picture2    = models.ImageField(upload_to=EntranceGroundCustomization)
    picture3    = models.ImageField(upload_to=EntranceGroundCustomization)
    picture4    = models.ImageField(upload_to=EntranceGroundCustomization, blank=True, null=True)
    picture5    = models.ImageField(upload_to=EntranceGroundCustomization, blank=True, null=True)
    other_entrance_ground = models.CharField(max_length=50, blank=True, null=True)


class AirConditionType(models.Model):
    air_condition_type = models.CharField(max_length=20)

    def __str__(self):
        return self.air_condition_type


class Unit(models.Model):
    floor           = models.ForeignKey(Floor, on_delete=models.CASCADE)
    unit_number     = models.SmallIntegerField(default=0)
    unit_type       = models.ForeignKey(UnitType, on_delete=models.CASCADE)
    unit_condition  = models.ForeignKey(UnitCondition, on_delete=models.CASCADE)
    outside_door    = models.ForeignKey(Door, related_name="unit_outside_door", on_delete=models.CASCADE)
    inside_door     = models.ForeignKey(Door, related_name="unit_inside_door", on_delete=models.CASCADE)
    receptionist_ground = models.ForeignKey(ReceptionistGround, on_delete=models.CASCADE)
    rooms_ground    = models.ForeignKey(RoomsGround, on_delete=models.CASCADE)
    entrance_ground = models.ForeignKey(EntranceGround, on_delete=models.CASCADE)

    ############### Is exist ? ##############

    double_wall     = models.BooleanField(default=False)
    double_glass    = models.BooleanField(default=False)
    gibs_in_roof    = models.BooleanField(default=False)
    hidden_lighting = models.BooleanField(default=False)
    stairs          = models.BooleanField(default=False)
    electric_garage = models.BooleanField(default=False)
    normal_garage   = models.BooleanField(default=False)
    doors           = models.BooleanField(default=False)
    elevator        = models.BooleanField(default=False)
    elevator_count  = models.SmallIntegerField(default=0)
    arabic_bathroom = models.BooleanField(default=False)
    arabic_bathroom_count = models.SmallIntegerField(default=0)
    heater          = models.BooleanField(default=False)
    heater_count    = models.SmallIntegerField(default=0)
    westorn_bathroom= models.BooleanField(default=False)
    westorn_bathroom_count = models.SmallIntegerField(default=0)

    ############ End of Is exist ? ##########

    air_condition_type = models.ManyToManyField(AirConditionType, through="AirConditionTypeUnit")

    def __str__(self):
        return self.unit_number



############## Function to Customize uploading file ################
def AirConditionTypeUnitCustomization(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (str(int(datetime.now().timestamp()+random.randrange(100000000,999999999))), ext)
    return 'case_{0}/{1}/{2}/{3}'.format(instance.Case.id, instance.unit.unit_number, 'AirConditionTypeUnit', filename)
############################ End Function###########################

class AirConditionTypeUnit(models.Model):
    air_condition_type  = models.ForeignKey(AirConditionType, on_delete=models.CASCADE)
    unit                = models.ForeignKey(Unit, on_delete=models.CASCADE)
    picture             = models.ImageField(upload_to=EntranceGroundCustomization)