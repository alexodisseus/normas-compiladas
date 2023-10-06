import model
asd = model
data = ["""Os equipamentos de varejo são administrados pela CEAGESP e operacionalizados pelo
DEPEC/SECME em se tratando de equipamentos instalados no ETSP e pela Unidade
quando instalados nos Entrepostos do Interior.""" , """Os equipamentos de varejo permitem disponibilizar ao consumidor final produtos a preços
mais acessíveis e com padrões mínimos de qualidade estabelecidos pela CEAGESP.""", """A concessão de uso dos equipamentos de varejo será outorgada mediante a celebração
de CCRU, precedida de licitação nos termos da legislação própria.""" , """O CCRU/TPRU não assegura ao concessionário/permissionário exclusividade de venda
de quaisquer produtos.""",
"""Os equipamentos de varejo vagos poderão ser ocupados provisoriamente em regime de
Autorização de Uso até a realização de procedimento licitatório, momento em que a
autorização será cancelada por solicitação da CEAGESP para atribuição ao vencedor do
certame""",
"""Será cancelado por motivo de abandono o Instrumento Contratual do
concessionário/permissionário/autorizatário varejista que não comparecer por 4 (quatro)
semanas consecutivas contadas a partir da data da primeira ausência, devendo ser
previamente comunicado ao DEPEC ou DEINT que, por meio da SAEXE ou Unidade,
solicitará a justificativa do abandono.""",
"""A justificativa da ausência do concessionário/permissionário/autorizatário no local de
comercialização está condicionada à análise e deferimento do DEPEC e DEINT."""
,
"""
As faltas não justificadas ou com justificativa não aceita pela CEAGESP motivará a
penalização do concessionário/permissionário/autorizatário que será aplicada conforme
segue:
a) 1ª (primeira) falta: tolerância;
b) 2ª (segunda) falta consecutiva: advertência;
c)
3ª (terceira) falta consecutiva: multa no valor de 1 (uma) remuneração mensal relativa
à banca/grupo de bancas;
d) 4ª (quarta) falta consecutiva: multa no valor de 1 (um) remuneração mensal relativa à
banca/grupo de bancas e cancelamento do Instrumento Contratual."""
,
"""
Os equipamentos de varejo serão formados por bancas com padrões, medidas e leiaute
fixados pelo DEPEC e DEINT.
"""
,
"""
Todas as informações relativas ao tamanho e padronização dos equipamentos de varejo,
leiaute de instalação, horário de funcionamento e uniforme utilizado ficarão à disposição
dos concessionários/permissionários no DEPEC, por meio da SECME, e nas Unidades.

"""
,
"""
Observando a setorização dos equipamentos de varejo, serão considerados os seguintes
grupos de produtos:
Frutas em geral: nacionais e importadas, exceto coco verde e banana;
Coco verde;
Banana;
Verduras: hortaliças herbáceas, ou seja, vegetais cujas partes consumidas estão
acima do solo, podendo ser incluídas, excepcionalmente, as hortaliças tuberosas
cujas partes consumidas crescem dentro do solo, desde que acompanhadas de suas
respectivas folhas e comercializadas em maços;
Legumes: hortaliças que produzem frutos comestíveis, ou cujas partes alimentícias
são subterrâneas como as raízes, caules modificados, dentre outros, exceto batata,
cebola e alho;
Batata, cebola e alho;
Abóboras: seca, moranga e japonesa;
Flores de corte;
Mudas e plantas ornamentais;
Artigos de floricultura;
Ovos;
Aves abatidas e vísceras bovinas;
Pescado;
Mercearia seca: cereais, leguminosas, frutas secas e correlatas;
Laticínios;
Alimentação;
Artesanato.
"""
,
"""
Poderá ser autorizada, a critério do DEPEC ou DEINT, a venda de outros produtos, desde
que observados os parâmetros fixados pela CEAGESP.
"""
,
"""
O DEPEC ou a Gerência da Unidade poderá, quando necessário, remanejar os
concessionários/permissionários e seus equipamentos de varejo, obedecendo a
setorização previamente elaborada para o equipamento.
"""
]
d = 1
for x in data:
	norm_iten = asd.Norm_iten_sub(

		iten_sub=str(d),
		tag="Descrição",
		description= x.rstrip('\n'),
		norm_iten_id= 9
		)
	d+=1
	asd.add_norm_mult(norm_iten)
