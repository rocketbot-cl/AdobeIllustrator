# Adobe Illustrator
  
Modulo para automatizar tarefas no Adobe Illustrator  

*Read this in other languages: [English](Manual_AdobeIllustrator.md), [Português](Manual_AdobeIllustrator.pr.md), [Español](Manual_AdobeIllustrator.es.md)*
  
![banner](imgs/Banner_AdobeIllustrator.jpg)
## Como instalar este módulo
  
Para instalar o módulo no Rocketbot Studio, pode ser feito de duas formas:
1. Manual: __Baixe__ o arquivo .zip e descompacte-o na pasta módulos. O nome da pasta deve ser o mesmo do módulo e dentro dela devem ter os seguintes arquivos e pastas: \__init__.py, package.json, docs, example e libs. Se você tiver o aplicativo aberto, atualize seu navegador para poder usar o novo módulo.
2. Automático: Ao entrar no Rocketbot Studio na margem direita você encontrará a seção **Addons**, selecione **Install Mods**, procure o módulo desejado e aperte instalar.  


## Descrição do comando

### Abrir Illustrator
  
Este comando permite abrir o programa Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do programa|Caminho do programa Adobe Illustrator.exe|C:/Program Files/Adobe/Adobe Illustrator CC 2019/Support Files/Contents/Windows/Illustrator.exe|
|Atribuir resultado à variável|Nome da variável onde True ou False será salvo dependendo se o programa abriu corretamente|variável|

### Abrir arquivo AutoCAD
  
Este comando permite abrir um arquivo AutoCAD no Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho do arquivo|Caminho do arquivo que você deseja abrir no Adobe Illustrator|C:/Users/Usuário/Desktop/imagem.dxf|
|Opção de escala global|Selecione uma opção de escala global|Tamanho original|
|Unidades|Unidades do arquivo|1|
|Unidade de medida|Selecione a unidade de medida do arquivo|Centimeters|
|Escala global (porcentagem)|Escala global em porcentagem|100|
|Centralizar desenho|Centraliza o desenho na área de trabalho|True|
|Escalar espessuras de linha|Escala as espessuras das linhas de acordo com a escala global|False|
|Combinar camadas|Combina todas as camadas em uma só|False|
|Atribuir resultado à variável|Nome da variável onde True ou False será salvo dependendo se o arquivo foi aberto corretamente|variável|

### Alterar o modo de cor do documento
  
Este comando permite alterar o modo de cor do documento atual do Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Modo de cor|Modo de cor que deseja aplicar ao documento atual do Adobe Illustrator|RGB|

### Alterar cor CMYK da camada
  
Este comando permite alterar a cor CMYK da camada selecionada no documento atual do Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Cor Cyan|Valor de 0 a 100 para a cor Cyan|100|
|Cor Magenta|Valor de 0 a 100 para a cor Magenta|100|
|Cor Yellow|Valor de 0 a 100 para a cor Yellow|100|
|Cor Black|Valor de 0 a 100 para a cor Black|100|

### Adicionar mesa de trabalho
  
Este comando permite adicionar uma mesa de trabalho ao documento atual do Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da mesa de trabalho|Nome da mesa de trabalho que você deseja adicionar ao documento atual do Adobe Illustrator|Mesa de trabalho 2|
|Comprimento da mesa de trabalho|Comprimento da mesa de trabalho que você deseja adicionar ao documento atual do Adobe Illustrator|100|
|Largura da mesa de trabalho|Largura da mesa de trabalho que você deseja adicionar ao documento atual do Adobe Illustrator|100|
|Posição X da mesa de trabalho|Posição X da mesa de trabalho que você deseja adicionar ao documento atual do Adobe Illustrator|0|
|Posição Y da mesa de trabalho|Posição Y da mesa de trabalho que você deseja adicionar ao documento atual do Adobe Illustrator|0|

### Selecionar mesa de trabalho
  
Este comando permite selecionar uma mesa de trabalho do documento atual do Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da mesa de trabalho|Nome da mesa de trabalho que você deseja selecionar do documento atual do Adobe Illustrator|Mesa de trabalho 1|

### Duplicar mesa de trabalho
  
Este comando permite duplicar uma mesa de trabalho do documento atual do Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da mesa de trabalho|Nome da mesa de trabalho que você deseja duplicar do documento atual do Adobe Illustrator|Mesa de trabalho 1|
|Nome da nova mesa de trabalho|Nome que a nova mesa de trabalho terá que será criada a partir da mesa de trabalho que você deseja duplicar|Mesa de trabalho 2|
|Posição da mesa de trabalho|Selecione onde colocar a nova mesa de trabalho|Abaixo|
|Copiar conteúdo|Selecione se deseja copiar o conteúdo da mesa de trabalho|True|

