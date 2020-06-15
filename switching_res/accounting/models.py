from django.db import models


class CircuitBreakers (models.Model):
    dispatcher_name = models.CharField(max_length=150, verbose_name="Диспетчерское наименование")
    switch_type = models.ForeignKey('SwitchType', on_delete=models.PROTECT, null=True, verbose_name="Тип выключателя")
    name_of_substation = models.ForeignKey('NameOfSubstation', on_delete=models.PROTECT, null=True, verbose_name="Наименование ПС")
    switching_resource = models.FloatField(verbose_name="Остаточный коммутационный ресурс, %")
    mechanical_resource = models.FloatField(verbose_name="Остаточный механический ресурс, %")
    branch = models.ForeignKey('NameOfBranch', on_delete=models.PROTECT, null=True, verbose_name="Филиал")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создано")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Изменено")

    def __str__(self):
        return self.dispatcher_name

    class Meta:
        verbose_name = 'Выключатель'
        verbose_name_plural = 'Выключатели'
        ordering = ['-created_at']


class CommutationJournal (models.Model):
    dispatcher_name = models.ForeignKey('CircuitBreakers', on_delete=models.PROTECT, null=True, verbose_name="Диспетчерское наименование")
    date_of_commutation = models.DateTimeField(verbose_name="Дата коммутации")
    current_of_commutation = models.FloatField(verbose_name="Ток комутации, А")
    user_name = models.CharField(max_length=150, verbose_name="Кто внес запись")
    name_of_substation = models.ForeignKey('NameOfSubstation', on_delete=models.PROTECT, null=True, verbose_name="Наименование ПС")
    branch = models.ForeignKey('NameOfBranch', on_delete=models.PROTECT, null=True, verbose_name="Филиал")


    def __str__(self):
        return self.user_name

    class Meta:
        verbose_name = 'Комутация'
        verbose_name_plural = 'Комутации'
        ordering = ['-date_of_commutation']


class NameOfSubstation(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование ПС")
    branch = models.ForeignKey('NameOfBranch', on_delete=models.PROTECT, null=True, verbose_name="Филиал")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Подстанция'
        verbose_name_plural = 'Подстанции'
        ordering = ['name']


class NameOfBranch(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование Филиала")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Филиал'
        verbose_name_plural = 'Филиалы'
        ordering = ['name']


class VoltageClass(models.Model):
    voltage_class = models.IntegerField(verbose_name="Класс напряжения Выключателя, кВ")
    name = models.CharField(max_length=20, blank=True, verbose_name="Наименование класса напряжения Выключателя, кВ")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Напряжение'
        verbose_name_plural = 'Напряжения'
        ordering = ['voltage_class']


class SwitchType(models.Model):
    switch_type = models.CharField(max_length=150, verbose_name="Тип выключателя")
    voltage_class = models.ForeignKey('VoltageClass', on_delete=models.PROTECT, null=True, verbose_name="Класс напряжения Выключателя,кВ")
    rated_breaking_current = models.FloatField(verbose_name="Номинальный ток отключения, кА")
    rated_current = models.FloatField(verbose_name="Номинальный ток, А")
    first_bound = models.FloatField(verbose_name="Нижняя граница первого интервала, %")
    second_bound = models.FloatField(verbose_name="Нижняя граница второго интервала, %")
    third_bound = models.FloatField(verbose_name="Нижняя граница третьего интервала, %")
    first_bound_number_of_commutation = models.FloatField(verbose_name="Количество комутаций первого интервала")
    second_bound_number_of_commutation = models.FloatField(verbose_name="Количество комутаций второго интервала")
    third_bound_number_of_commutation = models.FloatField(verbose_name="Количество комутаций третьего интервала")
    mechanical_resource = models.IntegerField(verbose_name="Механический ресурс")

    def __str__(self):
        return self.switch_type

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
        ordering = ['switch_type']