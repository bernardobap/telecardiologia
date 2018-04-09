# coding=utf-8
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import webbrowser
import csv
import os.path
import sys
import subprocess
from re import match

# Config Janela

root = Tk()
root.title('Atendimento Telecardiologia')
root.minsize(1500, 800)
root.state('zoomed')

# Dados do Atendimento

dados = ttk.LabelFrame(root, text='Dados do Contato:')
dados.pack(pady=10)

ttk.Label(dados, text='Paciente:').grid(row=0, column=0, padx=6, pady=3, sticky='W')
nome = ttk.Entry(dados, width=40)
nome.grid(row=0, column=1, padx=6, pady=3, sticky='W')

ttk.Label(dados, text='Idade:').grid(row=1, column=0, padx=6, pady=3, sticky='W')
idade = ttk.Entry(dados, width=5)
idade.grid(row=1, column=1, padx=6, pady=3, sticky='W')

ttk.Label(dados, text='Plano de Saúde:').grid(row=2, column=0, padx=6, pady=3, sticky='W')
plano_saude = ttk.Entry(dados, width=30)
plano_saude.grid(row=2, column=1, padx=6, pady=3, sticky='W')

ttk.Label(dados, text='Data (dd/mm/aaaa):').grid(row=0, column=3, padx=6, pady=3, sticky='W')
data_contato = ttk.Entry(dados, width=10)
data_contato.grid(row=0, column=4, padx=6, pady=3, sticky='W')

ttk.Label(dados, text='Hora (hh:mm):').grid(row=1, column=3, padx=6, pady=3, sticky='W')
hora_contato = ttk.Entry(dados, width=10)
hora_contato.grid(row=1, column=4, padx=6, pady=3, sticky='W')

ttk.Label(dados, text='Hospital:').grid(row=2, column=3, padx=6, pady=3, sticky='W')
hospital = ttk.Entry(dados, width=20)
hospital.grid(row=2, column=4, padx=6, pady=3, sticky='W')

ttk.Label(dados, text='Médico:').grid(row=0, column=5, padx=6, pady=3, sticky='W')
medico = ttk.Entry(dados, width=40)
medico.grid(row=0, column=6, padx=6, pady=3, sticky='W')

ttk.Label(dados, text='CRM:').grid(row=1, column=5, padx=6, pady=3, sticky='W')
crm = ttk.Entry(dados, width=10)
crm.grid(row=1, column=6, padx=6, pady=3, sticky='W')

ttk.Label(dados, text='Tel. Contato:').grid(row=2, column=5, padx=6, pady=3, sticky='W')
tel_contato = ttk.Entry(dados, width=15)
tel_contato.grid(row=2, column=6, padx=6, pady=3, sticky='W')

# 1 - Informações Clínicas

nb = ttk.Notebook(root)
nb.pack(pady=(0, 10), fill=X)

historia_clinica = ttk.Frame(nb)
nb.add(historia_clinica, text='História')

# 1.1 - Queixa Principal

qp = ttk.LabelFrame(historia_clinica, text='Queixa Principal:', borderwidth=5)
qp.pack(side=LEFT, anchor=N, padx=5, pady=10)


def nao_permite_entrada_de_outra_qp():
    outras_qp.config(state='disabled')


def permite_entrada_de_outra_qp():
    outras_qp.config(state='normal')


queixa_principal = StringVar()

ttk.Radiobutton(qp, text='Dor anginosa típica', value='Dor anginosa típica',
                variable=queixa_principal, command=nao_permite_entrada_de_outra_qp).pack(anchor=W)
ttk.Radiobutton(qp, text='Dor provavelmente anginosa', value='Dor provavelmente anginosa',
                variable=queixa_principal, command=nao_permite_entrada_de_outra_qp).pack(anchor=W)
ttk.Radiobutton(qp, text='Dor provavelmente não anginosa', value='Dor provavelmente não anginosa',
                variable=queixa_principal, command=nao_permite_entrada_de_outra_qp).pack(anchor=W)
ttk.Radiobutton(qp, text='Dor não anginosa', value='Dor não anginosa',
                variable=queixa_principal, command=nao_permite_entrada_de_outra_qp).pack(anchor=W)

ttk.Separator(qp, orient=HORIZONTAL).pack(fill=X, pady=3)

ttk.Radiobutton(qp, text='Dispnéia', value='Dispnéia',
                variable=queixa_principal, command=nao_permite_entrada_de_outra_qp).pack(anchor=W)
ttk.Radiobutton(qp, text='Edema periférico', value='Edema periférico',
                variable=queixa_principal, command=nao_permite_entrada_de_outra_qp).pack(anchor=W)
ttk.Radiobutton(qp, text='Palpitações', value='Palpitações',
                variable=queixa_principal, command=nao_permite_entrada_de_outra_qp).pack(anchor=W)
ttk.Radiobutton(qp, text='Síncope', value='Síncope',
                variable=queixa_principal, command=nao_permite_entrada_de_outra_qp).pack(anchor=W)
ttk.Radiobutton(qp, text='Lipotímia', value='Lipotímia',
                variable=queixa_principal, command=nao_permite_entrada_de_outra_qp).pack(anchor=W)
ttk.Radiobutton(qp, text='Tontura', value='Tontura',
                variable=queixa_principal, command=nao_permite_entrada_de_outra_qp).pack(anchor=W)
ttk.Radiobutton(qp, text='Náusea e/ou vômito', value='Náusea e/ou vômito',
                variable=queixa_principal, command=nao_permite_entrada_de_outra_qp).pack(anchor=W)
ttk.Radiobutton(qp, text='Mal estar inespecífico', value='Mal estar inespecífico',
                variable=queixa_principal, command=nao_permite_entrada_de_outra_qp).pack(anchor=W)

ttk.Separator(qp, orient=HORIZONTAL).pack(fill=X, pady=3)

ttk.Radiobutton(qp, text='Outra: ', value='Outra:', variable=queixa_principal,
                command=permite_entrada_de_outra_qp).pack(side=LEFT, pady=5)
outras_qp = ttk.Entry(qp, width=30, state='disabled')
outras_qp.pack(side=RIGHT)

# 1.2 - Resumo da História da Doença Atual

resumo_historia = ttk.LabelFrame(historia_clinica, text='Resumo da História Atual:', borderwidth=5)
resumo_historia.pack(side=LEFT, anchor=N, padx=(0, 5), pady=10)

historia_atual = Text(resumo_historia, height=6, width=45, wrap=WORD)
historia_atual.pack()

# 1.3 - Antecedentes Patológicos

ap_lf = ttk.LabelFrame(historia_clinica, text='Antecedentes:', borderwidth=7)
ap_lf.pack(side=LEFT, anchor=N, padx=(0, 5), pady=10)

ap_frame1 = ttk.Frame(ap_lf)
ap_frame1.grid(row=0, column=0, sticky='NW', padx=5)

ap_frame2 = ttk.Frame(ap_lf)
ap_frame2.grid(row=0, column=1, sticky='NW', padx=5)

has = StringVar()
dm2 = StringVar()
dlp = StringVar()
obesidade = StringVar()
sedentarismo = StringVar()
hf_dac = StringVar()
hf_ms = StringVar()
tbg = StringVar()
ex_tbg = StringVar()
dpoc = StringVar()
cocaina = StringVar()
crack = StringVar()
drogas_ev = StringVar()
dac_50 = StringVar()
dac_stent = StringVar()
dac_rm = StringVar()
iam = StringVar()
avei = StringVar()
aveh = StringVar()
daop = StringVar()
d_carotidea = StringVar()
fa = StringVar()
tpsv = StringVar()
ic_sem_etiologia = StringVar()
ic_valvar = StringVar()
ic_isquemica = StringVar()
icfep = StringVar()
drc_nd = StringVar()
drc_d = StringVar()
hipotireoidismo = StringVar()
hipertireoidismo = StringVar()

ttk.Checkbutton(ap_frame1, text='HAS', onvalue='hipertensão arterial', offvalue='',
                variable=has).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='DM2', onvalue='DM2', offvalue='',
                variable=dm2).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='DLP', onvalue='dislipidemia', offvalue='',
                variable=dlp).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='Obesidade', onvalue='obesidade', offvalue='',
                variable=obesidade).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='Sedentarismo', onvalue='sedentarismo', offvalue='',
                variable=sedentarismo).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='HF de DAC precoce', onvalue='história familiar de DAC precoce', offvalue='',
                variable=hf_dac).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='HF de morte súbita', onvalue='história familiar de morte súbita', offvalue='',
                variable=hf_ms).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='Tabagista', onvalue='tabagista', offvalue='',
                variable=tbg).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='Ex tabagista', onvalue='ex-tabagista', offvalue='',
                variable=ex_tbg).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='DPOC', onvalue='DPOC', offvalue='',
                variable=dpoc).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='Uso de cocaína', onvalue='usuário de cocaína', offvalue='',
                variable=cocaina).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='Uso de crack', onvalue='usuário de crack', offvalue='',
                variable=crack).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='Droga ilícita endovenosa', onvalue='usuário de droga ilícita endovenosa', offvalue='',
                variable=drogas_ev).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='DAC conhecida (>50%)', onvalue='DAC conhecida (>50%)', offvalue='',
                variable=dac_50).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='DAC conhecida (stent)', onvalue='DAC conhecida (stent)', offvalue='',
                variable=dac_stent).pack(anchor=W)
ttk.Checkbutton(ap_frame1, text='DAC conhecida (RM)', onvalue='DAC conhecida (RM)', offvalue='',
                variable=dac_rm).pack(anchor=W)
ttk.Checkbutton(ap_frame2, text='IAM prévio', onvalue='IAM prévio', offvalue='',
                variable=iam).pack(anchor=W)
ttk.Checkbutton(ap_frame2, text='AVEi prévio', onvalue='AVE isquêmico prévio', offvalue='',
                variable=avei).pack(anchor=W)
ttk.Checkbutton(ap_frame2, text='AVEh prévio', onvalue='AVE hemorrágico prévio', offvalue='',
                variable=aveh).pack(anchor=W)
ttk.Checkbutton(ap_frame2, text='D. arterial obstrutiva periférica', onvalue='doença arterial obstrutiva periférica',
                offvalue='', variable=daop).pack(anchor=W)
ttk.Checkbutton(ap_frame2, text='D. obstrutiva carotídea', onvalue='doença obstrutiva carotídea', offvalue='',
                variable=d_carotidea).pack(anchor=W)
ttk.Checkbutton(ap_frame2, text='FA/Flutter atrial', onvalue='FA/Flutter atrial', offvalue='',
                variable=fa).pack(anchor=W)
ttk.Checkbutton(ap_frame2, text='TPSV', onvalue='TPSV', offvalue='',
                variable=tpsv).pack(anchor=W)
ttk.Checkbutton(ap_frame2, text='IC sem etiologia', onvalue='IC sem etiologia', offvalue='',
                variable=ic_sem_etiologia).pack(anchor=W)
ttk.Checkbutton(ap_frame2, text='IC de etiologia valvar', onvalue='IC de etiologia valvar', offvalue='',
                variable=ic_valvar).pack(anchor=W)
ttk.Checkbutton(ap_frame2, text='IC de etiologia isquêmica', onvalue='IC de etiologia isquêmica', offvalue='',
                variable=ic_isquemica).pack(anchor=W)