### Ajustar aos limites da ilustração
  
Este comando permite ajustar o conteúdo da mesa de trabalho aos limites da ilustração selecionada. A camada de arte deve ser selecionada previamente.
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da mesa de trabalho|Nome da mesa de trabalho à qual você deseja ajustar o conteúdo do documento atual do Adobe Illustrator.|Mesa de trabalho 1|

### Excluir camada
  
Este comando permite excluir uma camada do documento atual do Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da camada|Nome da camada que você deseja excluir do documento atual do Adobe Illustrator|Camada 1|

### Selecione a camada
  
Este comando permite selecionar uma camada do documento atual do Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Camada para selecionar|Nome da camada que você deseja selecionar do documento atual do Adobe Illustrator|Camada 1|

### Atribuir visibilidade da camada
  
Este comando permite atribuir a visibilidade de uma camada do documento atual do Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da camada|Nome da camada que deseja definir a visibilidade do documento atual do Adobe Illustrator|Camada 1|
|Visibilidade|Visibilidade que deseja atribuir à camada do documento atual do Adobe Illustrator|Visible|

### Selecionar camada de arte
  
Este comando permite selecionar a camada de arte do documento atual do Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Nome da camada|Nome da camada que você deseja selecionar do documento atual do Adobe Illustrator|Camada 1|

### Executar script JS
  
Este comando permite executar um script JavaScript no documento atual do Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Arquivo JS|Selecione o arquivo JS que deseja executar no documento atual do Adobe Illustrator|C:/Users/User/Desktop/script.js|

### Ferramenta Refletir
  
Este comando permite refletir o objeto selecionado no documento atual do Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Eixo|Selecione o eixo de reflexão (horizontal ou vertical)|Horizontal|

### Salvar como EPS
  
Este comando permite salvar um arquivo do Adobe Illustrator em formato EPS
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho e nome do arquivo a salvar|Caminho e nome do arquivo a salvar. O caminho deve existir|C:/Users/usuario/Desktop/file.eps|
|Salvar múltiplas mesas de trabalho|Se ativo, todas as mesas de trabalho serão salvas exceto se for especificado um intervalo.|True|
|Intervalo de mesas de trabalho|Intervalo de mesas de trabalho a salvar. Exemplo 1-3,5,7-9|1-4|
|Incluir CMYK PostScript em arquivos RGB|Se ativo, será incluído um perfil CMYK PostScript em arquivos RGB|True|
|Incorporar todas as fontes|Se ativo, todas as fontes utilizadas pelo documento serão incorporadas no arquivo salvo|True|
|Incorporar arquivos vinculados|Se ativo, as imagens vinculadas serão incluídas no documento salvo.|True|
|Compatibilidade|Versão de compatibilidade do arquivo EPS|Illustrator CS6 (16)|
|Formato de visualização prévia|O formato para a imagem de visualização prévia EPS.|TIFF (8-bit Color)|
|Incluir miniaturas de documentos|Se ativo, será incluída uma imagem em miniatura do documento EPS.|True|
|Impressão de degradê compatível|Se ativo, será criado um item de raster do degradê ou malha de degradê para que as impressoras PostScript de nível 2 possam imprimir o objeto.|True|
|Nível de Adobe PostScript|Nível de linguagem PostScript para usar (Nível 1 válido para a versão do formato de arquivo 8 ou anterior).|Level 2|
|Atribuir resultado à variável|Nome da variável onde True ou False será salvo dependendo se o arquivo foi salvo corretamente|variável|

### Salvar .ai
  
Este comando permite salvar um arquivo do Adobe Illustrator no formato .ai
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Caminho e nome do arquivo a salvar|Caminho e nome do arquivo a salvar. O caminho deve existir|C:/Users/usuario/Desktop/imagem.ai|
|Atribuir resultado à variável|Nome da variável onde True ou False será salvo dependendo se o arquivo foi salvo corretamente|variável|

### Fechar Illustrator
  
Este comando permite fechar o programa Adobe Illustrator
|Parâmetros|Descrição|exemplo|
| --- | --- | --- |
|Atribuir resultado à variável|Nome da variável onde True ou False será salvo dependendo se o programa fechou corretamente|variável|
