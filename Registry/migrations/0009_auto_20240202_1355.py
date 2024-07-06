# Generated by Django 3.2.4 on 2024-02-02 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registry', '0008_auto_20240202_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoicereceipt',
            name='bank_branch',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    #     migrations.AddField(
    #         model_name='invoicereceipt',
    #         name='branch',
    #         field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Registry.branch'),
    #     ),
    #     migrations.AddField(
    #         model_name='invoicereceipt',
    #         name='company',
    #         field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Registry.company'),
    #     ),
    #     migrations.AddField(
    #         model_name='invoicereceipt',
    #         name='created_by',
    #         field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Registry.systemuser'),
    #     ),
    #     migrations.AddField(
    #         model_name='invoicereceipt',
    #         name='credited_account',
    #         field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='credited_receipts', to='Registry.generaljournal'),
    #     ),
    #     migrations.AddField(
    #         model_name='invoicereceipt',
    #         name='debited_account',
    #         field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='debited_receipts', to='Registry.generaljournal'),
    #     ),
    #     migrations.AddField(
    #         model_name='invoicereceipt',
    #         name='employee_debt',
    #         field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Registry.employeedebt'),
    #     ),
    #     migrations.AddField(
    #         model_name='invoicereceipt',
    #         name='invoice_line',
    #         field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Registry.invoiceline'),
    #     ),
    #     migrations.AddField(
    #         model_name='invoicereceipt',
    #         name='patient',
    #         field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Registry.patient'),
    #     ),
    #     migrations.AddField(
    #         model_name='invoicereceipt',
    #         name='transaction_fee_account',
    #         field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='transaction_fee_receipts', to='Registry.generaljournal'),
    #     ),
    ]