ttk.Checkbutton(ap_frame2, text='D. renal crônica (não dialítica)', onvalue='doença renal crônica (não dialítica)',
                offvalue='', variable=drc_nd).pack(anchor=W)
ttk.Checkbutton(ap_frame2, text='D. renal crônica (dialítica)', onvalue='doença renal crônica (não dialítica)',
                offvalue='', variable=drc_d).pack(anchor=W)
ttk.Checkbutton(ap_frame2, text='Hipotireoidismo', onvalue='hipotireoidismo', offvalue='',
                variable=hipotireoidismo).pack(anchor=W)
ttk.Checkbutton(ap_frame2, text='Hipertireoidismo', onvalue='hipertireoidismo', offvalue='',
                variable=hipertireoidismo).pack(anchor=W)

ttk.Label(ap_frame2, text='Outros: ').pack(anchor=W)
outros_ap = ttk.Entry(ap_frame2, width=30)
outros_ap.pack(anchor=W)

# 1.4 - Medicações em uso

medicacoes = ttk.LabelFrame(historia_clinica, text='Medicamentos (uso domiciliar):', borderwidth=5)
medicacoes.pack(side=LEFT, anchor=N, padx=(0, 5), pady=10)

aas = StringVar()
outros_antiplaquetarios = StringVar()
ieca_bra = StringVar()
estatina = StringVar()
beta_bloqueador = StringVar()
furosemida = StringVar()
tiazidico = StringVar()
bcc = StringVar()
bcc_nd = StringVar()
nitrato = StringVar()
digoxina = StringVar()
amiodarona = StringVar()
propafenona = StringVar()
outros_antiarritmicos = StringVar()
varfarina = StringVar()
noac = StringVar()
anti_dm_oral = StringVar()
insulina = StringVar()

ttk.Checkbutton(medicacoes, text='AAS', onvalue='AAS', offvalue='',
                variable=aas).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='Outros antiplaquetários', onvalue='Outros antiplaquetários', offvalue='',
                variable=outros_antiplaquetarios).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='IECA ou BRA', onvalue='IECA ou BRA', offvalue='', variable=ieca_bra).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='Estatina', onvalue='Estatina', offvalue='',
                variable=estatina).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='Beta-bloqueador', onvalue='Beta-bloqueador', offvalue='',
                variable=beta_bloqueador).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='Furosemida', onvalue='Furosemida', offvalue='',
                variable=furosemida).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='Tiazídico', onvalue='Tiazídico', offvalue='',
                variable=tiazidico).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='BCC', onvalue='BCC', offvalue='',
                variable=bcc).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='BCC (não-dihidropiridinas)', onvalue='BCC (não-dihidropiridinas)', offvalue='',
                variable=bcc_nd).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='Nitrato', onvalue='Nitrato', offvalue='',
                variable=nitrato).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='Digoxina', onvalue='Digoxina', offvalue='',
                variable=digoxina).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='Amiodarona', onvalue='Amiodarona', offvalue='',
                variable=amiodarona).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='Propafenona', onvalue='Propafenona', offvalue='',
                variable=propafenona).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='Outros antiarrítimicos', onvalue='Outros antiarrítimicos', offvalue='',
                variable=outros_antiarritmicos).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='Varfarina', onvalue='Varfarina', offvalue='',
                variable=varfarina).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='Novos anticoagulantes', onvalue='Novos anticoagulantes', offvalue='',
                variable=noac).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='Antidiabético oral', onvalue='Antidiabético oral', offvalue='',
                variable=anti_dm_oral).pack(anchor=W)
ttk.Checkbutton(medicacoes, text='Insulina', onvalue='Insulina', offvalue='',
                variable=insulina).pack(anchor=W)
ttk.Label(medicacoes, text='Outros: ').pack(anchor=W)
outras_medicacoes = ttk.Entry(medicacoes, width=30)
outras_medicacoes.pack(anchor=W)

# 2 - Exame Físico

exame_fisico = ttk.Frame(nb)
nb.add(exame_fisico, text='Exame Físico')

# 2.1 - Sinais Vitais

sinais_vitais = ttk.LabelFrame(exame_fisico, text='Sinais vitais:', borderwidth=5)
sinais_vitais.pack(side=LEFT, anchor=N, padx=5, pady=10)

ttk.Label(sinais_vitais, text='FC:').grid(row=0, column=0, padx=6, pady=3, sticky='W')
fc = ttk.Entry(sinais_vitais, width=3)
fc.grid(row=0, column=1, padx=6, pady=3, sticky='W')
ttk.Label(sinais_vitais, text='bpm').grid(row=0, column=2, padx=6, pady=3, sticky='W')

ttk.Label(sinais_vitais, text='PA:').grid(row=1, column=0, padx=6, pady=3, sticky='W')
pa = ttk.Entry(sinais_vitais, width=7)
pa.grid(row=1, column=1, padx=6, pady=3, sticky='W')
ttk.Label(sinais_vitais, text='mmHg').grid(row=1, column=2, padx=6, pady=3, sticky='W')

ttk.Label(sinais_vitais, text='SpO2:').grid(row=2, column=0, padx=6, pady=3, sticky='W')
spo2 = ttk.Entry(sinais_vitais, width=3)
spo2.grid(row=2, column=1, padx=6, pady=3, sticky='W')
ttk.Label(sinais_vitais, text='%').grid(row=2, column=2, padx=6, pady=3, sticky='W')

taquipneia = StringVar()

ttk.Checkbutton(sinais_vitais, text='Taquipnéia', onvalue='taquipnéia', offvalue='', variable=taquipneia)\
    .grid(row=3, column=0, columnspan=2, padx=6, pady=3, sticky='W')

# 2.2 - Cardiovascular

cardiovascular = ttk.LabelFrame(exame_fisico, text='Cardiovascular:', borderwidth=5)
cardiovascular.pack(side=LEFT, anchor=N, padx=(0, 5), pady=10)

ritmo_ef = StringVar()

ttk.Label(cardiovascular, text='Ritmo cardíaco:').pack(anchor=W)
ttk.Radiobutton(cardiovascular, text='Regular', value='ritmo cardíaco regular', variable=ritmo_ef).pack(anchor=W)
ttk.Radiobutton(cardiovascular, text='Irregular', value='ritmo cardíaco irregular', variable=ritmo_ef).pack(anchor=W)

ttk.Separator(cardiovascular, orient=HORIZONTAL).pack(fill=X, pady=3)

sopro_sist = StringVar()
sopro_diast = StringVar()
b3 = StringVar()
sopro_carotidas = StringVar()

tjp = StringVar()
pulso_assimetrico_mmss = StringVar()
pulso_assimetrico_mmii = StringVar()
enchimento_capilar_aum = StringVar()
edema_mmii = StringVar()
tvp = StringVar()

ttk.Checkbutton(cardiovascular, text='Sopro cardíaco sistólico', onvalue='sopro cardíaco sistólico',
                offvalue='', variable=sopro_sist).pack(anchor=W)
ttk.Checkbutton(cardiovascular, text='Sopro cardíaco diastólico', onvalue='sopro cardíaco diastólico',
                offvalue='', variable=sopro_diast).pack(anchor=W)
ttk.Checkbutton(cardiovascular, text='B3', onvalue='terceira bulha presente',
                offvalue='', variable=tvp).pack(anchor=W)
ttk.Checkbutton(cardiovascular, text='Sopro carotídeo', onvalue='sopro carotídeo',
                offvalue='', variable=sopro_carotidas).pack(anchor=W)

ttk.Separator(cardiovascular, orient=HORIZONTAL).pack(fill=X, pady=3)

ttk.Checkbutton(cardiovascular, text='Pulsos assimétricos (MMSS)', onvalue='pulsos assimétricos (MMSS)',
                offvalue='', variable=pulso_assimetrico_mmss).pack(anchor=W)
ttk.Checkbutton(cardiovascular, text='Pulsos assimétricos (MMII)', onvalue='pulsos assimétricos (MMII)',
                offvalue='', variable=pulso_assimetrico_mmii).pack(anchor=W)
ttk.Checkbutton(cardiovascular, text='TEC aumentado (>3seg)', onvalue='TEC aumentado (>3seg)',
                offvalue='', variable=enchimento_capilar_aum).pack(anchor=W)
ttk.Checkbutton(cardiovascular, text='Edema em MMII', onvalue='edema em MMII',
                offvalue='', variable=edema_mmii).pack(anchor=W)
ttk.Checkbutton(cardiovascular, text='Turgência jugular patológica', onvalue='turgência jugular patológica',
                offvalue='', variable=tjp).pack(anchor=W)
ttk.Checkbutton(cardiovascular, text='Sinais de TVP', onvalue='sinais de TVP',
                offvalue='', variable=tvp).pack(anchor=W)

# 2.2 - Respiratório

respiratorio = ttk.LabelFrame(exame_fisico, text='Respiratório:', borderwidth=5)
respiratorio.pack(side=LEFT, anchor=N, padx=(0, 5), pady=10)

suporte_ventilatorio = StringVar()

ttk.Radiobutton(respiratorio, text='Ar ambiente', value='em ar ambiente', variable=suporte_ventilatorio).pack(anchor=W)
ttk.Radiobutton(respiratorio, text='Cateter de O2', value='com suplementação O2', variable=suporte_ventilatorio).pack(anchor=W)
ttk.Radiobutton(respiratorio, text='VNI', value='sob ventilação não invasiva intermitente', variable=suporte_ventilatorio).pack(anchor=W)
ttk.Radiobutton(respiratorio, text='AVM', value='sob assistência ventilatória mecânica por tubo orotraqueal', variable=suporte_ventilatorio).pack(anchor=W)

ttk.Separator(respiratorio, orient=HORIZONTAL).pack(fill=X, pady=3)

estertores = StringVar()

ttk.Label(respiratorio, text='Estertores: ').pack(anchor=W)
ttk.Radiobutton(respiratorio, text='Não', value='sem estertores', variable=estertores).pack(anchor=W)
ttk.Radiobutton(respiratorio, text='1/3 inferior', value='estertores em terço inferior dos campos pulmonares', variable=estertores).pack(anchor=W)
ttk.Radiobutton(respiratorio, text='Até 1/3 médio', value='estertores até terço médio dos campos pulmonares', variable=estertores).pack(anchor=W)
ttk.Radiobutton(respiratorio, text='Até ápice', value='estertores até ápice dos campos pulmonares', variable=estertores).pack(anchor=W)

ttk.Separator(respiratorio, orient=HORIZONTAL).pack(fill=X, pady=3)

ttk.Label(respiratorio, text='Outros: ').pack(anchor=W)
outros_respiratorio = ttk.Entry(respiratorio, width=30)
outros_respiratorio.pack(anchor=W)

# 2.3 - Abdominal

abdominal = ttk.LabelFrame(exame_fisico, text='Abdominal:', borderwidth=5)
abdominal.pack(side=LEFT, anchor=N, padx=(0, 5), pady=10)

hepatomegalia = StringVar()
ascite = StringVar()
massa_pulsatil = StringVar()
irritacao_peritoneal = StringVar()

ttk.Checkbutton(abdominal, text='Hepatomegalia', onvalue='hepatomegalia',
                offvalue='', variable=hepatomegalia).pack(anchor=W)
ttk.Checkbutton(abdominal, text='Ascite', onvalue='sinais de ascite',
                offvalue='', variable=ascite).pack(anchor=W)
