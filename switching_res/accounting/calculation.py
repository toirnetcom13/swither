def vedenie_arhiva(nominal_tok_kommutacii, znachenie_meh_resursa, znachenie_com_resursa, tok_kommutacii, diap1, diap2, diap3, n_diap1, n_diap2, n_diap3, n_mehanichesk):
    '''
    Данный метод предназначен для расчета остаточного механического и коммутационного ресурса и возврата этих     величин.

    :param self:
    :param nominal_tok_kommutacii: ноимнальный ток коммутации (паспортное значение)
    :param znachenie_meh_resursa: текущее значение механического ресурса
    :param znachenie_com_resursa: текущее значение коммутационного ресурса
    :param tok_kommutacii: ток, который отключил выключатель
    :param diap1: верхняя граница диапазона ступенчатой характеристики (паспортное значение). Например 90
    :param diap2: средняя граница диапазона ступенчатой характеристики (паспортное значение). Например 60
    :param diap3: нижняя граница диапазона ступенчатой характеристики (паспортное значение). Например 30
    :param n_diap1:допустимое количество коммутаций в диапазоне тока отключения между (diap1) и 100%
    :param n_diap2:допустимое количество коммутаций в диапазоне тока отключения между (diap2) и (diap1)
    :param n_diap3:допустимое количество коммутаций в диапазоне тока отключения между (diap2) и (diap1)
    :param n_mehanichesk:допустимое количество коммутаций при опробовании выключателя
    :return:
    '''

    if tok_kommutacii >= nominal_tok_kommutacii*1000 * diap1/100 and tok_kommutacii <= nominal_tok_kommutacii*1000:
        znachenie_com_resursa = znachenie_com_resursa - 100/n_diap1
        znachenie_meh_resursa = znachenie_meh_resursa - 100/n_mehanichesk



    elif tok_kommutacii >= nominal_tok_kommutacii*1000 * diap2/100 and tok_kommutacii < nominal_tok_kommutacii*1000 * diap1/100:
        znachenie_com_resursa = znachenie_com_resursa - 100/n_diap2
        znachenie_meh_resursa = znachenie_meh_resursa - 100/n_mehanichesk



    elif tok_kommutacii > 0 and tok_kommutacii <= nominal_tok_kommutacii*1000 * diap2/100:
        znachenie_com_resursa = znachenie_com_resursa - 100/n_diap3
        znachenie_meh_resursa = znachenie_meh_resursa - 100/n_mehanichesk



    elif tok_kommutacii == 0:
        znachenie_meh_resursa = znachenie_meh_resursa - 100/n_mehanichesk

    else:
        znachenie_com_resursa = 9
        znachenie_meh_resursa = 7

    return [znachenie_com_resursa, znachenie_meh_resursa] #, ostatok_diap1, ostatok_diap2, ostatok_diap3
