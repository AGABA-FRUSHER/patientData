# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountType(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    start_range = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'account_type'


class AdministeredAncillaryCare(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_at = models.CharField(max_length=255, blank=True, null=True)
    administered_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='administered_ancillary_care')
    administered_on = models.DateTimeField(blank=True, null=True)
    ancillary_care = models.ForeignKey('AncillaryCare', models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='administered_ancillary_care_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_ancillary_care = models.ForeignKey('PatientAncillaryCare', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'administered_ancillary_care'


class AdministeredAncillaryCareBillableItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_ancillary_care = models.ForeignKey(AdministeredAncillaryCare, models.DO_NOTHING)
    billing_date = models.DateTimeField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    invoice_line = models.ForeignKey('InvoiceLine', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'administered_ancillary_care_billable_item'


class AdministeredAncillaryCareInventoryItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_ancillary_care = models.ForeignKey(AdministeredAncillaryCare, models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    cost_of_goods_sold_journal_entry = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='cost_of_goods_sold_ancillary_care_items')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    inventory_audit = models.ForeignKey('InventoryAudit', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_ancillary_care = models.ForeignKey('PatientAncillaryCare', models.DO_NOTHING)
    stock_control_journal_entry = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='stock_control_ancillary_care_items')
    usage_date = models.DateTimeField()
    void_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administered_ancillary_care_inventory_item'


class AdministeredFamilyPlanning(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_at = models.CharField(max_length=255, blank=True, null=True)
    administered_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='administered_family_planning')
    administered_on = models.DateTimeField(blank=True, null=True)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_family_planning')
    date_created = models.DateTimeField(blank=True, null=True)
    family_planning = models.ForeignKey('FamilyPlanning', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_family_planning = models.ForeignKey('PatientFamilyPlanning', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'administered_family_planning'


class AdministeredFamilyPlanningBillableItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_family_planning = models.ForeignKey(AdministeredFamilyPlanning, models.DO_NOTHING)
    billing_date = models.DateTimeField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    invoice_line = models.ForeignKey('InvoiceLine', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'administered_family_planning_billable_item'


class AdministeredFamilyPlanningInventoryItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_family_planning = models.ForeignKey(AdministeredFamilyPlanning, models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    cost_of_goods_sold_journal_entry = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='cost_of_goods_sold_family_planning_items')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    inventory_audit = models.ForeignKey('InventoryAudit', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_family_planning = models.ForeignKey('PatientFamilyPlanning', models.DO_NOTHING)
    stock_control_journal_entry = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='stock_control_family_planning_items')
    usage_date = models.DateTimeField()
    void_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administered_family_planning_inventory_item'


class AdministeredPrescription(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='administered_prescriptions')
    administered_on = models.DateTimeField(blank=True, null=True)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_prescriptions')
    date_created = models.DateTimeField(blank=True, null=True)
    dosage = models.CharField(max_length=255)
    drug = models.ForeignKey('Product', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    prescription = models.ForeignKey('PatientDrug', models.DO_NOTHING)
    route = models.CharField(max_length=17)

    class Meta:
        managed = False
        db_table = 'administered_prescription'


class AdministeredPrescriptionBillableItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_prescription = models.ForeignKey(AdministeredPrescription, models.DO_NOTHING)
    billing_date = models.DateTimeField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    invoice_line = models.ForeignKey('InvoiceLine', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'administered_prescription_billable_item'


class AdministeredPrescriptionInventoryItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_prescription = models.ForeignKey(AdministeredPrescription, models.DO_NOTHING, blank=True, null=True)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    cost_of_goods_sold_journal_entry = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='cost_of_goods_sold_prescription_items')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    inventory_audit = models.ForeignKey('InventoryAudit', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    prescription = models.ForeignKey('PatientDrug', models.DO_NOTHING)
    stock_control_journal_entry = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='stock_control_prescription_items')
    usage_date = models.DateTimeField()
    void_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administered_prescription_inventory_item'


class AdministeredTreatment(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_at = models.CharField(max_length=255, blank=True, null=True)
    administered_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='administered_treatments')
    administered_on = models.DateTimeField(blank=True, null=True)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_treatments')
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_minor_theater = models.ForeignKey('PatientMinorTheater', models.DO_NOTHING)
    treatment = models.ForeignKey('MinorTheater', models.DO_NOTHING)
    adverse_event = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administered_treatment'


class AdministeredTreatmentBillableItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_treatment = models.ForeignKey(AdministeredTreatment, models.DO_NOTHING)
    billing_date = models.DateTimeField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    invoice_line = models.ForeignKey('InvoiceLine', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'administered_treatment_billable_item'


class AdministeredTreatmentInventoryItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_treatment = models.ForeignKey(AdministeredTreatment, models.DO_NOTHING, blank=True, null=True)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    cost_of_goods_sold_journal_entry = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='cost_of_goods_sold_treatment_items')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    inventory_audit = models.ForeignKey('InventoryAudit', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_minor_theater = models.ForeignKey('PatientMinorTheater', models.DO_NOTHING)
    stock_control_journal_entry = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='stock_control_treatment_items')
    usage_date = models.DateTimeField()
    void_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administered_treatment_inventory_item'


class AdministeredVaccine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='administered_vaccines')
    administered_in_premise = models.BooleanField()
    administered_on = models.DateTimeField(blank=True, null=True)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    clinic_session = models.ForeignKey('ClinicSession', models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_vaccines')
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    vaccine = models.ForeignKey('Vaccine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'administered_vaccine'


class AdministeredVaccineBillableItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_vaccine = models.ForeignKey(AdministeredVaccine, models.DO_NOTHING)
    billing_date = models.DateTimeField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    invoice_line = models.ForeignKey('InvoiceLine', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'administered_vaccine_billable_item'


class AdministeredVaccineInventoryItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_vaccine = models.ForeignKey(AdministeredVaccine, models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    cost_of_goods_sold_journal_entry = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='cost_of_goods_sold_vaccine_items')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    inventory_audit = models.ForeignKey('InventoryAudit', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    stock_control_journal_entry = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='stock_control_vaccine_items')
    usage_date = models.DateTimeField()
    vaccine = models.ForeignKey('Vaccine', models.DO_NOTHING)
    void_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'administered_vaccine_inventory_item'


class AdmissionBillableItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    billing_date = models.DateTimeField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField()
    invoice_line = models.ForeignKey('InvoiceLine', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    patient_admission = models.ForeignKey('PatientAdmission', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'admission_billable_item'


class AdmissionInventoryItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    cost_of_goods_sold_journal_entry = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='cost_of_goods_sold_admission_items')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    inventory_audit = models.ForeignKey('InventoryAudit', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_admission = models.ForeignKey('PatientAdmission', models.DO_NOTHING)
    stock_control_journal_entry = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='stock_control_admission_items')
    usage_date = models.DateTimeField()
    void_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'admission_inventory_item'


class Allergen(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    remarks = models.TextField(blank=True, null=True)
    system_defined = models.BooleanField()
    type = models.CharField(max_length=13)

    class Meta:
        managed = False
        db_table = 'allergen'


class AncillaryCare(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    ancillary_care_category = models.ForeignKey('AncillaryCareCategory', models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ancillary_care'
        unique_together = (('branch', 'name'),)


class AncillaryCareCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ancillary_care_category'
        unique_together = (('branch', 'name'),)


class Announcement(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='announcements_created')
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField()
    expiry_date = models.DateTimeField(blank=True, null=True)
    is_public_announcement = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    processed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='announcements_processed')
    processing_comment = models.CharField(max_length=255, blank=True, null=True)
    processing_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=9)
    topic = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'announcement'


class AnnouncementDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    announcement = models.ForeignKey(Announcement, models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    system_file = models.ForeignKey('SystemFile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'announcement_document'


class AnnouncementRecipient(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    announcement = models.ForeignKey(Announcement, models.DO_NOTHING)
    date_opened = models.DateTimeField(blank=True, null=True)
    system_user = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='announcement_recipients_system_users')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='announcement_recipients_created')
    date_created = models.DateTimeField(blank=True, null=True)
    date_read = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'announcement_recipient'


class AnonymousPatientDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    patient = models.OneToOneField('Patient', models.DO_NOTHING)
    prescribing_authority = models.CharField(max_length=255, blank=True, null=True)
    prescription = models.CharField(max_length=255, blank=True, null=True)
    prescription_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'anonymous_patient_detail'


class AppConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    config_value = models.CharField(max_length=255)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    parent_config = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    value_type = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'app_config'
        unique_together = (('parent_config', 'name'),)


class Appointment(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    appointment_date = models.DateTimeField()
    appointment_doctor = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='appointments_as_doctor')
    appointment_type = models.CharField(max_length=255)
    booked_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='appointments_booked_by')
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    clinic = models.ForeignKey('Clinic', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='appointments_created')
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    encounter = models.ForeignKey('Encounter', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    referring_doctor = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='appointments_as_referring_doctor')

    class Meta:
        managed = False
        db_table = 'appointment'
        unique_together = (('appointment_date', 'clinic', 'patient'),)


class ApprovalAction(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    display_name = models.CharField(max_length=255)
    final_execution_method = models.TextField(blank=True, null=True)
    final_reversal_execution_method = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'approval_action'


class ApprovalActionAudit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    approval_action_level = models.ForeignKey('ApprovalActionLevel', models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    cancelled_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='approval_action_audits_cancelled')
    comment = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='approval_action_audits_created')
    date_cancelled = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    is_approved = models.BooleanField()
    is_cancelled = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    record_identifier = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'approval_action_audit'


class ApprovalActionLevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    allow_inferior_level_override = models.BooleanField()
    approval_action = models.ForeignKey(ApprovalAction, models.DO_NOTHING)
    approval_level = models.IntegerField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    print_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'approval_action_level'


class ApprovalDepartmentAssociation(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    department = models.ForeignKey('Department', models.DO_NOTHING)
    system_user = models.ForeignKey('SystemUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'approval_department_association'
        unique_together = (('department', 'system_user'),)


class ApprovalLevelUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    approval_action_level = models.ForeignKey(ApprovalActionLevel, models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='approval_level_users_created')
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    system_user = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='approval_level_users_system_users')

    class Meta:
        managed = False
        db_table = 'approval_level_user'
        unique_together = (('approval_action_level', 'system_user'),)


class ApprovalRequestNotification(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    approval_action_level = models.ForeignKey(ApprovalActionLevel, models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='approval_request_notifications_created')
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    record_identifier = models.BigIntegerField()
    system_user = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='approval_request_notifications_system_users')

    class Meta:
        managed = False
        db_table = 'approval_request_notification'


class ArtsonContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'artson_contact'


class ArtsonContactArtsonContactGroups(models.Model):
    artson_contact = models.OneToOneField(ArtsonContact, models.DO_NOTHING, primary_key=True)
    artson_contact_group = models.ForeignKey('ArtsonContactGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'artson_contact_artson_contact_groups'
        unique_together = (('artson_contact', 'artson_contact_group'),)


class ArtsonContactGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    group_type = models.CharField(max_length=6)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'artson_contact_group'


class Asset(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    accumulated_depreciation_ledger = models.ForeignKey('ChartOfAccount', models.DO_NOTHING, related_name='assets_accumulated_depreciation')
    asset_category = models.ForeignKey('AssetCategory', models.DO_NOTHING)
    asset_location = models.ForeignKey('AssetLocation', models.DO_NOTHING)
    asset_make = models.ForeignKey('AssetMake', models.DO_NOTHING)
    asset_model = models.ForeignKey('AssetModel', models.DO_NOTHING)
    asset_tag = models.CharField(max_length=255)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='assets_created')
    current_value = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField(blank=True, null=True)
    depreciation_expense_ledger = models.ForeignKey('ChartOfAccount', models.DO_NOTHING, related_name='assets_depreciation_expense')
    depreciation_percentage = models.DecimalField(max_digits=19, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    purchase_cost = models.DecimalField(max_digits=19, decimal_places=2)
    purchase_date = models.DateTimeField()
    serial_number = models.CharField(max_length=255)
    status = models.CharField(max_length=22)
    asset_assignee = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='assets_assigned')
    depreciation_method = models.CharField(max_length=17, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset'


class AssetCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'asset_category'
        unique_together = (('branch', 'name'),)


class AssetDepreciation(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    accumulated_depreciation_journal = models.ForeignKey('GeneralJournal', models.DO_NOTHING, related_name='asset_depreciation_accumulated_depreciation')
    asset = models.ForeignKey(Asset, models.DO_NOTHING)
    asset_book_value = models.DecimalField(max_digits=19, decimal_places=2)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    depreciation_amount = models.DecimalField(max_digits=19, decimal_places=2)
    depreciation_expense_journal = models.ForeignKey('GeneralJournal', models.DO_NOTHING, related_name='asset_depreciation_depreciation_expense')
    depreciation_percentage = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asset_depreciation'


class AssetLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'asset_location'
        unique_together = (('branch', 'name'),)


class AssetMaintenanceSchedule(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    asset = models.ForeignKey(Asset, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    maintenance_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='maintenance_schedule_maintenance_by')
    maintenance_date = models.DateTimeField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    received_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='maintenance_schedule_received_by')
    return_date = models.DateTimeField(blank=True, null=True)
    schedule_date = models.DateTimeField()
    scheduled_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='maintenance_schedule_scheduled_by')

    class Meta:
        managed = False
        db_table = 'asset_maintenance_schedule'


class AssetMake(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'asset_make'
        unique_together = (('branch', 'name'),)


class AssetModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    asset_make = models.ForeignKey(AssetMake, models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'asset_model'
        unique_together = (('branch', 'name'),)


class Audi3(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField()
    description = models.CharField(max_length=255)
    last_updated = models.DateTimeField()
    name = models.CharField(max_length=255)
    start_range = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'audi3'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bank(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    code = models.CharField(max_length=255)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    payee_account = models.ForeignKey('Supplier', models.DO_NOTHING, blank=True, null=True)
    system_defined = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'bank'
        unique_together = (('branch', 'name'),)


class BankBranch(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    bank = models.ForeignKey(Bank, models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    code = models.CharField(max_length=255)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    system_defined = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'bank_branch'
        unique_together = (('bank', 'branch', 'name'),)


class BankDeposit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    bank = models.ForeignKey('GeneralJournal', models.DO_NOTHING, related_name='bank_deposits')
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    cash = models.ForeignKey('GeneralJournal', models.DO_NOTHING, related_name='cash_deposits')
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    deposit_amount = models.DecimalField(max_digits=19, decimal_places=2)
    deposit_date = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    ledger_account = models.ForeignKey('ChartOfAccount', models.DO_NOTHING)
    void_status = models.TextField(blank=True, null=True)
    collection_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_deposit'


class BankDepositSystemFile(models.Model):
    bank_deposit_system_files = models.ForeignKey(BankDeposit, models.DO_NOTHING, blank=True, null=True)
    system_file = models.ForeignKey('SystemFile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank_deposit_system_file'


class BankReconciliation(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    bankestatement_line = models.ForeignKey('BankestatementLine', models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    is_reconciled_fully = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    ledger_entry = models.ForeignKey('GeneralLedger', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bank_reconciliation'


class Bankestatement(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    bank_account = models.ForeignKey('ChartOfAccount', models.DO_NOTHING)
    bankestatement_file = models.ForeignKey('SystemFile', models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField()
    last_updated = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField()
    closing_balance = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    statement_type = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bankestatement'


class BankestatementLine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    bankestatement = models.ForeignKey(Bankestatement, models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    credit = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    debit = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    description = models.TextField()
    last_updated = models.DateTimeField(blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    transaction_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bankestatement_line'


class Bed(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    bed_type = models.CharField(max_length=6)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField()
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    max_occupants = models.IntegerField()
    name = models.CharField(max_length=255)
    room = models.ForeignKey('Room', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bed'


class BedBillableItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    bed_movement = models.ForeignKey('BedMovement', models.DO_NOTHING)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField()
    invoice_line = models.ForeignKey('InvoiceLine', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bed_billable_item'


class BedMovement(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    admission = models.ForeignKey('PatientAdmission', models.DO_NOTHING)
    bed = models.ForeignKey(Bed, models.DO_NOTHING)
    bed_name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_occupied = models.DateTimeField()
    date_vacated = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    room = models.ForeignKey('Room', models.DO_NOTHING)
    ward = models.ForeignKey('Ward', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bed_movement'


class BloodBankStockLevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    blood_group = models.CharField(max_length=3)
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    max_stock = models.IntegerField()
    min_stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'blood_bank_stock_level'


class BloodTransfusion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey('Branch', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'blood_transfusion'
        unique_together = (('branch', 'name'),)


class BloodTransfusionInventoryItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comment = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField()
    inventory_audit = models.ForeignKey('InventoryAudit', models.DO_NOTHING)
    inventory_batch_level = models.ForeignKey('InventoryBatchLevel', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    number_of_pack = models.IntegerField()
    pack_number = models.CharField(max_length=255)
    patient_blood_transfusion = models.ForeignKey('PatientBloodTransfusion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'blood_transfusion_inventory_item'


class BloodTransfusionVitalMonitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    blood_pressure = models.CharField(max_length=255)
    comment = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_blood_transfusion = models.ForeignKey('PatientBloodTransfusion', models.DO_NOTHING)
    pulse = models.DecimalField(max_digits=19, decimal_places=2)
    respiratory = models.DecimalField(max_digits=19, decimal_places=2)
    taken_at = models.DateTimeField()
    temperature = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'blood_transfusion_vital_monitor'


class Branch(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    claim_schedule_item = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True,  related_name='branch_claim_schedule_items')
    communicare_password = models.CharField(max_length=255, blank=True, null=True)
    communicare_url = models.CharField(max_length=255, blank=True, null=True)
    communicare_username = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    country = models.ForeignKey('Country', models.DO_NOTHING)
    created_by_id = models.IntegerField()
    credit_period = models.IntegerField()
    currency = models.ForeignKey('Currency', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    dicom_pacs = models.CharField(max_length=255, blank=True, null=True)
    dicom_server = models.CharField(max_length=255, blank=True, null=True)
    dicom_toolkit = models.CharField(max_length=255, blank=True, null=True)
    geo_area_level5 = models.ForeignKey('GeoAreaLevel5', models.DO_NOTHING, blank=True, null=True)
    instance_identifier = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    minimum_taxable_income = models.DecimalField(max_digits=19, decimal_places=2)
    month_work_days = models.IntegerField()
    name = models.CharField(unique=True, max_length=255)
    payroll_deduction_item = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True, related_name='branch_payroll_deduction_items')
    petty_cashledger_account_id = models.BigIntegerField(blank=True, null=True)
    postal_address = models.CharField(max_length=255, blank=True, null=True)
    reminder_message = models.TextField()
    retirement_age = models.IntegerField()
    telephone = models.CharField(max_length=255)
    vat_ledger_account_id = models.BigIntegerField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    website = models.CharField(max_length=255, blank=True, null=True)
    artson_password = models.CharField(max_length=255, blank=True, null=True)
    artson_url = models.CharField(max_length=255, blank=True, null=True)
    artson_username = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'branch'


class Branding(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    template = models.TextField()

    class Meta:
        managed = False
        db_table = 'branding'
        unique_together = (('branch', 'name'),)


class BudgetLine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    budget_amount = models.DecimalField(max_digits=19, decimal_places=2)
    budget_period = models.ForeignKey('BudgetPeriod', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'budget_line'


class BudgetPeriod(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    begin_date = models.DateTimeField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    closed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='budget_periods_closed')
    closed_on = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='budget_periods_created')
    date_created = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField()
    financial_period = models.ForeignKey('FinancialPeriod', models.DO_NOTHING)
    is_closed = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'budget_period'


class BulkDrugDispense(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='bulk_drug_dispenses_created')
    date_created = models.DateTimeField(blank=True, null=True)
    dispensed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='bulk_drug_dispenses_dispensed')
    is_approved = models.CharField(max_length=7, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    processing_comment = models.CharField(max_length=255, blank=True, null=True)
    processing_date = models.DateTimeField(blank=True, null=True)
    received_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='bulk_drug_dispense_received_by')
    ward = models.ForeignKey('Ward', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bulk_drug_dispense'


class BulkDrugDispenseLine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    bulk_drug_dispense = models.ForeignKey(BulkDrugDispense, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    invoice_line = models.ForeignKey('InvoiceLine', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    prescription = models.ForeignKey('PatientDrug', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'bulk_drug_dispense_line'


class BusinessPartnerDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    client = models.OneToOneField('Patient', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    debtor_category = models.ForeignKey('DebtorCategory', models.DO_NOTHING)
    debtor_sub_category = models.ForeignKey('DebtorSubCategory', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'business_partner_detail'


class Cardex(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    admission = models.ForeignKey('PatientAdmission', models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    entry_date = models.DateTimeField()
    last_updated = models.DateTimeField(blank=True, null=True)
    note = models.TextField()
    nurse_id = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'cardex'


class CardexTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    is_default = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    system_defined = models.BooleanField()
    template = models.TextField()

    class Meta:
        managed = False
        db_table = 'cardex_template'
        unique_together = (('branch', 'name'),)


class CarePlanDiagnosis(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    diagnosis = models.TextField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'care_plan_diagnosis'


class CarePlanIntervention(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    diagnosis = models.ForeignKey(CarePlanDiagnosis, models.DO_NOTHING)
    intervention = models.TextField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'care_plan_intervention'


class CarePlanObjective(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    diagnosis = models.ForeignKey(CarePlanDiagnosis, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    objective = models.TextField()

    class Meta:
        managed = False
        db_table = 'care_plan_objective'


class CauseOfDeath(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    cause_type = models.CharField(max_length=10)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    condition = models.ForeignKey('Disease', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    deceased_patient = models.ForeignKey('DeceasedPatient', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cause_of_death'


class ChartOfAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    account_type = models.ForeignKey(AccountType, models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_debit_account = models.BooleanField()
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    org_code = models.CharField(max_length=255, blank=True, null=True)
    parent_id = models.IntegerField()
    allow_manual_journal_entry = models.BooleanField(blank=True, null=True)
    allow_negative = models.BooleanField(blank=True, null=True)
    account_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chart_of_account'
        unique_together = (('org_code', 'name'),)


class ChiefComplaint(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    chief_complaint_category = models.ForeignKey('ChiefComplaintCategory', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    system_defined = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'chief_complaint'
        unique_together = (('chief_complaint_category', 'branch', 'name'),)


class ChiefComplaintCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    system_defined = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'chief_complaint_category'
        unique_together = (('branch', 'name'),)


class ClaimSchedule(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    insurance_scheme = models.ForeignKey('InsuranceScheme', models.DO_NOTHING)
    invoice = models.ForeignKey('Invoice', models.DO_NOTHING)
    invoice_receipt = models.ForeignKey('InvoiceReceipt', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'claim_schedule'
        unique_together = (('invoice_receipt', 'insurance_scheme'),)


class Clinic(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    default_visit_type = models.ForeignKey('VisitType', models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    is_default = models.BooleanField()
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    vaccination_clinic = models.BooleanField()
    max_appointment = models.IntegerField(blank=True, null=True)
    order_sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinic'
        unique_together = (('branch', 'name'),)


class ClinicChargeDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    charge_type = models.CharField(max_length=12, blank=True, null=True)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING)
    clinic_charge = models.ForeignKey('Product', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    frequency = models.CharField(max_length=10)
    is_optional = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    single_clinic = models.BooleanField(blank=True, null=True)
    payable_at = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinic_charge_detail'


class ClinicClinicalProfiles(models.Model):
    clinical_profile = models.ForeignKey('ClinicalProfile', models.DO_NOTHING)
    clinic = models.OneToOneField(Clinic, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'clinic_clinical_profiles'
        unique_together = (('clinic', 'clinical_profile'),)


class ClinicOperatingTime(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING)
    closing_time = models.CharField(max_length=255)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    opening_time = models.CharField(max_length=255)
    workday = models.ForeignKey('Workday', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clinic_operating_time'


class ClinicReferralCharge(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING)
    clinic_charge_detail = models.ForeignKey(ClinicChargeDetail, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinic_referral_charge'
        unique_together = (('clinic', 'clinic_charge_detail'),)


class ClinicSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING)
    closed_at = models.DateTimeField(blank=True, null=True)
    closed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='clinic_session_closed_by')
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='clinic_session_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    health_education = models.TextField(blank=True, null=True)
    in_behalf_of = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='clinic_session_in_behalf_of')
    is_closed = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_visit = models.ForeignKey('PatientVisit', models.DO_NOTHING)
    visit_type = models.ForeignKey('VisitType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clinic_session'


class ClinicSessionInventoryItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic_session = models.ForeignKey(ClinicSession, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    cost_of_goods_sold_journal_entry = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='cost_of_goods_sold_inventory_items')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    inventory_audit = models.ForeignKey('InventoryAudit', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    stock_control_journal_entry = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='stock_control_inventory_items')
    usage_date = models.DateTimeField()
    void_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clinic_session_inventory_item'


class ClinicSessionItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic_session = models.ForeignKey(ClinicSession, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField()
    invoice_line = models.ForeignKey('InvoiceLine', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'clinic_session_item'


class ClinicVitalTypes(models.Model):
    vital_type = models.ForeignKey('VitalType', models.DO_NOTHING)
    clinic = models.OneToOneField(Clinic, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'clinic_vital_types'
        unique_together = (('clinic', 'vital_type'),)


class ClinicalProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinical_profile_category = models.ForeignKey('ClinicalProfileCategory', models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    hint = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    is_mandatory = models.BooleanField()
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.TextField()
    response_type = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'clinical_profile'


class ClinicalProfileCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'clinical_profile_category'
        unique_together = (('branch', 'name'),)


class CommunicareContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'communicare_contact'


class CommunicareContactCommunicareContactGroups(models.Model):
    communicare_contact_group = models.ForeignKey('CommunicareContactGroup', models.DO_NOTHING)
    communicare_contact = models.OneToOneField(CommunicareContact, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'communicare_contact_communicare_contact_groups'
        unique_together = (('communicare_contact', 'communicare_contact_group'),)


class CommunicareContactGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey('Company', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    group_type = models.CharField(max_length=6)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'communicare_contact_group'


class Company(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administrative_contact = models.CharField(max_length=255)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    pin = models.CharField(max_length=255, blank=True, null=True)
    postal_address = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255)
    web = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'


class CompanyModules(models.Model):
    company = models.OneToOneField(Company, models.DO_NOTHING, primary_key=True)
    module = models.ForeignKey('Module', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'company_modules'
        unique_together = (('company', 'module'),)


class ConductBookingAction(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'conduct_booking_action'
        unique_together = (('branch', 'name'),)


class ConductBookingMeetingEmployee(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comments = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='meeting_employees_created')
    date_created = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='meeting_employees')
    employee_conduct_booking = models.ForeignKey('EmployeeConductBooking', models.DO_NOTHING)
    has_attended = models.BooleanField()
    is_meeting_lead = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    meeting_type = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'conduct_booking_meeting_employee'
        unique_together = (('meeting_type', 'employee'),)


class ConsultantFee(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    consultant = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='consultant_fees')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='consultant_fees_created')
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    earning = models.ForeignKey('Earning', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    major_theater = models.ForeignKey('MajorTheater', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'consultant_fee'


class ContraindicatedAllergen(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    allergen = models.ForeignKey(Allergen, models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    pharmacology = models.ForeignKey('Pharmacology', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'contraindicated_allergen'


class CoreRegistry(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'core_registry'


class Country(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    geo_area_level1name = models.CharField(max_length=255, blank=True, null=True)
    geo_area_level2name = models.CharField(max_length=255, blank=True, null=True)
    geo_area_level3name = models.CharField(max_length=255, blank=True, null=True)
    geo_area_level4name = models.CharField(max_length=255, blank=True, null=True)
    geo_area_level5name = models.CharField(max_length=255, blank=True, null=True)
    iso_code2 = models.CharField(max_length=255)
    iso_code3 = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    telephone_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'


class CountyProInvoiceExchange(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    api_response = models.TextField()
    date_created = models.DateTimeField()
    invoice_line = models.ForeignKey('InvoiceLine', models.DO_NOTHING)
    return_code = models.CharField(max_length=255)
    return_message = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'county_pro_invoice_exchange'


class CountyProReceiptExchange(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    api_response = models.TextField()
    date_created = models.DateTimeField()
    invoice_receipt = models.ForeignKey('InvoiceReceipt', models.DO_NOTHING)
    return_code = models.CharField(max_length=255)
    return_message = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'county_pro_receipt_exchange'


class CreditNote(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    client = models.ForeignKey('Patient', models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_note'


class CreditNoteDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    credit_note = models.ForeignKey(CreditNote, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    invoice_receipt = models.OneToOneField('InvoiceReceipt', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    vat = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'credit_note_detail'


class CreditorPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount_settled = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    check_number = models.CharField(max_length=255)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'creditor_payment'


class Currency(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    code = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'currency'


class DailyInpatientStatistic(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    bed_capacity = models.IntegerField()
    current_female_admissions = models.IntegerField()
    current_male_admissions = models.IntegerField()
    date = models.DateTimeField()
    date_created = models.DateTimeField(blank=True, null=True)
    deaths = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    medically_discharged = models.IntegerField()
    new_admissions = models.IntegerField()
    released = models.IntegerField()
    ward = models.ForeignKey('Ward', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'daily_inpatient_statistic'


class DailyInpatientStatistics(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    bed_capacity = models.IntegerField()
    current_female_admissions = models.IntegerField()
    current_male_admissions = models.IntegerField()
    date = models.DateTimeField()
    date_created = models.DateTimeField(blank=True, null=True)
    deaths = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    medically_discharged = models.IntegerField()
    new_admissions = models.IntegerField()
    released = models.IntegerField()
    ward = models.ForeignKey('Ward', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'daily_inpatient_statistics'


class DatabaseBackup(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    end_time = models.DateTimeField()
    file_name = models.CharField(max_length=255)
    initiator = models.CharField(max_length=6)
    last_updated = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'database_backup'


class DeathCertificate(models.Model):
    id = models.OneToOneField('DeceasedPatient', models.DO_NOTHING, db_column='id', primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    deceased_patient_id = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    serial_number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'death_certificate'
        unique_together = (('branch', 'serial_number'),)


class DebitNote(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    vendor = models.ForeignKey('Supplier', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'debit_note'


class DebitNoteDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    debit_note = models.ForeignKey(DebitNote, models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    vat = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True)
    voucher_payment = models.OneToOneField('VoucherPayment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'debit_note_detail'


class DebtExtensionDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    debt_extension_line = models.ForeignKey('InvoiceLine', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    invoice_receipt = models.OneToOneField('InvoiceReceipt', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'debt_extension_detail'


class DebtorCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'debtor_category'
        unique_together = (('branch', 'name'),)


class DebtorSubCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    debtor_category = models.ForeignKey(DebtorCategory, models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'debtor_sub_category'
        unique_together = (('branch', 'name'),)


class DeceasedPatient(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    admission = models.ForeignKey('PatientAdmission', models.DO_NOTHING, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comments = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    death_certificate = models.ForeignKey(DeathCertificate, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    mp_certification = models.IntegerField()
    origin = models.CharField(max_length=2)
    patient = models.OneToOneField('Patient', models.DO_NOTHING)
    patient_visit = models.ForeignKey('PatientVisit', models.DO_NOTHING)
    place_of_death = models.CharField(max_length=255)
    time_of_death = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'deceased_patient'


class DeclaredLossSettlementDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    insurance_scheme = models.ForeignKey('InsuranceScheme', models.DO_NOTHING)
    invoice_receipt = models.OneToOneField('InvoiceReceipt', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'declared_loss_settlement_detail'


class Deduction(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    band_type = models.CharField(max_length=12)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    deduction_category = models.ForeignKey('DeductionCategory', models.DO_NOTHING)
    deduction_owner = models.ForeignKey('Supplier', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    is_recurrent = models.BooleanField()
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=19, decimal_places=2)
    reference_earning = models.ForeignKey('Earning', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deduction'


class DeductionCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    non_taxable_limit = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'deduction_category'


class DeductionEmploymentStatuses(models.Model):
    employment_status = models.ForeignKey('EmploymentStatus', models.DO_NOTHING)
    deduction = models.OneToOneField(Deduction, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'deduction_employment_statuses'
        unique_together = (('deduction', 'employment_status'),)


class DeductionLedgerLinkage(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    deduction = models.ForeignKey(Deduction, models.DO_NOTHING)
    default_credit_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING)
    department = models.ForeignKey('Department', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deduction_ledger_linkage'


class DeductionRate(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    deduction = models.ForeignKey(Deduction, models.DO_NOTHING)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    rate = models.DecimalField(max_digits=19, decimal_places=2)
    upper_bound = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deduction_rate'


class DefaultAncillaryCareImaging(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    ancillary_care = models.ForeignKey(AncillaryCare, models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    imaging = models.ForeignKey('Imaging', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_ancillary_care_imaging'


class DefaultAncillaryCareLabTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    ancillary_care = models.ForeignKey(AncillaryCare, models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    lab_test = models.ForeignKey('LabTest', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_ancillary_care_lab_test'


class DefaultBillableItemAdmission(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    ward = models.ForeignKey('Ward', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'default_billable_item_admission'


class DefaultBillableItemAncillaryCare(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    ancillary_care = models.ForeignKey(AncillaryCare, models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    ward = models.ForeignKey('Ward', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_billable_item_ancillary_care'


class DefaultBillableItemBed(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    bed = models.ForeignKey(Bed, models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'default_billable_item_bed'


class DefaultBillableItemFamilyPlanning(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    family_planning = models.ForeignKey('FamilyPlanning', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    ward = models.ForeignKey('Ward', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_billable_item_family_planning'


class DefaultBillableItemImaging(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    imaging = models.ForeignKey('Imaging', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    ward = models.ForeignKey('Ward', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_billable_item_imaging'


class DefaultBillableItemLabTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    lab_test = models.ForeignKey('LabTest', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    ward = models.ForeignKey('Ward', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_billable_item_lab_test'


class DefaultBillableItemMajorTheater(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    major_theater = models.ForeignKey('MajorTheater', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    ward = models.ForeignKey('Ward', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'default_billable_item_major_theater'


class DefaultBillableItemMinorTheater(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    minor_theater = models.ForeignKey('MinorTheater', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    ward = models.ForeignKey('Ward', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_billable_item_minor_theater'


class DefaultBillableItemMorgueAdmission(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    morgue_cabinet = models.ForeignKey('MorgueCabinet', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'default_billable_item_morgue_admission'


class DefaultBillableItemMorgueCabinet(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    lower_bound_days = models.IntegerField()
    morgue_cabinet = models.ForeignKey('MorgueCabinet', models.DO_NOTHING)
    origin = models.CharField(max_length=3)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    upper_bound_days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'default_billable_item_morgue_cabinet'


class DefaultBillableItemPatientDrug(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    pharmacology = models.ForeignKey('Pharmacology', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    ward = models.ForeignKey('Ward', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_billable_item_patient_drug'


class DefaultBillableItemVaccine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    vaccine = models.ForeignKey('Vaccine', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'default_billable_item_vaccine'


class DefaultBillableItemWard(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    frequency = models.CharField(max_length=5)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    ward = models.ForeignKey('Ward', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'default_billable_item_ward'


class DefaultBillableItemWellnessExamination(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    ward = models.ForeignKey('Ward', models.DO_NOTHING, blank=True, null=True)
    wellness_examination = models.ForeignKey('WellnessExamination', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'default_billable_item_wellness_examination'


class DefaultBloodTransfusionImaging(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    blood_transfusion = models.ForeignKey(BloodTransfusion, models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    imaging = models.ForeignKey('Imaging', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_blood_transfusion_imaging'


class DefaultBloodTransfusionLabTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    blood_transfusion = models.ForeignKey(BloodTransfusion, models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    lab_test = models.ForeignKey('LabTest', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_blood_transfusion_lab_test'


class DefaultInventoryItemAncillaryCare(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    ancillary_care = models.ForeignKey(AncillaryCare, models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    store = models.ForeignKey('Store', models.DO_NOTHING)
    bill_to_patient = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_inventory_item_ancillary_care'


class DefaultInventoryItemFamilyPlanning(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    family_planning = models.ForeignKey('FamilyPlanning', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    store = models.ForeignKey('Store', models.DO_NOTHING)
    bill_to_patient = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_inventory_item_family_planning'


class DefaultInventoryItemImaging(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    imaging = models.ForeignKey('Imaging', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    store = models.ForeignKey('Store', models.DO_NOTHING)
    bill_to_patient = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_inventory_item_imaging'


class DefaultInventoryItemLabTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    lab_test = models.ForeignKey('LabTest', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    store = models.ForeignKey('Store', models.DO_NOTHING)
    bill_to_patient = models.BooleanField(blank=True, null=True)
    is_shared = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_inventory_item_lab_test'


class DefaultInventoryItemMajorTheater(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    major_theater = models.ForeignKey('MajorTheater', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    store = models.ForeignKey('Store', models.DO_NOTHING)
    bill_to_patient = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_inventory_item_major_theater'


class DefaultInventoryItemMinorTheater(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    minor_theater = models.ForeignKey('MinorTheater', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    store = models.ForeignKey('Store', models.DO_NOTHING)
    bill_to_patient = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_inventory_item_minor_theater'


class DefaultInventoryItemPrescription(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    pharmacology = models.ForeignKey('Pharmacology', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    store = models.ForeignKey('Store', models.DO_NOTHING)
    bill_to_patient = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_inventory_item_prescription'


class DefaultInventoryItemVaccine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    store = models.ForeignKey('Store', models.DO_NOTHING)
    vaccine = models.ForeignKey('Vaccine', models.DO_NOTHING)
    bill_to_patient = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'default_inventory_item_vaccine'


class DefaultMajorProcedureImaging(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    imaging = models.ForeignKey('Imaging', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    major_theater = models.ForeignKey('MajorTheater', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'default_major_procedure_imaging'


class DefaultMajorProcedureLabTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    lab_test = models.ForeignKey('LabTest', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    major_theater = models.ForeignKey('MajorTheater', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'default_major_procedure_lab_test'


class DefaultMinorProcedureImaging(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    imaging = models.ForeignKey('Imaging', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    minor_theater = models.ForeignKey('MinorTheater', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'default_minor_procedure_imaging'


class DefaultMinorProcedureLabTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    lab_test = models.ForeignKey('LabTest', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    minor_theater = models.ForeignKey('MinorTheater', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'default_minor_procedure_lab_test'


class Department(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='created_departments')
    date_created = models.DateTimeField(blank=True, null=True)
    department_unit = models.ForeignKey('DepartmentUnit', models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    expense_ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, blank=True, null=True)
    include_income_and_expenditure = models.BooleanField()
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    org_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department'
        unique_together = (('branch', 'name'),)


class DepartmentExpenseAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    expense_account_id = models.BigIntegerField()
    expense_type = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'department_expense_account'
        unique_together = (('department', 'expense_type'),)


class DepartmentOperatingTime(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING, blank=True, null=True)
    closing_time = models.CharField(max_length=255)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    department_type = models.CharField(max_length=24)
    last_updated = models.DateTimeField(blank=True, null=True)
    opening_time = models.CharField(max_length=255)
    workday = models.ForeignKey('Workday', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'department_operating_time'


class DepartmentUnit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'department_unit'
        unique_together = (('branch', 'name'),)


class DepositDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    debit_balance = models.DecimalField(max_digits=19, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    imprest_surrender = models.ForeignKey('ImprestRequestProcessed', models.DO_NOTHING, blank=True, null=True)
    invoice_receipt = models.OneToOneField('InvoiceReceipt', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    medical_cover_line = models.ForeignKey('MedicalCoverLine', models.DO_NOTHING, blank=True, null=True)
    payment_mode = models.ForeignKey('PaymentMode', models.DO_NOTHING)
    tendered = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'deposit_detail'


class Disease(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    disease_block = models.ForeignKey('DiseaseBlock', models.DO_NOTHING)
    five_character_icd_code = models.CharField(max_length=255)
    four_character_icd_code = models.CharField(max_length=255)
    is_active = models.BooleanField()
    is_node = models.BooleanField()
    mortality_ref_list1 = models.CharField(max_length=255)
    mortality_ref_list2 = models.CharField(max_length=255)
    mortality_ref_list3 = models.CharField(max_length=255)
    mortality_ref_list4 = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    simplified_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease'


class DiseaseBlock(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    disease_chapter = models.ForeignKey('DiseaseChapter', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    block_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease_block'


class DiseaseChapter(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    chapter_number = models.CharField(max_length=255)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'disease_chapter'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DrugAdministered(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    admission = models.ForeignKey('PatientAdmission', models.DO_NOTHING)
    how_it_was_administered = models.CharField(max_length=255)
    patient_drug = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'drug_administered'


class DrugDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    classification = models.CharField(max_length=15)
    date_created = models.DateTimeField(blank=True, null=True)
    drug = models.OneToOneField('Product', models.DO_NOTHING)
    item_image = models.ForeignKey('SystemFile', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    msrp = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    unit_buying_price = models.DecimalField(max_digits=19, decimal_places=2)
    brand_name = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    formulation = models.CharField(max_length=255, blank=True, null=True)
    frequency = models.CharField(max_length=255, blank=True, null=True)
    route = models.CharField(max_length=17, blank=True, null=True)
    strength = models.CharField(max_length=255, blank=True, null=True)
    wavco = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drug_detail'


class EafyaPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount_paid = models.DecimalField(max_digits=19, decimal_places=2)
    amount_tendered = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    date_created = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    financial_period = models.ForeignKey('FinancialPeriod', models.DO_NOTHING)
    invoice_number = models.CharField(max_length=255)
    last_updated = models.DateTimeField()
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    payment_mode = models.ForeignKey('PaymentMode', models.DO_NOTHING)
    requested_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    settled_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    void_status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eafya_payment'


class Earning(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    deduction_owner = models.ForeignKey('Supplier', models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    earning_category = models.ForeignKey('EarningCategory', models.DO_NOTHING)
    earning_type = models.CharField(max_length=16)
    factor_denominator = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    factor_numerator = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField()
    is_recurrent = models.BooleanField()
    is_statutory = models.BooleanField()
    is_system_defined = models.BooleanField()
    is_taxable = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'earning'


class EarningCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'earning_category'


class EarningLedgerLinkage(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    default_credit_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, blank=True, null=True, related_name='earning_linkages_credit')
    default_debit_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, related_name='earning_linkages_debit')
    department = models.ForeignKey(Department, models.DO_NOTHING)
    earning = models.ForeignKey(Earning, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'earning_ledger_linkage'


class EarningRate(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    earning = models.ForeignKey(Earning, models.DO_NOTHING)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    rate = models.DecimalField(max_digits=19, decimal_places=2)
    upper_bound = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'earning_rate'


class EmergencyContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)
    phone_number = models.CharField(max_length=255)
    relationship = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'emergency_contact'


class Employee(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    city = models.CharField(max_length=255, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    contract_end_date = models.DateTimeField(blank=True, null=True)
    contract_start_date = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='created_employees')
    date_created = models.DateTimeField(blank=True, null=True)
    date_of_birth = models.DateTimeField()
    date_of_permanency = models.DateTimeField(blank=True, null=True)
    employee_image = models.ForeignKey('SystemFile', models.DO_NOTHING, blank=True, null=True)
    employee_tenure = models.ForeignKey('EmployeeTenure', models.DO_NOTHING, blank=True, null=True, related_name='employee_tenures')
    gender = models.CharField(max_length=6)
    home_phone = models.CharField(max_length=255, blank=True, null=True)
    identification_document_number = models.CharField(max_length=255, blank=True, null=True)
    identification_type = models.CharField(max_length=24)
    is_on_payroll = models.BooleanField()
    job_category = models.ForeignKey('JobCategory', models.DO_NOTHING, blank=True, null=True)
    job_scale = models.ForeignKey('JobScale', models.DO_NOTHING)
    job_title = models.ForeignKey('JobTitle', models.DO_NOTHING, blank=True, null=True)
    join_date = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    location = models.ForeignKey('JobLocation', models.DO_NOTHING, blank=True, null=True)
    marital_status = models.CharField(max_length=9)
    mobile_phone = models.CharField(max_length=255, blank=True, null=True)
    nationality = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    nhif_number = models.CharField(max_length=255, blank=True, null=True)
    nssf_number = models.CharField(max_length=255, blank=True, null=True)
    original_employee_number = models.CharField(max_length=255)
    other_email = models.CharField(max_length=255, blank=True, null=True)
    physical_address = models.CharField(max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=255)
    postal_address = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    probation_end_date = models.DateTimeField(blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    termination_date = models.DateTimeField(blank=True, null=True)
    termination_note = models.CharField(max_length=255, blank=True, null=True)
    termination_reason = models.CharField(max_length=31, blank=True, null=True)
    work_email = models.CharField(max_length=255, blank=True, null=True)
    work_phone = models.CharField(max_length=255, blank=True, null=True)
    effective_date = models.DateTimeField(blank=True, null=True)
    employment_status = models.ForeignKey('EmploymentStatus', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee'


class EmployeeBankAccount(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    account_name = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    bank_branch = models.ForeignKey(BankBranch, models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    pay_percentage = models.IntegerField()
    swift_code = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'employee_bank_account'


class EmployeeCarryForwardDays(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='carry_forward_days_created')
    date_created = models.DateTimeField(blank=True, null=True)
    days = models.FloatField()
    employee = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='carry_forward_days_employee')
    expiry_date = models.DateTimeField()
    last_updated = models.DateTimeField(blank=True, null=True)
    leave_type = models.ForeignKey('LeaveType', models.DO_NOTHING)
    source_leave_period = models.ForeignKey('LeavePeriod', models.DO_NOTHING, related_name='carry_forward_days_as_source')
    utilization_leave_period = models.ForeignKey('LeavePeriod', models.DO_NOTHING, related_name='carry_forward_days_as_utilization')

    class Meta:
        managed = False
        db_table = 'employee_carry_forward_days'


class EmployeeConductBooking(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    case_narration_notes = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    conduct_booking_action = models.ForeignKey(ConductBookingAction, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='employee_conduct_booking')
    employee_grievance_booking = models.ForeignKey('EmployeeGrievanceBooking', models.DO_NOTHING, blank=True, null=True)
    follow_up_date = models.DateTimeField(blank=True, null=True)
    follow_up_lead = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='follow_up_lead_conduct_booking')
    follow_up_meeting_notes = models.TextField(blank=True, null=True)
    initial_meeting_lead = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='initial_meeting_lead_conduct_booking')
    initial_meeting_notes = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    meeting_date = models.DateTimeField(blank=True, null=True)
    performance_review = models.ForeignKey('PerformanceReview', models.DO_NOTHING, blank=True, null=True)
    reporting_date = models.DateTimeField()
    review_date = models.DateTimeField(blank=True, null=True)
    review_lead = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='review_lead_conduct_booking')
    review_meeting_notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=12)
    suspension_approval_status = models.CharField(max_length=7, blank=True, null=True)
    suspension_end_date = models.DateTimeField(blank=True, null=True)
    suspension_processed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='suspension_processed_by_conduct_booking')
    suspension_processing_comments = models.CharField(max_length=255, blank=True, null=True)
    suspension_processing_date = models.DateTimeField(blank=True, null=True)
    suspension_start_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'employee_conduct_booking'


class EmployeeDebt(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_by_employee_debt')
    date_created = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey('SystemUser', models.DO_NOTHING)
    employee_debt_type = models.ForeignKey('EmployeeDebtType', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_debt'


class EmployeeDebtRepayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    deduction = models.ForeignKey('PayrollBreakdown', models.DO_NOTHING, blank=True, null=True)
    employee_debt_schedule = models.ForeignKey('EmployeeDebtSchedule', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    receipt = models.ForeignKey('InvoiceReceipt', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_debt_repayment'


class EmployeeDebtSchedule(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    deduction = models.ForeignKey(Deduction, models.DO_NOTHING)
    employee_debt = models.ForeignKey(EmployeeDebt, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    payroll_month = models.ForeignKey('SystemMonth', models.DO_NOTHING)
    payroll_year = models.ForeignKey('SystemYear', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee_debt_schedule'


class EmployeeDebtType(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'employee_debt_type'
        unique_together = (('branch', 'name'),)


class EmployeeDependant(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    date_of_birth = models.DateTimeField()
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    gender = models.CharField(max_length=6)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'employee_dependant'


class EmployeeDocumentAttachment(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    document_type = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    system_file = models.ForeignKey('SystemFile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employee_document_attachment'


class EmployeeEducation(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    end_date = models.DateTimeField(blank=True, null=True)
    institute = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    level = models.CharField(max_length=255)
    score = models.CharField(max_length=255, blank=True, null=True)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_education'


class EmployeeEmergencyContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    home_telephone = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    mobile_phone = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    relationship = models.CharField(max_length=255)
    work_telephone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_emergency_contact'


class EmployeeEmployeeTenure(models.Model):
    employee_employee_tenures = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    employee_tenure = models.ForeignKey('EmployeeTenure', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_employee_tenure'


class EmployeeGrievanceBooking(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_by_grievance_booking')
    date_created = models.DateTimeField(blank=True, null=True)
    details = models.TextField(blank=True, null=True)
    employee = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='employee_grievance_booking')
    follow_up_date = models.DateTimeField(blank=True, null=True)
    follow_up_lead = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='employee_grievance_follow_up_lead')
    follow_up_notes_notes = models.TextField(blank=True, null=True)
    initial_meeting_lead = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='employee_grievance_initial_meeting_lead')
    initial_meeting_notes = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    meeting_date = models.DateTimeField(blank=True, null=True)
    resolution_notes = models.TextField(blank=True, null=True)
    review_date = models.DateTimeField(blank=True, null=True)
    review_lead = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='employee_grievance_review_lead')
    review_notes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=12)
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'employee_grievance_booking'


class EmployeeJobHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comment = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    contract_end_date = models.DateTimeField(blank=True, null=True)
    contract_start_date = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    effective_date = models.DateTimeField()
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    employment_status = models.CharField(max_length=255, blank=True, null=True)
    end_date = models.DateTimeField()
    job_category = models.ForeignKey('JobCategory', models.DO_NOTHING, blank=True, null=True)
    job_location = models.ForeignKey('JobLocation', models.DO_NOTHING, blank=True, null=True)
    job_title = models.ForeignKey('JobTitle', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_job_history'


class EmployeeLanguage(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comments = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    competency = models.CharField(max_length=13)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    fluency = models.CharField(max_length=29)
    language = models.ForeignKey('Language', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_language'
        unique_together = (('employee', 'language'),)


class EmployeeLeaveAdjustment(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='employee_leave_adjustment_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    days = models.FloatField()
    employee = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='employee_leave_adjustment_employee')
    is_approved = models.CharField(max_length=7, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    leave_period = models.ForeignKey('LeavePeriod', models.DO_NOTHING)
    leave_type = models.ForeignKey('LeaveType', models.DO_NOTHING)
    processed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='employee_leave_adjustment_processed_by')
    processing_comment = models.CharField(max_length=255, blank=True, null=True)
    processing_date = models.DateTimeField(blank=True, null=True)
    reason = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'employee_leave_adjustment'


class EmployeeLicence(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comments = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    expiry_date = models.DateTimeField(blank=True, null=True)
    issue_date = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    licence = models.ForeignKey('JobQualificationLicence', models.DO_NOTHING)
    licence_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_licence'


class EmployeeMembership(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comments = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    currency = models.ForeignKey(Currency, models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    membership = models.ForeignKey('JobQualificationMembership', models.DO_NOTHING)
    subscription_amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    subscription_end_date = models.DateTimeField(blank=True, null=True)
    subscription_paid_by = models.CharField(max_length=10, blank=True, null=True)
    subscription_start_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_membership'


class EmployeeNextOfKin(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    id_type = models.CharField(max_length=255, blank=True, null=True)
    identification_number = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    mobile_phone = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    postal_address = models.CharField(max_length=255, blank=True, null=True)
    relationship = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'employee_next_of_kin'


class EmployeeProbationPeriod(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='employee_probation_period_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    employee = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='employee_probation_period_employee')
    end_date = models.DateTimeField()
    last_updated = models.DateTimeField(blank=True, null=True)
    probation_type = models.CharField(max_length=19)
    start_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'employee_probation_period'


class EmployeeReportingTo(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='employee_reporting_to_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    effective_date = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    reporting_type = models.CharField(max_length=8)
    subordinate = models.ForeignKey(Employee, models.DO_NOTHING, related_name='employee_reporting_to_subordinate')
    supervisor = models.ForeignKey(Employee, models.DO_NOTHING, related_name='employee_reporting_to_supervisor')
    system_user = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_reporting_to'
        unique_together = (('subordinate', 'supervisor'),)


class EmployeeSkill(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comments = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    period = models.CharField(max_length=255)
    skill = models.ForeignKey('JobQualificationSkill', models.DO_NOTHING)
    years_of_experience = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_skill'
        unique_together = (('employee', 'skill'),)


class EmployeeTenure(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    cancelled_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='employee_tenure_cancelled_by')
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='employee_tenure_created_by')
    date_cancelled = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    effective_date = models.DateTimeField()
    employee = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='employee_tenure_employee')
    employment_comments = models.CharField(max_length=255, blank=True, null=True)
    employment_is_approved = models.CharField(max_length=7, blank=True, null=True)
    employment_processing_comments = models.CharField(max_length=255, blank=True, null=True)
    employment_status = models.ForeignKey('EmploymentStatus', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    tenure_end_date = models.DateTimeField(blank=True, null=True)
    tenure_processed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='employee_tenure_tenure_processed_by')
    tenure_processing_date = models.DateTimeField(blank=True, null=True)
    terminated_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='employee_tenure_terminated_by')
    termination_comments = models.CharField(max_length=255, blank=True, null=True)
    termination_date = models.DateTimeField(blank=True, null=True)
    termination_is_approved = models.CharField(max_length=7, blank=True, null=True)
    termination_processed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='employee_tenure_termination_processed_by')
    termination_processing_comments = models.CharField(max_length=255, blank=True, null=True)
    termination_processing_date = models.DateTimeField(blank=True, null=True)
    termination_reason = models.ForeignKey('TerminationReason', models.DO_NOTHING, blank=True, null=True)
    is_cancelled = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employee_tenure'


class EmployeeWorkExperience(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comments = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    company_worked_for = models.CharField(max_length=255)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey(Employee, models.DO_NOTHING)
    end_date = models.DateTimeField()
    job_title = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'employee_work_experience'


class EmploymentStatus(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_permanent = models.BooleanField()
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'employment_status'
        unique_together = (('branch', 'name'),)


class EmploymentStatusDeduction(models.Model):
    employment_status_deductions = models.ForeignKey(EmploymentStatus, models.DO_NOTHING, blank=True, null=True)
    deduction = models.ForeignKey(Deduction, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employment_status_deduction'


class EmploymentStatusLeaveTypeRule(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    employment_status = models.ForeignKey(EmploymentStatus, models.DO_NOTHING)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    leave_type = models.ForeignKey('LeaveType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'employment_status_leave_type_rule'
        unique_together = (('leave_type', 'employment_status'),)


class Encounter(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic_session = models.ForeignKey(ClinicSession, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    encounter_notes = models.TextField(blank=True, null=True)
    illness_history = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    origin = models.CharField(max_length=2)
    physical_exam = models.TextField(blank=True, null=True)
    treatment_instruction = models.TextField(blank=True, null=True)
    family_social_history = models.TextField(blank=True, null=True)
    past_surgical_history = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'encounter'


class ExtPaediatricAdmission(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    data = models.TextField()
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    patient_admission = models.ForeignKey('PatientAdmission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ext_paediatric_admission'


class ExtendedBioDataField(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    allowed_values = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    data_group = models.CharField(max_length=255)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    field_name = models.CharField(max_length=255)
    field_type = models.CharField(max_length=13)
    is_active = models.BooleanField()
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'extended_bio_data_field'


class ExtendedPatientBio(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    extended_bio_data_field = models.ForeignKey(ExtendedBioDataField, models.DO_NOTHING)
    field_value = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'extended_patient_bio'


class FamilyPlanning(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    family_planning_category = models.ForeignKey('FamilyPlanningCategory', models.DO_NOTHING)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'family_planning'
        unique_together = (('branch', 'name'),)


class FamilyPlanningCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'family_planning_category'
        unique_together = (('branch', 'name'),)


class FinancialPeriod(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    begin_date = models.DateTimeField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    closed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='financial_period_closed_by')
    closed_on = models.DateTimeField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField()
    gain_loss_entry = models.ForeignKey('GeneralLedger', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    locked_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='financial_period_locked_by')
    locked_on = models.DateTimeField(blank=True, null=True)
    is_closed = models.BooleanField(blank=True, null=True)
    beginning_inventory = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'financial_period'


class FingerprintSpecimen(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    finger = models.CharField(max_length=12)
    fmd_file = models.ForeignKey('SystemFile', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)
    system_user = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fingerprint_specimen'


class FloatMovement(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    credited_account = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='float_movement_credited_account')
    date_created = models.DateTimeField(blank=True, null=True)
    debited_account = models.ForeignKey('GeneralJournal', models.DO_NOTHING, blank=True, null=True, related_name='float_movement_debited_account')
    last_updated = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'float_movement'


class GeneralExamination(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_default = models.BooleanField()
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'general_examination'
        unique_together = (('branch', 'name'),)


class GeneralJournal(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    account_title = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    credit = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    debit = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    financial_period = models.ForeignKey(FinancialPeriod, models.DO_NOTHING)
    journal_voucher_number = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING)
    ledger_entry = models.ForeignKey('GeneralLedger', models.DO_NOTHING, blank=True, null=True)
    ref = models.CharField(max_length=255)
    transaction_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'general_journal'


class GeneralJournalSystemFile(models.Model):
    general_journal_system_files = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True)
    system_file = models.ForeignKey('SystemFile', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_journal_system_file'


class GeneralLedger(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    credit = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    debit = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    entity_name = models.CharField(max_length=2550, blank=True, null=True)
    financial_period = models.ForeignKey(FinancialPeriod, models.DO_NOTHING, blank=True, null=True)
    is_closing_entry = models.BooleanField()
    is_opening_entry = models.BooleanField()
    item = models.CharField(max_length=2550, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    ledger_account_id = models.BigIntegerField()
    transaction_date = models.DateTimeField()
    transaction_number = models.CharField(max_length=255, blank=True, null=True)
    credit_balance = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    debit_balance = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_ledger'


class GeoAreaLevel1(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    country = models.ForeignKey(Country, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    geo_latitude = models.CharField(max_length=255, blank=True, null=True)
    geo_longitude = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'geo_area_level1'


class GeoAreaLevel2(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    geo_area_level1 = models.ForeignKey(GeoAreaLevel1, models.DO_NOTHING)
    geo_latitude = models.CharField(max_length=255, blank=True, null=True)
    geo_longitude = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'geo_area_level2'


class GeoAreaLevel3(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    geo_area_level2 = models.ForeignKey(GeoAreaLevel2, models.DO_NOTHING)
    geo_latitude = models.CharField(max_length=255, blank=True, null=True)
    geo_longitude = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'geo_area_level3'


class GeoAreaLevel4(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    geo_area_level3 = models.ForeignKey(GeoAreaLevel3, models.DO_NOTHING)
    geo_latitude = models.CharField(max_length=255, blank=True, null=True)
    geo_longitude = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'geo_area_level4'


class GeoAreaLevel5(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    geo_area_level4 = models.ForeignKey(GeoAreaLevel4, models.DO_NOTHING)
    geo_latitude = models.CharField(max_length=255, blank=True, null=True)
    geo_longitude = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'geo_area_level5'


class GrievanceBookingAccusedEmployee(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comments = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_grievance_booking_accusations')
    date_created = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='grievance_booking_accusations')
    employee_grievance_booking = models.ForeignKey(EmployeeGrievanceBooking, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'grievance_booking_accused_employee'


class GrievanceBookingMeetingEmployee(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comments = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_grievance_booking_meetings')
    date_created = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='employee_grievance_booking_meetings')
    employee_grievance_booking = models.ForeignKey(EmployeeGrievanceBooking, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    meeting_type = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'grievance_booking_meeting_employee'
        unique_together = (('meeting_type', 'employee'),)


class HealthEducation(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    health_education_category = models.ForeignKey('HealthEducationCategory', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    system_defined = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'health_education'
        unique_together = (('health_education_category', 'branch', 'name'),)


class HealthEducationCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    system_defined = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'health_education_category'
        unique_together = (('branch', 'name'),)


class HealthInsurance(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    insurance_scheme = models.ForeignKey('InsuranceScheme', models.DO_NOTHING)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    member_number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'health_insurance'


class Helpdesk(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    action = models.TextField()
    description = models.TextField(blank=True, null=True)
    module = models.ForeignKey('Module', models.DO_NOTHING)
    onsite_video_path = models.CharField(max_length=255, blank=True, null=True)
    remote_video_url = models.CharField(max_length=255, blank=True, null=True)
    write_up = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'helpdesk'


class Holiday(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date = models.DateTimeField()
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    repeats_annually = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'holiday'
        unique_together = (('branch', 'name'),)


class IllnessHistoryTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    is_default = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    system_defined = models.BooleanField()
    template = models.TextField()

    class Meta:
        managed = False
        db_table = 'illness_history_template'
        unique_together = (('branch', 'name'),)


class Imaging(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    allow_multiple_orders = models.BooleanField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    imaging_category = models.ForeignKey('ImagingCategory', models.DO_NOTHING)
    imaging_result_template = models.ForeignKey('ImagingResultTemplate', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    system_defined = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'imaging'
        unique_together = (('branch', 'name'),)


class ImagingCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    system_defined = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'imaging_category'
        unique_together = (('branch', 'name'),)


class ImagingDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    imaging = models.OneToOneField('Product', models.DO_NOTHING)
    item_image = models.ForeignKey('SystemFile', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    max_stock = models.IntegerField()
    min_stock = models.IntegerField()
    unit_buying_price = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'imaging_detail'


class ImagingResultTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    template = models.TextField()

    class Meta:
        managed = False
        db_table = 'imaging_result_template'
        unique_together = (('branch', 'name'),)


class Imprest(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    credited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True,related_name='credited_imprests')
    date_created = models.DateTimeField(blank=True, null=True)
    debited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='debited_imprests')
    description = models.TextField(blank=True, null=True)
    imprest_type = models.CharField(max_length=6)
    last_updated = models.DateTimeField(blank=True, null=True)
    ledger_account_id = models.BigIntegerField()
    payment_date = models.DateTimeField()
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    transaction_type = models.CharField(max_length=6)
    void_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imprest'


class ImprestOtherDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    imprest = models.OneToOneField(Imprest, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'imprest_other_detail'


class ImprestRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    ch = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    date_requested = models.DateTimeField()
    employee_debt = models.ForeignKey(EmployeeDebt, models.DO_NOTHING, blank=True, null=True)
    expected_amount = models.DecimalField(max_digits=19, decimal_places=2)
    imprest_type = models.CharField(max_length=13)
    is_approved = models.CharField(max_length=9, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    payroll_number = models.CharField(max_length=255, blank=True, null=True)
    reason = models.TextField()

    class Meta:
        managed = False
        db_table = 'imprest_request'


class ImprestRequestAllocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    credited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True,related_name='credited_imprest_allocations')
    date_created = models.DateTimeField(blank=True, null=True)
    date_utilized = models.DateTimeField()
    debited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='debited_imprest_allocations')
    imprest_request_processed = models.ForeignKey('ImprestRequestProcessed', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imprest_request_allocation'


class ImprestRequestProcessed(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING,related_name='created_imprest_request_processeds')
    credited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True,related_name='credited_imprest_request_processeds')
    date_created = models.DateTimeField(blank=True, null=True)
    date_processed = models.DateTimeField()
    date_received = models.DateTimeField(blank=True, null=True)
    debited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True,related_name='debited_imprest_request_processeds')
    imprest_request = models.ForeignKey(ImprestRequest, models.DO_NOTHING, blank=True, null=True)
    imprest_type = models.CharField(max_length=9)
    invoice_receipt = models.ForeignKey('InvoiceReceipt', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    paying_entity = models.ForeignKey('InsuranceScheme', models.DO_NOTHING, blank=True, null=True)
    reason = models.TextField()
    received_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='received_imprest_request_processeds')
    remarks = models.TextField(blank=True, null=True)
    transaction_number = models.CharField(max_length=255, blank=True, null=True)
    void_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imprest_request_processed'


class ImprestRequestTracker(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    credit = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    debit = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    debit_balance = models.DecimalField(max_digits=19, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING)
    medical_cover_line = models.ForeignKey('MedicalCoverLine', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'imprest_request_tracker'


class ImprestStaffDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    imprest = models.OneToOneField(Imprest, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey('SystemUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'imprest_staff_detail'


class InheritedRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    inherited_role = models.ForeignKey('Role', models.DO_NOTHING, related_name='inherited_roles')
    last_updated = models.DateTimeField(blank=True, null=True)
    role = models.ForeignKey('Role', models.DO_NOTHING, related_name='roles_inheriting')

    class Meta:
        managed = False
        db_table = 'inherited_role'


class Insurance(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    eclaim_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance'
        unique_together = (('branch', 'name'),)


class InsuranceClaimSettlement(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    credited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='credited_insurance_claim_settlements')
    date_created = models.DateTimeField(blank=True, null=True)
    debited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='debited_insurance_claim_settlements')
    description = models.TextField(blank=True, null=True)
    invoice_receipt = models.ForeignKey('InvoiceReceipt', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    settlement_date = models.DateTimeField()
    void_status = models.TextField(blank=True, null=True)
    payment_mode = models.ForeignKey('PaymentMode', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance_claim_settlement'


class InsuranceScheme(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, related_name='insurance_schemes')
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    can_be_renewed = models.BooleanField()
    company = models.ForeignKey(Company, models.DO_NOTHING)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    cover_percentage = models.DecimalField(max_digits=19, decimal_places=2)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    debtor_account = models.ForeignKey('Patient', models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    insurance = models.ForeignKey(Insurance, models.DO_NOTHING)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    overpayment_ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, blank=True, null=True, related_name='overpayment_ledger_insurance_schemes')
    rebate = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    service_package = models.ForeignKey('ServicePackage', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance_scheme'
        unique_together = (('branch', 'name'),)


class InsuranceSchemeAssignor(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_insurance_scheme_assignors')
    date_created = models.DateTimeField(blank=True, null=True)
    insurance_scheme = models.ForeignKey(InsuranceScheme, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    system_user = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='system_user_insurance_scheme_assignors')

    class Meta:
        managed = False
        db_table = 'insurance_scheme_assignor'
        unique_together = (('insurance_scheme', 'system_user'),)


class InsuranceSchemeLine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount_limit = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    insurance_scheme = models.ForeignKey(InsuranceScheme, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'insurance_scheme_line'


class InsuranceSettlementDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    insurance_scheme = models.ForeignKey(InsuranceScheme, models.DO_NOTHING)
    invoice_receipt = models.OneToOneField('InvoiceReceipt', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    medical_cover_line = models.ForeignKey('MedicalCoverLine', models.DO_NOTHING)
    member_insurance_number = models.CharField(max_length=255)
    overpayment_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'insurance_settlement_detail'


class InsuranceUtilizationTracker(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    medical_cover_line = models.ForeignKey('MedicalCoverLine', models.DO_NOTHING)
    utilized_amount = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'insurance_utilization_tracker'


class InternalConsumption(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_internal_consumptions')
    date_created = models.DateTimeField(blank=True, null=True)
    date_required = models.DateTimeField()
    debtor = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING)
    expense_type = models.IntegerField()
    internal_consumption_number = models.CharField(max_length=255, blank=True, null=True)
    invoice = models.ForeignKey('Invoice', models.DO_NOTHING, blank=True, null=True)
    is_approved = models.CharField(max_length=16, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    markup_rate = models.FloatField(blank=True, null=True)
    processed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='processed_internal_consumptions')
    processing_comment = models.TextField(blank=True, null=True)
    processing_date = models.DateTimeField(blank=True, null=True)
    requester_comment = models.TextField()
    source_store = models.ForeignKey('Store', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'internal_consumption'


class InternalConsumptionItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    credited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='credited_internal_consumption_items')
    date_created = models.DateTimeField(blank=True, null=True)
    debited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='debited_internal_consumption_items')
    expected_quantity = models.DecimalField(max_digits=19, decimal_places=2)
    internal_consumption = models.ForeignKey(InternalConsumption, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    unit_buying_price = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    unit_selling_price = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'internal_consumption_item'


class InternalConsumptionItemBatchAudit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    internal_consumption_item = models.ForeignKey(InternalConsumptionItem, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'internal_consumption_item_batch_audit'


class InternalInventoryUsage(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_internal_inventory_usages')
    date_created = models.DateTimeField(blank=True, null=True)
    date_taken = models.DateTimeField()
    department = models.ForeignKey(Department, models.DO_NOTHING)
    issued_at = models.DateTimeField(blank=True, null=True)
    issued_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='issued_internal_inventory_usages')
    justification = models.TextField()
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    source_store = models.ForeignKey('Store', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'internal_inventory_usage'


class InventoryAudit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    decrement = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    increment = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    level = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    reference = models.CharField(max_length=255, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    store_inventory = models.ForeignKey('StoreInventory', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'inventory_audit'


class InventoryBatchLevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    batch_number = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField()
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    store = models.ForeignKey('Store', models.DO_NOTHING)
    store_receipt_item = models.ForeignKey('StoreReceiptItem', models.DO_NOTHING, blank=True, null=True)
    unit_in_stock = models.DecimalField(max_digits=19, decimal_places=2)
    unit_selling_price = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    voucher_line = models.ForeignKey('VoucherLine', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_batch_level'


class InventoryUnit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    unit = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventory_unit'
        unique_together = (('unit', 'quantity', 'branch', 'name'),)


class Invoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    alert_frequency = models.CharField(max_length=9)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_invoices')
    date_created = models.DateTimeField(blank=True, null=True)
    date_verified = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField()
    financial_period = models.ForeignKey(FinancialPeriod, models.DO_NOTHING)
    invoice_number = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_visit = models.ForeignKey('PatientVisit', models.DO_NOTHING)
    settled_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=7)
    verified_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='verified_invoices')
    void_status = models.TextField(blank=True, null=True)
    invoice_type = models.CharField(max_length=5, blank=True, null=True)
    our_invoice = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice'


class InvoiceLine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    account_receivable = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='account_receivable_invoice_lines')
    billing_stage = models.CharField(max_length=5)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_invoice_lines')
    date_created = models.DateTimeField(blank=True, null=True)
    date_posted = models.DateTimeField(blank=True, null=True)
    default_sale_ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    discount_rate = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    invoice_line_number = models.CharField(max_length=255, blank=True, null=True)
    is_cost_fixed = models.BooleanField()
    item_name = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    sale = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='sale_invoice_lines')
    status = models.CharField(max_length=7)
    unit_cost = models.DecimalField(max_digits=19, decimal_places=2)
    vat = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='vat_invoice_lines')
    vat_rate = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    void_status = models.TextField(blank=True, null=True)
    specialist = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='specialist_invoice_lines')

    class Meta:
        managed = False
        db_table = 'invoice_line'


class InvoicePayrollBreakdown(models.Model):
    invoice_payroll_breakdown = models.ForeignKey(Invoice, models.DO_NOTHING, blank=True, null=True)
    payroll_breakdown = models.ForeignKey('PayrollBreakdown', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_payroll_breakdown'


class InvoiceReceipt(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    credited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True,related_name='credited_receipts')
    date_created = models.DateTimeField(blank=True, null=True)
    debited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='debited_receipts' )
    description = models.TextField(blank=True, null=True)
    employee_debt = models.ForeignKey(EmployeeDebt, models.DO_NOTHING, blank=True, null=True)
    invoice_line = models.ForeignKey(InvoiceLine, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient = models.ForeignKey('Patient', models.DO_NOTHING, blank=True, null=True)
    payment_date = models.DateTimeField()
    receipt_type = models.CharField(max_length=13)
    transaction_fee_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, related_name='transaction_fee_receipts', blank=True, null=True)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    void_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'invoice_receipt'


class InvoiceTemplatePackage(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'invoice_template_package'


class InvoiceTemplatePackageLine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    invoice_template_package = models.ForeignKey(InvoiceTemplatePackage, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    vat_class = models.ForeignKey('VatClass', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'invoice_template_package_line'


class JobCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'job_category'
        unique_together = (('branch', 'name'),)


class JobCategoryLeaveTypeRule(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    job_category = models.ForeignKey(JobCategory, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    leave_type = models.ForeignKey('LeaveType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'job_category_leave_type_rule'
        unique_together = (('leave_type', 'job_category'),)


class JobGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'job_group'


class JobGroupLeaveTypeRule(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    job_group = models.ForeignKey(JobGroup, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    leave_type = models.ForeignKey('LeaveType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'job_group_leave_type_rule'
        unique_together = (('leave_type', 'job_group'),)


class JobLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    city = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    physical_address = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'job_location'
        unique_together = (('branch', 'country'), ('branch', 'name'), ('branch', 'phone_number'), ('branch', 'physical_address'),)


class JobOrganizationStructure(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    parent_organization_structure = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_organization_structure'
        unique_together = (('branch', 'name'),)


class JobQualificationEducation(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'job_qualification_education'
        unique_together = (('branch', 'name'),)


class JobQualificationLicence(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'job_qualification_licence'
        unique_together = (('branch', 'name'),)


class JobQualificationMembership(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'job_qualification_membership'
        unique_together = (('branch', 'name'),)


class JobQualificationSkill(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'job_qualification_skill'
        unique_together = (('branch', 'name'),)


class JobScale(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    basic_pay = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    job_group = models.ForeignKey(JobGroup, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'job_scale'


class JobTitle(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'job_title'
        unique_together = (('branch', 'name'),)


class JobTitleLeaveTypeRule(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    job_title = models.ForeignKey(JobTitle, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    leave_type = models.ForeignKey('LeaveType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'job_title_leave_type_rule'
        unique_together = (('leave_type', 'job_title'),)


class JobTitlePerformanceIndicator(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    job_title = models.ForeignKey(JobTitle, models.DO_NOTHING)
    key_performance_indicator = models.ForeignKey('KeyPerformanceIndicator', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job_title_performance_indicator'
        unique_together = (('key_performance_indicator', 'job_title'),)


class JobWorkShift(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    end_time = models.CharField(max_length=255)
    hours_per_day = models.FloatField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    start_time = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'job_work_shift'
        unique_together = (('branch', 'name'),)


class KeyPerformanceIndicator(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    key_performance_indicator_category = models.ForeignKey('KeyPerformanceIndicatorCategory', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    performance_indicator_response_type = models.ForeignKey('PerformanceIndicatorResponseType', models.DO_NOTHING)
    respondents = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'key_performance_indicator'
        unique_together = (('key_performance_indicator_category', 'branch', 'name'),)


class KeyPerformanceIndicatorCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'key_performance_indicator_category'
        unique_together = (('branch', 'name'),)


class LabResultReferenceInterval(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=6)
    lab_test_id = models.BigIntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    lower_age = models.IntegerField()
    lower_age_limit = models.IntegerField()
    lower_unit = models.CharField(max_length=6)
    upper_age = models.IntegerField()
    upper_age_limit = models.IntegerField()
    upper_unit = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'lab_result_reference_interval'


class LabResultReferenceIntervalItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    flag = models.CharField(max_length=255, blank=True, null=True)
    include_in_report = models.BooleanField()
    lab_result_reference_interval = models.ForeignKey(LabResultReferenceInterval, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    lower_range = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    upper_range = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_result_reference_interval_item'


class LabResultReferenceIntervalItemPersist(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    flag = models.CharField(max_length=255, blank=True, null=True)
    include_in_report = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    lower_range = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    patient_lab_test = models.ForeignKey('PatientLabTest', models.DO_NOTHING)
    upper_range = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_result_reference_interval_item_persist'


class LabTest(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    allow_multiple_orders = models.BooleanField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    is_default = models.BooleanField()
    is_ordered_independently = models.BooleanField()
    is_system_defined = models.BooleanField()
    lab_test_category = models.ForeignKey('LabTestCategory', models.DO_NOTHING)
    lab_test_result_template = models.ForeignKey('LabTestResultTemplate', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    maximum_range = models.CharField(max_length=255, blank=True, null=True)
    minimum_range = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    order_sequence = models.IntegerField()
    parent_id = models.BigIntegerField()
    sample_type = models.CharField(max_length=255, blank=True, null=True)
    test_result_type = models.ForeignKey('TestResultType', models.DO_NOTHING)
    absolute_maximum = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    absolute_minimum = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    auto_calculation_formulae = models.CharField(max_length=255, blank=True, null=True)
    auto_calculation_formulae_suppress = models.CharField(max_length=255, blank=True, null=True)
    chart_result = models.BooleanField(blank=True, null=True)
    fractional_limit = models.CharField(max_length=255, blank=True, null=True)
    interfacing_db_conn = models.CharField(max_length=255, blank=True, null=True)
    interfacing_result_manipulator = models.CharField(max_length=255, blank=True, null=True)
    interfacing_test_code = models.CharField(max_length=255, blank=True, null=True)
    is_urgent = models.BooleanField(blank=True, null=True)
    lab_test_header_footer_template = models.ForeignKey('LabTestHeaderFooterTemplate', models.DO_NOTHING, blank=True, null=True)
    lab_test_worksheet = models.ForeignKey('LabTestWorksheet', models.DO_NOTHING, blank=True, null=True)
    processing_hour_type = models.CharField(max_length=255, blank=True, null=True)
    processing_time = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_test'


class LabTestCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    system_defined = models.BooleanField()
    order_sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_test_category'
        unique_together = (('branch', 'name'),)


class LabTestHeaderFooterTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    footer_template = models.TextField(blank=True, null=True)
    header_template = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'lab_test_header_footer_template'


class LabTestHeaderFooterTemplateLabTest(models.Model):
    lab_test_header_footer_template_lab_tests = models.ForeignKey(LabTestHeaderFooterTemplate, models.DO_NOTHING, blank=True, null=True)
    lab_test_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_test_header_footer_template_lab_test'


class LabTestResultTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    template = models.TextField()

    class Meta:
        managed = False
        db_table = 'lab_test_result_template'
        unique_together = (('branch', 'name'),)


class LabTestSampleType(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_url = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_test_sample_type'


class LabTestSampleTypeLabTest(models.Model):
    lab_test_sample_type_lab_tests = models.ForeignKey(LabTestSampleType, models.DO_NOTHING, blank=True, null=True)
    lab_test_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_test_sample_type_lab_test'


class LabTestWorkday(models.Model):
    lab_test_workdays = models.ForeignKey(LabTest, models.DO_NOTHING, blank=True, null=True)
    workday = models.ForeignKey('Workday', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_test_workday'


class LabTestWorksheet(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    body = models.TextField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'lab_test_worksheet'


class LabTestWorksheetLabTest(models.Model):
    lab_test_worksheet_lab_tests = models.ForeignKey(LabTestWorksheet, models.DO_NOTHING, blank=True, null=True)
    lab_test_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_test_worksheet_lab_test'


class Language(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'language'
        unique_together = (('branch', 'name'),)


class LateCharge(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.OneToOneField('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'late_charge'


class LateChargeTime(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    period_type = models.CharField(max_length=6)
    start_time = models.DateTimeField()
    system_defined = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'late_charge_time'


class Leave(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comments = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_leaves')
    date_created = models.DateTimeField(blank=True, null=True)
    duration = models.CharField(max_length=12)
    employee = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='employee_leaves')
    from_date = models.DateTimeField()
    is_approved = models.CharField(max_length=7, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    leave_period = models.ForeignKey('LeavePeriod', models.DO_NOTHING)
    leave_type = models.ForeignKey('LeaveType', models.DO_NOTHING)
    processed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='processed_leaves')
    processing_comment = models.CharField(max_length=255, blank=True, null=True)
    processing_date = models.DateTimeField(blank=True, null=True)
    to_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'leave'


class LeavePeriod(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255)
    end_date = models.DateTimeField()
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'leave_period'


class LeaveType(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    allow_carry_forward = models.BooleanField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    entitled_days = models.FloatField()
    gender_eligibility = models.CharField(max_length=6)
    is_accruable = models.BooleanField()
    is_active = models.BooleanField()
    is_weekend_inclusive = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    maximum_days = models.IntegerField(blank=True, null=True)
    minimum_days = models.IntegerField(blank=True, null=True)
    minimum_service_period_in_days = models.FloatField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'leave_type'
        unique_together = (('branch', 'name'),)


class LeaveTypeCarryForwardRule(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    carry_negative_balance = models.BooleanField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    expiry_period_in_days = models.IntegerField()
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    leave_type = models.ForeignKey(LeaveType, models.DO_NOTHING)
    maximum_carry_forward_days = models.FloatField()

    class Meta:
        managed = False
        db_table = 'leave_type_carry_forward_rule'
        unique_together = (('branch', 'leave_type'),)


class License(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    eafya_key_id = models.IntegerField(unique=True)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    license_hash = models.TextField()
    mac_address = models.CharField(max_length=255)
    c_r = models.TextField(blank=True, null=True)
    ct_sg = models.TextField(blank=True, null=True)
    s_p = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'license'


class LocalServiceOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    approval_comment = models.CharField(max_length=255, blank=True, null=True)
    approval_date = models.DateTimeField(blank=True, null=True)
    approved = models.CharField(max_length=16, blank=True, null=True)
    approved_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='approved_service_orders', blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    delivery_charge = models.DecimalField(max_digits=19, decimal_places=2)
    delivery_date_required = models.DateTimeField()
    department = models.ForeignKey(Department, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    local_service_order_number = models.CharField(max_length=255, blank=True, null=True)
    local_service_order_requisition = models.OneToOneField('LocalServiceOrderRequisition', models.DO_NOTHING)
    processed = models.CharField(max_length=9, blank=True, null=True)
    processed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='processed_service_orders', blank=True, null=True)
    processed_comment = models.TextField(blank=True, null=True)
    processing_date = models.DateTimeField(blank=True, null=True)
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local_service_order'


class LocalServiceOrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    budget_line = models.ForeignKey(BudgetLine, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    local_service_order = models.ForeignKey(LocalServiceOrder, models.DO_NOTHING)
    local_service_order_item_number = models.CharField(max_length=255, blank=True, null=True)
    local_service_order_requisition_item = models.ForeignKey('LocalServiceOrderRequisitionItem', models.DO_NOTHING)
    processed_commit = models.DecimalField(max_digits=19, decimal_places=2)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    unit_price = models.DecimalField(max_digits=19, decimal_places=2)
    vat_rate = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'local_service_order_item'
        unique_together = (('local_service_order', 'product'),)


class LocalServiceOrderRequisition(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    approval_comment = models.TextField(blank=True, null=True)
    approval_date = models.DateTimeField(blank=True, null=True)
    approved = models.CharField(max_length=16, blank=True, null=True)
    approved_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='approved_service_order_requisitions')
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_service_order_requisitions')
    date_created = models.DateTimeField(blank=True, null=True)
    delivery_date_required = models.DateTimeField()
    department = models.ForeignKey(Department, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    local_service_order_requisition_number = models.CharField(max_length=255, blank=True, null=True)
    requester_comment = models.CharField(max_length=255)
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'local_service_order_requisition'


class LocalServiceOrderRequisitionItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    local_service_order_requisition = models.ForeignKey(LocalServiceOrderRequisition, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    unit_price = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'local_service_order_requisition_item'
        unique_together = (('local_service_order_requisition', 'product'),)


class LocationMachineIdentity(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    user_operating_location = models.ForeignKey('UserOperatingLocation', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'location_machine_identity'


class LoginAudit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    login_date = models.DateTimeField()
    logout_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'login_audit'


class MajorTheater(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    major_theater_category = models.ForeignKey('MajorTheaterCategory', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'major_theater'
        unique_together = (('branch', 'major_theater_category', 'name'),)


class MajorTheaterCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'major_theater_category'
        unique_together = (('branch', 'name'),)


class MajorTheaterDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    cost = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField(blank=True, null=True)
    drug = models.ForeignKey('Product', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'major_theater_detail'


class MajorTheaterRoom(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'major_theater_room'
        unique_together = (('branch', 'name'),)


class MajorTheaterRoomMajorTheater(models.Model):
    major_theater_room_major_theaters = models.ForeignKey(MajorTheaterRoom, models.DO_NOTHING, blank=True, null=True)
    major_theater = models.ForeignKey(MajorTheater, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'major_theater_room_major_theater'


class MedicalCoverLine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount_limit = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    health_insurance = models.ForeignKey(HealthInsurance, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'medical_cover_line'


class MedicalCoverWithdrawalRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    financial_period = models.ForeignKey(FinancialPeriod, models.DO_NOTHING)
    imprest_request_tracker = models.ForeignKey(ImprestRequestTracker, models.DO_NOTHING, blank=True, null=True)
    is_approved = models.CharField(max_length=9)
    last_updated = models.DateTimeField(blank=True, null=True)
    medical_cover_line = models.ForeignKey(MedicalCoverLine, models.DO_NOTHING)
    reason = models.TextField()

    class Meta:
        managed = False
        db_table = 'medical_cover_withdrawal_request'


class Medicine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    active_ingredient = models.CharField(max_length=255, blank=True, null=True)
    atc_code = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    current_approval_status = models.CharField(max_length=255, blank=True, null=True)
    data_life_phase = models.CharField(max_length=255, blank=True, null=True)
    dosage_form = models.CharField(max_length=255, blank=True, null=True)
    dosage_form_code = models.IntegerField()
    generic_name = models.CharField(max_length=255, blank=True, null=True)
    generic_name_code = models.IntegerField()
    gpc_code = models.IntegerField()
    medicine_generic_product_key = models.CharField(max_length=255, blank=True, null=True)
    medicine_index_key = models.IntegerField()
    national_product_code = models.CharField(max_length=255, blank=True, null=True)
    next_approval_status = models.CharField(max_length=255, blank=True, null=True)
    pack_size = models.CharField(max_length=255, blank=True, null=True)
    pack_size_code = models.IntegerField()
    product_activation = models.BooleanField()
    product_activation_date = models.CharField(max_length=255, blank=True, null=True)
    product_description = models.CharField(max_length=255, blank=True, null=True)
    product_group = models.CharField(max_length=255, blank=True, null=True)
    product_group_code = models.CharField(max_length=255, blank=True, null=True)
    route_of_administration = models.CharField(max_length=255, blank=True, null=True)
    route_of_administration_code = models.IntegerField()
    strength = models.CharField(max_length=255, blank=True, null=True)
    strength_code = models.IntegerField()
    therapeutic_group = models.CharField(max_length=255, blank=True, null=True)
    therapeutic_group_code = models.IntegerField()
    unspsc_code = models.IntegerField()
    updated_at = models.DateTimeField(blank=True, null=True)
    ven_classification = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicine'


class MessageCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    code = models.IntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'message_code'


class MessagingContact(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    contact_group = models.ForeignKey('MessagingContactGroup', models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_deleted = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'messaging_contact'


class MessagingContactGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'messaging_contact_group'


class MinorTheater(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    minor_theater_category = models.ForeignKey('MinorTheaterCategory', models.DO_NOTHING)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'minor_theater'
        unique_together = (('branch', 'name'),)


class MinorTheaterCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'minor_theater_category'
        unique_together = (('branch', 'name'),)


class MinorTheaterDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    cost = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField(blank=True, null=True)
    drug = models.ForeignKey('Product', models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'minor_theater_detail'


class Module(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    display_name = models.CharField(unique=True, max_length=255)
    js = models.TextField()
    name = models.CharField(unique=True, max_length=255)
    usage_key = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'module'


class MohHealthFacility(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    code = models.IntegerField()
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)
    type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'moh_health_facility'


class MohReportConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'moh_report_config'
        unique_together = (('branch', 'name'),)


class MohReportConfigMohReportGroup(models.Model):
    moh_report_config_moh_report_groups = models.ForeignKey(MohReportConfig, models.DO_NOTHING, blank=True, null=True)
    moh_report_group = models.ForeignKey('MohReportGroup', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moh_report_config_moh_report_group'


class MohReportGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    order_seq = models.BigIntegerField()
    parent_id = models.BigIntegerField()
    moh_report_section = models.ForeignKey('MohReportSection', models.DO_NOTHING, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moh_report_group'


class MohReportItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    disease = models.ForeignKey(Disease, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    major_theater = models.ForeignKey(MajorTheater, models.DO_NOTHING, blank=True, null=True)
    minor_theater = models.ForeignKey(MinorTheater, models.DO_NOTHING, blank=True, null=True)
    moh_report_group = models.ForeignKey(MohReportGroup, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moh_report_item'


class MohReportSection(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    moh_report_config = models.ForeignKey(MohReportConfig, models.DO_NOTHING)
    name = models.CharField(max_length=255)
    section_type = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'moh_report_section'


class MonthlyAggregate(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField()
    general_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    payroll_period = models.ForeignKey('PayrollPeriod', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'monthly_aggregate'


class MorgueAdmission(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    admission_date = models.DateTimeField(blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    collector_identification = models.CharField(max_length=255, blank=True, null=True)
    collector_name = models.CharField(max_length=255, blank=True, null=True)
    collector_phone = models.CharField(max_length=255, blank=True, null=True)
    collector_physical_address = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    custodian_identification = models.CharField(max_length=255, blank=True, null=True)
    custodian_name = models.CharField(max_length=255)
    custodian_phone = models.CharField(max_length=255, blank=True, null=True)
    custodian_physical_address = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField()
    deceased_patient = models.ForeignKey(DeceasedPatient, models.DO_NOTHING)
    discharge_date = models.DateTimeField(blank=True, null=True)
    discharged_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='discharged_morgue_admissions', blank=True, null=True)
    disposal_address = models.TextField(blank=True, null=True)
    disposal_comments = models.TextField(blank=True, null=True)
    disposal_date = models.DateTimeField(blank=True, null=True)
    disposal_method = models.CharField(max_length=21, blank=True, null=True)
    last_updated = models.DateTimeField()
    next_of_kin_address = models.CharField(max_length=255, blank=True, null=True)
    next_of_kin_name = models.CharField(max_length=255, blank=True, null=True)
    next_of_kin_relation_ship = models.ForeignKey('RelationshipType', models.DO_NOTHING, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    notification_date = models.DateTimeField(blank=True, null=True)
    patient_admission = models.ForeignKey('PatientAdmission', models.DO_NOTHING, blank=True, null=True)
    received_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='received_morgue_admissions', blank=True, null=True)
    relatives_notified_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='notified_relatives')

    class Meta:
        managed = False
        db_table = 'morgue_admission'


class MorgueAdmissionBillableItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    billing_date = models.DateTimeField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField()
    invoice_line = models.ForeignKey(InvoiceLine, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    morgue_admission = models.ForeignKey(MorgueAdmission, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'morgue_admission_billable_item'


class MorgueCabinet(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'morgue_cabinet'


class MorgueCabinetBillableItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField()
    invoice_line = models.ForeignKey(InvoiceLine, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    lower_bound_days = models.IntegerField()
    morgue_cabinet_movement = models.ForeignKey('MorgueCabinetMovement', models.DO_NOTHING)
    origin = models.CharField(max_length=3)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.IntegerField()
    upper_bound_days = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'morgue_cabinet_billable_item'


class MorgueCabinetMovement(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    comment = models.TextField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    date_occupied = models.DateTimeField()
    date_vacated = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    morgue_admission = models.ForeignKey(MorgueAdmission, models.DO_NOTHING)
    morgue_cabinet = models.ForeignKey(MorgueCabinet, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'morgue_cabinet_movement'


class MpesaExpressRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.IntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    callback_payload = models.TextField(blank=True, null=True)
    checkout_requestid = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    customer_message = models.CharField(max_length=255, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    error_code = models.CharField(max_length=255, blank=True, null=True)
    error_message = models.CharField(max_length=255, blank=True, null=True)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    invoice_line_ids = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    merchant_requestid = models.CharField(max_length=255, blank=True, null=True)
    msisdn = models.CharField(max_length=255)
    payment_payload = models.TextField()
    request_id = models.CharField(max_length=255, blank=True, null=True)
    response_code = models.CharField(max_length=255, blank=True, null=True)
    response_description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'mpesa_express_request'


class MpesaTransaction(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    msisdn = models.CharField(max_length=255)
    bill_ref_number = models.CharField(max_length=255)
    business_short_code = models.CharField(max_length=255)
    date_created = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    invoice_number = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    middle_name = models.CharField(max_length=255)
    org_account_balance = models.CharField(max_length=255)
    third_party_transid = models.CharField(max_length=255)
    trans_amount = models.DecimalField(max_digits=19, decimal_places=2)
    transid = models.CharField(unique=True, max_length=255)
    trans_time = models.CharField(max_length=255)
    transaction_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mpesa_transaction'


class Newborn(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    baby_head_circumference = models.FloatField(blank=True, null=True)
    baby_height = models.FloatField(blank=True, null=True)
    baby_status = models.CharField(max_length=255)
    baby_weight = models.FloatField(blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_newborns')
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    first_apgar_score = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_admission = models.ForeignKey('PatientAdmission', models.DO_NOTHING, blank=True, null=True)
    patient_labour_monitor = models.ForeignKey('PatientLabourMonitor', models.DO_NOTHING)
    resuscitation = models.BooleanField(blank=True, null=True)
    second_apgar_score = models.IntegerField(blank=True, null=True)
    abdomen_condition = models.CharField(max_length=255, blank=True, null=True)
    anus_condition = models.CharField(max_length=255, blank=True, null=True)
    assesed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='assessed_newborns')
    assesed_on = models.DateTimeField(blank=True, null=True)
    back_condition = models.CharField(max_length=255, blank=True, null=True)
    chest_condition = models.CharField(max_length=255, blank=True, null=True)
    ears_condition = models.CharField(max_length=255, blank=True, null=True)
    eyes_condition = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    general_condition = models.CharField(max_length=255, blank=True, null=True)
    genitalia_condition = models.CharField(max_length=255, blank=True, null=True)
    head_condition = models.CharField(max_length=255, blank=True, null=True)
    hip_joints_condition = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    lower_limbs_condition = models.CharField(max_length=255, blank=True, null=True)
    mouth_condition = models.CharField(max_length=255, blank=True, null=True)
    neck_condition = models.CharField(max_length=255, blank=True, null=True)
    newborn_complication = models.CharField(max_length=255, blank=True, null=True)
    newborn_pmtct = models.CharField(max_length=255, blank=True, null=True)
    nose_condition = models.CharField(max_length=255, blank=True, null=True)
    other_name = models.CharField(max_length=255, blank=True, null=True)
    reflexes_condition = models.CharField(max_length=255, blank=True, null=True)
    third_apgar_score = models.IntegerField(blank=True, null=True)
    upper_limbs_condition = models.CharField(max_length=255, blank=True, null=True)
    baby_gender = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'newborn'


class NursingCarePlan(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    admission = models.ForeignKey('PatientAdmission', models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    entry_date = models.DateTimeField()
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nursing_care_plan'


class NursingCarePlanNote(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    assessment = models.TextField(blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    entry_date = models.DateTimeField()
    evaluation = models.TextField(blank=True, null=True)
    expected_outcome = models.TextField(blank=True, null=True)
    intervention = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    nursing_care_plan = models.ForeignKey(NursingCarePlan, models.DO_NOTHING)
    nursing_diagnosis = models.TextField(blank=True, null=True)
    objective = models.TextField(blank=True, null=True)
    rationale = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nursing_care_plan_note'


class NursingShiftCriticalPatient(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comments = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    nursing_shift_summary = models.ForeignKey('NursingShiftSummary', models.DO_NOTHING)
    patient_admission = models.ForeignKey('PatientAdmission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'nursing_shift_critical_patient'
        unique_together = (('nursing_shift_summary', 'patient_admission'),)


class NursingShiftSummary(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comments = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_shift_summaries')
    date_created = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField()
    last_updated = models.DateTimeField(blank=True, null=True)
    new_nurse_in_charge = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='new_in_charge_shift_summaries')
    start_time = models.DateTimeField()
    total_deaths = models.IntegerField()
    total_discharges = models.IntegerField()
    total_new_admissions = models.IntegerField()
    total_patients = models.IntegerField()
    total_transfers = models.IntegerField()
    ward = models.ForeignKey('Ward', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'nursing_shift_summary'


class OpNote(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    entry_date = models.DateTimeField()
    last_updated = models.DateTimeField(blank=True, null=True)
    note = models.TextField()
    patient_major_theater = models.ForeignKey('PatientMajorTheater', models.DO_NOTHING)
    type = models.CharField(max_length=4)

    class Meta:
        managed = False
        db_table = 'op_note'


class OpSessionTeam(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_op_session_teams')
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    op_note = models.ForeignKey(OpNote, models.DO_NOTHING)
    role = models.CharField(max_length=18)
    staff_member = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='staff_member_op_session_teams' )

    class Meta:
        managed = False
        db_table = 'op_session_team'


class OtherDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    item_image = models.ForeignKey('SystemFile', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    other = models.OneToOneField('Product', models.DO_NOTHING)
    unit_buying_price = models.DecimalField(max_digits=19, decimal_places=2)
    wavco = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'other_detail'


class OutboundMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    batch_identifier = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    contact_phone = models.ForeignKey(MessagingContact, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    delivery_status = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    message = models.TextField()
    message_code = models.ForeignKey(MessageCode, models.DO_NOTHING)
    message_id = models.CharField(max_length=255, blank=True, null=True)
    message_length = models.IntegerField()
    sender_id = models.CharField(max_length=255)
    sms_part = models.IntegerField()
    smsc_reponse = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'outbound_message'


class OutpatientBillableItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    billing_date = models.DateTimeField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic_session = models.ForeignKey(ClinicSession, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField()
    invoice_line = models.ForeignKey(InvoiceLine, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'outpatient_billable_item'


class OutsourcingFacility(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    contact = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'outsourcing_facility'


class PassThroughDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    exemption_type = models.CharField(max_length=9)
    invoice_receipt = models.OneToOneField(InvoiceReceipt, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pass_through_detail'


class Patient(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    version = models.BigIntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    city = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_patients')
    date_created = models.DateTimeField(blank=True, null=True)
    debtor_account = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    email = models.CharField(unique=True, max_length=255, blank=True, null=True)
    employee_account = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='employee_account_patients', blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    partner_type = models.CharField(max_length=18)
    phone_number = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient'


class PatientAdmission(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    admission_date = models.DateTimeField(blank=True, null=True)
    admission_ward = models.ForeignKey('Ward', models.DO_NOTHING)
    admitting_doctor = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='admitting_patient_admissions')
    assigned_doctor = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='assigned_patient_admissions')
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    brought_in_by = models.ForeignKey(EmergencyContact, models.DO_NOTHING, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING,  related_name='created_patient_admissions')
    date_created = models.DateTimeField(blank=True, null=True)
    discharge_care_plan = models.TextField(blank=True, null=True)
    discharge_date = models.DateTimeField(blank=True, null=True)
    discharge_encounter = models.ForeignKey(Encounter, models.DO_NOTHING, blank=True, null=True, related_name='patient_admission_discharge_encounter')
    discharging_doctor = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='discharging_patient_admissions' )
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING, related_name='patient_admission_encounter')
    escorting_nurse = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='escorting_patient_admissions')
    is_closed = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    medical_discharge_date = models.DateTimeField(blank=True, null=True)
    patient_visit = models.ForeignKey('PatientVisit', models.DO_NOTHING)
    receiving_nurse = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='receiving_patient_admissions')
    released_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='released_patient_admissions')
    is_admission_approved = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_admission'


class PatientAllergy(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    allergen = models.ForeignKey(Allergen, models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField()
    patient = models.ForeignKey(Patient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_allergy'
        unique_together = (('patient', 'allergen'),)


class PatientAncillaryCare(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    ancillary_care = models.ForeignKey(AncillaryCare, models.DO_NOTHING)
    annulled_at = models.DateTimeField(blank=True, null=True)
    annulled_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='annulled_ancillary_care')
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_ancillary_care')
    date_created = models.DateTimeField(blank=True, null=True)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    linked_care = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_ancillary_care'


class PatientArtsonContactGroups(models.Model):
    patient = models.OneToOneField(Patient, models.DO_NOTHING, primary_key=True)
    artson_contact_group = models.ForeignKey(ArtsonContactGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_artson_contact_groups'
        unique_together = (('patient', 'artson_contact_group'),)


class PatientBloodTransfusion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    annulled_at = models.DateTimeField(blank=True, null=True)
    annulled_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='annulled_blood_transfusion')
    blood_transfusion = models.ForeignKey(BloodTransfusion, models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='created_blood_transfusion')
    date_created = models.DateTimeField(blank=True, null=True)
    degree_of_urgency = models.CharField(max_length=9)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    number_of_pack = models.IntegerField()
    patient_type = models.CharField(max_length=9)
    validated = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'patient_blood_transfusion'


class PatientChiefComplaint(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    chief_complaint = models.ForeignKey(ChiefComplaint, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_chief_complaint'


class PatientChronicDisease(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    disease = models.ForeignKey(Disease, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_chronic_disease'
        unique_together = (('patient', 'disease'),)


class PatientClinicQueue(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_visit = models.ForeignKey('PatientVisit', models.DO_NOTHING)
    referral_facility = models.ForeignKey('ReferralFacility', models.DO_NOTHING, blank=True, null=True)
    referral_notes = models.CharField(max_length=255)
    referral_type = models.CharField(max_length=8)
    scheduled_date = models.DateTimeField()
    status = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'patient_clinic_queue'


class PatientClinicalProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic_session = models.ForeignKey(ClinicSession, models.DO_NOTHING)
    clinical_profile = models.ForeignKey(ClinicalProfile, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    response = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_clinical_profile'
        unique_together = (('clinic_session', 'clinical_profile'),)


class PatientCommunicareContactGroups(models.Model):
    communicare_contact_group = models.ForeignKey(CommunicareContactGroup, models.DO_NOTHING)
    patient = models.OneToOneField(Patient, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'patient_communicare_contact_groups'
        unique_together = (('patient', 'communicare_contact_group'),)


class PatientDisease(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    classification = models.CharField(max_length=11)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='patient_disease_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    disease = models.ForeignKey(Disease, models.DO_NOTHING)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    is_surveilled = models.BooleanField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    annulled_at = models.DateTimeField(blank=True, null=True)
    annulled_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_disease_annulled_by')

    class Meta:
        managed = False
        db_table = 'patient_disease'
        unique_together = (('encounter', 'disease'),)


class PatientDocumentAttachment(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    document_type = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_visit = models.ForeignKey('PatientVisit', models.DO_NOTHING)
    system_file = models.ForeignKey('SystemFile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_document_attachment'


class PatientDrug(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    annulled_at = models.DateTimeField(blank=True, null=True)
    annulled_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_drug_annulled_by')
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='patient_drug_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    dosage = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    frequency = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    pharmacology = models.ForeignKey('Pharmacology', models.DO_NOTHING)
    route = models.CharField(max_length=17)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_drug'


class PatientDrugBillableItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    cost_of_goods_sold_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='patient_drug_billable_item_cogs_journal_entry')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField()
    inventory_audit = models.ForeignKey(InventoryAudit, models.DO_NOTHING, blank=True, null=True)
    invoice_line = models.ForeignKey(InvoiceLine, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    patient_drug = models.ForeignKey(PatientDrug, models.DO_NOTHING, blank=True, null=True)
    source_store = models.ForeignKey('Store', models.DO_NOTHING)
    stock_control_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='patient_drug_billable_item_stock_journal_entry')
    inventory_batch_level = models.ForeignKey(InventoryBatchLevel, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_drug_billable_item'


class PatientDrugProductCount(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    expected_count = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_drug = models.ForeignKey(PatientDrug, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_drug_product_count'
        unique_together = (('patient_drug', 'product'),)


class PatientEmployer(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    occupation = models.CharField(max_length=255)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    phone_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_employer'


class PatientExternalReferral(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='patient_external_referral_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    referral_facility = models.ForeignKey('ReferralFacility', models.DO_NOTHING, blank=True, null=True)
    referral_location = models.CharField(max_length=255)
    referral_procedure = models.ForeignKey('ReferralProcedure', models.DO_NOTHING, blank=True, null=True)
    referral_type = models.CharField(max_length=255)
    call_made_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_external_referral_call_made_by')
    call_made_on = models.DateTimeField(blank=True, null=True)
    call_received_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_external_referral'


class PatientFamilyPlanning(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    annulled_at = models.DateTimeField(blank=True, null=True)
    annulled_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_family_planning_annulled_by')
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='patient_family_planning_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    family_planning = models.ForeignKey(FamilyPlanning, models.DO_NOTHING)
    is_new_tofp = models.BooleanField()
    is_new_to_method = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    treatment_stage = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_family_planning'


class PatientGeneralExamination(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comment = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    general_examination = models.ForeignKey(GeneralExamination, models.DO_NOTHING)
    is_present = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'patient_general_examination'


class PatientHeadInjury(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_head_injury'


class PatientHealthEducation(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic_session = models.ForeignKey(ClinicSession, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    health_education = models.ForeignKey(HealthEducation, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_health_education'


class PatientHealthInsurances(models.Model):
    health_insurance = models.ForeignKey(HealthInsurance, models.DO_NOTHING)
    patient = models.OneToOneField(Patient, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'patient_health_insurances'
        unique_together = (('patient', 'health_insurance'),)


class PatientImaging(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    annulled_at = models.DateTimeField(blank=True, null=True)
    annulled_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_imaging_annulled_by')
    attended_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_imaging_attended_by')
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='patient_imaging_created_by')
    date_created = models.DateTimeField()
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    imaging = models.ForeignKey(Imaging, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    performed_at = models.DateTimeField(blank=True, null=True)
    procedure_notes = models.TextField(blank=True, null=True)
    remarks = models.TextField(blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'patient_imaging'


class PatientImagingDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_imaging = models.ForeignKey(PatientImaging, models.DO_NOTHING)
    system_file = models.ForeignKey('SystemFile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_imaging_document'


class PatientImagingInventoryItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    cost_of_goods_sold_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='imaging_inventory_item_cogs_journal_entry')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    inventory_audit = models.ForeignKey(InventoryAudit, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_imaging = models.ForeignKey(PatientImaging, models.DO_NOTHING)
    stock_control_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='imaging_inventory_item_stock_journal_entry')
    usage_date = models.DateTimeField()
    void_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_imaging_inventory_item'


class PatientImagingItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField()
    invoice_line = models.ForeignKey(InvoiceLine, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    patient_imaging = models.ForeignKey(PatientImaging, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_imaging_item'


class PatientInputFluidChart(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    additive = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField()
    invoice_line = models.ForeignKey(InvoiceLine, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    patient_admission = models.ForeignKey(PatientAdmission, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    route = models.CharField(max_length=4)
    taken_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'patient_input_fluid_chart'


class PatientInsuranceReference(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    health_insurance = models.ForeignKey(HealthInsurance, models.DO_NOTHING)
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    reference_number = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'patient_insurance_reference'


class PatientLabTest(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    annulled_at = models.DateTimeField(blank=True, null=True)
    annulled_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_lab_test_annulled_by')
    attended_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_lab_test_attended_by')
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinical_note = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    conclusion = models.TextField(blank=True, null=True)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='patient_lab_test_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    is_default = models.BooleanField()
    is_first_time_test = models.BooleanField()
    is_urgent = models.BooleanField()
    lab_test = models.ForeignKey(LabTest, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    linked_test = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    parent_id = models.BigIntegerField()
    performed_at = models.DateTimeField(blank=True, null=True)
    posted_to_external_system = models.BooleanField()
    posting_attempts = models.IntegerField(blank=True, null=True)
    posting_failure_message = models.CharField(max_length=255, blank=True, null=True)
    procedure_notes = models.TextField(blank=True, null=True)
    requires_urgent_action = models.BooleanField()
    result = models.CharField(max_length=255, blank=True, null=True)
    sample_collected_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_lab_test_sample_collected_by')
    sample_collection_time = models.DateTimeField(blank=True, null=True)
    sample_rejected_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_lab_test_sample_rejected_by')
    sample_rejection_note = models.CharField(max_length=255, blank=True, null=True)
    sample_rejection_time = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=255)
    technician_comment = models.TextField(blank=True, null=True)
    verified_at = models.DateTimeField(blank=True, null=True)
    verified_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_lab_test_verified_by')
    visit_type = models.CharField(max_length=28, blank=True, null=True)
    additional_processing_time = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    annullment_location = models.CharField(max_length=255, blank=True, null=True)
    annullment_reason = models.TextField(blank=True, null=True)
    ap_number = models.CharField(max_length=255, blank=True, null=True)
    emailed_at = models.DateTimeField(blank=True, null=True)
    is_leaf = models.BooleanField(blank=True, null=True)
    outsourcing_facility = models.ForeignKey(OutsourcingFacility, models.DO_NOTHING, blank=True, null=True)
    printed_at = models.DateTimeField(blank=True, null=True)
    request_location = models.CharField(max_length=255, blank=True, null=True)
    result_alteration_reason = models.TextField(blank=True, null=True)
    sample_collection_location = models.CharField(max_length=255, blank=True, null=True)
    sample_rejection_location = models.CharField(max_length=255, blank=True, null=True)
    test_unit = models.CharField(max_length=255, blank=True, null=True)
    testing_location = models.CharField(max_length=255, blank=True, null=True)
    high_range = models.CharField(max_length=255, blank=True, null=True)
    low_range = models.CharField(max_length=255, blank=True, null=True)
    sample_type = models.CharField(max_length=255, blank=True, null=True)
    code = models.CharField(max_length=255, blank=True, null=True)
    code_name = models.CharField(max_length=255, blank=True, null=True)
    code_url = models.CharField(max_length=255, blank=True, null=True)
    lab_ext_id = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_lab_test'


class PatientLabTestArchive(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    changed_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    changed_on = models.DateTimeField()
    clinical_note = models.TextField(blank=True, null=True)
    conclusion = models.TextField(blank=True, null=True)
    ip_address = models.CharField(max_length=255)
    patient_lab_test = models.ForeignKey(PatientLabTest, models.DO_NOTHING)
    perpetual_result_alteration_reason = models.CharField(max_length=255, blank=True, null=True)
    perpetual_status = models.CharField(max_length=255, blank=True, null=True)
    result = models.TextField(blank=True, null=True)
    result_alteration_reason = models.TextField(blank=True, null=True)
    technician_comment = models.TextField(blank=True, null=True)
    test_unit = models.CharField(max_length=255, blank=True, null=True)
    user_operating_location = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_lab_test_archive'


class PatientLabTestDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_lab_test = models.ForeignKey(PatientLabTest, models.DO_NOTHING)
    system_file = models.ForeignKey('SystemFile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_lab_test_document'


class PatientLabTestInventoryItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    cost_of_goods_sold_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='lab_test_inventory_item_cogs_journal_entry')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    inventory_audit = models.ForeignKey(InventoryAudit, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_lab_test = models.ForeignKey(PatientLabTest, models.DO_NOTHING)
    stock_control_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='lab_test_inventory_item_stock_journal_entry')
    usage_date = models.DateTimeField()
    void_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_lab_test_inventory_item'


class PatientLabTestOrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    invoice_line = models.ForeignKey(InvoiceLine, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_lab_test = models.ForeignKey(PatientLabTest, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_lab_test_order_item'


class PatientLabourMonitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    bba = models.BooleanField(blank=True, null=True)
    blood_loss_volume = models.FloatField(blank=True, null=True)
    blood_pressure = models.CharField(max_length=255, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    cord_normal = models.BooleanField(blank=True, null=True)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='patient_labour_monitor_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    delivered_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_labour_monitor_delivered_by')
    delivery_comments = models.CharField(max_length=255, blank=True, null=True)
    delivery_mode = models.CharField(max_length=255, blank=True, null=True)
    delivery_time = models.DateTimeField(blank=True, null=True)
    drugs_given = models.CharField(max_length=255, blank=True, null=True)
    episiotomy = models.BooleanField(blank=True, null=True)
    first_stage_duration = models.FloatField(blank=True, null=True)
    gravidity = models.CharField(max_length=255, blank=True, null=True)
    hours_since_rupture = models.FloatField(blank=True, null=True)
    induced_labour = models.BooleanField(blank=True, null=True)
    induction_drug_route = models.CharField(max_length=255, blank=True, null=True)
    induction_drugs = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    membranes_complete = models.BooleanField(blank=True, null=True)
    mother_status = models.CharField(max_length=255, blank=True, null=True)
    parity = models.CharField(max_length=255, blank=True, null=True)
    patient_admission = models.OneToOneField(PatientAdmission, models.DO_NOTHING)
    perineal_tear = models.BooleanField(blank=True, null=True)
    placenta_complete = models.BooleanField(blank=True, null=True)
    placental_weight = models.FloatField(blank=True, null=True)
    pulse = models.IntegerField(blank=True, null=True)
    repair = models.BooleanField(blank=True, null=True)
    respiratory_rate = models.IntegerField(blank=True, null=True)
    ruptured_membranes = models.BooleanField(blank=True, null=True)
    second_stage_duration = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    vaginal_exams_count = models.IntegerField(blank=True, null=True)
    edd = models.DateTimeField(blank=True, null=True)
    lmp = models.DateTimeField(blank=True, null=True)
    obstetric_care = models.CharField(max_length=255, blank=True, null=True)
    obstetric_complication = models.CharField(max_length=255, blank=True, null=True)
    pregnancy_history = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_labour_monitor'


class PatientMajorTheater(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    administered_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_major_theater_administered_by')
    approx_duration = models.IntegerField()
    attendant_comment = models.TextField(blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='patient_major_theater_created_by')
    date_created = models.DateTimeField()
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    major_theater = models.ForeignKey(MajorTheater, models.DO_NOTHING)
    major_theater_room = models.ForeignKey(MajorTheaterRoom, models.DO_NOTHING, blank=True, null=True)
    performed_at = models.DateTimeField(blank=True, null=True)
    scheduled_date = models.DateTimeField()
    scheduled_time = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'patient_major_theater'


class PatientMajorTheaterInventoryItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    cost_of_goods_sold_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='major_theater_inventory_item_cogs_journal_entry')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    inventory_audit = models.ForeignKey(InventoryAudit, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_major_theater = models.ForeignKey(PatientMajorTheater, models.DO_NOTHING)
    stock_control_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='major_theater_inventory_item_stock_journal_entry')
    usage_date = models.DateTimeField()
    void_status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_major_theater_inventory_item'


class PatientMajorTheaterItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    invoice_line = models.ForeignKey(InvoiceLine, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_major_theater = models.ForeignKey(PatientMajorTheater, models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_major_theater_item'


class PatientMinorTheater(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    annulled_at = models.DateTimeField(blank=True, null=True)
    annulled_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_minor_theater_annulled_by')
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='patient_minor_theater_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    minor_theater = models.ForeignKey(MinorTheater, models.DO_NOTHING)
    treatment_duration = models.CharField(max_length=26, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_minor_theater'


class PatientMinorTheaterPatientMinorTheater(models.Model):
    patient_minor_theater_patient_minor_theater_items = models.ForeignKey(PatientMinorTheater, models.DO_NOTHING, blank=True, null=True, related_name='patient_minor_theater_patient_minor_theater_items')
    patient_minor_theater = models.ForeignKey(PatientMinorTheater, models.DO_NOTHING, blank=True, null=True, related_name='patient_minor_theater_patient_minor_theater')

    class Meta:
        managed = False
        db_table = 'patient_minor_theater_patient_minor_theater'


class PatientOutputFluidChart(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    patient_admission = models.ForeignKey(PatientAdmission, models.DO_NOTHING)
    remarks = models.CharField(max_length=255, blank=True, null=True)
    taken_at = models.DateTimeField()
    type = models.CharField(max_length=17)
    urine_comments = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'patient_output_fluid_chart'


class PatientRelationship(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    direction = models.CharField(max_length=3)
    last_updated = models.DateTimeField(blank=True, null=True)
    persona = models.ForeignKey(Patient, models.DO_NOTHING, related_name='patient_relationship_persona')
    personb = models.ForeignKey(Patient, models.DO_NOTHING, related_name='patient_relationship_personb')
    relationship = models.ForeignKey('RelationshipType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_relationship'
        unique_together = (('direction', 'personb', 'relationship', 'persona'),)


class PatientRequisition(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='patient_requisition_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    is_approved = models.CharField(max_length=16, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    patient_requisition_number = models.CharField(max_length=255, blank=True, null=True)
    processed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='patient_requisition_processed_by')
    processing_comment = models.CharField(max_length=255, blank=True, null=True)
    processing_date = models.DateTimeField(blank=True, null=True)
    requester_comment = models.CharField(max_length=255, blank=True, null=True)
    source_store = models.ForeignKey('Store', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'patient_requisition'


class PatientRequisitionItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    bill_to_patient = models.BooleanField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    cost_of_goods_sold_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='patient_requisition_item_cogs_journal_entry')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    expected_quantity = models.DecimalField(max_digits=19, decimal_places=2)
    invoice_line = models.ForeignKey(InvoiceLine, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient_requisition = models.ForeignKey(PatientRequisition, models.DO_NOTHING)
    patient_visit = models.ForeignKey('PatientVisit', models.DO_NOTHING)
    product = models.ForeignKey('Product', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    stock_control_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='patient_requisition_item_stock_journal_entry')
    unit_buying_price = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_requisition_item'


class PatientSickOff(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    narration = models.TextField()

    class Meta:
        managed = False
        db_table = 'patient_sick_off'


class PatientVisit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    b_referring_facility = models.ForeignKey('ReferringFacility', models.DO_NOTHING, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_closed = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    medical_cover_line = models.ForeignKey(MedicalCoverLine, models.DO_NOTHING, blank=True, null=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    process = models.CharField(max_length=9)
    referring_facility = models.CharField(max_length=255, blank=True, null=True)
    referring_physician = models.CharField(max_length=255, blank=True, null=True)
    referring_physician_contact = models.CharField(max_length=255, blank=True, null=True)
    service_package = models.ForeignKey('ServicePackage', models.DO_NOTHING, blank=True, null=True)
    waiver_case = models.ForeignKey('WaiverCase', models.DO_NOTHING, blank=True, null=True)
    b_referring_physician = models.ForeignKey('ReferringPhysician', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patient_visit'


class PaymentMode(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    credit_ledger_account_id = models.BigIntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    debit_ledger_account_id = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    transaction_fee_fixed = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    transaction_fee_ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, blank=True, null=True)
    transaction_fee_percentage = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_mode'


class PayrollBreakdown(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='payroll_breakdown_created_by')
    credited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='payroll_breakdown_credited_account')
    date_created = models.DateTimeField(blank=True, null=True)
    debited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='payroll_breakdown_debited_account')
    deduction = models.ForeignKey(Deduction, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    earning = models.ForeignKey(Earning, models.DO_NOTHING, blank=True, null=True)
    is_taxable = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    payroll_period = models.ForeignKey('PayrollPeriod', models.DO_NOTHING)
    personal_relief = models.ForeignKey('PersonalRelief', models.DO_NOTHING, blank=True, null=True)
    ref_entry = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='payroll_breakdown_staff')

    class Meta:
        managed = False
        db_table = 'payroll_breakdown'


class PayrollDeductionPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    credited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='payroll_deduction_payment_credited_account')
    date_created = models.DateTimeField(blank=True, null=True)
    debited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='payroll_deduction_payment_debited_account')
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    payment_date = models.DateTimeField()
    payroll_breakdown = models.ForeignKey(PayrollBreakdown, models.DO_NOTHING)
    voucher_payment = models.ForeignKey('VoucherPayment', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payroll_deduction_payment'


class PayrollPayBankSchedule(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    employee_bank_account = models.ForeignKey(EmployeeBankAccount, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    payroll_breakdown = models.ForeignKey(PayrollBreakdown, models.DO_NOTHING)
    payroll_period = models.ForeignKey('PayrollPeriod', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'payroll_pay_bank_schedule'


class PayrollPayableDay(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='payroll_payable_day_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    payroll_days = models.IntegerField()
    payroll_period = models.ForeignKey('PayrollPeriod', models.DO_NOTHING)
    staff = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='payroll_payable_day_staff')

    class Meta:
        managed = False
        db_table = 'payroll_payable_day'


class PayrollPeriod(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    bank_schedule_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='payroll_period_bank_schedule_by')
    bank_schedule_on = models.DateTimeField(blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    month = models.ForeignKey('SystemMonth', models.DO_NOTHING)
    prepared_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='payroll_period_prepared_by')
    prepared_on = models.DateTimeField(blank=True, null=True)
    processed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='payroll_period_processed_by')
    processed_on = models.DateTimeField(blank=True, null=True)
    year = models.ForeignKey('SystemYear', models.DO_NOTHING)
    is_approved = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payroll_period'
        unique_together = (('year', 'month'),)


class PayrollSettlementDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    invoice_receipt = models.OneToOneField(InvoiceReceipt, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payroll_settlement_detail'


class PerformanceIndicatorResponseType(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'performance_indicator_response_type'
        unique_together = (('branch', 'name'),)


class PerformanceIndicatorResponseTypeOption(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    order_sequence = models.IntegerField(blank=True, null=True)
    performance_indicator_response_type = models.ForeignKey(PerformanceIndicatorResponseType, models.DO_NOTHING)
    rating = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'performance_indicator_response_type_option'


class PerformanceQuestionsGroup(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'performance_questions_group'
        unique_together = (('branch', 'name'),)


class PerformanceQuestionsGroupKeyPerformanceIndicator(models.Model):
    performance_questions_group_key_performance_indicators = models.ForeignKey(PerformanceQuestionsGroup, models.DO_NOTHING, blank=True, null=True)
    key_performance_indicator = models.ForeignKey(KeyPerformanceIndicator, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'performance_questions_group_key_performance_indicator'


class PerformanceReview(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='performance_review_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    due_date = models.DateTimeField()
    employee = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='performance_review_employee')
    employee_department_unit = models.ForeignKey(Department, models.DO_NOTHING, related_name='performance_review_employee_department_unit')
    employee_job_title = models.ForeignKey(JobTitle, models.DO_NOTHING, related_name='performance_review_employee_job_title')
    end_date = models.DateTimeField()
    last_updated = models.DateTimeField(blank=True, null=True)
    reviewer = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='performance_review_reviewer')
    reviewer_department_unit = models.ForeignKey(Department, models.DO_NOTHING, related_name='performance_review_reviewer_department_unit')
    reviewer_job_title = models.ForeignKey(JobTitle, models.DO_NOTHING, related_name='performance_review_reviewer_job_title')
    start_date = models.DateTimeField()
    status = models.CharField(max_length=11)
    target_setting_deadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'performance_review'


class PerformanceReviewKeyIndicator(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    actual = models.IntegerField(blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    employee_comments = models.TextField(blank=True, null=True)
    employee_edit_date = models.DateTimeField(blank=True, null=True)
    employee_rating = models.ForeignKey(PerformanceIndicatorResponseTypeOption, models.DO_NOTHING, blank=True, null=True, related_name='performance_key_indicator_employee_rating')
    key_performance_indicator = models.ForeignKey(KeyPerformanceIndicator, models.DO_NOTHING)
    performance_review = models.ForeignKey(PerformanceReview, models.DO_NOTHING)
    planned = models.IntegerField(blank=True, null=True)
    reviewer_comments = models.TextField(blank=True, null=True)
    reviewer_edit_date = models.DateTimeField(blank=True, null=True)
    reviewer_rating = models.ForeignKey(PerformanceIndicatorResponseTypeOption, models.DO_NOTHING, blank=True, null=True, related_name='performance_key_indicator_reviewer_rating')

    class Meta:
        managed = False
        db_table = 'performance_review_key_indicator'
        unique_together = (('performance_review', 'key_performance_indicator'),)


class PersonalRelief(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    deduction = models.ForeignKey(Deduction, models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    max_relief_amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'personal_relief'


class PettyCashMovement(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    credited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='petty_cash_movement_credited_account')
    date_created = models.DateTimeField(blank=True, null=True)
    debited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='petty_cash_movement_debited_account')
    last_updated = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'petty_cash_movement'


class Pharmacology(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    dosage = models.CharField(max_length=255, blank=True, null=True)
    drug_name = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    frequency = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    prescription_category = models.ForeignKey('PrescriptionCategory', models.DO_NOTHING)
    route = models.CharField(max_length=17)
    system_defined = models.BooleanField()
    is_active = models.BooleanField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pharmacology'


class PhysicalExaminationTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    is_default = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    system_defined = models.BooleanField()
    template = models.TextField()

    class Meta:
        managed = False
        db_table = 'physical_examination_template'
        unique_together = (('branch', 'name'),)


class PostOpChecklist(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    blades_add = models.IntegerField(blank=True, null=True)
    blades_end = models.CharField(max_length=255, blank=True, null=True)
    blades_start = models.IntegerField(blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    circulator_nurse = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='postopchecklist_created_by')
    cs_pack = models.BooleanField()
    cs_pack_at = models.DateTimeField(blank=True, null=True)
    date_created = models.DateTimeField()
    general_pack = models.BooleanField()
    general_pack_at = models.DateTimeField(blank=True, null=True)
    laparatomy_pack = models.BooleanField()
    laparatomy_pack_at = models.DateTimeField(blank=True, null=True)
    large_gauze_add = models.IntegerField(blank=True, null=True)
    large_gauze_end = models.CharField(max_length=255, blank=True, null=True)
    large_gauze_start = models.IntegerField(blank=True, null=True)
    last_updated = models.DateTimeField()
    medium_gauze_add = models.IntegerField(blank=True, null=True)
    medium_gauze_end = models.CharField(max_length=255, blank=True, null=True)
    medium_gauze_start = models.IntegerField(blank=True, null=True)
    ortho_pack = models.BooleanField()
    ortho_pack_at = models.DateTimeField(blank=True, null=True)
    patient_major_theater = models.ForeignKey(PatientMajorTheater, models.DO_NOTHING)
    scrub_nurse = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='postopchecklist_scrub_nurse')
    small_gauze_add = models.IntegerField(blank=True, null=True)
    small_gauze_end = models.CharField(max_length=255, blank=True, null=True)
    small_gauze_start = models.IntegerField(blank=True, null=True)
    sutures_add = models.IntegerField(blank=True, null=True)
    sutures_end = models.CharField(max_length=255, blank=True, null=True)
    sutures_start = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post_op_checklist'


class PreOpChecklist(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    bp = models.CharField(max_length=255, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    by_whom = models.CharField(max_length=255, blank=True, null=True)
    catheterization = models.BooleanField()
    company = models.ForeignKey(Company, models.DO_NOTHING)
    consent = models.BooleanField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField()
    dentures = models.BooleanField()
    drug_dosage = models.CharField(max_length=255, blank=True, null=True)
    drug_given = models.CharField(max_length=255, blank=True, null=True)
    gown = models.BooleanField()
    gx = models.CharField(max_length=255, blank=True, null=True)
    hb = models.CharField(max_length=255, blank=True, null=True)
    ivline = models.BooleanField()
    jewellery = models.BooleanField()
    last_updated = models.DateTimeField()
    patient_major_theater = models.ForeignKey(PatientMajorTheater, models.DO_NOTHING)
    premedication = models.BooleanField()
    prepared_by = models.CharField(max_length=255, blank=True, null=True)
    pulse = models.CharField(max_length=255, blank=True, null=True)
    received_by = models.CharField(max_length=255, blank=True, null=True)
    resp = models.CharField(max_length=255, blank=True, null=True)
    shave = models.BooleanField()
    starve = models.BooleanField()
    temp = models.CharField(max_length=255, blank=True, null=True)
    time_given = models.DateTimeField(blank=True, null=True)
    wristband = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pre_op_checklist'


class PrescriptionCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'prescription_category'
        unique_together = (('branch', 'name'),)


class PrescriptionDuration(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    aliases = models.TextField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    duration = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescription_duration'


class PrescriptionFrequency(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    aliases = models.TextField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    frequency = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescription_frequency'


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    dispensing_unit = models.ForeignKey(InventoryUnit, models.DO_NOTHING, blank=True, null=True, related_name='product_dispensing_unit')
    is_available = models.BooleanField()
    is_cost_fixed = models.BooleanField()
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    product = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True, related_name='product_related_name')
    product_category = models.ForeignKey('ProductCategory', models.DO_NOTHING)
    product_type = models.CharField(max_length=10)
    purchase_cr_ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, blank=True, null=True, related_name='product_purchase_cr_ledger_account')
    purchase_dr_ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, blank=True, null=True, related_name='product_purchase_dr_ledger_account')
    qty_per_unit = models.IntegerField()
    receiving_unit = models.ForeignKey(InventoryUnit, models.DO_NOTHING, blank=True, null=True, related_name='product_receiving_unit')
    saleipcr_ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, blank=True, null=True, related_name='product_saleipcr_ledger_account')
    saleipdr_ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, blank=True, null=True, related_name='product_saleipdr_ledger_account')
    saleopcr_ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, blank=True, null=True, related_name='product_saleopcr_ledger_account')
    saleopdr_ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, blank=True, null=True, related_name='product_saleopdr_ledger_account')
    sku = models.CharField(max_length=255, blank=True, null=True)
    unit_selling_price = models.DecimalField(max_digits=19, decimal_places=2)
    vat_class = models.ForeignKey('VatClass', models.DO_NOTHING)
    product_bill_category = models.ForeignKey('ProductBillCategory', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product'
        unique_together = (('sku', 'branch', 'name'),)


class ProductBatchLevel(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    batch_number = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    expiry_date = models.DateTimeField(blank=True, null=True)
    initial_quantity = models.DecimalField(max_digits=19, decimal_places=2)
    inventory_audit = models.ForeignKey(InventoryAudit, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    store = models.ForeignKey('Store', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_batch_level'


class ProductBillCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    product_category_type = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'product_bill_category'
        unique_together = (('product_category_type', 'branch', 'name'),)


class ProductCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    product_category_type = models.CharField(max_length=10)
    expense_code = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_category'
        unique_together = (('product_category_type', 'branch', 'name'),)


class ProductCategoryLedgerLinkage(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING)
    product_category = models.ForeignKey(ProductCategory, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_category_ledger_linkage'


class ProductPatientDrug(models.Model):
    product_patient_drugs = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    patient_drug = models.ForeignKey(PatientDrug, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_patient_drug'


class ProductPatientImaging(models.Model):
    product_patient_imaging = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    patient_imaging = models.ForeignKey(PatientImaging, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_patient_imaging'


class ProductPatientLabTest(models.Model):
    product_patient_lab_tests = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    patient_lab_test = models.ForeignKey(PatientLabTest, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'product_patient_lab_test'


class ProductPharmacology(models.Model):
    pharmacology = models.ForeignKey(Pharmacology, models.DO_NOTHING)
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'product_pharmacology'
        unique_together = (('product', 'pharmacology'),)


class ProductSuppliers(models.Model):
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING)
    product = models.OneToOneField(Product, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'product_suppliers'
        unique_together = (('product', 'supplier'),)


class ProjectFinancing(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    completion_date = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'project_financing'


class ProjectFinancingLine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    direct_expense = models.ForeignKey(GeneralLedger, models.DO_NOTHING, blank=True, null=True, related_name='project_financing_line_direct_expense')
    direct_income = models.ForeignKey(GeneralLedger, models.DO_NOTHING, blank=True, null=True, related_name='project_financing_line_direct_income')
    invoice = models.ForeignKey(Invoice, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    project_financing = models.ForeignKey(ProjectFinancing, models.DO_NOTHING)
    rate = models.DecimalField(max_digits=19, decimal_places=2)
    voucher = models.ForeignKey('Voucher', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_financing_line'
        unique_together = (('project_financing', 'direct_expense'), ('project_financing', 'direct_income'), ('project_financing', 'invoice'), ('project_financing', 'voucher'),)


class ProvisionalPayslip(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='provisional_payslip_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    deduction = models.ForeignKey(Deduction, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    earning = models.ForeignKey(Earning, models.DO_NOTHING, blank=True, null=True)
    is_taxable = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    payroll_period = models.ForeignKey(PayrollPeriod, models.DO_NOTHING)
    personal_relief = models.ForeignKey(PersonalRelief, models.DO_NOTHING, blank=True, null=True)
    ref_entry = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='provisional_payslip_staff')

    class Meta:
        managed = False
        db_table = 'provisional_payslip'


class PurchaseOrder(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    approval_comment = models.CharField(max_length=255, blank=True, null=True)
    approval_date = models.DateTimeField(blank=True, null=True)
    approved = models.CharField(max_length=16, blank=True, null=True)
    approved_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='purchase_order_approved_by')
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='purchase_order_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    delivery_charge = models.DecimalField(max_digits=19, decimal_places=2)
    delivery_date_required = models.DateTimeField()
    department = models.ForeignKey(Department, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    processed = models.CharField(max_length=9, blank=True, null=True)
    processed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='purchase_order_processed_by')
    processed_comment = models.TextField(blank=True, null=True)
    processing_date = models.DateTimeField(blank=True, null=True)
    purchase_order_number = models.CharField(max_length=255, blank=True, null=True)
    purchase_requisition = models.OneToOneField('PurchaseRequisition', models.DO_NOTHING)
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_order'


class PurchaseOrderItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    budget_line = models.ForeignKey(BudgetLine, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    inventory_audit = models.ForeignKey(InventoryAudit, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    processed_commit = models.DecimalField(max_digits=19, decimal_places=2)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    purchase_order = models.ForeignKey(PurchaseOrder, models.DO_NOTHING)
    purchase_order_item_number = models.CharField(max_length=255, blank=True, null=True)
    purchase_requisition_item = models.ForeignKey('PurchaseRequisitionItem', models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    unit_price = models.DecimalField(max_digits=19, decimal_places=2)
    vat_rate = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'purchase_order_item'
        unique_together = (('purchase_order', 'product'),)


class PurchaseRequisition(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    approval_comment = models.TextField(blank=True, null=True)
    approval_date = models.DateTimeField(blank=True, null=True)
    approved = models.CharField(max_length=16, blank=True, null=True)
    approved_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='purchase_requisition_approved_by')
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='purchase_requisition_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    delivery_date_required = models.DateTimeField()
    department = models.ForeignKey(Department, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    purchase_requisition_number = models.CharField(max_length=255, blank=True, null=True)
    requester_comment = models.CharField(max_length=255)
    supplier = models.ForeignKey('Supplier', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'purchase_requisition'


class PurchaseRequisitionItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    purchase_requisition = models.ForeignKey(PurchaseRequisition, models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    unit_price = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'purchase_requisition_item'
        unique_together = (('purchase_requisition', 'product'),)


class QueuedOutboundMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    entity_id = models.BigIntegerField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    message = models.TextField()
    message_type = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=255)
    relay_attempt = models.IntegerField()
    reminder_date = models.DateTimeField()
    sent_at = models.DateTimeField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'queued_outbound_message'


class Quotation(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    quotation_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quotation'


class QuotationLine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    item_name = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    quotation = models.ForeignKey(Quotation, models.DO_NOTHING)
    quotation_line_number = models.CharField(max_length=255, blank=True, null=True)
    unit_cost = models.DecimalField(max_digits=19, decimal_places=2)
    vat_rate = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quotation_line'


class ReferralFacility(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    code = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    owner = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referral_facility'


class ReferralProcedure(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'referral_procedure'


class ReferringFacility(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'referring_facility'


class ReferringPhysician(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    contact = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    referring_facility = models.ForeignKey(ReferringFacility, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'referring_physician'


class RefundRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    client = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='refund_request_created_by')
    credited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True,related_name='refund_request_credited_account')
    date_created = models.DateTimeField(blank=True, null=True)
    date_processed = models.DateTimeField(blank=True, null=True)
    debited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True,related_name='refund_request_debited_account')
    invoice_line = models.ForeignKey(InvoiceLine, models.DO_NOTHING, blank=True, null=True)
    invoice_receipt = models.ForeignKey(InvoiceReceipt, models.DO_NOTHING, blank=True, null=True)
    is_approved = models.CharField(max_length=9)
    last_updated = models.DateTimeField(blank=True, null=True)
    processed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='refund_request_processed_by')
    reason = models.TextField()
    refund_type = models.CharField(max_length=7)
    transaction_number = models.CharField(max_length=255, blank=True, null=True)
    void_invoice_item = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'refund_request'
class RegisteredPatientDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    birth_date = models.DateTimeField()
    date_created = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6)
    geo_area_level5 = models.ForeignKey(GeoAreaLevel5, models.DO_NOTHING, blank=True, null=True)
    id_no = models.CharField(unique=True, max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    marital_status = models.CharField(max_length=9, blank=True, null=True)
    nationality = models.ForeignKey(Country, models.DO_NOTHING)
    other_name = models.CharField(max_length=255, blank=True, null=True)
    patient = models.OneToOneField(Patient, models.DO_NOTHING)
    patient_image = models.ForeignKey('SystemFile', models.DO_NOTHING, blank=True, null=True)
    sub_location = models.CharField(max_length=255, blank=True, null=True)
    village = models.CharField(max_length=255, blank=True, null=True)
    ethnicity = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registered_patient_detail'

class RegisteredPatientDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    birth_date = models.DateTimeField()
    date_created = models.DateTimeField(blank=True, null=True)
    first_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=6)
    geo_area_level5 = models.ForeignKey(GeoAreaLevel5, models.DO_NOTHING, blank=True, null=True)
    id_no = models.CharField(unique=True, max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    marital_status = models.CharField(max_length=9, blank=True, null=True)
    nationality = models.ForeignKey(Country, models.DO_NOTHING)
    other_name = models.CharField(max_length=255, blank=True, null=True)
    patient = models.OneToOneField(Patient, models.DO_NOTHING)
    patient_image = models.ForeignKey('SystemFile', models.DO_NOTHING, blank=True, null=True)
    sub_location = models.CharField(max_length=255, blank=True, null=True)
    village = models.CharField(max_length=255, blank=True, null=True)
    ethnicity = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'registered_patient_detail'


class RelationshipType(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    a_is_tob = models.CharField(max_length=255)
    b_is_toa = models.CharField(max_length=255)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'relationship_type'


class ReportAudit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    begin_timestamp = models.DateTimeField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    end_timestamp = models.DateTimeField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    report_group = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'report_audit'
        unique_together = (('branch', 'name'),)


class Role(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by_id = models.IntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    system_defined = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'role'
        unique_together = (('branch', 'name'),)


class RoleSystemArtifact(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    can_create = models.BooleanField()
    can_delete = models.BooleanField()
    can_execute = models.BooleanField()
    can_read = models.BooleanField()
    can_update = models.BooleanField()
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    role = models.ForeignKey(Role, models.DO_NOTHING)
    system_artifact = models.ForeignKey('SystemArtifact', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'role_system_artifact'
        unique_together = (('system_artifact', 'role'),)


class Room(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='room_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    in_charge = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='room_in_charge')
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    ward = models.ForeignKey('Ward', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'room'
        unique_together = (('ward', 'branch', 'name'),)


class ScaleEarning(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by_id = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    earning = models.ForeignKey(Earning, models.DO_NOTHING)
    is_active = models.BooleanField()
    job_scale = models.ForeignKey(JobScale, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'scale_earning'


class ScaleEarningEmploymentStatuses(models.Model):
    employment_status = models.ForeignKey(EmploymentStatus, models.DO_NOTHING)
    scale_earning = models.OneToOneField(ScaleEarning, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'scale_earning_employment_statuses'
        unique_together = (('scale_earning', 'employment_status'),)


class ScaleEarningRate(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by_id = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    reference_amount = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    reference_earning = models.ForeignKey(ScaleEarning, models.DO_NOTHING, blank=True, null=True, related_name='scale_earning_rate_reference_earning')
    scale_earning = models.ForeignKey(ScaleEarning, models.DO_NOTHING, related_name='scale_earning_rate_scale_earning')

    class Meta:
        managed = False
        db_table = 'scale_earning_rate'


class SchemaMigrations(models.Model):
    version = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'schema_migrations'


class SchemeExclusion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    insurance_scheme = models.ForeignKey(InsuranceScheme, models.DO_NOTHING)
    last_updated = models.DateTimeField()
    product = models.ForeignKey(Product, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'scheme_exclusion'


class ServicePackage(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'service_package'


class ServicePackageLine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    service_package = models.ForeignKey(ServicePackage, models.DO_NOTHING)
    unit_selling_price = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'service_package_line'


class ShiftAudit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    end_break_date = models.DateTimeField(blank=True, null=True)
    end_break_time = models.TimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    punch_in_date = models.DateTimeField()
    punch_in_time = models.TimeField()
    punch_out_date = models.DateTimeField(blank=True, null=True)
    punch_out_time = models.TimeField(blank=True, null=True)
    staff = models.ForeignKey('SystemUser', models.DO_NOTHING)
    start_break_date = models.DateTimeField(blank=True, null=True)
    start_break_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shift_audit'


class StaffPayrollDeduction(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='staff_payroll_deduction_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    deduction = models.ForeignKey(Deduction, models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    reference_earning = models.ForeignKey('StaffPayrollEarning', models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='staff_payroll_deduction_staff')

    class Meta:
        managed = False
        db_table = 'staff_payroll_deduction'


class StaffPayrollEarning(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='staff_payroll_earning_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    earning = models.ForeignKey(Earning, models.DO_NOTHING)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    reference_earning = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    staff = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='staff_payroll_earning_staff')

    class Meta:
        managed = False
        db_table = 'staff_payroll_earning'


class StaffPersonalReliefPremium(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='staff_personal_relief_premium_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    personal_relief = models.ForeignKey(PersonalRelief, models.DO_NOTHING)
    staff = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='staff_personal_relief_premium_staff')

    class Meta:
        managed = False
        db_table = 'staff_personal_relief_premium'


class StandardDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    invoice_receipt = models.OneToOneField(InvoiceReceipt, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    payment_mode = models.ForeignKey(PaymentMode, models.DO_NOTHING)
    receipt_number = models.CharField(max_length=255, blank=True, null=True)
    tendered = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'standard_detail'


class Store(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    cogs_account_id = models.BigIntegerField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    parent_id = models.BigIntegerField()
    stock_control_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, blank=True, null=True, related_name='store_stock_control_account'
                                                )
    adjustment_control_ledger = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, blank=True, null=True, related_name='store_adjustment_control_ledger')

    class Meta:
        managed = False
        db_table = 'store'
        unique_together = (('branch', 'name'),)


class StoreInventory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    replenishment_level = models.DecimalField(max_digits=19, decimal_places=2)
    store = models.ForeignKey(Store, models.DO_NOTHING)
    unit_in_stock = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'store_inventory'
        unique_together = (('product', 'store'),)


class StoreManager(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='store_manager_created_by')
    date_created = models.DateTimeField()
    last_updated = models.DateTimeField()
    manager = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='store_manager_manager')
    store = models.ForeignKey(Store, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'store_manager'
        unique_together = (('store', 'manager'),)


class StoreReceipt(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='store_receipt_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    date_received = models.DateTimeField()
    delivering_department = models.ForeignKey(Department, models.DO_NOTHING, blank=True, null=True)
    deliveringic = models.ForeignKey(InternalConsumption, models.DO_NOTHING, blank=True, null=True)
    delivering_staff = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='store_receipt_delivering_staff')
    delivering_supplier = models.ForeignKey('Supplier', models.DO_NOTHING, blank=True, null=True)
    destination_store = models.ForeignKey(Store, models.DO_NOTHING)
    is_approved = models.CharField(max_length=7, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    other_delivery = models.CharField(max_length=255, blank=True, null=True)
    processed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='store_receipt_processed_by')
    processing_comment = models.TextField(blank=True, null=True)
    processing_date = models.DateTimeField(blank=True, null=True)
    receipt_type = models.CharField(max_length=15)
    receiver_comment = models.TextField()
    store_receipt_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store_receipt'


class StoreReceiptItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    store_receipt = models.ForeignKey(StoreReceipt, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'store_receipt_item'


class StoreRequisition(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, related_name='store_requisition_created_by')
    date_created = models.DateTimeField(blank=True, null=True)
    date_required = models.DateTimeField()
    destination_store = models.ForeignKey(Store, models.DO_NOTHING, related_name='store_requisition_destination_store')
    is_approved = models.CharField(max_length=16, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    processed_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True, related_name='store_requisition_processed_by')
    processing_comment = models.TextField(blank=True, null=True)
    processing_date = models.DateTimeField(blank=True, null=True)
    requester_comment = models.TextField()
    source_store = models.ForeignKey(Store, models.DO_NOTHING, related_name='store_requisition_source_store')
    store_requisition_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store_requisition'


class StoreRequisitionItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    destination_stock_control_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='destination_requisition_items')
    expected_quantity = models.DecimalField(max_digits=19, decimal_places=2)
    last_updated = models.DateTimeField(blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    source_stock_control_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='source_requisition_items')
    store_requisition = models.ForeignKey(StoreRequisition, models.DO_NOTHING)
    unit_buying_price = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store_requisition_item'


class StoreRequisitionItemBatchAudit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    store_requisition_item = models.ForeignKey(StoreRequisitionItem, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'store_requisition_item_batch_audit'


class StoreSale(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    cost_of_goods_sold_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='cost_of_goods_sold_sales')
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    invoice_line = models.OneToOneField(InvoiceLine, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    status = models.CharField(max_length=8)
    stock_control_journal_entry = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='stock_control_sales')
    store = models.ForeignKey(Store, models.DO_NOTHING)
    unit_buying_price = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'store_sale'


class Supplier(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    address = models.CharField(max_length=255, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    city = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    contact_email = models.CharField(max_length=255, blank=True, null=True)
    contact_name = models.CharField(max_length=255, blank=True, null=True)
    contact_phone_number = models.CharField(max_length=255, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    credit_period = models.IntegerField(blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    fax = models.CharField(max_length=255, blank=True, null=True)
    is_suspended = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    pin = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=255, blank=True, null=True)
    supplier_category = models.ForeignKey('SupplierCategory', models.DO_NOTHING)
    website = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supplier'


class SupplierArtsonContactGroups(models.Model):
    artson_contact_group = models.ForeignKey(ArtsonContactGroup, models.DO_NOTHING)
    supplier = models.OneToOneField(Supplier, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'supplier_artson_contact_groups'
        unique_together = (('supplier', 'artson_contact_group'),)


class SupplierCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'supplier_category'
        unique_together = (('branch', 'name'),)


class SupplierCommunicareContactGroups(models.Model):
    communicare_contact_group = models.ForeignKey(CommunicareContactGroup, models.DO_NOTHING)
    supplier = models.OneToOneField(Supplier, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'supplier_communicare_contact_groups'
        unique_together = (('supplier', 'communicare_contact_group'),)


class SupplyDetail(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    item_image = models.ForeignKey('SystemFile', models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    supply = models.OneToOneField(Product, models.DO_NOTHING)
    unit_buying_price = models.DecimalField(max_digits=19, decimal_places=2)
    max_stock = models.IntegerField(blank=True, null=True)
    min_stock = models.IntegerField(blank=True, null=True)
    wavco = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'supply_detail'


class SystemArtifact(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    display_name = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    module = models.ForeignKey(Module, models.DO_NOTHING)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'system_artifact'


class SystemConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey('SystemUser', models.DO_NOTHING, blank=True, null=True)
    ctype = models.CharField(max_length=7)
    cvalue = models.TextField()
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_config'
        unique_together = (('parent', 'name'),)


class SystemConfigCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    display_name = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'system_config_category'


class SystemFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    display_name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    path = models.CharField(max_length=255)
    size = models.IntegerField()
    storage_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'system_file'


class SystemJob(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_enabled = models.BooleanField()
    last_executed = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'system_job'


class SystemJobAudit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comment = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField()
    system_job = models.ForeignKey(SystemJob, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'system_job_audit'


class SystemMonth(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'system_month'


class SystemUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING)
    description = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=255)
    employee = models.ForeignKey(Employee, models.DO_NOTHING, blank=True, null=True)
    first_name = models.CharField(max_length=255)
    infinity_employee_number = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField()
    last_name = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    other_name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    role = models.ForeignKey(Role, models.DO_NOTHING)
    title = models.CharField(max_length=255, blank=True, null=True)
    user_signature = models.ForeignKey(SystemFile, models.DO_NOTHING, blank=True, null=True)
    is_locked = models.BooleanField(blank=True, null=True)
    last_login_attempt = models.DateTimeField(blank=True, null=True)
    login_attempts = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'system_user'
        unique_together = (('branch', 'email'),)


class SystemUserArtsonContactGroups(models.Model):
    artson_contact_group = models.ForeignKey(ArtsonContactGroup, models.DO_NOTHING)
    system_user = models.OneToOneField(SystemUser, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'system_user_artson_contact_groups'
        unique_together = (('system_user', 'artson_contact_group'),)


class SystemUserCommunicareContactGroups(models.Model):
    communicare_contact_group = models.ForeignKey(CommunicareContactGroup, models.DO_NOTHING)
    system_user = models.OneToOneField(SystemUser, models.DO_NOTHING, primary_key=True)

    class Meta:
        managed = False
        db_table = 'system_user_communicare_contact_groups'
        unique_together = (('system_user', 'communicare_contact_group'),)


class SystemUserProfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    system_user = models.OneToOneField(SystemUser, models.DO_NOTHING)
    theme = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'system_user_profile'


class SystemYear(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'system_year'


class TerminationReason(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'termination_reason'
        unique_together = (('branch', 'name'),)


class TestResultType(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    caption = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    result_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'test_result_type'


class ThothReportingAudit(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    thoth_reporting_period = models.ForeignKey('ThothReportingPeriod', models.DO_NOTHING)
    thoth_reporting_tool = models.ForeignKey('ThothReportingTool', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'thoth_reporting_audit'
        unique_together = (('thoth_reporting_tool', 'thoth_reporting_period'),)


class ThothReportingPeriod(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    day = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    month = models.ForeignKey(SystemMonth, models.DO_NOTHING)
    year = models.ForeignKey(SystemYear, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'thoth_reporting_period'


class ThothReportingPeriodMonthlyAggregate(models.Model):
    thoth_reporting_period_monthly_aggregates = models.ForeignKey(ThothReportingPeriod, models.DO_NOTHING, blank=True, null=True)
    monthly_aggregate = models.ForeignKey(MonthlyAggregate, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thoth_reporting_period_monthly_aggregate'


class ThothReportingPeriodPayrollBreakdown(models.Model):
    thoth_reporting_period_payroll_breakdowns = models.ForeignKey(ThothReportingPeriod, models.DO_NOTHING, blank=True, null=True)
    payroll_breakdown = models.ForeignKey(PayrollBreakdown, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'thoth_reporting_period_payroll_breakdown'


class ThothReportingTool(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    name = models.CharField(max_length=255)
    period_type = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'thoth_reporting_tool'


class Thothdhis2Exchange(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    completed_date = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    data = models.TextField()
    data_set_complete = models.BooleanField()
    date_created = models.DateTimeField(blank=True, null=True)
    deleted = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    dhis2response = models.TextField(blank=True, null=True)
    ignored = models.IntegerField()
    imported = models.IntegerField()
    last_updated = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField()
    thoth_reporting_audit = models.ForeignKey(ThothReportingAudit, models.DO_NOTHING)
    updated = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'thothdhis2exchange'


class Tracker(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    login_audit = models.ForeignKey(LoginAudit, models.DO_NOTHING)
    parameters = models.TextField()
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tracker'


class Training(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    coordinator = models.ForeignKey(SystemUser, models.DO_NOTHING, related_name='coordinated_trainings')
    cost = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING, blank=True, null=True, related_name='created_trainings')
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField()
    details = models.TextField()
    end_date = models.DateTimeField()
    last_updated = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    processed_by = models.ForeignKey(SystemUser, models.DO_NOTHING, blank=True, null=True,related_name='trainings_processed')
    processing_comment = models.CharField(max_length=255, blank=True, null=True)
    processing_date = models.DateTimeField(blank=True, null=True)
    start_date = models.DateTimeField()
    status = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'training'


class TrainingAttendant(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    confirmation = models.CharField(max_length=7)
    confirmation_date = models.DateTimeField(blank=True, null=True)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING, blank=True, null=True, related_name='created_training_attendants')
    date_created = models.DateTimeField(blank=True, null=True)
    employee = models.ForeignKey(SystemUser, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    training = models.ForeignKey(Training, models.DO_NOTHING, related_name='training_attendants')

    class Meta:
        managed = False
        db_table = 'training_attendant'
        unique_together = (('training', 'employee'),)


class TrainingMaterial(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    material = models.TextField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'training_material'


class TrainingMaterialAcknowledgement(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING, blank=True, null=True, related_name='created_material_acknowledgements')
    date_created = models.DateTimeField(blank=True, null=True)
    date_read = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    system_user = models.ForeignKey(SystemUser, models.DO_NOTHING, related_name='system_user_material_acknowledgements')
    training_material = models.ForeignKey(TrainingMaterial, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'training_material_acknowledgement'
        unique_together = (('training_material', 'system_user'),)


class TrainingMaterialDocument(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    system_file = models.ForeignKey(SystemFile, models.DO_NOTHING)
    training_material = models.ForeignKey(TrainingMaterial, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'training_material_document'


class TrainingMaterialTrainingMaterial(models.Model):
    training_material_training_material_documents = models.ForeignKey(TrainingMaterial, models.DO_NOTHING, blank=True, null=True, related_name='document_relationships')
    training_material = models.ForeignKey(TrainingMaterial, models.DO_NOTHING, blank=True, null=True,related_name='training_material_relationships')

    class Meta:
        managed = False
        db_table = 'training_material_training_material'


class TransportRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    approval_comment = models.CharField(max_length=255, blank=True, null=True)
    approval_date = models.DateTimeField(blank=True, null=True)
    approved = models.CharField(max_length=16, blank=True, null=True)
    approved_by = models.ForeignKey(SystemUser, models.DO_NOTHING, blank=True, null=True, related_name='approved_transport_requests')
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING, related_name='created_transport_requests')
    date_created = models.DateTimeField(blank=True, null=True)
    destinations = models.TextField()
    from_date = models.DateTimeField()
    last_updated = models.DateTimeField(blank=True, null=True)
    no_of_persons = models.IntegerField()
    purpose = models.TextField()
    to_date = models.DateTimeField()
    use_by = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'transport_request'


class Triage(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic_session = models.ForeignKey(ClinicSession, models.DO_NOTHING)
    comment = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    priority_level = models.CharField(max_length=24, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'triage'


class TriageType(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'triage_type'


class TriageTypeVitalSign(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    triage_type = models.ForeignKey(TriageType, models.DO_NOTHING)
    vital_type = models.ForeignKey('VitalType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'triage_type_vital_sign'


class TunaForm(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    template = models.TextField()

    class Meta:
        managed = False
        db_table = 'tuna_form'
        unique_together = (('branch', 'name'),)


class TunaUpdate(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    first_level = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    marked_ready_by = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    processed_at = models.DateTimeField(blank=True, null=True)
    second_level = models.CharField(max_length=255, blank=True, null=True)
    third_level = models.CharField(max_length=255, blank=True, null=True)
    update_type = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'tuna_update'


class TunaUpdateLine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    access_path = models.CharField(max_length=255)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=12)
    last_updated = models.DateTimeField(blank=True, null=True)
    processed_at = models.DateTimeField(blank=True, null=True)
    tuna_update = models.ForeignKey(TunaUpdate, models.DO_NOTHING)
    update_path = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'tuna_update_line'


class UnitLedgerAccountLinkage(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    department = models.ForeignKey(Department, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    ledger_account = models.OneToOneField(ChartOfAccount, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'unit_ledger_account_linkage'


class UpdateVerifier(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    token = models.CharField(max_length=255)
    verification_level = models.IntegerField()
    verifier_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'update_verifier'


class UserClinic(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    clinic = models.ForeignKey(Clinic, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING, related_name='created_user_clinics')
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    system_user = models.ForeignKey(SystemUser, models.DO_NOTHING, related_name='system_user_clinics')

    class Meta:
        managed = False
        db_table = 'user_clinic'
        unique_together = (('clinic', 'system_user'),)


class UserInheritedRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING, related_name='created_user_inherited_roles')
    date_created = models.DateTimeField(blank=True, null=True)
    inherited_role = models.ForeignKey(Role, models.DO_NOTHING)
    last_updated = models.DateTimeField(blank=True, null=True)
    system_user = models.ForeignKey(SystemUser, models.DO_NOTHING, related_name='system_user_inherited_roles')

    class Meta:
        managed = False
        db_table = 'user_inherited_role'


class UserOperatingLocation(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'user_operating_location'


class UserSystemArtifact(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    can_create = models.BooleanField()
    can_delete = models.BooleanField()
    can_execute = models.BooleanField()
    can_read = models.BooleanField()
    can_update = models.BooleanField()
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    system_artifact = models.ForeignKey(SystemArtifact, models.DO_NOTHING)
    system_user = models.ForeignKey(SystemUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_system_artifact'
        unique_together = (('system_artifact', 'system_user'),)


class UserWard(models.Model):
    id = models.BigIntegerField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING, related_name='created_user_wards')
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    system_user = models.ForeignKey(SystemUser, models.DO_NOTHING, related_name='system_user_wards')
    ward = models.ForeignKey('Ward', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_ward'
        unique_together = (('ward', 'system_user'),)


class Vaccine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_children_vaccine = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'vaccine'


class VaccineReportBand(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    dhis2data_element_id = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    max_age = models.IntegerField(blank=True, null=True)
    min_age = models.IntegerField()
    name = models.CharField(max_length=255)
    vaccine = models.ForeignKey(Vaccine, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vaccine_report_band'


class VatClass(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    rate = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'vat_class'
        unique_together = (('branch', 'name'),)


class VisitType(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'visit_type'


class VitalMonitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    admission = models.ForeignKey(PatientAdmission, models.DO_NOTHING, blank=True, null=True)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    comments = models.TextField(blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    encounter = models.ForeignKey(Encounter, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING)
    patient_labour_monitor = models.ForeignKey(PatientLabourMonitor, models.DO_NOTHING, blank=True, null=True)
    post_op_checklist = models.ForeignKey(PostOpChecklist, models.DO_NOTHING, blank=True, null=True)
    taken_at = models.DateTimeField()
    triage = models.ForeignKey(Triage, models.DO_NOTHING, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    vital_type = models.ForeignKey('VitalType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vital_monitor'


class VitalType(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    caption = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    is_default = models.BooleanField()
    is_mandatory = models.BooleanField()
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    place_holder_hint = models.CharField(max_length=255, blank=True, null=True)
    validation_error_message = models.CharField(max_length=255, blank=True, null=True)
    validator_pattern = models.CharField(max_length=255, blank=True, null=True)
    vitals_value_type = models.ForeignKey('VitalsValueType', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vital_type'


class VitalsValueType(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    value_type = models.TextField()

    class Meta:
        managed = False
        db_table = 'vitals_value_type'


class Voucher(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    cleared = models.BooleanField()
    comment = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING, related_name='created_vouchers')
    date_created = models.DateTimeField(blank=True, null=True)
    delivery_charge = models.DecimalField(max_digits=19, decimal_places=2)
    delivery_note_number = models.CharField(max_length=255, blank=True, null=True)
    due_date = models.DateTimeField(blank=True, null=True)
    financial_period = models.ForeignKey(FinancialPeriod, models.DO_NOTHING)
    invoice_number = models.CharField(max_length=255, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    local_service_order = models.ForeignKey(LocalServiceOrder, models.DO_NOTHING, blank=True, null=True)
    purchase_order = models.ForeignKey(PurchaseOrder, models.DO_NOTHING, blank=True, null=True)
    received_by = models.ForeignKey(SystemUser, models.DO_NOTHING, blank=True, null=True, related_name='received_vouchers')
    received_comment = models.CharField(max_length=255, blank=True, null=True)
    received_date = models.DateTimeField(blank=True, null=True)
    settled_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=7)
    supplier = models.ForeignKey(Supplier, models.DO_NOTHING)
    supplier_delivery_note = models.ForeignKey(SystemFile, models.DO_NOTHING, blank=True, null=True, related_name='supplier_delivery_notes')
    supplier_invoice = models.ForeignKey(SystemFile, models.DO_NOTHING, blank=True, null=True, related_name='supplier_invoices')
    void_status = models.TextField(blank=True, null=True)
    voucher_number = models.CharField(max_length=255, blank=True, null=True)
    voucher_receipt_date = models.DateTimeField(blank=True, null=True)
    voucher_type = models.CharField(max_length=7)
    remarks = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voucher'


class VoucherLine(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    account_payable = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='account_payable_voucher_lines')
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    budget_line = models.ForeignKey(BudgetLine, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    date_posted = models.DateTimeField(blank=True, null=True)
    default_purchase_ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    discount_rate = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    item_name = models.CharField(max_length=255)
    last_updated = models.DateTimeField(blank=True, null=True)
    local_service_order_item = models.ForeignKey(LocalServiceOrderItem, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(Product, models.DO_NOTHING, blank=True, null=True)
    purchase = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='purchase_voucher_lines')
    purchase_order_item = models.ForeignKey(PurchaseOrderItem, models.DO_NOTHING, blank=True, null=True)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    receipt_store = models.ForeignKey(Store, models.DO_NOTHING, blank=True, null=True)
    status = models.CharField(max_length=7)
    unit_price = models.DecimalField(max_digits=19, decimal_places=2)
    vat = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='vat_voucher_lines')
    vat_rate = models.DecimalField(max_digits=19, decimal_places=2)
    void_status = models.TextField(blank=True, null=True)
    voucher = models.ForeignKey(Voucher, models.DO_NOTHING)
    voucher_line_number = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voucher_line'


class VoucherPayment(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    budget_line = models.ForeignKey(BudgetLine, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    credited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='credited_account_voucher_payments')
    creditor_payment = models.ForeignKey(CreditorPayment, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    debited_account = models.ForeignKey(GeneralJournal, models.DO_NOTHING, blank=True, null=True, related_name='debited_account_voucher_payments')
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    payment_date = models.DateTimeField()
    payment_mode = models.ForeignKey(PaymentMode, models.DO_NOTHING, blank=True, null=True)
    payment_number = models.CharField(max_length=255, blank=True, null=True)
    payment_type = models.CharField(max_length=9)
    supplier = models.ForeignKey(Supplier, models.DO_NOTHING)
    transaction_id = models.CharField(max_length=255, blank=True, null=True)
    void_status = models.TextField(blank=True, null=True)
    voucher_line = models.ForeignKey(VoucherLine, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'voucher_payment'


class WaiverCase(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    system_defined = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'waiver_case'
        unique_together = (('branch', 'name'),)


class WaiverCaseExclusion(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField()
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField()
    product = models.ForeignKey(Product, models.DO_NOTHING)
    waiver_case = models.ForeignKey(WaiverCase, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'waiver_case_exclusion'


class Ward(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING, related_name='created_wards')
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    in_charge = models.ForeignKey(SystemUser, models.DO_NOTHING, blank=True, null=True, related_name='in_charge_wards')
    income_ledger_account = models.ForeignKey(ChartOfAccount, models.DO_NOTHING)
    is_active = models.BooleanField()
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    ward_category = models.ForeignKey('WardCategory', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ward'
        unique_together = (('branch', 'name'),)


class WardBillableItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    bed_movement = models.ForeignKey(BedMovement, models.DO_NOTHING)
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField()
    invoice_line = models.ForeignKey(InvoiceLine, models.DO_NOTHING, blank=True, null=True)
    last_updated = models.DateTimeField()
    product = models.ForeignKey(Product, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ward_billable_item'


class WardCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_system_defined = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'ward_category'
        unique_together = (('branch', 'name'),)


class WardStorageArea(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    is_drug_storage = models.BooleanField()
    last_updated = models.DateTimeField(blank=True, null=True)
    store = models.ForeignKey(Store, models.DO_NOTHING)
    ward = models.ForeignKey(Ward, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ward_storage_area'


class Watchdog(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING, blank=True, null=True)
    company = models.ForeignKey(Company, models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    login_audit = models.ForeignKey(LoginAudit, models.DO_NOTHING)
    message = models.TextField()
    parameters = models.TextField()
    severity = models.CharField(max_length=9)
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'watchdog'


class WellnessExamination(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    company = models.ForeignKey(Company, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING)
    date_created = models.DateTimeField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'wellness_examination'


class WellnessExaminationAncillaryCare(models.Model):
    wellness_examination_ancillary_cares = models.ForeignKey(WellnessExamination, models.DO_NOTHING, blank=True, null=True)
    ancillary_care = models.ForeignKey(AncillaryCare, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wellness_examination_ancillary_care'


class WellnessExaminationFamilyPlanning(models.Model):
    wellness_examination_family_healths = models.ForeignKey(WellnessExamination, models.DO_NOTHING, blank=True, null=True)
    family_planning = models.ForeignKey(FamilyPlanning, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wellness_examination_family_planning'


class WellnessExaminationImaging(models.Model):
    wellness_examination_imagings = models.ForeignKey(WellnessExamination, models.DO_NOTHING, blank=True, null=True)
    imaging = models.ForeignKey(Imaging, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wellness_examination_imaging'


class WellnessExaminationLabTest(models.Model):
    wellness_examination_lab_tests = models.ForeignKey(WellnessExamination, models.DO_NOTHING, blank=True, null=True)
    lab_test_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wellness_examination_lab_test'


class WellnessExaminationLabTests(models.Model):
    wellness_examination = models.OneToOneField(WellnessExamination, models.DO_NOTHING, primary_key=True)
    lab_test = models.ForeignKey(LabTest, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wellness_examination_lab_tests'
        unique_together = (('wellness_examination', 'lab_test'),)


class WellnessExaminationMinorTheater(models.Model):
    wellness_examination_minor_theaters = models.ForeignKey(WellnessExamination, models.DO_NOTHING, blank=True, null=True)
    minor_theater = models.ForeignKey(MinorTheater, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wellness_examination_minor_theater'


class WorkWeek(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    branch = models.ForeignKey(Branch, models.DO_NOTHING)
    created_by = models.ForeignKey(SystemUser, models.DO_NOTHING, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    day_name = models.CharField(max_length=255)
    day_of_week = models.CharField(max_length=255)
    day_proportion = models.FloatField()
    last_updated = models.DateTimeField(blank=True, null=True)
    working_hours = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'work_week'
        unique_together = (('branch', 'day_name'),)


class Workday(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    day_of_week = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    short_name = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'workday'


class ZscoreReferenceBoy(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    month = models.IntegerField()
    sd1height = models.DecimalField(max_digits=19, decimal_places=2)
    sd1weight = models.DecimalField(max_digits=19, decimal_places=2)
    sd1neg_height = models.DecimalField(max_digits=19, decimal_places=2)
    sd1neg_weight = models.DecimalField(max_digits=19, decimal_places=2)
    sd2height = models.DecimalField(max_digits=19, decimal_places=2)
    sd2weight = models.DecimalField(max_digits=19, decimal_places=2)
    sd2neg_height = models.DecimalField(max_digits=19, decimal_places=2)
    sd2neg_weight = models.DecimalField(max_digits=19, decimal_places=2)
    sd3height = models.DecimalField(max_digits=19, decimal_places=2)
    sd3weight = models.DecimalField(max_digits=19, decimal_places=2)
    sd3neg_height = models.DecimalField(max_digits=19, decimal_places=2)
    sd3neg_weight = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'zscore_reference_boy'


class ZscoreReferenceGirl(models.Model):
    id = models.BigAutoField(primary_key=True)
    version = models.BigIntegerField()
    month = models.IntegerField()
    sd1height = models.DecimalField(max_digits=19, decimal_places=2)
    sd1weight = models.DecimalField(max_digits=19, decimal_places=2)
    sd1neg_height = models.DecimalField(max_digits=19, decimal_places=2)
    sd1neg_weight = models.DecimalField(max_digits=19, decimal_places=2)
    sd2height = models.DecimalField(max_digits=19, decimal_places=2)
    sd2weight = models.DecimalField(max_digits=19, decimal_places=2)
    sd2neg_height = models.DecimalField(max_digits=19, decimal_places=2)
    sd2neg_weight = models.DecimalField(max_digits=19, decimal_places=2)
    sd3height = models.DecimalField(max_digits=19, decimal_places=2)
    sd3weight = models.DecimalField(max_digits=19, decimal_places=2)
    sd3neg_height = models.DecimalField(max_digits=19, decimal_places=2)
    sd3neg_weight = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'zscore_reference_girl'