ttk.Checkbutton(abdominal, text='Massa pulsátil', onvalue='massa pulsátil em topografia aórtica',
                offvalue='', variable=massa_pulsatil).pack(anchor=W)
ttk.Checkbutton(abdominal, text='Sinais de irritação peritoneal', onvalue='sinais de irritação peritoneal',
                offvalue='', variable=irritacao_peritoneal).pack(anchor=W)

ttk.Label(abdominal, text='Outros: ').pack(anchor=W)
outros_abdominal = ttk.Entry(abdominal, width=30)
outros_abdominal.pack(anchor=W)

# 2.3 - Neurológico

neurologico = ttk.LabelFrame(exame_fisico, text='Neurológico:', borderwidth=5)
neurologico.pack(side=LEFT, anchor=N, padx=(0, 5), pady=10)

nivel_consciencia = StringVar()

ttk.Label(neurologico, text='Nível de consciência: ').pack(anchor=W)
ttk.Radiobutton(neurologico, text='Vigil', value='Vigil', variable=nivel_consciencia).pack(anchor=W)
ttk.Radiobutton(neurologico, text='Torporoso', value='Torporoso', variable=nivel_consciencia).pack(anchor=W)
ttk.Radiobutton(neurologico, text='Comatoso', value='Comatoso', variable=nivel_consciencia).pack(anchor=W)

ttk.Separator(neurologico, orient=HORIZONTAL).pack(fill=X, pady=3)

conteudo_consciencia = StringVar()

ttk.Label(neurologico, text='Conteúdo da consciência: ').pack(anchor=W)
ttk.Radiobutton(neurologico, text='Orientado', value='Orientado', variable=conteudo_consciencia).pack(anchor=W)
ttk.Radiobutton(neurologico, text='Desorientado', value='Desorientado', variable=conteudo_consciencia).pack(anchor=W)

ttk.Separator(neurologico, orient=HORIZONTAL).pack(fill=X, pady=3)

hp_completa_d = StringVar()
hp_completa_e = StringVar()
hp_incompleta_d = StringVar()
hp_incompleta_e = StringVar()

ttk.Checkbutton(neurologico, text='Hemiparesia completa à direita', onvalue='Hemiparesia completa à direita',
                offvalue='', variable=hp_completa_d).pack(anchor=W)
ttk.Checkbutton(neurologico, text='Hemiparesia completa à esquerda', onvalue='Hemiparesia completa à esquerda',
                offvalue='', variable=hp_completa_e).pack(anchor=W)
ttk.Checkbutton(neurologico, text='Hemiparesia incompleta à direita', onvalue='Hemiparesia incompleta à direita',
                offvalue='', variable=hp_incompleta_d).pack(anchor=W)
ttk.Checkbutton(neurologico, text='Hemiparesia incompleta à esquerda', onvalue='Hemiparesia incompleta à esquerda',
                offvalue='', variable=hp_incompleta_e).pack(anchor=W)

# 3 - Exames Complementares
exames_complementares = ttk.Frame(nb)
nb.add(exames_complementares, text='Exames Complementares')

# 3.1 - ECG

# 3.1.1 - Ritmo

ritmo_ecg_lf = ttk.LabelFrame(exames_complementares, text='Ritmo do ECG:', borderwidth=5)
ritmo_ecg_lf.pack(side=LEFT, anchor=N, padx=5, pady=10)

hora_ecg_frame = ttk.Frame(ritmo_ecg_lf)
hora_ecg_frame.pack(pady=4)
ttk.Label(hora_ecg_frame, text='ECG realizado às (hh:mm): ').pack(side=LEFT)
hora_ecg = ttk.Entry(hora_ecg_frame, width=6)
hora_ecg.pack(side=RIGHT)

ttk.Separator(ritmo_ecg_lf, orient=HORIZONTAL).pack(fill=X, pady=3)

ritmo = StringVar()

ttk.Radiobutton(ritmo_ecg_lf, text='Ritmo sinusal', value='sinusal',
                variable=ritmo).pack(anchor=W)
ttk.Radiobutton(ritmo_ecg_lf, text='Bradicardia sinusal', value='bradicardia sinusal',
                variable=ritmo).pack(anchor=W)
ttk.Radiobutton(ritmo_ecg_lf, text='Taquicardia sinusal', value='taquicardia sinusal',
                variable=ritmo).pack(anchor=W)
ttk.Radiobutton(ritmo_ecg_lf, text='Ritmo de Marcapasso', value='marcapasso',
                variable=ritmo).pack(anchor=W)
ttk.Separator(ritmo_ecg_lf, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Radiobutton(ritmo_ecg_lf, text='Bloqueio AV 1o grau', value='bloqueio AV 1o grau',
                variable=ritmo).pack(anchor=W)
ttk.Radiobutton(ritmo_ecg_lf, text='Bloqueio AV 2o grau (Mobitz 1)', value='bloqueio AV 2o grau (Mobitz 1)',
                variable=ritmo).pack(anchor=W)
ttk.Radiobutton(ritmo_ecg_lf, text='Bloqueio AV 2o grau (Mobitz 2)', value='bloqueio AV 2o grau (Mobitz 2)',
                variable=ritmo).pack(anchor=W)
ttk.Radiobutton(ritmo_ecg_lf, text='Bloqueio AV 2:1', value='bloqueio AV 2:1',
                variable=ritmo).pack(anchor=W)
ttk.Radiobutton(ritmo_ecg_lf, text='Bloqueio AV avançado (3:1 em diante)', value='bloqueio AV avançado (3:1 em diante)',
                variable=ritmo).pack(anchor=W)
ttk.Radiobutton(ritmo_ecg_lf, text='Bloqueio AV total', value='bloqueio AV total',
                variable=ritmo).pack(anchor=W)
ttk.Radiobutton(ritmo_ecg_lf, text='Ritmo juncional', value='juncional',
                variable=ritmo).pack(anchor=W)
ttk.Separator(ritmo_ecg_lf, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Radiobutton(ritmo_ecg_lf, text='Taquicardia supraventricular', value='taquicardia supraventricular',
                variable=ritmo).pack(anchor=W)
ttk.Radiobutton(ritmo_ecg_lf, text='Fibrilação atrial', value='fibrilação atrial',
                variable=ritmo).pack(anchor=W)
ttk.Radiobutton(ritmo_ecg_lf, text='Flutter atrial', value='flutter atrial',
                variable=ritmo).pack(anchor=W)
ttk.Radiobutton(ritmo_ecg_lf, text='Taquicardia atrial', value='taquicardia atrial',
                variable=ritmo).pack(anchor=W)
ttk.Radiobutton(ritmo_ecg_lf, text='Taquicardia ventricular', value='taquicardia ventricular',
                variable=ritmo).pack(anchor=W)

# 3.1.1 - Achados

achados_ecg_lf = ttk.LabelFrame(exames_complementares, text='Achados do ECG:', borderwidth=5)
achados_ecg_lf.pack(side=LEFT, anchor=N, padx=(0, 5), pady=10)

achados_ecg_frame1 = ttk.Frame(achados_ecg_lf)
achados_ecg_frame1.grid(row=0, column=0, sticky='NW', pady=10, padx=10)

achados_ecg_frame2 = ttk.Frame(achados_ecg_lf)
achados_ecg_frame2.grid(row=0, column=1, sticky='NW', pady=10, padx=10)

ecg_supra_anterosseptal = StringVar()
ecg_supra_anterior = StringVar()
ecg_supra_anterior_localizada = StringVar()
ecg_supra_anterolateral = StringVar()
ecg_supra_anterior_extensa = StringVar()
ecg_supra_lateral_baixa = StringVar()
ecg_supra_lateral_alta = StringVar()
ecg_supra_inferior = StringVar()
ecg_supra_vd = StringVar()
ecg_aei_septal = StringVar()
ecg_aei_anteroapical = StringVar()
ecg_aei_anterior_media = StringVar()
ecg_aei_lateral = StringVar()
ecg_aei_inferior = StringVar()
ecg_infra_difuso = StringVar()
ecg_infra = StringVar()
ecg_onda_t_isquemia = StringVar()
ecg_alt_dinamica_stt = StringVar()
ecg_airv = StringVar()
ecg_miopericardite = StringVar()
ecg_repol_precoce = StringVar()
ecg_discinesia = StringVar()
ecg_hipercalemia = StringVar()
ecg_bre = StringVar()
ecg_brd = StringVar()
ecg_bdas = StringVar()
ecg_bdam = StringVar()
ecg_bdpi = StringVar()
ecg_sae = StringVar()
ecg_sad = StringVar()
ecg_sve = StringVar()
ecg_svd = StringVar()
ecg_qt_longo = StringVar()
ecg_ev_frequentes = StringVar()
ecg_esv_frequentes = StringVar()
ecg_tvns = StringVar()

ttk.Label(achados_ecg_frame1, text='Supra de ST:').pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Parede anterosseptal (V1, V2 e V3)',
                onvalue='supra de ST em parede anterosseptal', offvalue='',
                variable=ecg_supra_anterosseptal).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Parede anterior (V1, V2, V3 e V4)',
                onvalue='supra de ST em parede anterior', offvalue='',
                variable=ecg_supra_anterior).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Parede anterior localizada (V3, V4 ou V3-V5)',
                onvalue='supra de ST em parede anterior localizada', offvalue='',
                variable=ecg_supra_anterior_localizada).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Parede anterolateral (V4 a V5, V6, D1 e aVL)',
                onvalue='supra de ST em parede anterolateral', offvalue='',
                variable=ecg_supra_anterolateral).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Parede anterior extensa (V1 a V6 , D1 e aVL)',
                onvalue='supra de ST em parede anterior extensa', offvalue='',
                variable=ecg_supra_anterior_extensa).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Parede lateral baixa (V5 e V6)',
                onvalue='supra de ST em parede lateral baixa', offvalue='',
                variable=ecg_supra_lateral_baixa).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Parede lateral alta (D1 e aVL)',
                onvalue='supra de ST em parede lateral alta', offvalue='',
                variable=ecg_supra_lateral_alta).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Parede inferior (D2, D3 e aVF)',
                onvalue='supra de ST em parede inferior', offvalue='',
                variable=ecg_supra_inferior).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Ventrículo direito (V1, V3R, V4R, V5R e V6R)',
                onvalue='supra de ST em derivações direitas (VD)', offvalue='',
                variable=ecg_supra_vd).pack(anchor=W)
ttk.Separator(achados_ecg_frame1, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Label(achados_ecg_frame1, text='Área eletricamente inativa:').pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Parede septal (V1 e V2)',
                onvalue='área eletricamente inativa em parede septal', offvalue='',
                variable=ecg_aei_septal).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Parede anteroapical (V1, V2 até V3-V6)',
                onvalue='área eletricamente inativa em parede anteroapical', offvalue='',
                variable=ecg_aei_anteroapical).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Parede anterior média (D1, aVL, às vezes V2 e V3)',
                onvalue='área eletricamente inativa em parede anterior média', offvalue='',
                variable=ecg_aei_anterior_media).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Parede lateral (D1, aVL, V5-V6 e/ou RS em V1)',
                onvalue='área eletricamente inativa em parede lateral', offvalue='',
                variable=ecg_aei_lateral).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Parede inferior (D2, D3 e aVF)',
                onvalue='área eletricamente inativa em parede inferior', offvalue='',
                variable=ecg_aei_inferior).pack(anchor=W)
