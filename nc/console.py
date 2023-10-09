import model
asd = model
data = [
"""
A AU - Autorização de Uso é instrumento de caráter precário, utilizado pela CEAGESP para
autorizar a ocupação e o uso provisório de suas áreas pelo prazo máximo de 180 (cento e
oitenta) dias e será encerrado sempre no último dia do mês. Se verificada a possibilidade do
prazo ultrapassar o determinado, o vencimento será antecipado para o último dia do mês
anterior à outorga da AU.
"""
,
"""
A CEAGESP divulgará aos interessados a relação de áreas disponíveis para AU no
endereço eletrônico www.ceagesp.gov.br
"""
,

"""
Ocorrida a outorga de AU, será obrigatória a abertura de procedimento licitatório pelo
DEPEC ou DEINT para a área autorizada.
"""
,
"""
Na ocorrência de procedimento licitatório da área em uso em regime de AU, a autorização
concedida será cancelada por solicitação da CEAGESP para atribuição ao vencedor do
certame.
"""
,

"""
A CEAGESP poderá autorizar a renovação da AU por mais um período de 180 (cento e
oitenta) dias.
"""
,
"""

Se necessário, uma segunda renovação da AU poderá ser autorizada desde que seja:
a)
comprovada a abertura de procedimento licitatório para atribuição da área em CCRU;
b)
estabelecido o período de uso provisório da área até a conclusão do procedimento
licitatório;
c)
condicionada à apresentação de justificativa pelo departamento responsável, DEPEC
ou DEINT;
d)
referendado pela DIOPE.
"""
,
"""
A comercialização ou desenvolvimento de atividades atípicas em regime de AU em área
com metragem igual ou superior a 200 m2 (duzentos metros quadrados) será considerada
operação de grande vulto cuja outorga a pessoas jurídicas observará as condições
seguintes:
a)
realização de visita técnica pelos interessados, se for o caso;
b)
apresentação de atestado de capacitação técnica;
c)
entrega de documentação exigida.
"""
,
"""
A AU poderá ser revogada a qualquer momento por solicitação da CEAGESP ou do
autorizatário.
"""
,
"""
A área disponibilizada em procedimento licitatório que não apresentou ganhador do certame
retornará para uso em regime de AU até a realização de novo certame.
"""
,
"""
Para concessionários e permissionários em final de contrato, somente será autorizada AU
em razão da necessidade de se manter a área ocupada, ou seja, se o DEPEC ou DEINT
tenha iniciado novo processo licitatório nos 6 (seis) meses anteriores ao término do referido
contrato e que, por quaisquer motivos, a licitação apresentou-se fracassada ou deserta.
"""
,
"""
Em caso de encerramento da AU a pedido da CEAGESP, será concedido ao autorizatário o
prazo de até 2 (dois) dias úteis para desocupação da área. Após este prazo a mercadoria e
equipamentos encontrados no local serão apreendidos.
"""
,
"""
Considerando o período de deterioração dos produtos, o prazo máximo para a retirada da
mercadoria apreendida, que contará a partir da data e horário da apreensão, será:
a) Hortifrutigranjeiros (exceto verduras): 24 (vinte e quatro) horas;
b) Verduras: 12 (doze) horas;
c) Flores: 12 (doze) horas;
d) Grãos: 24 (vinte e quatro) horas;
e) Pescados: 24 (vinte e quatro) horas armazenados em câmara (resfriados/congelados);
f)
Produtos Atípicos perecíveis: 01 (uma) hora;
g) Produtos Atípicos não perecíveis: 24 (vinte e quatro) horas;
h) Produtos ligados à floricultura: 24 (vinte e quatro) horas;
i)
Aparelhos eletrônicos, móveis ou utensílios: 15 (quinze) dias úteis.
"""
,
"""
As mercadorias perecíveis não retiradas pelo proprietário no prazo determinado serão
consideradas abandonadas e, portanto, encaminhadas ao Banco de Alimentos da
CEAGESP.
"""
,
"""
As mercadorias não perecíveis e/ou utensílios não retirados no prazo determinado serão
considerados abandonados e, portanto, propriedade da CEAGESP que deliberará sobre a
sua destinação, podendo integrar o patrimônio da Companhia, serem leiloados ou doados a
entidades públicas.
"""
,
"""
No encerramento da AU, se constatadas benfeitorias realizadas na área, estas serão
incorporadas ao patrimônio da CEAGESP não cabendo ao autorizatário direito à retenção,
indenização ou compensação.
"""
,
"""
Não será permitido o uso parcial de áreas em regime de AU.
"""
,

"""
A autorização concedida para uso de áreas da CEAGESP em regime de AU é pessoal e
intransferível ficando, portanto, proibido ceder ou transferir a terceiros. Na inobservância
desta regra a autorização será cancelada e o autorizatário ficará impedido de utilizar outra
área nesta modalidade.
"""
,
"""
Para o desenvolvimento de suas atividades, os autorizatários estão sujeitos as mesmas
condições estabelecidas no presente Regulamento para os concessionários e
permissionários dos Entrepostos.
"""


]
d = 1
for x in data:
	norm_iten = asd.Norm_iten_sub(

		iten_sub=str(d),
		tag="Descrição",
		description= x.replace('\n', ''),
		norm_iten_id= 15
		)
	#print(norm_iten)
	d+=1

	asd.add_norm_mult(norm_iten)
