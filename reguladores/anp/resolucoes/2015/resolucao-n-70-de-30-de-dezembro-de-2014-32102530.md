---
titulo: "RESOLUÇÃO Nº 70, DE 30 DE DEZEMBRO DE 2014"
orgao: "Ministério de Minas e Energia/AGÊNCIA NACIONAL DO PETRÓLEO, GÁS NATURAL E BIOCOMBUSTÍVEIS"
tipo: "Resolução"
numero: "70"
data: 2014-12-30
revogada: null
versao_texto: "publicação original"
publicacao: "DOU de 12/01/2015, seção 1, p. 31"
data_publicacao: 2015-01-12
edicao: "7"
fonte: "https://www.in.gov.br/web/dou/-/resolucao-n-70-de-30-de-dezembro-de-2014-32102530"
sha256_html_fonte: d559d0787591aeb13906a8b1be9d61f447b2075fe0d49e8dce86caec96082b27
baixado_em: 2026-10-28
---
# RESOLUÇÃO Nº 70, DE 30 DE DEZEMBRO DE 2014

RESOLUÇÃO Nº 70, DE 30 DE DEZEMBRO DE 2014

(Publicada no DOU de 31-12-2014)

ANEXO (\*)

Padrão ANP4C

Dados e Informações de Coordenadas e Feições Geográficas

1.Das disposições gerais

1.1.O presente padrão visa estabelecer o modo como devemser comunicadas à Agência Nacional do Petróleo, Gâs Natural eBiocombustíveis - ANP os dados e informações de coordenadas efeições geográficas: pontos, linhas ou polígonos.

1.2.As informações devem ser apresentadas em meio digital,gravadas em CD, DVD, ou outra mídia que, em função do volumedos dados, se faça necessário. Para o envio automatizado entre sistemas,as informações devem ser apresentadas conforme a especificaçãode interfaces própria de cada sistema, a ser fornecida pelaANP no momento de implantação de cada novo sistema.

1.3.Todas as feições geográficas serão representadas e informadasà ANP de duas maneiras:

a)por meio de listagem de suas coordenadas;

b)por meio de feições georreferenciadas em formato SIG("Sistema de Informação Geográfica").

1.4.Não serão aceitas representações de coordenadas ou feiçõesgeográficas em desacordo com o presente Padrão.

2.Dos pares de coordenadas

2.1.Todos os pares de coordenadas devem ser informadosexclusivamente em coordenadas geográficas referenciadas ao referencialgeodésico SIRGAS2000.

2.1.1 Toda e qualquer transformação dos pares de coordenadasentre diferentes referenciais geodésicos devem seguir o modelomatemático e parâmetros de transformação publicados oficialmentepelo IBGE.

2.2.Cada coordenada será expressa no formato"GG:MM:SS,SSS" (graus, com dois algarismos, seguidos de doispontos, seguidos de minutos, com dois algarismos, seguidos de doispontos, seguidos de segundos, com dois algarismos na parte inteira etrês na parte decimal, sendo separadas essas partes por vírgula).

2.3.A indicação do hemisfério que contém a coordenada seráfeita apenas através de um sinal, imediatamente anteposto à representaçãoda coordenada, respeitando a seguinte convenção:

a)Sinal Positivo ("+"): hemisférios Norte e Leste. Ex:"+GG:MM:SS,SSS";

b)Sinal Negativo ("-"): hemisférios Sul e Oeste. Ex "GG:MM:SS,SSS".

3.Listagensde coordenadas

3.1.As listagens de coordenadas, enviadas à ANP por meioimpresso ou em mídia digital, devem ser informadas em planilha deformato compatível com o Microsoft Excel (\*.xls ou \*.xlsx), conformeos modelos do Anexo 1. Deverá ser criada uma planilha paracada conjunto de feições: uma planilha para as feições pontuais, outraplanilha para as feições lineares e uma terceira planilha para as

feições poligonais, no caso de ocorrerem os três tipos de feiçõesgeográficas. Para o envio de informações automatizadas entre sistemas,as listagens de coordenadas devem ser informadas conforme aespecificação de interfaces própria de cada sistema (por exemplo, nopadrão texto, ou XML - eXtensible Markup Language - ou em outropadrão informado nas especificações de interface no momento daimplantação de cada novo sistema).

3.2.Todas as colunas (atributos) devem estar identificadas, naprimeira linha de cada planilha.

3.3.A primeira coluna deverá trazer a identificação da feição.Ex. "Área Santos" ou "0300\_CABO\_FRIO".