ttk.Separator(achados_ecg_frame1, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Label(achados_ecg_frame1, text='Isquemia sem supra de ST:').pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Infra de ST >=6 derivações + supra aVR',
                onvalue='infra de ST em 6 ou mais derivações com supra de aVR', offvalue='',
                variable=ecg_infra_difuso).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Infra de ST >=2 derivações contíguas',
                onvalue='infra de ST em 2 ou mais derivações contíguas', offvalue='',
                variable=ecg_infra).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Onda T simétrica e/ou apiculada e/ou bifásica',
                onvalue='onda T simétrica e/ou apiculada e/ou bifásica', offvalue='',
                variable=ecg_onda_t_isquemia).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame1, text='Alteração dinâmica de ST-T',
                onvalue='alteração dinâmica de ST-T', offvalue='',
                variable=ecg_alt_dinamica_stt).pack(anchor=W)

ttk.Label(achados_ecg_frame2, text='Diagnósticos diferenciais:').pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='Alterações inespecíficas da repolarização',
                onvalue='alterações inespecíficas da repolarização', offvalue='',
                variable=ecg_airv).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='Sugestivo de mio/pericardite',
                onvalue='sugestivo de mio/pericardite', offvalue='',
                variable=ecg_miopericardite).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='Sugestivo de repolarização precoce',
                onvalue='sugestivo de repolarização precoce', offvalue='',
                variable=ecg_repol_precoce).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='Sugestivo de área discinética',
                onvalue='sugestivo de área discinética', offvalue='',
                variable=ecg_discinesia).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='Sugestivo de hipercalemia',
                onvalue='sugestivo de hipercalemia', offvalue='',
                variable=ecg_hipercalemia).pack(anchor=W)
ttk.Separator(achados_ecg_frame2, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Label(achados_ecg_frame2, text='Bloqueios intraventriculares:').pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='BRE', onvalue='BRE', offvalue='', variable=ecg_bre).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='BRD', onvalue='BRD', offvalue='', variable=ecg_brd).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='BDAS', onvalue='BDAS', offvalue='', variable=ecg_bdas).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='BDAM', onvalue='BDAM', offvalue='', variable=ecg_bdam).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='BDPI', onvalue='BDPI', offvalue='', variable=ecg_bdpi).pack(anchor=W)
ttk.Separator(achados_ecg_frame2, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Label(achados_ecg_frame2, text='Sobrecargas:').pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='SAE', onvalue='sobrecarga de AE', offvalue='', variable=ecg_sae).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='SAD', onvalue='sobrecarga de AD', offvalue='', variable=ecg_sad).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='SVE', onvalue='sobrecarga de VE', offvalue='', variable=ecg_sve).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='SVD', onvalue='sobrecarga de VD', offvalue='', variable=ecg_svd).pack(anchor=W)
ttk.Separator(achados_ecg_frame2, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Label(achados_ecg_frame2, text='Outros:').pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='QT longo', onvalue='QT longo', offvalue='',
                variable=ecg_qt_longo).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='EV frequentes', onvalue='extrassístoles ventriculares frequentes', offvalue='',
                variable=ecg_ev_frequentes).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='ESV frequentes', onvalue='extrassístoles supraventriculares frequentes', offvalue='',
                variable=ecg_esv_frequentes).pack(anchor=W)
ttk.Checkbutton(achados_ecg_frame2, text='TVNS', onvalue='taquicardia ventricular não sustentada', offvalue='',
                variable=ecg_tvns).pack(anchor=W)

# 3.2 - Radiografia de Tórax

rx = ttk.LabelFrame(exames_complementares, text='Radiografia de Tórax:', borderwidth=5)
rx.pack(side=LEFT, anchor=N, padx=(0, 5), pady=10)

ac_aumentada = StringVar()
derrame_pleural = StringVar()
congestao = StringVar()
opacidades = StringVar()
ptx = StringVar()
alargamento_mediastinal = StringVar()

ttk.Checkbutton(rx, text='Área cardíaca aumentada', onvalue='Área cardíaca aumentada',
                offvalue='', variable=ac_aumentada).pack(anchor=W)
ttk.Checkbutton(rx, text='Derrame pleural', onvalue='Derrame pleural',
                offvalue='', variable=derrame_pleural).pack(anchor=W)
ttk.Checkbutton(rx, text='Congestão pulmonar', onvalue='Sinais de congestão pulmonar',
                offvalue='', variable=congestao).pack(anchor=W)
ttk.Checkbutton(rx, text='Opacidades pulmonares', onvalue='Opacidades no parênquima pulmonar',
                offvalue='', variable=opacidades).pack(anchor=W)
ttk.Checkbutton(rx, text='Pneumotórax', onvalue='Pneumotórax (unilateral)',
                offvalue='', variable=ptx).pack(anchor=W)
ttk.Checkbutton(rx, text='Alargamento mediastinal', onvalue='Alargamento mediastinal',
                offvalue='', variable=alargamento_mediastinal).pack(anchor=W)

# 3.3 - Exames Laboratoriais

lab = ttk.LabelFrame(exames_complementares, text='Laboratoriais:', borderwidth=5)
lab.pack(side=LEFT, anchor=N, padx=(0, 5), pady=10)

troponina = StringVar()


def permite_entradada_troponina():
    troponina_valor.config(state='normal')


def nao_permite_entradada_troponina():
    troponina_valor.config(state='disabled')


ttk.Label(lab, text='Troponina:').grid(column=0, row=0, columnspan=2, sticky=W)
ttk.Radiobutton(lab, text='Não coletada', value='não coletada', variable=troponina,
                command=nao_permite_entradada_troponina).grid(column=0, row=1, columnspan=2, sticky=W)
ttk.Radiobutton(lab, text='Aguardando', value='aguarda resultado', variable=troponina,
                command=nao_permite_entradada_troponina).grid(column=0, row=2, columnspan=2, sticky=W)
ttk.Radiobutton(lab, text='Positiva', value='positiva', variable=troponina,
                command=permite_entradada_troponina).grid(column=0, row=3, columnspan=2, sticky=W)
ttk.Radiobutton(lab, text='Negativa', value='negativa', variable=troponina,
                command=nao_permite_entradada_troponina).grid(column=0, row=4, columnspan=2, sticky=W)

ttk.Label(lab, text='Valor:').grid(column=0, row=5, pady=5, sticky=W)
troponina_valor = ttk.Entry(lab, width=5, state='disabled')
troponina_valor.grid(column=1, row=5, pady=5, sticky=W)

ttk.Separator(lab, orient=HORIZONTAL).grid(column=0, row=6, columnspan=2, pady=3, sticky=EW)


def permite_lab(lab_cb, lab_entry):
    if lab_cb.get() == 0:
        lab_entry.configure(state='disabled')
    else:
        lab_entry.configure(state='normal')


creatinina_cb = IntVar()
ureia_cb = IntVar()
potassio_cb = IntVar()
glicemia_cb = IntVar()
hemoglobina_cb = IntVar()
plaquetas_cb = IntVar()
inr_cb = IntVar()

ttk.Label(lab, text='Outros:').grid(column=0, row=7, columnspan=2, sticky=W)

ttk.Checkbutton(lab, text='Cr:', variable=creatinina_cb, command=lambda:
                permite_lab(creatinina_cb, creatinina_entry)).grid(column=0, row=8, pady=3, sticky=W)
creatinina_entry = ttk.Entry(lab, state='disabled', width=5)
creatinina_entry.grid(column=1, row=8, pady=3, sticky=W)

ttk.Checkbutton(lab, text='Ur:', variable=ureia_cb, command=lambda:
                permite_lab(ureia_cb, ureia_entry)).grid(column=0, row=9, pady=3, sticky=W)
ureia_entry = ttk.Entry(lab, state='disabled', width=5)
ureia_entry.grid(column=1, row=9, pady=3, sticky=W)

ttk.Checkbutton(lab, text='K:', variable=potassio_cb, command=lambda:
                permite_lab(potassio_cb, potassio_entry)).grid(column=0, row=10, pady=3, sticky=W)
potassio_entry = ttk.Entry(lab, state='disabled', width=5)
potassio_entry.grid(column=1, row=10, pady=3, sticky=W)

ttk.Checkbutton(lab, text='Glicemia:', variable=glicemia_cb, command=lambda:
                permite_lab(glicemia_cb, glicemia_entry)).grid(column=0, row=11, pady=3, sticky=W)
glicemia_entry = ttk.Entry(lab, state='disabled', width=5)
glicemia_entry.grid(column=1, row=11, pady=3, sticky=W)

ttk.Checkbutton(lab, text='Hb:', variable=hemoglobina_cb, command=lambda:
                permite_lab(hemoglobina_cb, hemoglobina_entry)).grid(column=0, row=12, pady=3, sticky=W)
hemoglobina_entry = ttk.Entry(lab, state='disabled', width=5)
hemoglobina_entry.grid(column=1, row=12, pady=3, sticky=W)

ttk.Checkbutton(lab, text='Plaquetas:', variable=plaquetas_cb, command=lambda:
                permite_lab(plaquetas_cb, plaquetas_entry)).grid(column=0, row=13, pady=3, sticky=W)
plaquetas_entry = ttk.Entry(lab, state='disabled', width=5)
plaquetas_entry.grid(column=1, row=13, pady=3, sticky=W)

ttk.Checkbutton(lab, text='INR:', variable=inr_cb, command=lambda:
                permite_lab(inr_cb, inr_entry)).grid(column=0, row=14, pady=3, sticky=W)
inr_entry = ttk.Entry(lab, state='disabled', width=5)
inr_entry.grid(column=1, row=14, pady=3, sticky=W)

# 3.4 - Outros Exames

outros_exames = ttk.LabelFrame(exames_complementares, text='Outros Exames:', borderwidth=5)
outros_exames.pack(side=LEFT, anchor=N, padx=(0, 5), pady=10)

eco_ve = StringVar()
eco_estresse_alterado = StringVar()
eco_disfuncao_vd = StringVar()
eco_hp = StringVar()
eco_disfuncao_diastolica = StringVar()
eco_estenose_importante = StringVar()
eco_insuficiencia_importante = StringVar()
eco_derrame = StringVar()
eco_disseccao = StringVar()
cintilo_transitoria = StringVar()
cintilo_fixa = StringVar()
dac_presente = StringVar()
reestenose_stent = StringVar()
enxerto_ocluido = StringVar()
disseccao_aortica = StringVar()

ttk.Label(outros_exames, text='Ecocardiograma:').pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Diminuição contrátil segmentar no VE',
                onvalue='ecocardiograma com alteração contrátil segmentar no VE', offvalue='', variable=eco_ve).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Diminuição contrátil difusa no VE',
                onvalue='ecocardiograma com diminuição contrátil difusa no VE', offvalue='', variable=eco_ve).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Ecocardiograma com estresse alterado',
                onvalue='ecocardiograma com estresse alterado', offvalue='', variable=eco_estresse_alterado).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Disfunção sistólica do VD',
                onvalue='ecocardiograma com disfunção sistólica do VD', offvalue='', variable=eco_disfuncao_vd).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Hipertensão pulmonar',
                onvalue='ecocardiograma com hipertensão pulmonar', offvalue='', variable=eco_hp).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Disfunção diastólica do VE',
                onvalue='ecocardiograma com disfunção diastólica do VE', offvalue='', variable=eco_disfuncao_diastolica).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Estenose valvar importante',
                onvalue='ecocardiograma com estenose valvar importante', offvalue='', variable=eco_estenose_importante).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Insuficiência valvar importante',
                onvalue='ecocardiograma com insuficiência valvar importante', offvalue='',
                variable=eco_insuficiencia_importante).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Derrame pericárdico',
                onvalue='ecocardiograma com derrame pericárdico', offvalue='', variable=eco_derrame).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Sinais de dissecção aórtica',
                onvalue='ecocardiograma com sinais de dissecção aórtica', offvalue='', variable=eco_disseccao).pack(anchor=W)
ttk.Separator(outros_exames, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Label(outros_exames, text='Cintilografia:').pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Hipocaptação transitoria discreta',
                onvalue='cintilografia com hipocaptação transitoria discreta', offvalue='', variable=cintilo_transitoria).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Hipocaptação transitoria moderada',
                onvalue='cintilografia com hipocaptação transitoria moderada', offvalue='', variable=cintilo_transitoria).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Hipocaptação transitoria importante',
                onvalue='cintilografia com hipocaptação transitoria importante', offvalue='', variable=cintilo_transitoria).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Hipocaptação fixa', onvalue='cintilografia com hipocaptação fixa', offvalue='',
                variable=cintilo_fixa).pack(anchor=W)
ttk.Separator(outros_exames, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Label(outros_exames, text='Angiotomografia de Coronárias ou CATE:').pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Uni ou biarterial > 50%', onvalue='angiotomo de coronárias ou CATE com DAC uni ou biarterial > 50%', offvalue='',
                variable=dac_presente).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Triarterial ou Tronco > 50%', onvalue='angiotomo de coronárias ou CATE com DAC triarterial ou tronco > 50%', offvalue='',
                variable=dac_presente).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='DAC não obstrutiva', onvalue='angiotomo de coronárias ou CATE com DAC não obstrutiva', offvalue='',
                variable=dac_presente).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Reestenose de Stent', onvalue='angiotomo de coronárias ou CATE com reestenose de stent', offvalue='',
                variable=reestenose_stent).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Enxerto (mamária e/ou safena) ocluído',
                onvalue='angiotomo de coronárias ou CATE com enxerto (mamária e/ou safena) ocluído', offvalue='', variable=enxerto_ocluido).pack(anchor=W)
ttk.Checkbutton(outros_exames, text='Dissecção aórtica', onvalue='angiotomografia ou CATE com dissecção aórtica', offvalue='',
                variable=disseccao_aortica).pack(anchor=W)

# 4 - Diagnóstico e Conduta
diagnostico_e_conduta = ttk.Frame(nb)
nb.add(diagnostico_e_conduta, text='Diagnóstico e Conduta')

# 4.1 - Hipótese Diagnóstica

hipotese_diagnostica = ttk.LabelFrame(diagnostico_e_conduta, text='Hipótese Diagnóstica:', borderwidth=5)
hipotese_diagnostica.pack(side=LEFT, anchor=N, padx=5, pady=10)

hd_frame1 = ttk.Frame(hipotese_diagnostica)
hd_frame1.grid(row=0, column=0, sticky='NW', pady=10, padx=5)

hd_frame2 = ttk.Frame(hipotese_diagnostica)
hd_frame2.grid(row=0, column=1, sticky='NW', pady=10, padx=5)


def nao_permite_entradada_de_outra_hd():
    outra_hd.config(state='disabled')


def permite_entradada_de_outra_hd():
    outra_hd.config(state='normal')


hd = StringVar()