3.4.A segunda coluna deverá identificar o tipo da feição, seponto, linha ou polígono.

3.5.Na terceira coluna deverá ser informado o número dovértice. No caso de feição pontual, um único vértice para cada ponto.No caso de feições lineares, não é necessário que o primeiro vérticeseja o número 1, ele pode ser qualquer número desde que os vérticessubseqüentes possuam numeração superior ao primeiro vértice anterior.No caso de feição poligonal (uma sequência de linhas onde oprimeiro ponto da primeira linha coincide com o último ponto daúltima linha), a numeração dos vértices deverá começar pelo número1, com incrementos unitários no sentido horário.

3.6.A quarta coluna deverá trazer as latitudes dos vértices,conforme item 2.

3.7.A quinta coluna deverá trazer as longitudes dos vértices,conforme item 2.

3.8.A listagem de coordenadas de feições do tipo polígonodeve sempre ser "fechada", isto é, as coordenadas do último pontolistado devem ser as mesmas do primeiro ponto.

3.9.Em uma mesma planilha poderão ser representadas tantasfeições quantas se queira, desde que de um mesmo tipo, pontuais,lineares ou poligonais, obedecendo às regras indicadas acima.

3.10.Outras colunas poderão ser adicionadas, a partir da sextacoluna, para armazenar quaisquer informações que se julgar relevantes.

3.11.Osnomes das colunas das listagens de coordenadas nãodevem conter: qualquer acentuação; caracteres "ç", "!", "@", "#", "-","$", "%"; ou qualquer outro caracter especial. No caso do nome dacoluna ser composto por mais de uma palavra, a separação entre elasdeve ser feita utilizando-se o caracter sublinhado ("underscore"), conformeindicado nas planilhas exemplificadas no Anexo 1.

4.Informações padrão SIG ("Sistema de Informação Geográfica")

4.1.Asinformações no padrão SIG devem ser apresentadasem arquivo vetorial no formato "shapefile" (shp), acompanhado dosdemais arquivos de suporte ao shapefile: banco de dados/atributos(em formato dbf) e de vínculo (em formato shx). Além destes, asinformações apresentadas devem obigatoriamente conter arquivo noformato prj com informação do referencial geodésico, conforme indicadono Anexo 2 (feições geradas a partir das feições descritas nasplanilhas do Anexo 1).

4.1.1 O arquivo no formato prj no referencial geodésicoSIRGAS2000 deverá conter as seguintes informações, em conformidadecom os parâmetros de caracterização do SIRGAS2000 daR.PR 01/2005 do IBGE:

GEOGCS["SIRGAS\_2000",DATUM["D\_SIRGAS\_2000",SPHEROID["GRS\_1980",6378137,298.257222101]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]

4.2.Nocaso de feições lineares ou poligonais poderão sersolicitadas duas classes de feições geográficas: uma linear ou poligonal,correspondente, e outra pontual. Esta última deverá indicar ospontos correspondentes aos vértices das feições lineares ou poligonaisque estão sendo representadas.

4.3.Nenhuma das classes de feições geográficas referidas deveser projetada, ou seja, todas devem ser representadas como coordenadasgeográficas, referenciadas ao referencial geodésico SIRGAS2000.

4.4.Todasas colunas informadas na listagem de coordenadasdas feições geográficas, incluindo aquelas definidas no item 3.10acima, devem estar ligadas às feições SIG como atributos.

4.5.Os rótulos não devem ser anexados às classes de feições.Eles estão indicados no Anexo 2 apenas para facilidade de entendimento.

5.OutrosDocumentos Normativos Complementares que façamreferência a Dados Georreferenciados.

5.1.Todos os dados georreferenciados entregues à ANP deverãoatender ao definido neste padrão. Para casos específicos, poderãoser solicitados dados complementares em sistemas de coordenadase/ou referenciais geodésicos diferentes dos especificadas nestepadrão desde que previstos em documentos complementares daárea responsável por essas informações.

5.2.Outros documentos normativos que padronizem dadoscom conteúdo que possa ser georreferenciado, deverão fazer referênciaexplícita com indicação do uso do PADRÃO ANP4C.

Os anexos I e II, partes integrantes do Padrão ANP4C, encontram-sedisponíveis no sítio eletrônico da ANP na internet, noendereço www.anp.gov.br.

(\*) Publicado nesta data por ter sido omitido no DOU de 31/12/2014,Seção 1, página 138.