ttk.Radiobutton(hd_frame1, text='IAM com supra de ST', value='IAM com supra de ST',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame1, text='IAM sem supra de ST', value='IAM sem supra de ST',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame1, text='Angina Instável', value='Angina Instável',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Separator(hd_frame1, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Radiobutton(hd_frame1, text='Fibrilação atrial de alta resposta ventricular',
                value='FA de alta resposta ventricular', variable=hd,
                command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame1, text='Flutter atrial de alta resposta ventricular',
                value='Flutter de alta resposta ventricular', variable=hd,
                command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame1, text='Taquicardia supraventricular paroxística',
                value='Taquicardia supraventricular paroxística', variable=hd,
                command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame1, text='Taquicardia ventricular estável', value='Taquicardia ventricular sintomática',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame1, text='Taquicardia ventricular instável', value='Taquicardia ventricular instável',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Separator(hd_frame1, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Radiobutton(hd_frame1, text='Bloqueio atrioventricular avançado ou total estável',
                value='Bloqueio atrioventricular avançado ou total estável', variable=hd,
                command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame1, text='Bloqueio atrioventricular avançado ou total instável',
                value='Bloqueio atrioventricular avançado ou total instável', variable=hd,
                command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame1, text='Doença do nó sinusal sintomática',
                value='Doença do nó sinusal sintomática', variable=hd,
                command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame1, text='Disfunção do marcapasso', value='Disfunção do marcapasso',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Separator(hd_frame1, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Radiobutton(hd_frame1, text='Síncope vasovagal (neuromediada)',
                value='Síncope vasovagal (neuromediada)', variable=hd,
                command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame1, text='Síncope por hipersensibilidade do seio carotídeo',
                value='Síncope por hipersensibilidade do seio carotídeo', variable=hd,
                command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame1, text='Lipotímia', value='Lipotímia',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame1, text='Hipotensão ortostática',
                value='Hipotensão ortostática', variable=hd,
                command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame1, text='Vertigem', value='Vertigem',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame1, text='Tontura', value='Tontura',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)

ttk.Radiobutton(hd_frame2, text='IC descompensada perfil A', value='IC descompensada perfil A',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame2, text='IC descompensada perfil B', value='IC descompensada perfil B',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame2, text='IC descompensada perfil C', value='IC descompensada perfil C',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame2, text='IC descompensada perfil D', value='IC descompensada perfil D',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Separator(hd_frame2, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Radiobutton(hd_frame2, text='Miocardite e/ou pericardite aguda', value='Miocardite e/ou pericardite aguda',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame2, text='Dissecção aórtica', value='Dissecção aórtica',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame2, text='Embolia pulmonar', value='Embolia pulmonar',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame2, text='Dor retroesternal e/ou epigástrica esofago/gástrica',
                value='Dor retroesternal e/ou epigástrica esofago/gástrica', variable=hd,
                command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame2, text='Dor torácica musculoesquelética', value='Dor torácica musculoesquelética',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)
ttk.Radiobutton(hd_frame2, text='Dor torácica pleuro/pulmonar', value='Dor torácica pleuro/pulmonar',
                variable=hd, command=nao_permite_entradada_de_outra_hd).pack(anchor=W)

ttk.Separator(hd_frame2, orient=HORIZONTAL).pack(fill=X, pady=3)

ttk.Radiobutton(hd_frame2, text='Outra: ', value='Outra:',
                variable=hd, command=permite_entradada_de_outra_hd).pack(side=LEFT, pady=5)
outra_hd = ttk.Entry(hd_frame2, width=40, state='disabled')
outra_hd.pack(side=RIGHT)

# 4.2 - Escores Clínicos

escores = ttk.LabelFrame(diagnostico_e_conduta, text='Escores Clínicos:', borderwidth=5)
escores.pack(side=LEFT, anchor=N, padx=(0, 5), pady=10)

escores_frame_label = ttk.Frame(escores)
escores_frame_label.grid(row=0, column=0, sticky='NW')

escores_frame_entry = ttk.Frame(escores)
escores_frame_entry.grid(row=0, column=1, sticky='NW')

timi_risk_var = IntVar()
grace_var = IntVar()
heart_var = IntVar()
crusade_var = IntVar()
chads_vasc_var = IntVar()
has_bled_var = IntVar()
atria_var = IntVar()
ehmrg_var = IntVar()


def abrir_entry_e_link(escore_var, entry_state, endereco):
    if escore_var.get() == 0:
        entry_state.configure(state='disabled')
    else:
        entry_state.configure(state='normal')
        confirma_redirecionamento = messagebox.askyesno(message='Deseja ser redirecionado para calculadora online?', title='Confirmação')
        if confirma_redirecionamento:
            webbrowser.open_new(endereco)


timi_risk_end = 'https://www.mdcalc.com/timi-risk-score-ua-nstemi'
ttk.Checkbutton(escores_frame_label, text='TIMI-RISK (SCASST):', cursor="hand2", variable=timi_risk_var,
                command=lambda: abrir_entry_e_link(timi_risk_var, timi_risk, timi_risk_end)).pack(anchor=W, pady=4)
timi_risk = ttk.Entry(escores_frame_entry, state='disabled', width=4)
timi_risk.pack(anchor=W, pady=4)

grace_end = 'https://www.mdcalc.com/grace-acs-risk-mortality-calculator'
ttk.Checkbutton(escores_frame_label, text='GRACE:', cursor="hand2", variable=grace_var,
                command=lambda: abrir_entry_e_link(grace_var, grace, grace_end)).pack(anchor=W, pady=4)
grace = ttk.Entry(escores_frame_entry, state='disabled', width=4)
grace.pack(anchor=W, pady=4)

heart_end = 'https://www.mdcalc.com/heart-score-major-cardiac-events'
ttk.Checkbutton(escores_frame_label, text='HEART:', cursor="hand2", variable=heart_var,
                command=lambda: abrir_entry_e_link(heart_var, heart, heart_end)).pack(anchor=W, pady=4)
heart = ttk.Entry(escores_frame_entry, state='disabled', width=4)
heart.pack(anchor=W, pady=4)

crusade_end = 'https://www.mdcalc.com/crusade-score-post-mi-bleeding-risk'
ttk.Checkbutton(escores_frame_label, text='CRUSADE:', cursor="hand2", variable=crusade_var,
                command=lambda: abrir_entry_e_link(crusade_var, crusade, crusade_end)).pack(anchor=W, pady=4)
crusade = ttk.Entry(escores_frame_entry, state='disabled', width=4)
crusade.pack(anchor=W, pady=4)

ttk.Separator(escores_frame_label, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Separator(escores_frame_entry, orient=HORIZONTAL).pack(fill=X, pady=3)

chads_vasc_end = 'https://www.mdcalc.com/cha2ds2-vasc-score-atrial-fibrillation-stroke-risk'
ttk.Checkbutton(escores_frame_label, text='CHADS-VASc:', cursor="hand2", variable=chads_vasc_var,
                command=lambda: abrir_entry_e_link(chads_vasc_var, chads_vasc, chads_vasc_end)).pack(anchor=W, pady=4)
chads_vasc = ttk.Entry(escores_frame_entry, state='disabled', width=4)
chads_vasc.pack(anchor=W, pady=4)

has_bled_end = 'https://www.mdcalc.com/has-bled-score-major-bleeding-risk'
ttk.Checkbutton(escores_frame_label, text='HAS-BLED:', cursor="hand2", variable=has_bled_var,
                command=lambda: abrir_entry_e_link(has_bled_var, has_bled, has_bled_end)).pack(anchor=W, pady=4)
has_bled = ttk.Entry(escores_frame_entry, state='disabled', width=4)
has_bled.pack(anchor=W, pady=4)

atria_end = 'https://www.mdcalc.com/atria-bleeding-risk-score'
ttk.Checkbutton(escores_frame_label, text='ATRIA:', cursor="hand2", variable=atria_var,
                command=lambda: abrir_entry_e_link(atria_var, atria, atria_end)).pack(anchor=W, pady=4)
atria = ttk.Entry(escores_frame_entry, state='disabled', width=4)
atria.pack(anchor=W, pady=4)

ttk.Separator(escores_frame_label, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Separator(escores_frame_entry, orient=HORIZONTAL).pack(fill=X, pady=3)

ehmrg_end = 'https://www.mdcalc.com/emergency-heart-failure-mortality-risk-grade-ehmrg'
ttk.Checkbutton(escores_frame_label, text='EHMRG:', cursor="hand2", variable=ehmrg_var,
                command=lambda: abrir_entry_e_link(ehmrg_var, ehmrg, ehmrg_end)).pack(anchor=W, pady=4)
ehmrg = ttk.Entry(escores_frame_entry, state='disabled', width=4)
ehmrg.pack(anchor=W, pady=4)

# 4.3 - Condutas

condutas = ttk.LabelFrame(diagnostico_e_conduta, text='Condutas Sugeridas:', borderwidth=5)
condutas.pack(side=LEFT, anchor=N, padx=(0, 5), pady=10)

cd_aas = StringVar()
cd_clopidogrel_300 = StringVar()
cd_clopidogrel_75 = StringVar()
cd_enoxa_1_12em12 = StringVar()
cd_enoxa_075_12em12 = StringVar()
cd_enoxa_1_1xdia = StringVar()
cd_enoxa_ataque = StringVar()
cd_fondaparinux = StringVar()
cd_hnf = StringVar()
cd_tenecteplase = StringVar()
cd_alteplase = StringVar()
cd_morfina = StringVar()
cd_nitrato = StringVar()
cd_betabloq = StringVar()
cd_ieca_bra = StringVar()
cd_espironolactona = StringVar()
cd_estatina = StringVar()

ttk.Checkbutton(condutas, text='AAS 200mg VO', onvalue='AAS 200mg VO', offvalue='',
                variable=cd_aas).pack(anchor=W)
ttk.Checkbutton(condutas, text='Clopidogrel 300mg VO', onvalue='Clopidogrel 300mg VO', offvalue='',
                variable=cd_clopidogrel_300).pack(anchor=W)
ttk.Checkbutton(condutas, text='Clopidogrel 75mg VO', onvalue='Clopidogrel 75mg VO', offvalue='',
                variable=cd_clopidogrel_75).pack(anchor=W)
ttk.Separator(condutas, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Checkbutton(condutas, text='Enoxaparina 1mg/kg SC 12/12h', onvalue='Enoxaparina 1mg/kg SC 12/12h', offvalue='',
                variable=cd_enoxa_1_12em12).pack(anchor=W)
ttk.Checkbutton(condutas, text='Enoxaparina 0,75mg/kg SC 12/12h', onvalue='Enoxaparina 0,75mg/kg SC 12/12h',
                offvalue='', variable=cd_enoxa_075_12em12).pack(anchor=W)
ttk.Checkbutton(condutas, text='Enoxaparina 1mg/kg SC 1x/dia', onvalue='Enoxaparina 1mg/kg SC 1x/dia', offvalue='',
                variable=cd_enoxa_1_1xdia).pack(anchor=W)
ttk.Checkbutton(condutas, text='Enoxaparina ataque 30mg EV', onvalue='Enoxaparina ataque 30mg EV', offvalue='',
                variable=cd_enoxa_ataque).pack(anchor=W)
ttk.Checkbutton(condutas, text='Fondaparinux 2,5mg SC', onvalue='Fondaparinux 2,5mg SC', offvalue='',
                variable=cd_fondaparinux).pack(anchor=W)
ttk.Checkbutton(condutas, text='Heparina não fracionada EV', onvalue='Heparina não fracionada EV', offvalue='',
                variable=cd_hnf).pack(anchor=W)
ttk.Separator(condutas, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Checkbutton(condutas, text='Tenecteplase', onvalue='Tenecteplase EV', offvalue='',
                variable=cd_tenecteplase).pack(anchor=W)
ttk.Checkbutton(condutas, text='Alteplase', onvalue='Alteplase EV', offvalue='',
                variable=cd_alteplase).pack(anchor=W)
ttk.Separator(condutas, orient=HORIZONTAL).pack(fill=X, pady=3)
ttk.Checkbutton(condutas, text='Morfina', onvalue='Isordil SL', offvalue='',
                variable=cd_morfina).pack(anchor=W)
ttk.Checkbutton(condutas, text='Nitrato', onvalue='Morfina EV', offvalue='',
                variable=cd_nitrato).pack(anchor=W)
ttk.Checkbutton(condutas, text='Betabloqueador', onvalue='Betabloqueador VO', offvalue='',
                variable=cd_betabloq).pack(anchor=W)
ttk.Checkbutton(condutas, text='IECA/BRA', onvalue='IECA/BRA', offvalue='',
                variable=cd_ieca_bra).pack(anchor=W)
ttk.Checkbutton(condutas, text='Espironolactona', onvalue='Espironolactona', offvalue='',
                variable=cd_espironolactona).pack(anchor=W)
ttk.Checkbutton(condutas, text='Estatina', onvalue='Estatina', offvalue='',
                variable=cd_estatina).pack(anchor=W)

ttk.Separator(condutas, orient=HORIZONTAL).pack(fill=X, pady=3)

ttk.Label(condutas, text='Outras:').pack(anchor=W)
conduta1 = ttk.Entry(condutas, width=40)
conduta1.pack(anchor=W, pady=3)
conduta2 = ttk.Entry(condutas, width=40)
conduta2.pack(anchor=W, pady=3)
conduta3 = ttk.Entry(condutas, width=40)
conduta3.pack(anchor=W, pady=3)

# 4.4 - Destino


def nao_permite_entradada_de_outro_destino():
    outro_destino.config(state='disabled')


def permite_entradada_de_outro_destino():
    outro_destino.config(state='normal')


destino = ttk.LabelFrame(diagnostico_e_conduta, text='Destino Sugerido:', borderwidth=5)
destino.pack(side=LEFT, anchor=N, padx=(0, 5), pady=10)

destino_var = StringVar()

ttk.Radiobutton(destino, text='Alta após medidas orientadas',
                value='Alta após medidas orientadas',
                variable=destino_var, command=nao_permite_entradada_de_outro_destino).pack(anchor=W)
ttk.Radiobutton(destino, text='Retornar contato após medidas orientadas',
                value='Retornar contato após medidas orientadas',
                variable=destino_var, command=nao_permite_entradada_de_outro_destino).pack(anchor=W)
ttk.Radiobutton(destino, text='Internação hospitalar',
                value='Internação hospitalar',
                variable=destino_var, command=nao_permite_entradada_de_outro_destino).pack(anchor=W)
ttk.Radiobutton(destino, text='Transferência para hospital de referência',
                value='Transferência para hospital de referência',
                variable=destino_var, command=nao_permite_entradada_de_outro_destino).pack(anchor=W)
ttk.Radiobutton(destino, text='Transferência para hospital de referência (linha vermelha)',
                value='Transferência para hospital de referência (linha vermelha)',
                variable=destino_var, command=nao_permite_entradada_de_outro_destino).pack(anchor=W)

ttk.Separator(destino, orient=HORIZONTAL).pack(fill=X, pady=3)

ttk.Radiobutton(destino, text='Outro: ', value='Outro:',
                variable=destino_var, command=permite_entradada_de_outro_destino).pack(side=LEFT, pady=5)
outro_destino = ttk.Entry(destino, width=42, state='disabled')
outro_destino.pack(side=RIGHT)


# Rodapé

rodape = ttk.Frame(root)
rodape.pack()

obs_final_cb = IntVar()


def permite_obs_final():
    if obs_final_cb.get() == 0:
        obs_final_entry.configure(state='disabled')
    else:
        obs_final_entry.configure(state='normal')


medicos = ('Pedro', 'Vinicius', 'Bernardo')


ttk.Label(rodape, text='Médico Responsável: ').grid(row=0, column=0)
medico_responsavel = ttk.Combobox(rodape, values=medicos, width=25, state="readonly")
medico_responsavel.grid(row=0, column=1, padx=(0, 30))

ttk.Checkbutton(rodape, text='Observação final: ', variable=obs_final_cb,
                command=permite_obs_final).grid(row=0, column=2)
obs_final_entry = ttk.Entry(rodape, state='disabled', width=80)
obs_final_entry.grid(row=0, column=3, padx=(0, 20))

#------------------------------------------------------------------------------

# Validação de entradas

def validar_entradas():

    padrao_data = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/[12][0-9]{3}$'
    padrao_hora = r'^([0-1][0-9]|[2][0-3]):[0-5][0-9]$'

    if not nome.get():
        messagebox.showinfo(message='Insira um nome para o paciente! Somente caracteres do alfabeto.',
                            title='Erro', icon='error')
    elif not idade.get().isdigit():
        messagebox.showinfo(message='Insira uma idade válida! Somente números.', title='Erro', icon='error')
    elif int(idade.get()) > 120:
        messagebox.showinfo(message='Insira uma idade válida! Idade menor que 120 anos.', title='Erro', icon='error')
    elif not match(padrao_data, data_contato.get()):
        messagebox.showinfo(message='Insira uma data válida para o atendimento! Seguir o padrão dia/mês/ano, sendo dia e mês com 2 digitos e ano com 4 dígitos.\n\n\n   Exemplo:  05/04/2018',
                            title='Erro', icon='error')
    elif not hora_contato.get():
        messagebox.showinfo(message='Insira uma hora para o atendimento!',
                            title='Erro', icon='error')
    elif not match(padrao_hora, hora_contato.get()):
        messagebox.showinfo(message='Insira uma hora válida para o atendimento! Seguir o padrão hora:minuto no sistema de 24 horas.\n\n\n   Exemplo:  00:12',
                            title='Erro', icon='error')
    elif not hospital.get():
        messagebox.showinfo(message='Insira o nome do hospital de onde está sendo realizado o contato!',
                            title='Erro', icon='error')
    elif not hospital.get():
        messagebox.showinfo(message='Insira um nome para o hospital! Somente caracteres do alfabeto.',
                            title='Erro', icon='error')
    elif not medico.get():
        messagebox.showinfo(message='Insira o nome do médico que realiza o contato!',
                            title='Erro', icon='error')
    elif not medico.get():
        messagebox.showinfo(message='Insira um nome para o médico que realiza o atendimento! Somente caracteres do alfabeto.',
                            title='Erro', icon='error')
    elif not crm.get():
        messagebox.showinfo(message='Insira o CRM do médico que realiza o contato!',
                            title='Erro', icon='error')
    elif not crm.get().isdigit():
        messagebox.showinfo(message='Insira um CRM válido! Somente números.', title='Erro', icon='error')
    elif not medico_responsavel.get():
        messagebox.showinfo(message='Insira o nome do médico responsável pelo atendimento!',
                            title='Erro', icon='error')
    elif hora_ecg.get() and (not match(padrao_hora, hora_ecg.get())):
        messagebox.showinfo(message='Insira uma hora de realização do ECG válida! Seguir o padrão hora:minuto no sistema de 24 horas.\n\n\n   Exemplo:  00:12',
                            title='Erro', icon='error')

    else:
        confirma_submeter = messagebox.askyesno(
            message='Confirma a inclusão do atendimento?', title='Confirmação')
        if confirma_submeter:
            montar_texto()
        else:
            pass

#------------------------------------------------------------------------------

# Montar texto e CSV

def montar_texto():
    texto = str()

    # Cabeçalho

    texto += 'Dados do Contato:' + '\n\n'

    entradas_cabecalho = [
        'Nome: ' + nome.get(),
        'Idade: ' + idade.get(),
        'Plano de Saúde: ' + plano_saude.get(),
        'Data do Contato: ' + data_contato.get(),
        'Hora do Contato: ' + hora_contato.get(),
        'Hospital: ' + hospital.get(),
        'Médico: ' + medico.get(),
        'CRM: ' + crm.get(),
        'Telefone para Contato: ' + tel_contato.get()
    ]

    for i in entradas_cabecalho:
        texto += i + '\n'

    # Separador

    texto += '-----------------------------------------' + '\n'

    # História

    texto += 'História Clínica:' + '\n'

    # Queixa Principal
    filtro_qp = str()
    if queixa_principal.get() == 'Outra:':
        texto += '\n' + 'Queixa Principal: ' + outras_qp.get().lower() + '.'
        filtro_qp = 'Outra: ' + outras_qp.get().lower()
    else:
        texto += '\n' + 'Queixa Principal: ' + queixa_principal.get().lower() + '.'
        filtro_qp = queixa_principal.get().lower()

    # Resumo da História

    texto += '\n' + 'Resumo da História Atual: ' + historia_atual.get('1.0', END)

    # Antecedentes

    entradas_antecedentes = [
        has.get(),
        dm2.get(),
        dlp.get(),
        obesidade.get(),
        sedentarismo.get(),
        hf_dac.get(),
        hf_ms.get(),
        tbg.get(),
        ex_tbg.get(),
        dpoc.get(),
        cocaina.get(),
        crack.get(),
        drogas_ev.get(),
        dac_50.get(),
        dac_stent.get(),
        dac_rm.get(),
        iam.get(),
        avei.get(),
        aveh.get(),
        daop.get(),
        d_carotidea.get(),
        fa.get(),
        tpsv.get(),
        ic_sem_etiologia.get(),
        ic_valvar.get(),
        ic_isquemica.get(),
        icfep.get(),
        drc_nd.get(),
        drc_d.get(),
        hipotireoidismo.get(),
        hipertireoidismo.get(),
        outros_ap.get()
    ]

    filtro_antecedentes = []

    for i in entradas_antecedentes:
        if i:
            filtro_antecedentes.append(i)
        else:
            pass

    if len(filtro_antecedentes) == 0:
        texto += 'Antecedentes: ' + 'não há.'
    elif len(filtro_antecedentes) == 1:
        texto += 'Antecedentes: ' + filtro_antecedentes[0] + '.'
    else:
        texto += 'Antecedentes: ' + ', '.join(filtro_antecedentes) + '.'

    # Medicamentos

    entradas_medicamentos = [
        aas.get(),
        outros_antiplaquetarios.get(),
        ieca_bra.get(),
        estatina.get(),
        beta_bloqueador.get(),
        furosemida.get(),
        tiazidico.get(),
        bcc.get(),
        bcc_nd.get(),
        nitrato.get(),
        digoxina.get(),
        amiodarona.get(),
        propafenona.get(),
        outros_antiarritmicos.get(),
        varfarina.get(),
        noac.get(),
        anti_dm_oral.get(),
        insulina.get(),
        outras_medicacoes.get()
    ]

    filtro_medicamentos = []
    for i in entradas_medicamentos:
        if i:
            filtro_medicamentos.append(i)
        else:
            pass

    if len(filtro_medicamentos) == 0:
        texto += '\n' + 'Medicações de uso contínuo: ' + 'não.'
    elif len(filtro_medicamentos) == 1:
        texto += '\n' + 'Medicações de uso contínuo: ' + filtro_medicamentos[0].lower() + '.'
    else:
        texto += '\n' + 'Medicações de uso contínuo: ' + ', '.join(filtro_medicamentos).lower() + '.'

    # Separador

    texto += '\n' + '-----------------------------------------'

    # Exame físico

    texto += '\n' + 'Exame Físico:' + '\n'

    # Sinais vitais

    entradas_sinais_vitais = [
        ['FC ', fc.get(), ' bpm'],
        ['PA ', pa.get(), ' mmHg'],
        ['SpO2 ', spo2.get(), '%'],
        ['', taquipneia.get(), '']
    ]

    filtro_sinais_vitais = []
    for i in entradas_sinais_vitais:
        if i[1]:
            filtro_sinais_vitais.append(''.join(i))
        else:
            pass

    if len(filtro_sinais_vitais) == 0:
        texto += '\n' + 'Sinais vitais: ' + 'sem achados relevantes segundo informações fornecidas.'
    elif len(filtro_sinais_vitais) == 1:
        texto += '\n' + 'Sinais vitais: ' + filtro_sinais_vitais[0] + '.'
    else:
        texto += '\n' + 'Sinais vitais: ' + ', '.join(filtro_sinais_vitais) + '.'

    # Cardiovascular

    entradas_cardiovascular = [
        ritmo_ef.get(),
        sopro_sist.get(),
        sopro_diast.get(),
        b3.get(),
        sopro_carotidas.get(),
        tjp.get(),
        pulso_assimetrico_mmss.get(),
        pulso_assimetrico_mmii.get(),
        enchimento_capilar_aum.get(),
        edema_mmii.get(),
        tvp.get()
    ]

    filtro_cardiovascular = []
    for i in entradas_cardiovascular:
        if i:
            filtro_cardiovascular.append(i)
        else:
            pass

    if len(filtro_cardiovascular) == 0:
        texto += '\n' + 'Cardiovascular: ' + 'sem achados relevantes segundo informações fornecidas.'
    elif len(filtro_cardiovascular) == 1:
        texto += '\n' + 'Cardiovascular: ' + filtro_cardiovascular[0] + ', sem outros achados relevantes segundo informações fornecidas.'
    else:
        texto += '\n' + 'Cardiovascular: ' + ', '.join(filtro_cardiovascular) + '.'

    # Respiratório

    entradas_respiratorio = [
        suporte_ventilatorio.get(),
        estertores.get(),
        outros_respiratorio.get()
    ]

    filtro_respiratorio = []
    for i in entradas_respiratorio:
        if i:
            filtro_respiratorio.append(i)
        else:
            pass

    if len(filtro_respiratorio) == 0:
        texto += '\n' + 'Respiratório: ' + 'sem achados relevantes segundo informações fornecidas.'
    elif len(filtro_respiratorio) == 1:
        texto += '\n' + 'Respiratório: ' + filtro_respiratorio[0] + ', sem outros achados relevantes segundo informações fornecidas.'
    else:
        texto += '\n' + 'Respiratório: ' + ', '.join(filtro_respiratorio) + '.'

    # Abdominal

    entradas_abdominal = [
        hepatomegalia.get(),
        ascite.get(),
        massa_pulsatil.get(),
        irritacao_peritoneal.get(),
        outros_abdominal.get()
    ]

    filtro_abdominal = []
    for i in entradas_abdominal:
        if i:
            filtro_abdominal.append(i)
        else:
            pass

    if len(filtro_abdominal) == 0:
        texto += '\n' + 'Abdominal: ' + 'sem achados relevantes segundo informações fornecidas.'
    elif len(filtro_abdominal) == 1:
        texto += '\n' + 'Abdominal: ' + filtro_abdominal[0] + ', sem outros achados relevantes segundo informações fornecidas.'
    else:
        texto += '\n' + 'Abdominal: ' + ', '.join(filtro_abdominal) + '.'

    # Neurológico

    entradas_neurológico = [
        nivel_consciencia.get(),
        conteudo_consciencia.get(),
        hp_completa_d.get(),
        hp_completa_e.get(),
        hp_incompleta_d.get(),
        hp_incompleta_e.get()
    ]

    filtro_neurologico = []
    for i in entradas_neurológico:
        if i:
            filtro_neurologico.append(i)
        else:
            pass

    if len(filtro_neurologico) == 0:
        texto += '\n' + 'Neurológico: ' + 'sem achados relevantes segundo informações fornecidas.'
    elif len(filtro_neurologico) == 1:
        texto += '\n' + 'Neurológico: ' + filtro_neurologico[0].lower() + ', sem outros achados relevantes segundo informações fornecidas.'
    else:
        texto += '\n' + 'Neurológico: ' + ', '.join(filtro_neurologico).lower() + '.'

    # Separador

    texto += '\n' + '-----------------------------------------'

    # Exames Complementares

    texto += '\n' + 'Exames Complementares:' + '\n'

    # ECG

    texto += '\n' + 'ECG'

    entrada_ecg_hora = hora_ecg.get()
    entrada_ecg_ritmo = ritmo.get()

    entradas_ecg_achados = [
        ecg_supra_anterosseptal.get(),
        ecg_supra_anterior.get(),
        ecg_supra_anterior_localizada.get(),
        ecg_supra_anterolateral.get(),
        ecg_supra_anterior_extensa.get(),
        ecg_supra_lateral_baixa.get(),
        ecg_supra_lateral_alta.get(),
        ecg_supra_inferior.get(),
        ecg_supra_vd.get(),
        ecg_aei_septal.get(),
        ecg_aei_anteroapical.get(),
        ecg_aei_anterior_media.get(),
        ecg_aei_lateral.get(),
        ecg_aei_inferior.get(),
        ecg_infra_difuso.get(),
        ecg_infra.get(),
        ecg_onda_t_isquemia.get(),
        ecg_alt_dinamica_stt.get(),
        ecg_airv.get(),
        ecg_miopericardite.get(),
        ecg_repol_precoce.get(),
        ecg_discinesia.get(),
        ecg_hipercalemia.get(),
        ecg_bre.get(),
        ecg_brd.get(),
        ecg_bdas.get(),
        ecg_bdam.get(),
        ecg_bdpi.get(),
        ecg_sae.get(),
        ecg_sad.get(),
        ecg_sve.get(),
        ecg_svd.get(),
        ecg_qt_longo.get(),
        ecg_ev_frequentes.get(),
        ecg_esv_frequentes.get(),
        ecg_tvns.get()
    ]

    if entrada_ecg_hora:
        texto += '\n' + 'Hora: ' + entrada_ecg_hora
    else:
        texto += '\n' + 'Hora: não informada.'

    if entrada_ecg_ritmo:
        texto += '\n' + 'Ritmo: ' + entrada_ecg_ritmo
    else:
        texto += '\n' + 'Ritmo: não informado.'

    filtro_ecg_achados = []
    for i in entradas_ecg_achados:
        if i:
            filtro_ecg_achados.append(i)
        else:
            pass

    if len(filtro_ecg_achados) == 0:
        texto += '\n' + 'Achados: ' + 'sem achados relevantes.'
    elif len(filtro_ecg_achados) == 1:
        texto += '\n' + 'Achados: ' + filtro_ecg_achados[0] + ', sem outros achados relevantes.'
    else:
        texto += '\n' + 'Achados: ' + ', '.join(filtro_ecg_achados) + '.'

    # Radiografia de Tórax

    entradas_rx = [
        ac_aumentada.get(),
        derrame_pleural.get(),
        congestao.get(),
        opacidades.get(),
        ptx.get(),
        alargamento_mediastinal.get()
    ]

    filtro_rx = []
    for i in entradas_rx:
        if i:
            filtro_rx.append(i)
        else:
            pass

    if len(filtro_rx) == 0:
        texto += '\n\n' + 'Radiografia de Tórax: ' + 'sem achados relevantes segundo informações fornecidas.'
    elif len(filtro_rx) == 1:
        texto += '\n\n' + 'Radiografia de Tórax: ' + filtro_rx[0].lower() + ', sem outros achados relevantes segundo informações fornecidas.'
    else:
        texto += '\n\n' + 'Radiografia de Tórax: ' + ', '.join(filtro_rx).lower() + '.'

    # Exames Laboratoriais

    entrada_troponina = ('troponina ', troponina.get())
    entradas_lab = [
        ('creatinina ', creatinina_entry.get(), creatinina_entry),
        ('uréia ', ureia_entry.get(), ureia_entry),
        ('potássio ', potassio_entry.get(), potassio_entry),
        ('glicemia ', glicemia_entry.get(), glicemia_entry),
        ('hemoglobina ', hemoglobina_entry.get(), hemoglobina_entry),
        ('plaquetas ', plaquetas_entry.get(), plaquetas_entry),
        ('INR ', inr_entry.get(), inr_entry)
    ]

    filtro_lab = []

    for i in entradas_lab:
        if i[1] and str(i[2]['state']) == 'normal':
            filtro_lab.append(i[0] + i[1])

    if entrada_troponina[1] == 'positiva':
        filtro_lab.append(entrada_troponina[0] + entrada_troponina[1] + ' (' + troponina_valor.get() + ')')

    if len(filtro_lab) == 0:
        texto += '\n' + 'Exames Séricos: ' + 'sem achados relevantes segundo informações fornecidas.'
    elif len(filtro_lab) == 1:
        texto += '\n' + 'Exames Séricos: ' + filtro_lab[0] + ', sem outros achados relevantes segundo informações fornecidas.'
    else:
        texto += '\n' + 'Exames Séricos: ' + ', '.join(filtro_lab) + '.'

    # Outros Exames

    entradas_outros_exames = [
        eco_ve.get(),
        eco_estresse_alterado.get(),
        eco_disfuncao_vd.get(),
        eco_hp.get(),
        eco_disfuncao_diastolica.get(),
        eco_estenose_importante.get(),
        eco_insuficiencia_importante.get(),
        eco_derrame.get(),
        eco_disseccao.get(),
        cintilo_transitoria.get(),
        cintilo_fixa.get(),
        dac_presente.get(),
        reestenose_stent.get(),
        enxerto_ocluido.get(),
        disseccao_aortica.get()
    ]

    filtro_outros_exames = []
    for i in entradas_outros_exames:
        if i:
            filtro_outros_exames.append(i)
        else:
            pass

    if len(filtro_outros_exames) == 0:
        texto += '\n' + 'Outros Exames: ' + 'sem exames relevantes segundo informações fornecidas.'
    elif len(filtro_outros_exames) == 1:
        texto += '\n' + 'Outros Exames: ' + filtro_outros_exames[0] + ', sem outros exames relevantes segundo informações fornecidas.'
    else:
        texto += '\n' + 'Outros Exames: ' + ', '.join(filtro_outros_exames) + '.'

    # Separador

    texto += '\n' + '-----------------------------------------'

    # Diagnóstico e Conduta

    texto += '\n' + 'Diagnóstico e Conduta:' + '\n'

    # Hipótese Diagnóstica

    if hd.get() == 'Outra:':
        texto += '\n' + 'Diagnóstico: ' + outra_hd.get() + '.'
        filtro_diagnostico = 'Outro:' + outra_hd.get()
    else:
        texto += '\n' + 'Diagnóstico: ' + hd.get() + '.'
        filtro_diagnostico = hd.get()

    # Escores Clínicos

    entradas_escores_clinicos = [
        ('TIMI-RISK (SCASST) de ', timi_risk.get(), timi_risk),
        ('GRACE (SCASST) de ', grace.get(), grace),
        ('HEART de ', heart.get(), heart),
        ('CRUSADE de ', crusade.get(), crusade),
        ('CHADS-VASc de ', chads_vasc.get(), chads_vasc),
        ('HAS-BLED de ', has_bled.get(), has_bled),
        ('ATRIA de ', atria.get(), atria),
        ('EHMRG de ', ehmrg.get(), ehmrg)
    ]

    filtro_escores_clinicos = []
    for i in entradas_escores_clinicos:
        if i[1] and str(i[2]['state']) == 'normal':
            filtro_escores_clinicos.append(i[0] + i[1])

    if len(filtro_escores_clinicos) == 0:
        texto += '\n' + 'Escores Clínicos: ' + 'não calculados.'
    elif len(filtro_escores_clinicos) == 1:
        texto += '\n' + 'Escores Clínicos: ' + filtro_escores_clinicos[0] + '.'
    else:
        texto += '\n' + 'Escores Clínicos: ' + ', '.join(filtro_escores_clinicos) + '.'

    # Condutas

    entradas_condutas = [
        cd_aas.get(),
        cd_clopidogrel_300.get(),
        cd_clopidogrel_75.get(),
        cd_enoxa_1_12em12.get(),
        cd_enoxa_075_12em12.get(),
        cd_enoxa_1_1xdia.get(),
        cd_enoxa_ataque.get(),
        cd_fondaparinux.get(),
        cd_hnf.get(),
        cd_tenecteplase.get(),
        cd_alteplase.get(),
        cd_morfina.get(),
        cd_nitrato.get(),
        cd_betabloq.get(),
        cd_ieca_bra.get(),
        cd_espironolactona.get(),
        cd_estatina.get(),
        conduta1.get(),
        conduta2.get(),
        conduta3.get()
    ]

    filtro_condutas = []

    for i in entradas_condutas:
        if i:
            filtro_condutas.append(i)
        else:
            pass

    if len(filtro_condutas) == 1:
        texto += '\n' + 'Conduta: ' + filtro_condutas[0] + '.'
    else:
        texto += '\n' + 'Condutas: ' + ', '.join(filtro_condutas) + '.'

    # Destino

    if destino_var.get() == 'Outro:':
        texto += '\n' + 'Destino: ' + outro_destino.get() + '.'
        destino_filtro = 'Outro:' + outro_destino.get()
    else:
        texto += '\n' + 'Destino: ' + destino_var.get() + '.'
        destino_filtro = destino_var.get()

    # Médico Responsável

    texto += '\n\n' + 'Médico Responsável: ' + medico_responsavel.get() + '.'

    # Observação final

    if obs_final_entry.get() and str(obs_final_entry['state']) == 'normal':
        texto += '\n\n' + 'Observação Final: ' + obs_final_entry.get() + '.'
        obs_filtro = obs_final_entry.get()
    else:
        texto += '\n\n' + 'Observação Final: não.'
        obs_filtro = 'não'

    # Gerar/atualizar CSV
    try:
        dados = {
            'Nome': nome.get(),
            'Idade': idade.get(),
            'Plano de Saúde': plano_saude.get(),
            'Data do Contato': data_contato.get(),
            'Hora do Contato': hora_contato.get(),
            'Hospital': hospital.get(),
            'Médico': medico.get(),
            'CRM': crm.get(),
            'Telefone para Contato': tel_contato.get(),
            'QP': filtro_qp,
            'HDA': historia_atual.get('1.0', END),
            'AP': ', '.join(filtro_antecedentes),
            'Medicamentos': ', '.join(filtro_medicamentos).lower(),
            'Sinais Vitais': ', '.join(filtro_sinais_vitais),
            'CV': ', '.join(filtro_cardiovascular),
            'AR': ', '.join(filtro_respiratorio),
            'Abdominal': ', '.join(filtro_abdominal),
            'Neuro': ', '.join(filtro_neurologico).lower(),
            'ECG hora': entrada_ecg_hora,
            'ECG ritmo': entrada_ecg_ritmo,
            'ECG achados': ', '.join(filtro_ecg_achados),
            'Rx tórax': ', '.join(filtro_rx).lower(),
            'Lab': ', '.join(filtro_lab),
            'Outros exames': ', '.join(filtro_outros_exames),
            'Diagnóstico': filtro_diagnostico,
            'Escores Clínicos': ', '.join(filtro_escores_clinicos),
            'Condutas': ', '.join(filtro_condutas),
            'Destino': destino_filtro,
            'Observação': obs_filtro,
            'Médico Responsável': medico_responsavel.get()
        }

        path_arquivo = os.path.join('C:\\Users\\Public\\Telecardiologia\\Atendimentos', 'atendimentos1.csv')
        path_arquivo_backup = os.path.join('C:\\Users\\Public\\Telecardiologia\\Backup', 'backup_atendimentos1.csv')

        arquivo_existe = os.path.isfile(path_arquivo)
        arquivo_backup_existe = os.path.isfile(path_arquivo_backup)

        with open(path_arquivo, 'a') as arquivo_csv, open(path_arquivo_backup, 'a') as arquivo_csv_backup:
            campos = list(dados.keys())
            csv_writer1 = csv.DictWriter(arquivo_csv, fieldnames=campos, delimiter=';', lineterminator='\n')
            csv_writer2 = csv.DictWriter(arquivo_csv_backup, fieldnames=campos, delimiter=';', lineterminator='\n')

            if not (arquivo_existe and arquivo_backup_existe):
                csv_writer1.writeheader()
                csv_writer2.writeheader()

            csv_writer1.writerow(dados)
            csv_writer2.writerow(dados)

    except TclError:
        messagebox.showinfo(message='Reveja as informações inseridas!',
                            title='Erro', icon='error')

    # Gerar texto
    paciente = nome.get() + '.txt'
    arquivo_paciente = os.path.join('C:\\Users\\Public\\Telecardiologia\\Atendimentos', paciente)
    arquivo_paciente_backup = os.path.join('C:\\Users\\Public\\Telecardiologia\\Backup', paciente)
    with open(arquivo_paciente, 'w') as txt_paciente, open(arquivo_paciente_backup, 'w') as txt_paciente_backup:
        txt_paciente.write(texto)
        txt_paciente_backup.write(texto)

    reiniciar_apos_envio()


# Reiniciar


def reiniciar_apos_envio():
    confirma_reiniciar = messagebox.askyesno(message='Seu atendimento foi enviado com sucesso! Deseja iniciar um novo atendimento?', title='Confirmação')
    if confirma_reiniciar:
        root.destroy()
        subprocess.call(["python", os.path.join(sys.path[0], __file__)] + sys.argv[1:])
    else:
        pass


def reiniciar_sem_envio():
    confirma_reiniciar = messagebox.askyesno(message='Confirma a reinicialização do atendimento? Você irá perder todos os dados preenchidos.', title='Confirmação')
    if confirma_reiniciar:
        root.destroy()
        subprocess.call(["python", os.path.join(sys.path[0], __file__)] + sys.argv[1:])
    else:
        pass


# Botões do rodapé

ttk.Button(rodape, text='REINICIAR', command=reiniciar_sem_envio).grid(row=0, column=4)
ttk.Button(rodape, text='FINALIZAR', command=validar_entradas).grid(row=0, column=5, padx=(8, 0))

root.mainloop()
